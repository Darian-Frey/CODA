#!/usr/bin/env python3
"""
CODA SPARC Rotation Curve Simulation
=====================================
Tests the CODA MOND prediction against all 175 galaxies in the SPARC
dataset (Lelli, McGaugh & Schombert 2016).

CODA MOND theorem (theory/coda_mond_theorem.md):
    aN · tanh(aN/a0) = ab  [spherically symmetric MOND equation]
    vc = sqrt(aN · r)

    μ(x) = tanh(x)      derived from DSSYK: d(log cosh)/dx
    a0 = c·H0/(2π)      from de Sitter temperature — zero free parameters

Reference comparison: μ(x) = x/sqrt(1+x²)  [standard "simple" MOND]

Data:
    MassModels_Lelli2016c.mrt  — rotation curves (Lelli et al. 2016)
    SPARC_Lelli2016c.mrt       — galaxy catalog (type, quality, Vflat)

Usage:
    python3 sparc_simulation.py
    python3 sparc_simulation.py --data-dir /path/to/data
    python3 sparc_simulation.py --q-max 1          # high-quality only
    python3 sparc_simulation.py --no-plot           # text output only
"""

import argparse
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings('ignore')

# ─── Physical constants ───────────────────────────────────────────────────────

c    = 2.998e8           # m/s
G    = 6.674e-11         # m³ kg⁻¹ s⁻²
H0   = 70.0e3 / 3.086e22 # s⁻¹  (H0 = 70 km/s/Mpc)
Msun = 1.989e30          # kg
kpc  = 3.086e19          # m/kpc

# ─── CODA prediction (zero free parameters) ───────────────────────────────────

a0_CODA = c * H0 / (2.0 * np.pi)   # 1.082e-10 m/s²  from dS temperature
a0_OBS  = 1.2e-10                   # m/s²  canonical observational value

# Stellar mass-to-light ratios at 3.6 μm (Schombert & McGaugh 2014)
Yd = 0.5   # disk  [M☉/L☉]
Yb = 0.7   # bulge [M☉/L☉]

# Hubble type names
T_NAMES = {0:'S0',1:'Sa',2:'Sab',3:'Sb',4:'Sbc',5:'Sc',
           6:'Scd',7:'Sd',8:'Sdm',9:'Sm',10:'Im',11:'BCD'}

# ─── Data loading ─────────────────────────────────────────────────────────────

def load_massmodels(path):
    """
    Parse MassModels_Lelli2016c.mrt.
    Fixed-width format; columns documented in file header.

    Returns dict {name: {D, r, vobs, evobs, vgas, vdisk, vbul}}
    Note: Vdisk, Vbul are given at M/L=1; use sqrt(Y)*V for actual contribution.
    Note: Vgas includes helium factor 1.33; may be negative (sign-preserving accel).
    """
    galaxies = {}
    with open(path) as f:
        for line in f:
            if len(line) < 52:
                continue
            try:
                d     = float(line[12:18])
                r     = float(line[19:25])
                vobs  = float(line[26:32])
                evobs = float(line[33:38])
                vgas  = float(line[39:45])
                vdisk = float(line[46:52])
                vbul  = float(line[53:59]) if len(line) > 59 else 0.0
            except ValueError:
                continue
            name = line[0:11].strip()
            if not name:
                continue
            if name not in galaxies:
                galaxies[name] = {'D': d,
                                  'r':[], 'vobs':[], 'evobs':[],
                                  'vgas':[], 'vdisk':[], 'vbul':[]}
            galaxies[name]['r'].append(r)
            galaxies[name]['vobs'].append(vobs)
            galaxies[name]['evobs'].append(max(evobs, 1.0))
            galaxies[name]['vgas'].append(vgas)
            galaxies[name]['vdisk'].append(vdisk)
            galaxies[name]['vbul'].append(vbul)

    for name in galaxies:
        for k in ('r','vobs','evobs','vgas','vdisk','vbul'):
            galaxies[name][k] = np.array(galaxies[name][k], dtype=float)

    return galaxies


