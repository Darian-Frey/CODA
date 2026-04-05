# CODA Tier 2 — Black Hole Phenomenology

**Document:** `phenomenology/black_hole_phenomenology.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Depends on:** `theory/field_equations.md` v0.3,
`phenomenology/weak_field_limit.md` v0.1  
**Primary sources:** Stelle (1977); Lu, Perkins, Pope & Stelle (2015),
*Phys. Rev. Lett.* **114**, 171601; Lü & Perkins (2015)  
**Epistemic flags:**
- `[ESTABLISHED]` — results from primary sources or standard GR
- `[CODA-PREDICTION]` — follows from Tier 2 field equations
- `[OPEN]` — unresolved, requires further calculation or observation

---

## 0. Purpose and Scope

This document analyses CODA Tier 2 predictions in the strong-field regime
around black holes. The central structural result (established in
`theory/field_equations.md` v0.3, §7.0) is:

**All Einstein metrics satisfy $B_{\mu\nu} = 0$ and are exact solutions of
CODA Tier 2 with the same matter content as GR.**

Since Schwarzschild, Kerr, and all their dS/AdS generalisations are Einstein
metrics, they are **unmodified** by CODA Tier 2. The interesting black hole
physics arises from a **second branch** of solutions — non-Schwarzschild black
holes carrying massive spin-2 "Weyl hair" — that exists precisely because the
$\xi C^2$ term admits additional gravitational degrees of freedom.

**Scope:**
- §1: The two branches — GR solutions vs. non-Schwarzschild solutions
- §2: The non-Schwarzschild black hole — metric and properties
- §3: Thermodynamics
- §4: Quasi-normal modes and gravitational wave signatures
- §5: Near-horizon structure and the ghost
- §6: Observational status and constraints
- §7: CODA Tier 1 implications for black holes
- §8: Open problems

---

## 1. The Two Solution Branches

### 1.1 Branch 1 — GR Solutions (Einstein Metrics) [ESTABLISHED]

Any metric satisfying $R_{\mu\nu} = \lambda g_{\mu\nu}$ is Bach-flat
($B_{\mu\nu} = 0$) and satisfies the CODA Tier 2 field equations with the
same matter as GR. The complete set of GR black holes falls in this class:

| Solution | $\lambda$ | CODA status |
|----------|-----------|-------------|
| Schwarzschild | $0$ | GR solution exactly; $B_{\mu\nu} = 0$ |
| Kerr | $0$ | GR solution exactly; $B_{\mu\nu} = 0$ |
| Reissner-Nordström | $0$ (vacuum + EM) | GR solution exactly |
| Kerr-Newman | $0$ (vacuum + EM) | GR solution exactly |
| Schwarzschild-dS/AdS | $\pm\Lambda/3$ | GR solution exactly |
| Kerr-dS/AdS | $\pm\Lambda/3$ | GR solution exactly |

All observational signatures of these black holes in CODA Tier 2 are
**identical to GR**. Merger ringdown, quasi-normal modes, photon rings,
shadow size — all are unmodified. The CODA coupling $\xi$ plays no role.

### 1.2 Branch 2 — Non-Schwarzschild Solutions (Weyl Hair) [ESTABLISHED]

The $\xi C^2$ term in the CODA action introduces a massive spin-2 degree of
freedom with mass $m_2$. This opens a second branch of asymptotically flat,
static, spherically symmetric solutions distinct from Schwarzschild. These
solutions carry **massive spin-2 hair** — a non-trivial Weyl tensor profile
that cannot be removed by a gauge transformation.

**Key reference:** Lu, Perkins, Pope & Stelle (2015), *Phys. Rev. Lett.*
**114**, 171601. (Hereafter LPPS 2015.)

These solutions exist for the same ADM mass as a Schwarzschild black hole
but differ in their near-horizon structure and in the long-range metric
through a Yukawa-type correction.

---

## 2. The Non-Schwarzschild Black Hole

### 2.1 Metric Ansatz and Field Equations

For a static, spherically symmetric metric in CODA Tier 2 (vacuum,
$T_{\mu\nu} = 0$):

$$ds^2 = -f(r)dt^2 + \frac{dr^2}{h(r)} + r^2 d\Omega^2$$

In GR, $f = h = 1 - 2GM/r$ (Schwarzschild). In CODA Tier 2, the full
field equations $G_{\mu\nu} = 32\pi G\xi\,B_{\mu\nu}$ (vacuum) admit a
second branch with $f \neq h$ in general.

### 2.2 Far-Field Expansion

At large $r$, the non-Schwarzschild solution has the form (LPPS 2015):

$$f(r) = 1 - \frac{2GM}{r} + \frac{\beta}{r}\,e^{-m_2 r}
+ \mathcal{O}(e^{-m_2 r}/r^2)$$

$$h(r) = 1 - \frac{2GM}{r} + \frac{\gamma_h}{r}\,e^{-m_2 r}
+ \mathcal{O}(e^{-m_2 r}/r^2)$$

where $\beta$ and $\gamma_h$ are integration constants parametrising the
hair amplitude, related by the field equations.

The two key points:
- At $r \gg m_2^{-1} \sim \ell_P$: the Yukawa corrections are
  $\sim e^{-m_2 r} \to 0$, and the metric is asymptotically Schwarzschild
- At $r \sim m_2^{-1}$ (sub-Planckian): the hair is non-negligible
  and the metric deviates from Schwarzschild

**For EFT-consistent $\xi < 1/4$:** $m_2^{-1} \leq \ell_P \approx 10^{-35}$ m.
The Yukawa hair is confined to sub-Planckian distances from the horizon.
At all astrophysical scales, the non-Schwarzschild solution is
observationally indistinguishable from Schwarzschild. `[CODA-PREDICTION]`

### 2.3 Near-Horizon Structure

The non-Schwarzschild solutions of LPPS (2015) have a horizon at $r = r_h$
that differs from the Schwarzschild radius $2GM$. The deviation:

$$\frac{r_h - 2GM}{2GM} \sim \frac{m_2^{-1}}{2GM} \sim \frac{\ell_P}{r_s}$$

where $r_s = 2GM$ is the Schwarzschild radius. For a solar-mass black hole:

$$\frac{r_h - r_s}{r_s} \sim \frac{10^{-35}\,\text{m}}{3\,\text{km}}
\sim 10^{-38}$$

**The horizon shift is $10^{-38}$ of the Schwarzschild radius — beyond any
conceivable measurement.** `[CODA-PREDICTION]`

### 2.4 The One-Parameter Family

For each ADM mass $M$, the non-Schwarzschild solutions form a
one-parameter family labelled by the hair amplitude $\beta$. The limiting
cases are:

- $\beta = 0$: Schwarzschild (Branch 1)
- $\beta \neq 0$: Non-Schwarzschild with Weyl hair (Branch 2)

The family interpolates continuously between Schwarzschild and solutions
with increasingly strong near-horizon Weyl corrections. LPPS (2015) find
that the two branches meet at a minimum mass (bifurcation point), analogous
to the extremal limit in charged black holes.

---

## 3. Black Hole Thermodynamics

### 3.1 Wald Entropy

In higher-derivative gravity, the Bekenstein-Hawking area formula
$S = A/4G$ is replaced by the Wald entropy:

$$S_{\rm Wald} = -2\pi\oint_{\mathcal{H}}
\frac{\partial\mathcal{L}}{\partial R_{\mu\nu\rho\sigma}}
\hat{\epsilon}_{\mu\nu}\hat{\epsilon}_{\rho\sigma}\,d\Sigma$$

where $\hat{\epsilon}_{\mu\nu}$ is the binormal to the horizon.

For CODA Tier 2 ($\mathcal{L} = R/16\pi G + \xi C^2$):

$$S_{\rm Wald} = \frac{A}{4G} + 2\xi\oint_\mathcal{H}
C^{\mu\nu\rho\sigma}\hat{\epsilon}_{\mu\nu}\hat{\epsilon}_{\rho\sigma}\,d\Sigma$$

### 3.2 Schwarzschild Black Hole (Branch 1)

For Schwarzschild, $R_{\mu\nu} = 0$ but $C_{\mu\nu\rho\sigma} \neq 0$.
However, by the symmetry of the horizon (bifurcation sphere), the Weyl
correction to the Wald entropy vanishes:

$$\oint_\mathcal{H}
C^{\mu\nu\rho\sigma}\hat{\epsilon}_{\mu\nu}\hat{\epsilon}_{\rho\sigma} = 0$$

Therefore for Schwarzschild in CODA Tier 2:

$$S_{\rm Schwarzschild}^{\rm CODA} = \frac{A}{4G}
= \frac{\pi r_s^2}{G} = 4\pi(GM)^2/G$$

**The Bekenstein-Hawking entropy of the Schwarzschild black hole is
unmodified by CODA Tier 2.** `[CODA-PREDICTION]`

### 3.3 Non-Schwarzschild Black Hole (Branch 2)

For the non-Schwarzschild branch, $C_{\mu\nu\rho\sigma} \neq 0$ at the
horizon with a specific horizon profile that does not vanish upon integration.
The Wald entropy acquires a correction:

$$S_{\rm non-Sch}^{\rm CODA} = \frac{A_h}{4G} + \delta S_{\rm Weyl}(\beta)$$

where $\delta S_{\rm Weyl} \sim \xi \cdot (m_2^{-1}/r_h)^2$ is suppressed
by the ratio of the Planck length to the horizon size — again negligible for
astrophysical black holes. `[CODA-PREDICTION]`

**Hawking temperature:** For Branch 1, $T_H = \hbar c^3/(8\pi G M k_B)$ —
identical to GR. For Branch 2, the temperature receives corrections of
order $\ell_P^2/r_h^2$. `[CODA-PREDICTION]`

---

## 4. Quasi-Normal Modes and GW Signatures

### 4.1 QNM Spectrum — Branch 1 (Schwarzschild)

The quasi-normal modes (QNMs) of Schwarzschild in CODA Tier 2 include both
the standard GR modes and new modes from the massive spin-2 sector:

**Standard graviton modes:** The massless spin-2 graviton spectrum is
identical to GR QNMs for Schwarzschild, since the background is the GR
Schwarzschild solution and the Bach tensor perturbation is suppressed at
the horizon scale.

**Massive spin-2 modes:** The ghost field of mass $m_2$ also admits QNM
oscillations around the Schwarzschild background. However, these modes
have frequencies $\omega_{\rm massive} \sim m_2 c^2/\hbar \sim M_P c^2/\hbar$
— of order the Planck frequency $\sim 10^{43}$ Hz. These are completely
outside the LIGO/Virgo/LISA band and cannot be observed.

**At observable frequencies:** CODA Tier 2 predicts identical QNMs to GR
for all standard (Branch 1) black holes. `[CODA-PREDICTION]`

### 4.2 GW Ringdown — No Deviation from GR

Current GW observations probe the ringdown signal from binary black hole
mergers at frequencies $\sim 10$–$1000$ Hz. All ringdown QNMs at these
frequencies are massless graviton modes, identical between GR and CODA
Tier 2.

**GW250114 (SNR $\approx 80$, the strongest event to date):** CODA Tier 2
predicts zero deviation from GR in the ringdown spectrum.
LVK spectroscopy (residual SNR $\leq 6.86$, $p = 0.34$) is consistent with
GR — consistent with CODA Tier 2 equally. `[CODA-PREDICTION]`

### 4.3 QNM Spectrum — Branch 2 (Non-Schwarzschild)

The non-Schwarzschild solutions carry Weyl hair that modifies the effective
potential for gravitational perturbations. Their QNM spectrum differs from
Schwarzschild by corrections of order $(m_2^{-1}/r_h)^2$.

For EFT-consistent $\xi$: the correction is $({\ell_P}/{r_h})^2 \ll 1$.
**No observable QNM difference between Branch 1 and Branch 2 black holes
for astrophysical black holes.** `[CODA-PREDICTION]`

For near-extremal or Planck-mass black holes, the two branches might be
distinguishable in principle, but such objects are not accessible to current
observations. `[OPEN]`

---

## 5. Near-Horizon Structure and the Ghost

### 5.1 The Ghost Near a Black Hole Horizon

Near a black hole horizon, spacetime curvature is $\sim 1/r_h^2$. For a
stellar-mass black hole ($r_h \sim $ km), this curvature is vastly below
the Planck scale. The ghost mass $m_2 \sim M_P$ is at the Planck scale.
Since $m_2^{-1} \sim \ell_P \ll r_h$, the ghost is essentially frozen
near astrophysical horizons — it is far too heavy to be excited by the
horizon curvature.

**For Planck-mass black holes** ($r_h \sim \ell_P$): the ghost mass $m_2$
becomes comparable to the inverse horizon radius, and the ghost can be
dynamically relevant. At this point the EFT itself breaks down, and a full
quantum gravity theory is required. `[OPEN — beyond EFT scope]`

### 5.2 Information Paradox

CODA Tier 2 does not resolve the information paradox. For Branch 1 black
holes, the near-horizon physics is identical to GR, and the information
problem is unchanged.

The CODA Tier 1 construction (`theory/covariant_ck.md`) — if completed —
would couple a dynamical complexity density to the metric. The hypothesis
that Krylov complexity encodes information content (DSSYK holographic
dictionary: complexity = bulk volume) could in principle modify the
near-horizon information structure. This is a speculative connection to
the Tier 1 programme. `[OPEN — Tier 1 question]`

---

## 6. Observational Status and Constraints

### 6.1 Shadow Size and Photon Ring

The photon ring radius and shadow size are determined by the unstable
circular orbit at $r_{\rm ph} = 3GM$ for Schwarzschild. CODA Tier 2
(Branch 1) predicts the same photon ring as GR.

**Event Horizon Telescope constraints:** The M87* and Sgr A* shadow radii
are consistent with GR Kerr to $\sim 10\%$ precision. CODA Tier 2 predicts
zero deviation. `[CODA-PREDICTION: no EHT tension]`

### 6.2 Gravitational Redshift

The gravitational redshift for photons escaping a Schwarzschild black hole
is $1 + z = (1 - r_s/r)^{-1/2}$. CODA Tier 2 gives the same result for
Branch 1. At radius $r$, the CODA correction is $\sim e^{-m_2 r}$,
completely negligible for $r \gg \ell_P$. `[CODA-PREDICTION]`

### 6.3 Binary Inspiral

The GW waveform during binary inspiral depends on the post-Newtonian
expansion of the two-body potential. At leading post-Newtonian order, the
CODA Tier 2 correction to the binary potential is:

$$\delta V_{\rm CODA}(r) = \frac{4}{3}\frac{GM_1 M_2}{r}\,e^{-m_2 r}$$

For separation $r \gg m_2^{-1} \sim \ell_P$ (all observed binary mergers):
$\delta V_{\rm CODA} \sim e^{-m_2 r} \to 0$. The inspiral waveform is
identical to GR. `[CODA-PREDICTION]`

### 6.4 Constraint Table

| Observable | CODA Tier 2 | Observation | Status |
|-----------|-------------|-------------|--------|
| Ringdown QNMs | GR values | Consistent with GR | ✓ No tension |
| Shadow radius | GR value | GR within $\sim 10\%$ | ✓ No tension |
| GW speed | $c$ | $|c_{GW}-c|/c < 5\times10^{-16}$ | ✓ No tension |
| GW polarisation | Two (TT) | Two TT modes | ✓ No tension |
| Inspiral phase | GR | Consistent with GR | ✓ No tension |
| Wald entropy | $A/4G$ (Branch 1) | Not directly measured | ✓ Consistent |

CODA Tier 2 has **no tension with any black hole observation**. It makes
no new predictions distinguishable from GR at any currently accessible scale.

---

## 7. CODA Tier 1 Implications for Black Holes

When the Tier 1 construction is completed ($\mathcal{C}_K(x)$ as a dynamical
field), it will modify the black hole field equations. Based on the DSSYK
holographic evidence (`theory/covariant_ck.md` §4), three effects are
expected:

### 7.1 Modified Near-Horizon Complexity

The DSSYK programme identifies holographic complexity with the volume of
extremal slices behind the horizon. If $\mathcal{C}_K(x)$ is the bulk
density of this complexity, it will be non-trivial near the horizon and
grow linearly in the interior (consistent with the Susskind "complexity
equals volume" picture). This would modify the near-horizon stress-energy
sourcing the metric without modifying the asymptotic behaviour.

### 7.2 Complexity-Dependent Wald Entropy

If $\mathcal{C}_K$ is a scalar field in the action, the Wald formula
acquires a $\mathcal{C}_K$-dependent correction at the horizon. For
Schwarzschild, where the DSSYK picture gives $\mathcal{C}_K \propto S_{BH}
\cdot T_H \propto M$ near the horizon, the entropy correction could be
of order $\xi \alpha \cdot S_{BH}^2/M_P^2$ — suppressed but in principle
relevant for near-extremal black holes. `[OPEN — Tier 1]`

### 7.3 BH Information Paradox

The DSSYK complexity-equals-volume dictionary gives a precise microscopic
picture: the interior of a black hole is mapped to the Krylov space of the
boundary theory. The scrambling time $t_s \sim \beta\log S$ is the timescale
for information to propagate from the horizon to the interior. If
$\mathcal{C}_K(x)$ encodes this scrambling, the information paradox becomes
a question about the structure of the Krylov basis near the Page time.

This is speculative but well-motivated by the holographic evidence.
`[OPEN — Tier 1 problem]`

---

## 8. Open Problems

| Priority | Problem | Notes |
|----------|---------|-------|
| 1 | QNM spectrum of non-Schwarzschild (Branch 2) solutions | Observable in principle for near-Planck BHs |
| 2 | Thermodynamic stability — is Branch 1 or Branch 2 preferred? | Phase structure, bifurcation point |
| 3 | Does Branch 2 merge with Branch 1 at the Planck mass? | Minimum mass / extremal limit |
| 4 | Rotating non-Schwarzschild BHs (non-Kerr with Weyl hair) | Astrophysical BHs are spinning |
| 5 | Tier 1 $\mathcal{C}_K(x)$ near the horizon — explicit calculation | DSSYK-motivated programme |
| 6 | Complexity growth inside BH and the Page time | BH information paradox |

---

## 9. Summary

**CODA Tier 2 black hole predictions:**

The vast majority of black hole physics is unmodified. GR solutions (Schwarzschild,
Kerr, etc.) are exact CODA Tier 2 solutions. All observational signatures at
astrophysical scales are identical to GR.

The only genuinely new feature is the non-Schwarzschild (Branch 2) black hole
of Lu, Perkins, Pope & Stelle (2015), which carries massive spin-2 Weyl hair.
For EFT-consistent $\xi < 1/4$, this hair is confined to sub-Planckian
distances from the horizon and is unobservable at any current or planned
experiment.

The interesting strong-field CODA physics lies in the Tier 1 construction
— the dynamical $\mathcal{C}_K(x)$ field, which will modify the near-horizon
interior in ways connected to the DSSYK holographic complexity picture.

---

*Document version 0.1. Tier 2 results established. Tier 1 black hole
predictions open pending `theory/covariant_ck.md` Tier 1 construction.*
