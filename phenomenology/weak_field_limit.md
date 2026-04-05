# CODA Tier 2 — Weak Field Limit, PPN Parameters, and Observational Tests

**Document:** `phenomenology/weak_field_limit.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Depends on:** `theory/field_equations.md` v0.2, `theory/action_principle.md` v0.2  
**Primary source:** Stelle (1977), *Phys. Rev. D* **16**, 953  
**Epistemic flags:**
- `[ESTABLISHED]` — results verified against primary sources
- `[CODA-PREDICTION]` — follows from CODA Tier 2 equations by calculation
- `[OPEN]` — unresolved question

---

## 0. Purpose and Scope

This document derives the observable predictions of CODA's Tier 2 working
theory in the weak field, slow-motion (post-Newtonian) limit. It answers
the question: *does CODA Tier 2 conflict with known Solar System tests,
short-range gravity measurements, or gravitational wave observations?*

The short answer is no — and this document explains precisely why, and at
what scale (if any) CODA Tier 2 deviates from GR.

**What this document covers:**
- The Newtonian potential correction from the Weyl² coupling
- The PPN parameters and their observational status
- Solar System tests (light deflection, perihelion advance, Shapiro delay)
- Gravitational wave speed and polarization content
- EFT self-consistency and the observational status of the ghost

**What this document does not cover:**
- MOND and galactic phenomenology → see `phenomenology/mond_thread.md`
- The Tier 1 construction → see `theory/covariant_ck.md`
- Black hole and strong-field regime → future document

---

## 1. The CODA Tier 2 Action

The working theory (from `theory/action_principle.md` v0.2):

$$S = \int d^4x\sqrt{-g}\left[\frac{R}{16\pi G}
+ \xi\, C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}
+ \mathcal{L}_m\right]$$

where $C_{\alpha\beta\gamma\delta}$ is the Weyl tensor and $\xi$ is a
dimensionless coupling constant. The field equations are:

$$G_{\mu\nu} - 32\pi G\xi\, B_{\mu\nu} = 8\pi G\, T_{\mu\nu}$$

where $B_{\mu\nu}$ is the Bach tensor (see `theory/field_equations.md` v0.2).

**Key canonical properties (established):**
- All GR vacuum solutions satisfy $B_{\mu\nu} = 0$ exactly
- FLRW cosmology is unmodified (Weyl tensor vanishes for conformally flat backgrounds)
- The trace equation is unmodified: $R = -8\pi G\, T$
- No scalar pole in the propagator (pure Einstein-Weyl, no $R^2$ term)

---

## 2. The Linearized Propagator

Linearising around flat spacetime ($g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$,
$|h_{\mu\nu}| \ll 1$), the graviton propagator in momentum space for the
spin-2 sector is (Stelle 1977):

$$\tilde{D}^{(2)}(k) \propto \frac{1}{k^2} - \frac{1}{k^2 - m_2^2}$$

where the **ghost mass** $m_2$ is set by the coupling $\xi$. From the
CODA Tier 2 equations (verified against Stelle 1977 Eq. 2.3,
$\kappa^2 = 32\pi G$, $\alpha = 2\xi$):

$$\boxed{m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}}$$

`[ESTABLISHED — Stelle 1977 Eq. 2.3]`

**Structure:** The first term is the familiar massless graviton (helicity-2,
attractive). The second is a massive spin-2 ghost at $k^2 = m_2^2$
(helicity-2, same spin but *repulsive*, due to the wrong-sign residue from
the Ostrogradski instability of the higher-derivative term). There is no
scalar (spin-0) pole because CODA Tier 2 contains no $R^2$ term.

---

## 3. The Newtonian Potential

The static potential produced by a point mass $M$ is obtained from the
propagator via a Fourier transform. From Stelle (1977) Eq. 2.3:

$$\boxed{\Phi(r) = -\frac{GM}{r}\left(1 - \frac{4}{3}\,e^{-m_2 r}\right)}$$

`[ESTABLISHED — Stelle 1977 Eq. 2.3]`

**Interpretation:**

- **Massless graviton term** $(-GM/r)$: the standard Newtonian attraction.
- **Yukawa correction** $(+\frac{4}{3}GM e^{-m_2 r}/r)$: a *repulsive*
  Yukawa correction from the massive ghost. It partially screens the
  Newtonian attraction at short ranges.

**Limiting behaviour:**

| Range | $\Phi(r)$ | Force |
|-------|-----------|-------|
| $r \gg m_2^{-1}$ | $-GM/r$ | $-GM/r^2$ (standard Newtonian) |
| $r \sim m_2^{-1}$ | $-GM/r \cdot (1 - 4/3 e^{-1})$ | Modified |
| $r \ll m_2^{-1}$ | $+GM/(3r)$ | $+GM/(3r^2)$ (repulsive!) |

The gravity becomes *repulsive* at sub-Planckian distances — a gravitational
short-distance screening effect from the ghost. This is academically
interesting but observationally inaccessible.

**The fractional deviation from Newtonian gravity:**

$$\frac{|\Phi_{\rm CODA} - \Phi_{\rm GR}|}{|\Phi_{\rm GR}|}
= \frac{4}{3}\,e^{-m_2 r}$$

For natural coupling $\xi \sim O(1)$: $m_2 \sim M_P$,
so $m_2^{-1} \sim \ell_P \approx 1.6 \times 10^{-35}$ m.

At $r = 50\,\mu\text{m}$ (the most sensitive sub-mm gravity test):

$$\frac{4}{3}\,e^{-m_2 r} \approx \frac{4}{3}\,
\exp\!\left(-\frac{5 \times 10^{-5}}{1.6 \times 10^{-35}}\right)
= \frac{4}{3}\,e^{-3 \times 10^{30}} \approx 10^{-10^{30}}$$

This is unmeasurably zero. **[CODA-PREDICTION]**

---

## 4. PPN Parameters

The Parametrized Post-Newtonian (PPN) framework characterises weak-field
gravity theories by a set of dimensionless parameters. The two most
important are:

**$\gamma$** — measures how much space is curved per unit rest mass
(probed by light deflection, Shapiro delay, VLBI):
$$1 + \gamma = \frac{\Phi_{ij}}{\Phi_{00}}
\quad\text{(ratio of spatial to time-time metric perturbation)}$$

**$\beta$** — measures nonlinearity in the gravitational superposition
(probed by perihelion advance):

For GR: $\gamma = \beta = 1$.

### 4.1 CODA Tier 2 PPN Values

At scales $r \gg m_2^{-1}$ (all experimentally accessible scales), the
Yukawa correction $e^{-m_2 r} \to 0$ identically. The linearised metric
at these scales is the GR weak-field metric. Therefore:

$$\gamma = 1, \qquad \beta = 1 \qquad (r \gg m_2^{-1})$$

`[CODA-PREDICTION]`

CODA Tier 2 makes no deviation from GR in any PPN parameter at any
measurable scale. This is not fine-tuning — it follows structurally
from the Yukawa range being sub-Planckian.

### 4.2 Observational Constraints vs. CODA Tier 2

| Test | Quantity | Measurement | CODA Tier 2 | Reference |
|------|----------|-------------|-------------|-----------|
| Cassini Shapiro delay | $\gamma - 1$ | $(2.1 \pm 2.3)\times 10^{-5}$ | $0$ | Bertotti et al. 2003 |
| Lunar Laser Ranging | $\beta - 1$ | $(-1.2 \pm 1.1)\times 10^{-4}$ | $0$ | Williams et al. 2004 |
| Mercury perihelion | $2\gamma - \beta + 2$ | $0.9998 \pm 0.0006$ | $3$ | match | Pireaux & Rozelot 2003 |
| VLBI light deflection | $\gamma$ | $0.99983 \pm 0.00045$ | $1$ | match | Fomalont et al. 2009 |
| Eöt-Wash ($r > 52\,\mu$m) | Yukawa deviation | $|\alpha| < 10^{-2}$ | $\sim e^{-10^{30}}$ | match | Kapner et al. 2007 |

All Solar System and sub-mm gravity tests are passed with zero tension.

### 4.3 Constraint on $\xi$ from Sub-mm Gravity

The Eöt-Wash torsion balance tests (Kapner et al. 2007) rule out Yukawa
deviations from Newtonian gravity at strength $|\alpha| > 10^{-2}$
for ranges $\lambda > 52\,\mu$m, constraining:

$$m_2^{-1} < 52\,\mu\text{m}
\implies m_2 > 3.8 \times 10^{-3}\,\text{eV}/c^2$$

In terms of $\xi$:

$$\xi < \frac{M_P^2 c^4}{4 m_2^2 c^4}
= \frac{(1.22 \times 10^{28}\,\text{eV})^2}
{4\,(3.8 \times 10^{-3}\,\text{eV})^2}
\approx 10^{61}$$

**The observational upper bound is $\xi \lesssim 10^{61}$.**

The EFT self-consistency bound (ghost mass above Planck scale) requires
$m_2 > M_P$, giving:

$$\xi < \frac{1}{4}$$

**The theoretical EFT bound ($\xi < 1/4$) is $62$ orders of magnitude more
restrictive than the observational bound.** All observational tests are
trivially satisfied for any $\xi$ in the natural EFT range. `[CODA-PREDICTION]`

---

## 5. Solar System Tests

### 5.1 Light Deflection

Light bending by the Sun is controlled by $(1 + \gamma)/2$. For CODA Tier 2
with $\gamma = 1$, the predicted deflection is:

$$\delta\theta = \frac{4GM_\odot}{c^2 b}\,\frac{1+\gamma}{2}
= \frac{4GM_\odot}{c^2 b}$$

where $b$ is the impact parameter. This matches GR exactly. The observed
value (VLBI) agrees with GR to $0.045\%$. `[CODA-PREDICTION: matches GR]`

### 5.2 Perihelion Advance of Mercury

The relativistic contribution to Mercury's perihelion advance is:

$$\dot{\omega}_{\rm rel} = \frac{6\pi GM_\odot}{c^2 a(1-e^2)}
\left(\frac{2 + 2\gamma - \beta}{3}\right)$$

For CODA Tier 2 ($\gamma = \beta = 1$):
$\dot{\omega}_{\rm CODA} = \dot{\omega}_{\rm GR} = 42.98$ arcsec/century.

Observed: $43.13 \pm 0.14$ arcsec/century (consistent with GR).
`[CODA-PREDICTION: matches GR]`

### 5.3 Shapiro Time Delay

The radar echo delay for signals passing near the Sun:

$$\Delta t = \frac{2GM_\odot}{c^3}(1 + \gamma)\log\!\left(\frac{4r_E r_P}{b^2}\right)$$

For CODA Tier 2 ($\gamma = 1$): matches GR. The Cassini measurement
$|\gamma - 1| < 2.3 \times 10^{-5}$ is trivially satisfied. `[CODA-PREDICTION: matches GR]`

---

## 6. Gravitational Wave Sector

### 6.1 Propagating Degrees of Freedom

CODA Tier 2 has two classes of propagating gravitational degrees of freedom:

**Massless spin-2 (graviton):** Standard GR gravitational waves with
two polarizations (plus $h_+$ and cross $h_\times$). Speed $c_{GW} = c$.

**Massive spin-2 (ghost):** Additional propagating mode with mass $m_2$.
Below the mass threshold frequency $f < m_2 c^2/h$, this mode does not
propagate as a real on-shell state. Above threshold, it appears as a
massive ghost resonance.

**The threshold frequency:**

$$f_{\rm threshold} = \frac{m_2 c^2}{h}
= \frac{M_P c^2}{2\sqrt{\xi}\,h}$$

For $\xi = 1/4$ (the EFT boundary):

$$f_{\rm threshold} = \frac{M_P c^2}{h}
= \frac{(1.22 \times 10^{19}\,\text{GeV})\cdot c^2}{h}
\approx 2.9 \times 10^{42}\,\text{Hz}$$

For natural coupling $\xi \sim O(1)$, the threshold frequency is of order
$10^{42}$–$10^{43}$ Hz. `[CODA-PREDICTION]`

**For comparison:**
| Detector | Frequency band | CODA ghost threshold |
|----------|---------------|---------------------|
| LIGO/Virgo | $10$–$10^3$ Hz | $\sim 10^{43}$ Hz (unreachable) |
| LISA | $10^{-4}$–$10^{-1}$ Hz | $\sim 10^{43}$ Hz (unreachable) |
| PTA (NANOGrav) | $\sim 10^{-9}$ Hz | $\sim 10^{43}$ Hz (unreachable) |

**The massive ghost is unobservable at any planned or conceivable detector.**

### 6.2 GW Propagation Speed

For massless gravitons in CODA Tier 2: $c_{GW} = c$ exactly.

The GW170817 / GRB170817A constraint:
$$\left|\frac{c_{GW} - c}{c}\right| < 5 \times 10^{-16}$$

CODA Tier 2 satisfies this constraint exactly, with zero tension.
`[CODA-PREDICTION: $c_{GW} = c$]`

### 6.3 GW Polarization Content

At observable frequencies ($f \ll f_{\rm threshold}$), CODA Tier 2 predicts
exactly two GW polarizations ($h_+$ and $h_\times$), identical to GR.

The massive spin-2 mode, even if it were kinematically accessible, would
add four additional polarization states (the massive spin-2 has five
helicity states, minus the two that coincide with the massless ones). At
sub-threshold frequencies these are not propagating on-shell modes and
do not appear in the GW polarization spectrum.

LISA polarization tests and pulsar timing anisotropy tests will measure
GW polarization content. CODA Tier 2 predicts: two polarizations, GR
values. `[CODA-PREDICTION]`

---

## 7. EFT Validity and the Ghost

### 7.1 Why the Ghost Is Not a Problem for CODA

The massive spin-2 ghost (Ostrogradski instability from the $C^2$ term)
is a well-known feature of higher-derivative gravity. It appears in the
propagator as a pole with the wrong sign. In quantum field theory language,
this corresponds to a state with negative norm — a pathology that would
signal non-unitarity.

However, CODA adopts the standard **EFT perspective** on this ghost:

1. The ghost mass $m_2 = M_P/(2\sqrt{\xi}) \geq M_P$ (for $\xi \leq 1/4$)
   is at or above the Planck scale.
2. The EFT description of CODA is only valid below the Planck scale.
3. Above $M_P$, quantum gravity effects (whatever their full form) will
   resolve the ghost. The Weyl² term is itself an EFT correction to GR;
   its pathological UV behaviour is a signal that the EFT breaks down, not
   that the physical theory is sick.

This is the same argument used for all higher-derivative EFTs — the
Euler-Heisenberg Lagrangian contains higher-derivative terms whose
Ostrogradski modes sit above the electron mass; they are not "real"
instabilities of electrodynamics, just signals that the EFT breaks down
above that scale.

### 7.2 The EFT Condition

For CODA Tier 2 to be a self-consistent EFT, the ghost mass must lie above
the cutoff of the EFT. Taking the cutoff at $M_P$:

$$m_2 \geq M_P \iff \xi \leq \frac{1}{4}$$

For $\xi \ll 1$ (perturbative regime), $m_2 \gg M_P$ and the EFT is
well-behaved over an even wider range. For $\xi \sim O(1)$, the EFT is
valid up to Planck scale, which is all that is needed.

**Summary of constraints on $\xi$:**

| Constraint | Bound | Type |
|-----------|-------|------|
| EFT self-consistency | $\xi < 1/4$ | Theoretical (sharp) |
| Sub-mm gravity (Eöt-Wash) | $\xi < 10^{61}$ | Observational (weak) |
| GW speed (GW170817) | $\xi$ unconstrained | No tension |
| PPN $\gamma$ (Cassini) | $\xi$ unconstrained | No tension |

The EFT bound is the operative constraint, and it is satisfied for any
$\xi \sim O(1)$.

---

## 8. What Tier 2 Cannot Predict

For completeness, this section states explicitly what CODA Tier 2 does
**not** predict and **cannot** predict within its domain of validity:

| Observable | Tier 2 prediction | Actual observation | Status |
|-----------|------------------|-------------------|--------|
| MOND rotation curves | GR (flat to $r^{-2}$) | Flat at large $r$ | **Tier 2 cannot explain MOND** |
| $a_0 = 1.2\times 10^{-10}$ m/s² | Not predicted | Observed empirically | Requires Tier 1 |
| Bullet Cluster dark matter | GR lensing only | Anomalous mass distribution | Requires Tier 1 or CDM |
| PPN deviations | GR values | GR values | Match (no tension, no new prediction) |
| Sub-mm Yukawa | $\sim 10^{-10^{30}}$ | No deviation detected | Match (no tension, no new prediction) |

The UV/IR polarity problem documented in `phenomenology/mond_thread.md`
§0 means that Tier 2 is constitutionally unable to produce MOND-scale
modifications. This is not a failure of CODA as a programme — it is
a correct assignment of phenomena to their proper theoretical tier.

---

## 9. Summary

**CODA Tier 2 in the weak field limit:**

$$\Phi(r) = -\frac{GM}{r}\left(1 - \frac{4}{3}\,e^{-m_2 r}\right),
\qquad m_2 = \frac{M_P}{2\sqrt{\xi}}$$

**For $\xi \sim O(1)$ (natural EFT coupling):**

- Yukawa correction range: $m_2^{-1} \sim \ell_P \approx 10^{-35}$ m
- Fractional deviation from Newtonian gravity at 50 μm:
  $\sim e^{-10^{30}} \approx 0$
- PPN parameters: $\gamma = \beta = 1$ (GR values)
- All Solar System tests: passed with zero tension
- GW speed: $c_{GW} = c$ exactly
- GW polarizations: two (plus, cross), GR values
- Ghost mass: $m_2 \sim M_P$, threshold frequency $\sim 10^{43}$ Hz
- EFT validity: self-consistent for $\xi < 1/4$

**CODA Tier 2 is phenomenologically indistinguishable from GR at all
currently accessible scales.** This is a structural feature, not fine-tuning.
The Weyl² coupling is a UV modification; all deviations are Planck-suppressed.

Any new observable predictions from CODA require the Tier 1 construction
(see `theory/covariant_ck.md` and `phenomenology/mond_thread.md`).

---

## 10. Open Questions

`[OPEN]` — How does the weak field limit change in the presence of
the Tier 1 correction $\alpha\mathcal{C}_K(x)$? If $\mathcal{C}_K(x)$
acquires a gradient in the weak field, it will contribute to PPN parameters.
This requires completing the Tier 1 construction.

`[OPEN]` — Are there stochastic GW background signals from the Planck-scale
ghost modes in the early universe? This would require a cosmological
perturbation theory analysis beyond the scope of this document.

`[OPEN]` — Does the Bach tensor $B_{\mu\nu}$ receive corrections from
the Tier 1 complexity density at sub-Planckian curvatures? If so, the
field equations are modified at scales below the standard EFT cutoff.

---

*Document version 0.1. All Tier 2 results established and verified against
Stelle (1977). PPN values follow from the Yukawa potential by standard
post-Newtonian expansion.*