def load_catalog(path):
    """
    Parse SPARC_Lelli2016c.mrt (whitespace-delimited).
    Returns dict {name: {T, Tname, D, Inc, Vflat, Q}}
    """
    catalog = {}
    if not os.path.exists(path):
        print(f"  [catalog not found: {path} — proceeding without metadata]")
        return catalog
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            parts = s.split()
            if len(parts) < 17:
                continue
            try:
                name   = parts[0]
                T      = int(parts[1])
                D      = float(parts[2])
                Inc    = float(parts[5])
                Vflat  = float(parts[15])
                eVflat = float(parts[16])
                Q      = int(parts[17])
                catalog[name] = dict(T=T, Tname=T_NAMES.get(T,'?'),
                                     D=D, Inc=Inc,
                                     Vflat=Vflat, eVflat=eVflat, Q=Q)
            except (ValueError, IndexError):
                continue
    return catalog


# ─── Baryonic acceleration ────────────────────────────────────────────────────

def ab_from_components(r_kpc, vgas, vdisk, vbul):
    """
    Baryonic Newtonian centripetal acceleration [m/s²].

    Sign-preserving convention for negative Vgas: V|V|/r.
    Vdisk, Vbul are at M/L=1; actual contribution scaled by Yd, Yb.
    """
    r_m   = r_kpc * kpc
    vg    = vgas  * 1e3
    vd    = vdisk * 1e3
    vb    = vbul  * 1e3
    return (vg * np.abs(vg) + Yd * vd**2 + Yb * vb**2) / r_m


# ─── MOND solvers ─────────────────────────────────────────────────────────────

def _solve(ab, a0, mu_fn):
    if ab <= 0:
        return 0.0
    try:
        return brentq(lambda aN: mu_fn(aN, a0) - ab,
                      ab * 1e-6, max(20*np.sqrt(ab*a0), 2*ab),
                      xtol=1e-32, rtol=1e-10)
    except ValueError:
        return np.sqrt(ab * a0)


def solve_tanh(ab_arr, a0):
    """CODA: μ = tanh(x).  Solve aN·tanh(aN/a0) = ab."""
    fn = lambda aN, a0: aN * np.tanh(aN / a0)
    return np.array([_solve(a, a0, fn) for a in np.atleast_1d(ab_arr)])


def solve_simple(ab_arr, a0):
    """Reference: μ = x/√(1+x²).  Closed-form solution."""
    ab = np.atleast_1d(ab_arr)
    aN_sq = (ab**2 + np.sqrt(ab**4 + 4*ab**2*a0**2)) / 2.0
    return np.sqrt(np.where(ab > 0, aN_sq, 0.0))


def vc_pred(r_kpc, ab_ms2, a0, solver):
    fn  = solve_tanh if solver == 'tanh' else solve_simple
    aN  = fn(ab_ms2, a0)
    return np.sqrt(np.maximum(aN * r_kpc * kpc, 0.0)) / 1e3   # km/s


# ─── Per-galaxy fit ───────────────────────────────────────────────────────────

def fit_galaxy(gdata, a0, solver):
    r    = gdata['r']
    vobs = gdata['vobs']
    ev   = gdata['evobs']
    ab   = ab_from_components(r, gdata['vgas'], gdata['vdisk'], gdata['vbul'])
    vp   = vc_pred(r, ab, a0, solver)
    res  = vobs - vp
    n    = len(vobs)
    fn   = solve_tanh if solver == 'tanh' else solve_simple
    return dict(r=r, vobs=vobs, evobs=ev, vpred=vp,
                ab=ab, aN=fn(ab, a0),
                aobs=(vobs*1e3)**2 / (r*kpc),
                resid=res,
                chi2r=np.sum((res/ev)**2)/n if n else np.nan,
                rms=np.sqrt(np.mean(res**2)),
                bias=np.mean(res),
                n=n)


# ─── Run all galaxies ─────────────────────────────────────────────────────────

CONFIGS = [
    ('tanh',   a0_CODA, 'CODA'),       # CODA prediction, zero free params
    ('tanh',   a0_OBS,  'tanh_obs'),   # tanh with observed a0
    ('simple', a0_OBS,  'simple'),     # simple μ reference
]

def run_all(galaxies, q_max=3, catalog=None):
    results = {}
    for name, gdata in galaxies.items():
        Q = catalog[name]['Q'] if (catalog and name in catalog) else 2
        if Q > q_max:
            continue
        results[name] = {label: fit_galaxy(gdata, a0, solver)
                         for solver, a0, label in CONFIGS}
    return results


# ─── Statistics helpers ───────────────────────────────────────────────────────

