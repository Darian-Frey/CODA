# CODA Tier 2 — Cosmological Background and Perturbation Theory

**Document:** `phenomenology/cosmological_background.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Depends on:** `theory/field_equations.md` v0.2,
`phenomenology/weak_field_limit.md` v0.1  
**Primary sources:** Stelle (1977); Skordis & Złośnik (2021) PRL 127, 161302  
**Epistemic flags:**
- `[ESTABLISHED]` — results verified against primary sources or standard GR
- `[CODA-PREDICTION]` — follows from Tier 2 field equations by calculation
- `[OPEN]` — requires Tier 1 construction; status unknown

---

## 0. Purpose and Scope

This document derives the cosmological predictions of CODA Tier 2. The central
result is stark: **CODA Tier 2 is exactly GR at the cosmological background level,
and deviates from GR at the perturbative level by corrections suppressed by
$(k/M_P)^2 \sim 10^{-60}$ at CMB scales.**

This is not a fine-tuning result. It is a structural consequence of a single
geometric fact: FLRW spacetimes are conformally flat, so their Weyl tensor
vanishes identically. The Weyl-squared term in the CODA action contributes
nothing to conformally flat backgrounds.

**Scope:**
- §1–2: The FLRW background — exact GR
- §3: Cosmological perturbations — suppressed Bach tensor corrections
- §4: Specific tests — BBN, CMB, inflation, large-scale structure
- §5: The ghost in cosmology
- §6: CODA Tier 2 vs. AeST in the cosmological sector
- §7: What Tier 2 does not explain
- §8: Tier 1 and cosmology — status and open questions

---

## 1. The FLRW Background — Exact GR

### 1.1 Conformal Flatness of FLRW

The spatially flat FLRW metric:

$$ds^2 = -dt^2 + a^2(t)\left(dx^2 + dy^2 + dz^2\right)$$

is conformally flat — it is related to Minkowski space by a conformal rescaling:

$$ds^2 = a^2(\eta)\left(-d\eta^2 + d\vec{x}^2\right) = a^2(\eta)\,\eta_{\mu\nu}\,dx^\mu dx^\nu$$

where $\eta$ is conformal time. The Weyl tensor is invariant under conformal
rescalings of the metric (it is conformally covariant with zero weight in 4D):

$$C_{\mu\nu\rho\sigma}[a^2\eta] = C_{\mu\nu\rho\sigma}[\eta] = 0$$

**Therefore:** `[ESTABLISHED]`

$$C_{\mu\nu\rho\sigma}^{(\rm FLRW)} = 0$$

for all spatially flat FLRW backgrounds, regardless of the form of $a(t)$,
the matter content, or the cosmological constant. The same result holds for
spatially curved ($k = \pm 1$) FLRW metrics, which are also conformally flat.

### 1.2 Vanishing of the Bach Tensor

The Bach tensor is:

$$B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma}
+ \tfrac{1}{2}R^{\rho\sigma}C_{\mu\rho\nu\sigma}$$

Both terms contain the Weyl tensor as a factor. Since
$C_{\mu\nu\rho\sigma}^{(\rm FLRW)} = 0$:

$$B_{\mu\nu}^{(\rm FLRW)} = 0$$

`[ESTABLISHED — follows from conformal flatness and the definition of $B_{\mu\nu}$]`

### 1.3 The CODA Field Equations Reduce Exactly to GR

The CODA Tier 2 field equations are:

$$G_{\mu\nu} - 32\pi G\xi\, B_{\mu\nu} = 8\pi G\, T_{\mu\nu}$$

On any FLRW background, $B_{\mu\nu} = 0$ exactly, so:

$$G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$$

**CODA Tier 2 reduces exactly to the Einstein equations on all FLRW
backgrounds, for all values of $\xi$ and all matter content.** `[CODA-PREDICTION]`

---

## 2. The Friedmann Equations — Unmodified

From $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ with the FLRW metric, the standard
Friedmann equations follow without modification:

$$H^2 \equiv \left(\frac{\dot{a}}{a}\right)^2
= \frac{8\pi G}{3}\rho - \frac{k}{a^2} + \frac{\Lambda}{3}$$

$$\dot{H} + H^2 = \frac{\ddot{a}}{a}
= -\frac{4\pi G}{3}(\rho + 3p) + \frac{\Lambda}{3}$$

$$\dot{\rho} + 3H(\rho + p) = 0$$

All of these are identical to GR. The coupling $\xi$ does not appear.
`[CODA-PREDICTION]`

**Consequences — CODA Tier 2 predicts identical values to GR for:**

| Observable | CODA Tier 2 | Source |
|-----------|-------------|--------|
| Hubble parameter $H_0$ | GR value | Friedmann Eq. 1 |
| Deceleration parameter $q_0$ | GR value | Friedmann Eq. 2 |
| Age of the universe $t_0$ | GR value | $\int da/(aH)$ |
| Matter-radiation equality $z_{\rm eq}$ | GR value | $\rho_m = \rho_r$ |
| Recombination $z_{\rm rec}$ | GR value | $T = 3000$ K |
| BBN epoch | GR value | $T = 1$ MeV |
| Dark energy equation of state $w$ | Model-dependent, same as GR | $p_\Lambda = -\rho_\Lambda$ |

The coupling $\xi$ is entirely invisible in all FLRW observables. No
cosmological measurement can constrain $\xi$ at the background level.

---

## 3. Cosmological Perturbations

### 3.1 The Perturbed Weyl Tensor

At first order in perturbations around FLRW, the metric in conformal
Newtonian gauge is:

$$ds^2 = -(1+2\Phi)dt^2 + a^2(t)(1-2\Psi)\delta_{ij}\,dx^idx^j$$

The perturbed Weyl tensor is non-zero at first order. For scalar perturbations,
the electric part of the Weyl tensor is:

$$\delta E_{ij} \sim \partial_i\partial_j(\Phi - \Psi) + \text{(time derivative terms)}$$

The perturbed Bach tensor involves two covariant derivatives acting on
$\delta C_{\mu\rho\nu\sigma}$. Since $C^{(0)} = 0$, the first-order Bach
tensor is:

$$\delta B_{\mu\nu} = \nabla^{(0)\rho}\nabla^{(0)\sigma}\delta C_{\mu\rho\nu\sigma}
+ \tfrac{1}{2}R^{(0)\rho\sigma}\delta C_{\mu\rho\nu\sigma}$$

In Fourier space, this involves **four spatial derivatives** of the metric
perturbation, giving schematically:

$$\delta B_{\mu\nu} \sim \frac{k^4}{a^4} \delta g_{\mu\nu} + \mathcal{O}(k^2 H^2)$$

### 3.2 The Suppression Factor

The CODA Tier 2 correction to the perturbed field equations is
$32\pi G\xi \,\delta B_{\mu\nu}$. Comparing to the leading Einstein tensor term
$\delta G_{\mu\nu} \sim k^2/a^2$:

$$\frac{32\pi G\xi\,\delta B_{\mu\nu}}{\delta G_{\mu\nu}}
\sim \frac{32\pi G\xi \cdot k^4/a^4}{k^2/a^2}
= \frac{32\pi G\xi\, k^2}{a^2}
= \frac{k^2}{m_2^2 a^2}
= \left(\frac{k_{\rm phys}}{m_2}\right)^2$$

where $k_{\rm phys} = k/a$ is the physical wavenumber and $m_2 = M_P/(2\sqrt{\xi})$
is the ghost mass. `[CODA-PREDICTION]`

**For CMB multipoles** ($\ell \sim 100$–$3000$, $k_{\rm phys} \sim 10^{-4}$–$10^{-2}$ Mpc$^{-1}$):

$$\frac{k_{\rm phys}}{m_2} \sim \frac{10^{-29}\,\text{eV}}{M_P}
\approx 10^{-57}$$

$$\left(\frac{k_{\rm phys}}{m_2}\right)^2 \sim 10^{-114}$$

This is not small — it is **inconceivably negligible**. No cosmological
perturbation measurement at any planned experiment can probe corrections at
this level.

### 3.3 The Gravitational Slip Parameter

The ratio $\eta_{\rm slip} \equiv \Phi/\Psi$ is the gravitational slip
parameter, probed by weak lensing and CMB polarization cross-correlations.
In GR with perfect fluids, $\eta_{\rm slip} = 1$. In CODA Tier 2:

$$\eta_{\rm slip} = 1 + \mathcal{O}\!\left(\frac{k^2}{m_2^2}\right) = 1$$

to all measurable precision. `[CODA-PREDICTION]`

### 3.4 The Modified Dispersion Relation for Gravitational Waves

The tensor mode equation in CODA Tier 2:

$$h_k'' + 2\mathcal{H}h_k' + \left(k^2 + 32\pi G\xi a^2 k^4/c^2\right)h_k = 0$$

This gives a frequency-dependent GW phase velocity:

$$v_{\rm ph}(k) = c\sqrt{1 + k_{\rm phys}^2/m_2^2}
\approx c\left(1 + \frac{k_{\rm phys}^2}{2m_2^2}\right)$$

**At LIGO frequencies** ($f \sim 100$ Hz):

$$v_{\rm ph} - c \approx c\,\frac{k_{\rm phys}^2}{2m_2^2}
\approx c \times \frac{(2\pi \times 100\,\text{Hz}/c)^2}{2 M_P^2/\hbar^2}
\sim 10^{-72}\,c$$

Unmeasurable. `[CODA-PREDICTION]`

---

## 4. Specific Cosmological Tests

### 4.1 Big Bang Nucleosynthesis (BBN)

BBN predictions depend on the Hubble rate at $T \sim 1$ MeV. Since the CODA
Tier 2 Friedmann equation is identical to GR, the expansion rate at BBN
is unchanged. Light element abundances (D, $^4$He, $^7$Li) are identical
to the standard model + GR predictions.

**Constraint on $\xi$ from BBN:** None. The CODA Tier 2 correction at
$T = 1$ MeV involves $(T/M_P)^2 \sim (1\,\text{MeV}/10^{28}\,\text{eV})^2
\sim 10^{-56}$. `[CODA-PREDICTION: no BBN constraint on $\xi$]`

### 4.2 CMB Temperature and Polarization

The CMB power spectra depend on:
1. The background expansion history (§2 — identical to GR)
2. The perturbation equations for scalar, vector, and tensor modes (§3)
3. The photon transfer function (unmodified — photons do not couple to the
   Bach tensor directly)

All three are identical to GR at any measurable precision in CODA Tier 2.
The CMB places **no constraint on $\xi$**. `[CODA-PREDICTION]`

Note for contrast: AeST (Skordis & Złośnik 2021) is CMB-compatible by
construction but requires non-trivial tuning of its kinetic function to
reproduce the observed acoustic peaks. CODA Tier 2 requires no such tuning
because it is exactly GR in the CMB sector. This is not a virtue of CODA Tier 2
but a consequence of its UV nature — it simply has nothing to say about the CMB.

### 4.3 Inflation

For a de Sitter inflationary background ($H = \text{const}$, $a = e^{Ht}$):
- The de Sitter metric is conformally flat: $C_{\mu\nu\rho\sigma} = 0$
- Therefore $B_{\mu\nu} = 0$
- CODA Tier 2 field equations = GR during inflation

The inflationary background dynamics are unmodified. The Hubble rate,
number of e-folds, and slow-roll dynamics are identical to GR.

**Primordial power spectrum:** The scalar tilt $n_s$ and tensor-to-scalar
ratio $r$ receive CODA Tier 2 corrections at order
$(H_{\rm inf}/M_P)^2 \sim 10^{-10}$ (for $H_{\rm inf} \sim 10^{14}$ GeV) —
at the level of slow-roll corrections but with an extra $(H/M_P)^2$ suppression.
Unobservable with current or planned CMB experiments.
`[CODA-PREDICTION: no inflationary signature]`

### 4.4 Large-Scale Structure

The linear matter power spectrum $P(k)$ is governed by the growth factor
$D(a)$ and the sound speed of perturbations — both determined by the
perturbed Friedmann equations and perturbation growth equations. Since
CODA Tier 2 corrections to the perturbation equations are $\sim (k/M_P)^2$,
the matter power spectrum is identical to GR at all observable scales.

**Euclid / DESI / LSST constraints on $\xi$:** None from the linear power
spectrum. `[CODA-PREDICTION]`

---

## 5. The Ghost in Cosmology

### 5.1 Ghost Production in the Early Universe

The massive spin-2 ghost with mass $m_2 \sim M_P$ can in principle be
produced thermally in the early universe when $T \sim m_2 \sim M_P$ (the
Planck epoch, $t \sim t_P \sim 10^{-43}$ s).

At $T \sim M_P$: ghost production rate $\sim T^4/M_P^2$; Hubble rate
$\sim T^2/M_P$. The production-to-Hubble ratio $\sim T^2/M_P^2 \sim 1$.
Ghost modes are thermally excited near the Planck epoch.

### 5.2 Ghost Decay and Thermalization

At $T \ll M_P$ (all of observable cosmology), the ghost is non-relativistic
and cannot be thermally produced. The ghost population from the Planck epoch
would decay via its coupling to the Standard Model on timescales $\sim m_2^{-1}
\sim t_P \sim 10^{-43}$ s — far shorter than any observable epoch. By BBN
($t \sim 1$ s), any ghost population has been gone for $10^{43}$ Hubble times.

**Observational consequence:** No relic ghost density, no ghost contribution
to dark matter, no ghost-mediated interaction at BBN or later.
`[CODA-PREDICTION — note: this relies on the ghost having non-zero decay width,
which requires it to couple to Standard Model particles; this coupling is
inherited from the graviton coupling but suppressed by $m_2^{-2}$]`

### 5.3 EFT Validity in the Early Universe

The CODA EFT breaks down when the curvature scale $\sqrt{R} \sim m_2 \sim M_P$,
i.e., near the Planck epoch. The cosmological history of CODA Tier 2 is only
reliable for $t \gg t_P$ — which encompasses all of observable cosmology.
`[ESTABLISHED — standard EFT argument]`

---

## 6. CODA Tier 2 vs. AeST in the Cosmological Sector

AeST (Skordis & Złośnik 2021, PRL 127, 161302) is the current gold standard
for covariant MOND — a theory that modifies gravity in the galactic IR while
being compatible with the CMB.

| Property | GR | CODA Tier 2 | AeST |
|----------|-----|-------------|------|
| FLRW background | Standard | Identical to GR | Modified (scalar + vector sectors) |
| Friedmann equations | Standard | Identical to GR | Modified at cosmological scales |
| CMB acoustic peaks | Standard | Identical to GR | CMB-compatible by construction |
| Gravitational slip $\eta$ | 1 | 1 | $\neq 1$ (modified gravity signal) |
| MOND rotation curves | Not predicted | Not predicted | Predicted |
| Cosmological dark matter | Needs CDM | Needs CDM | Not needed (MOND replaces) |

CODA Tier 2 provides no advantage over GR in the cosmological sector —
it is simply GR at those scales. The AeST framework is the cosmological
target for CODA's **Tier 1** construction, not Tier 2.

A future CODA Tier 1 theory with a dynamical $\mathcal{C}_K(x)$ will have
cosmological perturbation equations that could potentially match AeST.
Until the Tier 1 construction is complete, CODA makes no CMB predictions
beyond GR. `[OPEN]`

---

## 7. What Tier 2 Cannot Explain

| Cosmological phenomenon | Tier 2 prediction | Observation | Status |
|------------------------|------------------|-------------|--------|
| Dark energy / $\Lambda$ | $\Lambda$ is free parameter, same as GR | Observed as $w \approx -1$ | No new prediction |
| Dark matter | Not predicted | Required for CMB + LSS | Requires CDM or Tier 1 MOND |
| Hubble tension | GR value of $H_0$ | $H_0 \approx 67$–$73$ km/s/Mpc | No resolution |
| $\sigma_8$ tension | GR value | Mild tension with CMB | No resolution |
| Baryon asymmetry | Not modified | Observed | Outside scope |
| Inflation (model) | Unmodified GR + inflaton | Many models | No prediction |
| CMB anomalies | GR predictions | Large-angle anomalies | No resolution |

All of these remain as open questions or are referred to the Tier 1 construction.

---

## 8. Tier 1 in Cosmology — Open Questions

When the Tier 1 construction ($\mathcal{C}_K(x)$ as a dynamical field) is
completed, it will modify both the background and perturbation equations in
cosmology. Based on the AeST structural target (`phenomenology/mond_thread.md`
§4.3) and the DSSYK evidence (`theory/covariant_ck.md` §4), the expected
Tier 1 cosmological modifications are:

**Background (FLRW):** A non-zero $\mathcal{C}_K(x)$ in FLRW would require
$\mathcal{C}_K \neq 0$ even in conformally flat backgrounds — this would only
be possible if $\mathcal{C}_K$ is not purely Weyl-based (Tier 2 proxy) but
has a volume-law entanglement contribution that is non-zero even in FLRW. This
is precisely what the DSSYK construction suggests: the complexity of the de
Sitter background is non-trivial (it grows as $e^{H_0 t}$) even though the
Weyl tensor vanishes. `[OPEN — Tier 1 problem]`

**Cosmological constant from complexity:** If $\mathcal{C}_K^{(dS)} \propto
S_{dS} \cdot H_0$ is the cosmological complexity, and this enters the action,
it could contribute to an effective cosmological constant. The de Sitter
DSSYK complexity growth rate $\propto S_{dS} \cdot T_{dS} \propto M_P^2 H_0$
is of order $(M_P H_0)^2 \cdot \ell_P^4 \sim H_0^2$, which is the correct
magnitude for a cosmological constant contribution. Whether this is
$\Lambda = 3H_0^2$ or a correction to it requires the full Tier 1 action
with FLRW background. `[OPEN — potentially important]`

**Cosmological perturbations with Tier 1:** Once $\mathcal{C}_K(x)$ is a
dynamical field, it contributes to both the background stress-energy and the
perturbed field equations. For the theory to be CMB-compatible (as AeST is),
the cosmological perturbations with $\mathcal{C}_K$ must reproduce the observed
CMB power spectrum. This is an explicit constraint on the Tier 1 construction —
it must pass the AeST CMB test. `[OPEN — this is the Tier 1 CMB constraint]`

---

## 9. Summary

**CODA Tier 2 in cosmology:**

The Weyl tensor vanishes for all conformally flat spacetimes. FLRW is conformally
flat. Therefore CODA Tier 2 is exactly GR at all cosmological background levels
and deviates from GR in perturbation theory only at order $(k/M_P)^2 \sim
10^{-114}$ at CMB scales.

| Test | CODA Tier 2 prediction | Observational status |
|------|----------------------|---------------------|
| Friedmann equations | Identical to GR | ✓ No tension |
| BBN light elements | Identical to GR | ✓ No tension |
| CMB power spectra | Identical to GR | ✓ No tension |
| CMB gravitational slip | $\eta = 1$ | ✓ No tension |
| Inflation background | Identical to GR | ✓ No tension |
| Primordial GW | $n_T$, $r$ identical to GR | ✓ No tension |
| GW dispersion | $v_{\rm ph} = c(1 + 10^{-72})$ | ✓ No tension |
| MOND / dark matter | Not predicted | ✗ Not addressed |
| Dark energy | Free parameter as in GR | ✗ Not addressed |

CODA Tier 2 has no observable cosmological signature at any scale accessible
to current or planned experiments. All cosmological predictions are identical
to GR. **This is not a failure of the theory — it is a correct consequence of
its UV nature.** Cosmological-scale physics belongs to the Tier 1 construction.

---

*Document version 0.1. All Tier 2 results established. Tier 1 cosmological
predictions are open pending the construction in `theory/covariant_ck.md`.*