def get_metric(results, label, key):
    vals = [results[n][label][key] for n in results
            if np.isfinite(results[n][label][key])]
    return np.array(vals)


def group_names(results, catalog, T_range):
    lo, hi = T_range
    if not catalog:
        return list(results.keys())
    return [n for n in results
            if n in catalog and lo <= catalog[n]['T'] <= hi]


# ─── Plotting ─────────────────────────────────────────────────────────────────

BG    = '#0d0d0d'
AX_BG = '#111111'
GR    = '#222222'
C_CODA   = '#00d4ff'
C_TANH   = '#4CAF50'
C_SIMPLE = '#FF7043'
C_OBS    = '#ffffff'
C_BAR    = '#ffaa00'

def sax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(AX_BG)
    for sp in ax.spines.values():
        sp.set_color('#333')
    ax.tick_params(colors='#888', labelsize=7.5)
    if xlabel: ax.set_xlabel(xlabel, color='#aaa', fontsize=8)
    if ylabel: ax.set_ylabel(ylabel, color='#aaa', fontsize=8)
    ax.grid(True, color=GR, lw=0.5, alpha=0.8)
    if title:
        ax.set_title(title, color='white', fontsize=8.5, fontweight='bold', pad=3)


def plot_rc(ax, gdata, res_c, res_t, res_s, name):
    r   = gdata['r']
    r_m = r * kpc
    vc_b = np.sqrt(np.maximum(res_c['ab'] * r_m, 0)) / 1e3
    ax.fill_between(r, gdata['vobs']-gdata['evobs'], gdata['vobs']+gdata['evobs'],
                    color=C_OBS, alpha=0.12, zorder=1)
    ax.errorbar(r, gdata['vobs'], yerr=gdata['evobs'],
                fmt='o', ms=2.5, color=C_OBS, lw=0.8, capsize=1.5, zorder=5)
    ax.plot(r, vc_b,           '-.', color=C_BAR,    lw=1.0, alpha=0.5, zorder=2)
    ax.plot(r, res_s['vpred'], ':',  color=C_SIMPLE, lw=1.6, zorder=3)
    ax.plot(r, res_t['vpred'], '--', color=C_TANH,   lw=1.8, zorder=4)
    ax.plot(r, res_c['vpred'], '-',  color=C_CODA,   lw=2.2, zorder=6)
    sax(ax, title=name, xlabel='r (kpc)', ylabel='vc (km/s)')
    ax.text(0.97, 0.05,
            f"χ²ᵣ: {res_c['chi2r']:.1f}|{res_t['chi2r']:.1f}|{res_s['chi2r']:.1f}",
            transform=ax.transAxes, ha='right', va='bottom',
            color='#aaa', fontsize=6.0)


def make_figure(galaxies, results, catalog, outpath, n_gal):
    fig = plt.figure(figsize=(21, 17))
    fig.patch.set_facecolor(BG)
    gs  = gridspec.GridSpec(4, 4, figure=fig, hspace=0.50, wspace=0.37)

    # ── Six rotation curves ───────────────────────────────────────────────────
    showcase = [
        ('NGC3198',   '(0,0)'),  # classic flat curve
        ('NGC6503',   '(0,1)'),  # isolated spiral
        ('DDO154',    '(0,2)'),  # gas-dominated dwarf
        ('NGC7331',   '(0,3)'),  # massive Sb
        ('UGC02885',  '(1,0)'),  # largest SPARC galaxy
        ('IC2574',    '(1,1)'),  # LSB dwarf
    ]
    for name, pos_str in showcase:
        row, col = map(int, pos_str.strip('()').split(','))
        if name not in results:
            continue
        ax = fig.add_subplot(gs[row, col])
        plot_rc(ax, galaxies[name],
                results[name]['CODA'],
                results[name]['tanh_obs'],
                results[name]['simple'], name)
        if (row, col) == (0, 0):
            from matplotlib.lines import Line2D
            handles = [
                Line2D([0],[0], color=C_CODA,   lw=2.0, label='CODA tanh (a₀=cH₀/2π)'),
                Line2D([0],[0], color=C_TANH,   lw=1.8, ls='--', label='tanh (a₀=obs)'),
                Line2D([0],[0], color=C_SIMPLE, lw=1.6, ls=':', label='simple μ'),
                Line2D([0],[0], color=C_BAR,    lw=1.0, ls='-.', label='baryonic (Newton)'),
            ]
            ax.legend(handles=handles, fontsize=5.8,
                      facecolor='#1a1a1a', edgecolor='#444',
                      labelcolor='#ccc', framealpha=0.9, loc='lower right')

    # ── χ²r histogram by Hubble type ─────────────────────────────────────────
    ax_hist = fig.add_subplot(gs[1, 2])
    for label, color, ls in [('simple','#FF7043',':'),
                               ('tanh_obs','#4CAF50','--'),
                               ('CODA',    '#00d4ff','-')]:
        chi2r = get_metric(results, label, 'chi2r')
        bins  = np.logspace(-1, 2.5, 28)
        ax_hist.hist(chi2r, bins=bins, histtype='step', lw=1.6,
                     color=color, ls=ls, density=True,
                     label=f"{label}  med={np.median(chi2r):.2f}")
    ax_hist.set_xscale('log')
    sax(ax_hist, title='χ²ᵣ distribution', xlabel='χ²ᵣ', ylabel='density')
    ax_hist.legend(fontsize=6.5, facecolor='#1a1a1a', edgecolor='#444',
                   labelcolor='#ccc', framealpha=0.9)

    # ── RMS residual sorted ───────────────────────────────────────────────────
    ax_rms = fig.add_subplot(gs[1, 3])
    rms_c = np.array([results[n]['CODA']['rms']     for n in results])
    rms_t = np.array([results[n]['tanh_obs']['rms'] for n in results])
    rms_s = np.array([results[n]['simple']['rms']   for n in results])
    order = np.argsort(rms_t)
    idx   = np.arange(len(order))
    ax_rms.plot(idx, rms_s[order], '.', color=C_SIMPLE, ms=2.5, alpha=0.6,
                label=f'simple  μ={np.mean(rms_s):.1f}')
    ax_rms.plot(idx, rms_t[order], '.', color=C_TANH,   ms=2.5, alpha=0.6,
                label=f'tanh obs μ={np.mean(rms_t):.1f}')
    ax_rms.plot(idx, rms_c[order], '.', color=C_CODA,   ms=3.0, alpha=0.8,
                label=f'CODA    μ={np.mean(rms_c):.1f}')
    sax(ax_rms, title='RMS residual per galaxy', xlabel='rank', ylabel='RMS (km/s)')
    ax_rms.legend(fontsize=6.5, facecolor='#1a1a1a', edgecolor='#444',
                  labelcolor='#ccc', framealpha=0.9)

    # ── Full RAR ──────────────────────────────────────────────────────────────
    ax_rar = fig.add_subplot(gs[2, 0:2])
    ab_all, aobs_all = [], []
    for n in results:
        res = results[n]['CODA']
        mask = (res['ab'] > 0) & (res['aobs'] > 0)
        ab_all.extend(res['ab'][mask])
        aobs_all.extend(res['aobs'][mask])
    ab_all   = np.array(ab_all)
    aobs_all = np.array(aobs_all)

    ax_rar.scatter(ab_all/a0_OBS, aobs_all/a0_OBS,
                   s=2.5, alpha=0.15, color='#888', zorder=1, rasterized=True)

    s = np.logspace(-3, 2.5, 500)
    ax_rar.plot(s * a0_CODA/a0_OBS,
                solve_tanh(s * a0_CODA, a0_CODA) / a0_OBS,
                '-', color=C_CODA,   lw=2.5, zorder=5,
                label=f'CODA tanh (a₀={a0_CODA:.2e})')
    ax_rar.plot(s, solve_tanh(s*a0_OBS, a0_OBS) / a0_OBS,
                '--', color=C_TANH,  lw=2.0, zorder=4,
                label='tanh (a₀=obs)')
    ax_rar.plot(s, solve_simple(s*a0_OBS, a0_OBS) / a0_OBS,
                ':', color=C_SIMPLE, lw=2.0, zorder=3,
                label='simple μ')
    ax_rar.plot([1e-3,1e3],[1e-3,1e3], 'w:', lw=0.8, alpha=0.3, label='Newton')
    ax_rar.plot(s, np.sqrt(s), 'w--', lw=0.8, alpha=0.3, label='Deep MOND')
    ax_rar.set_xscale('log'); ax_rar.set_yscale('log')
    ax_rar.set_xlim(3e-3, 2e2); ax_rar.set_ylim(3e-3, 2e2)
    sax(ax_rar, title=f'Radial Acceleration Relation  ({len(ab_all)} data points)',
        xlabel='a_bar / a₀(obs)', ylabel='a_obs / a₀(obs)')
    ax_rar.legend(fontsize=7.5, facecolor='#1a1a1a', edgecolor='#444',
                  labelcolor='#ccc', framealpha=0.9, loc='upper left')

    # ── μ(x) comparison ───────────────────────────────────────────────────────
    ax_mu = fig.add_subplot(gs[2, 2])
    x = np.linspace(0, 6, 600)
    ax_mu.plot(x, np.tanh(x),        '-',  color=C_CODA,   lw=2.5,
               label=f'CODA: tanh(x)  μ(1)={np.tanh(1):.4f}')
    ax_mu.plot(x, x/np.sqrt(1+x**2), '--', color=C_TANH,   lw=2.0,
               label=f'simple: x/√(1+x²)  μ(1)={1/np.sqrt(2):.4f}')
    ax_mu.plot(x, x/(1+x),           ':',  color=C_SIMPLE, lw=2.0,
               label='standard: x/(1+x)')
    ax_mu.axvline(1, color='#ffcc00', lw=1, ls='--', alpha=0.6)
    ax_mu.text(1.07, 0.06, 'x=1', color='#ffcc00', fontsize=7,
               transform=ax_mu.get_xaxis_transform())
    delta = 100*(np.tanh(1) - 1/np.sqrt(2)) / (1/np.sqrt(2))
    ax_mu.text(0.05, 0.58,
               f'Δμ at transition:\n+{delta:.1f}% (tanh vs simple)\nDiscriminable with\nEuclid at ~5% level',
               transform=ax_mu.transAxes, color='#ccc', fontsize=7.5,
               bbox=dict(boxstyle='round', fc='#1a1a1a', alpha=0.85))
    ax_mu.set_xlim(0,6); ax_mu.set_ylim(0,1.06)
    sax(ax_mu, title='Interpolating functions μ(x)',
        xlabel='x = aN/a₀', ylabel='μ(x)')
    ax_mu.legend(fontsize=6.8, facecolor='#1a1a1a', edgecolor='#444',
                 labelcolor='#ccc', framealpha=0.9, loc='lower right')

    # ── χ²r by Hubble type ────────────────────────────────────────────────────
    ax_type = fig.add_subplot(gs[2, 3])
    if catalog:
        groups = [('Early\nT≤3', 0,3), ('Late\nT4-7', 4,7), ('Dwarf\nT≥8', 8,11)]
        x_pos  = np.arange(len(groups))
        width  = 0.28
        for i, (label, color) in enumerate([('CODA',C_CODA),
                                             ('tanh_obs',C_TANH),
                                             ('simple',C_SIMPLE)]):
            meds = []
            for gname, lo, hi in groups:
                names = [n for n in results
                         if n in catalog and lo <= catalog[n]['T'] <= hi]
                vals  = [results[n][label]['chi2r'] for n in names
                         if np.isfinite(results[n][label]['chi2r'])]
                meds.append(np.median(vals) if vals else 0)
            ax_type.bar(x_pos + (i-1)*width, meds, width=width*0.9,
                        color=color, alpha=0.7,
                        label=label.replace('_obs',' obs'))
        ax_type.set_xticks(x_pos)
        ax_type.set_xticklabels([g[0] for g in groups], color='#aaa', fontsize=8)
        sax(ax_type, title='Median χ²ᵣ by Hubble type',
            xlabel='', ylabel='Median χ²ᵣ')
        ax_type.legend(fontsize=7, facecolor='#1a1a1a', edgecolor='#444',
                       labelcolor='#ccc', framealpha=0.9)
    else:
        ax_type.text(0.5, 0.5, 'Catalog not loaded',
                     ha='center', va='center', color='#888',
                     transform=ax_type.transAxes)

    # ── Δχ²r: tanh − simple per galaxy ───────────────────────────────────────
    ax_dc = fig.add_subplot(gs[3, 0:2])
    chi2r_t = get_metric(results, 'tanh_obs', 'chi2r')
    chi2r_s = get_metric(results, 'simple',   'chi2r')
    dc      = chi2r_t - chi2r_s
    dc_sort = np.sort(dc)
    colors  = [C_SIMPLE if d > 0 else C_CODA for d in dc_sort]
    ax_dc.bar(range(len(dc_sort)), dc_sort, color=colors, alpha=0.7, width=1.0)
    ax_dc.axhline(0, color='white', lw=0.8)
    ax_dc.axhline(np.mean(dc), color='#ffcc00', lw=1.5, ls='--',
                  label=f'mean Δ = {np.mean(dc):+.2f}')
    ax_dc.text(0.97, 0.95 if np.mean(dc) > 0 else 0.05,
               f'tanh worse:  {(dc>0).sum()}/{len(dc)}\n'
               f'tanh better: {(dc<0).sum()}/{len(dc)}',
               transform=ax_dc.transAxes, ha='right', va='top',
               color='#ccc', fontsize=8,
               bbox=dict(boxstyle='round', fc='#1a1a1a', alpha=0.85))
    sax(ax_dc, title='χ²ᵣ(tanh) − χ²ᵣ(simple) per galaxy  '
                     '[orange=tanh worse, blue=tanh better]',
        xlabel='Galaxy (ranked)', ylabel='Δχ²ᵣ')
    ax_dc.legend(fontsize=8, facecolor='#1a1a1a', edgecolor='#444',
                 labelcolor='#ccc', framealpha=0.9)

    # ── Tully-Fisher ──────────────────────────────────────────────────────────
    ax_tf = fig.add_subplot(gs[3, 2])
    if catalog:
        vflat_obs, vflat_pred_c, vflat_pred_t = [], [], []
        for name in results:
            if name not in catalog:
                continue
            vf = catalog[name]['Vflat']
            if vf <= 0:
                continue
            # Asymptotic baryonic mass from last 3 data points
            r3   = results[name]['CODA']['r'][-3:]
            ab3  = results[name]['CODA']['ab'][-3:]
            r_m  = r3 * kpc
            Mb   = np.mean(ab3 * r_m**2 / G) / Msun
            if Mb <= 0:
                continue
            vTF_c = (a0_CODA * G * Mb * Msun)**0.25 / 1e3
            vTF_t = (a0_OBS  * G * Mb * Msun)**0.25 / 1e3
            vflat_obs.append(vf)
            vflat_pred_c.append(vTF_c)
            vflat_pred_t.append(vTF_t)

        vflat_obs   = np.array(vflat_obs)
        vflat_pred_c = np.array(vflat_pred_c)
        vflat_pred_t = np.array(vflat_pred_t)

        ax_tf.scatter(vflat_obs, vflat_pred_c, s=12, color=C_CODA,   alpha=0.6,
                      zorder=3, label='CODA')
        ax_tf.scatter(vflat_obs, vflat_pred_t, s=12, color=C_TANH,   alpha=0.4,
                      zorder=2, marker='s', label='tanh obs')
        lims = [15, 350]
        ax_tf.plot(lims, lims, 'w--', lw=1, alpha=0.5, label='1:1')
        ax_tf.set_xlim(*lims); ax_tf.set_ylim(*lims)
        ax_tf.set_xscale('log'); ax_tf.set_yscale('log')
        sax(ax_tf, title='Tully-Fisher: v_TF⁴ = a₀GM_b',
            xlabel='Vflat observed (km/s)', ylabel='v_TF predicted (km/s)')
        ax_tf.legend(fontsize=7, facecolor='#1a1a1a', edgecolor='#444',
                     labelcolor='#ccc', framealpha=0.9)

    # ── Summary table ─────────────────────────────────────────────────────────
    ax_tbl = fig.add_subplot(gs[3, 3])
    ax_tbl.axis('off')
    ax_tbl.set_facecolor(AX_BG)

    chi2r_c = get_metric(results, 'CODA',     'chi2r')
    chi2r_t = get_metric(results, 'tanh_obs', 'chi2r')
    chi2r_s = get_metric(results, 'simple',   'chi2r')
    rms_c   = get_metric(results, 'CODA',     'rms')
    rms_t   = get_metric(results, 'tanh_obs', 'rms')
    rms_s   = get_metric(results, 'simple',   'rms')

    rows = [
        ['',               'CODA',              'tanh\n(obs a₀)',     'simple'],
        ['Mean χ²ᵣ',       f'{np.mean(chi2r_c):.2f}', f'{np.mean(chi2r_t):.2f}', f'{np.mean(chi2r_s):.2f}'],
        ['Median χ²ᵣ',     f'{np.median(chi2r_c):.2f}', f'{np.median(chi2r_t):.2f}', f'{np.median(chi2r_s):.2f}'],
        ['Mean RMS km/s',  f'{np.mean(rms_c):.1f}', f'{np.mean(rms_t):.1f}', f'{np.mean(rms_s):.1f}'],
        ['χ²ᵣ < 5',        f'{(chi2r_c<5).sum()}/{n_gal}', f'{(chi2r_t<5).sum()}/{n_gal}', f'{(chi2r_s<5).sum()}/{n_gal}'],
        ['χ²ᵣ < 2',        f'{(chi2r_c<2).sum()}/{n_gal}', f'{(chi2r_t<2).sum()}/{n_gal}', f'{(chi2r_s<2).sum()}/{n_gal}'],
        ['a₀ (m/s²)',      f'{a0_CODA:.3e}', f'{a0_OBS:.3e}', f'{a0_OBS:.3e}'],
        ['Free params',    '0', '0', '0'],
        ['μ(1)',           f'{np.tanh(1):.4f}', f'{np.tanh(1):.4f}', f'{1/np.sqrt(2):.4f}'],
    ]
    tbl = ax_tbl.table(cellText=rows[1:], colLabels=rows[0],
                       loc='center', cellLoc='center',
                       bbox=[0, 0.05, 1, 0.92])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8.5)
    for (r,c), cell in tbl.get_celld().items():
        cell.set_facecolor('#1a1a1a' if r%2==0 else '#151515')
        cell.set_edgecolor('#333')
        cell.set_text_props(color='#ccc')
        if r == 0:
            cell.set_facecolor('#1f3a4a')
            cell.set_text_props(color='white', fontweight='bold')
        if c == 1 and r > 0:
            cell.set_text_props(color=C_CODA)
    ax_tbl.set_title(f'Summary — {n_gal} SPARC galaxies\n'
                     '(Yd=0.5  Yb=0.7  H₀=70 km/s/Mpc)',
                     color='white', fontsize=8.5, pad=5)

    # ── Global title ──────────────────────────────────────────────────────────
    fig.text(0.5, 0.985,
             'CODA MOND Prediction: μ(x)=tanh(x),  a₀=cH₀/2π  —  zero free parameters',
             ha='center', va='top', color='white', fontsize=13, fontweight='bold')
    fig.text(0.5, 0.963,
             'SPARC dataset: Lelli, McGaugh & Schombert (2016)  ·  175 galaxies, 3391 data points',
             ha='center', va='top', color='#aaaaaa', fontsize=8.5)

    plt.savefig(outpath, dpi=150, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close()
    print(f"\n  Figure: {outpath}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir', default='data',
                    help='Directory containing the two .mrt files')
    ap.add_argument('--output', default='coda_sparc_rotation_curves.png',
                    help='Output figure path')
    ap.add_argument('--q-max', type=int, default=3, choices=[1,2,3],
                    help='Maximum quality flag to include (1=high only, 3=all)')
    ap.add_argument('--no-plot', action='store_true',
                    help='Skip figure generation')
    args = ap.parse_args()

    mm_path  = os.path.join(args.data_dir, 'MassModels_Lelli2016c.mrt')
    cat_path = os.path.join(args.data_dir, 'SPARC_Lelli2016c.mrt')

    # ── Load ──────────────────────────────────────────────────────────────────
    print(f"\nLoading {mm_path} ...")
    galaxies = load_massmodels(mm_path)
    npts = sum(len(g['r']) for g in galaxies.values())
    print(f"  {len(galaxies)} galaxies  {npts} data points")

    print(f"Loading {cat_path} ...")
    catalog = load_catalog(cat_path)
    print(f"  {len(catalog)} catalog entries")

    # ── Run ───────────────────────────────────────────────────────────────────
    print(f"\nFitting (Q ≤ {args.q_max}) ...")
    results = run_all(galaxies, q_max=args.q_max, catalog=catalog)
    n_gal   = len(results)
    print(f"  {n_gal} galaxies fitted")

    # ── Statistics ────────────────────────────────────────────────────────────
    chi2r_c = get_metric(results, 'CODA',     'chi2r')
    chi2r_t = get_metric(results, 'tanh_obs', 'chi2r')
    chi2r_s = get_metric(results, 'simple',   'chi2r')
    rms_c   = get_metric(results, 'CODA',     'rms')
    rms_t   = get_metric(results, 'tanh_obs', 'rms')
    rms_s   = get_metric(results, 'simple',   'rms')
    dc_ts   = chi2r_t - chi2r_s   # tanh_obs vs simple

    print(f"""
{'='*65}
CODA MOND RESULTS — {n_gal} SPARC galaxies  (Q ≤ {args.q_max})
{'='*65}

  a₀ (CODA = cH₀/2π):    {a0_CODA:.4e}  m/s²  [zero free params]
  a₀ (observed):           {a0_OBS:.4e}  m/s²
  Ratio CODA/obs:          {a0_CODA/a0_OBS:.4f}   (10% discrepancy = open 2π problem)

  {'Metric':<28} {'CODA':>10} {'tanh obs':>10} {'simple':>10}
  {'-'*62}
  {'Mean χ²ᵣ':<28} {np.mean(chi2r_c):>10.2f} {np.mean(chi2r_t):>10.2f} {np.mean(chi2r_s):>10.2f}
  {'Median χ²ᵣ':<28} {np.median(chi2r_c):>10.2f} {np.median(chi2r_t):>10.2f} {np.median(chi2r_s):>10.2f}
  {'Mean RMS (km/s)':<28} {np.mean(rms_c):>10.1f} {np.mean(rms_t):>10.1f} {np.mean(rms_s):>10.1f}
  {'χ²ᵣ < 5':<28} {(chi2r_c<5).sum():>10}/{n_gal} {(chi2r_t<5).sum():>10}/{n_gal} {(chi2r_s<5).sum():>10}/{n_gal}
  {'χ²ᵣ < 2':<28} {(chi2r_c<2).sum():>10}/{n_gal} {(chi2r_t<2).sum():>10}/{n_gal} {(chi2r_s<2).sum():>10}/{n_gal}

  tanh vs simple (obs a₀):
    Δ mean χ²ᵣ  = {np.mean(dc_ts):+.2f}   {'tanh worse' if np.mean(dc_ts)>0 else 'tanh better'}
    Galaxies tanh better: {(dc_ts<0).sum()}/{n_gal}
    Galaxies tanh worse:  {(dc_ts>0).sum()}/{n_gal}

  μ at transition (x=1):
    tanh(1)       = {np.tanh(1):.4f}
    simple μ(1)   = {1/np.sqrt(2):.4f}
    Δ             = {100*(np.tanh(1)-1/np.sqrt(2))/(1/np.sqrt(2)):+.1f}%
    → Euclid weak lensing can discriminate at ~5% per galaxy bin

  Tully-Fisher (deep MOND, a₀ = CODA):
    v_c⁴ = a₀ · G · M_b""")

    for log_M in [9, 10, 11, 12]:
        vc = (a0_CODA * G * 10**log_M * Msun)**0.25 / 1e3
        print(f"    10^{log_M} M☉  →  {vc:.0f} km/s")

    # Per Hubble type if catalog available
    if catalog:
        print(f"\n  Median χ²ᵣ by Hubble type:")
        for gname, lo, hi in [('Early T≤3',0,3),('Late T4-7',4,7),('Dwarf T≥8',8,11)]:
            nms = [n for n in results if n in catalog and lo<=catalog[n]['T']<=hi]
            vc  = np.median([results[n]['CODA']['chi2r']     for n in nms
                              if np.isfinite(results[n]['CODA']['chi2r'])])
            vt  = np.median([results[n]['tanh_obs']['chi2r'] for n in nms
                              if np.isfinite(results[n]['tanh_obs']['chi2r'])])
            vs  = np.median([results[n]['simple']['chi2r']   for n in nms
                              if np.isfinite(results[n]['simple']['chi2r'])])
            print(f"    {gname:<14} (n={len(nms):2d})  "
                  f"CODA={vc:.2f}  tanh={vt:.2f}  simple={vs:.2f}")

    print(f"\n{'='*65}")

    if not args.no_plot:
        print("\nGenerating figure...")
        make_figure(galaxies, results, catalog, args.output, n_gal)

    print("\nDone.")


if __name__ == '__main__':
    main()