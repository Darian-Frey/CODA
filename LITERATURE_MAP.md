# CODA Literature Map

**Document:** `LITERATURE_MAP.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.2  
**Purpose:** Maps the theoretical lineage of CODA, organises the
literature by role, and records what has been drawn from, adapted,
ruled out, or targeted from each source.

**Changelog v0.2:**
- Heller et al. (2025) added as `[FOUNDATION]` in Tier 2
- Aguilar-Gutierrez (2024) added as `[FOUNDATION]` in Tier 2
- Lu, Perkins, Pope & Stelle (2015) added as `[FOUNDATION]` in Tier 1
- Blommaert, Mertens & Papalini (2024) added as `[FOUNDATION]` in Tier 2
- Maldacena-Shenker-Stanford entry updated with DSSYK/chaos bound route
- Bisognano-Wichmann section reference corrected to `covariant_ck.md` §7
- Monitoring table updated — DSSYK/dS Krylov entry substantially advanced

---

## How to Read This Document

References are organised by their **role in CODA**, not by topic or
date. Each entry states what CODA takes from that work, what it
modifies or extends, and any critical limitations.

**Role tags:**
- `[FOUNDATION]` — Results used directly in CODA derivations
- `[TEMPLATE]` — Structural or methodological model for CODA
- `[TARGET]` — Framework CODA aims to derive from first principles
- `[BRIDGE]` — Connects CODA's information-theoretic foundations to phenomenology
- `[CONSTRAINT]` — Observational or theoretical result CODA must satisfy
- `[RULED OUT]` — Work considered but found incompatible with CODA's framework

---

## Tier 1 — Direct Foundations

### Stelle, K.S. (1977) `[FOUNDATION]`
**"Renormalization of Higher-Derivative Quantum Gravity"**  
*Phys. Rev. D* **16**, 953.

The authoritative source for all numerical results in CODA's Tier 2
working theory. CODA draws directly on:

- **Eq. 2.1** — Action convention and $\kappa^2 = 32\pi G$ definition
- **Eq. 2.3** — Ghost mass $m_2 = (\frac{1}{2}\alpha\kappa^2)^{-1/2}$
  and Newtonian potential $\Phi = -GM/r(1 - \frac{4}{3}e^{-m_2 r})$
- **Appendix Eq. A5** — Weyl identity:
  $\int\sqrt{-g}(R_{\mu\nu}^2 - \frac{1}{3}R^2) = \frac{1}{2}\int\sqrt{-g}C^2$

Resolved a factor-of-4 disagreement between three independent models
in CODA's research sessions (see `audit/`). All CODA ghost mass and
coupling results are verified against this source.

---

### Bach, R. (1921) `[FOUNDATION]`
**"Zur Weylschen Relativitätstheorie"**  
*Mathematische Zeitschrift* **9**, 110.

Original definition of the Bach tensor $B_{\mu\nu}$ as the equation
of motion for the Weyl-squared action. CODA uses:
- The definition $B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma}
  + \frac{1}{2}R^{\rho\sigma}C_{\mu\rho\nu\sigma}$
- Its properties: symmetric, traceless (4D), covariantly conserved,
  vanishes for all Einstein metrics

---

### Boulware, D.G. & Deser, S. (1985) `[FOUNDATION]`
**"String-Generated Gravity Models"**  
*Phys. Rev. Lett.* **55**, 2656.

Variation of Weyl-squared action and ghost analysis for
Einstein-Weyl gravity. Confirms $\frac{\delta(\sqrt{-g}C^2)}
{\delta g^{\mu\nu}} = -2\sqrt{-g}B_{\mu\nu}$ (in CODA's Bach
tensor convention).

---

### Lu, H., Perkins, A., Pope, C.N. & Stelle, K.S. (2015) `[FOUNDATION]`
**"Black Holes in Higher-Derivative Gravity"**  
*Phys. Rev. Lett.* **114**, 171601.

Establishes the existence of a second branch of static, spherically
symmetric, asymptotically flat black hole solutions in Einstein-Weyl
gravity — distinct from Schwarzschild and carrying massive spin-2
Weyl hair. CODA draws directly on:

- The non-Schwarzschild metric ansatz and far-field Yukawa expansion:
  $f(r) = 1 - 2GM/r + (\beta/r)e^{-m_2 r} + \ldots$
- The two-branch structure: Branch 1 (Schwarzschild, Bach-flat) and
  Branch 2 (Weyl hair, $B_{\mu\nu} \neq 0$)
- The bifurcation point where the two branches meet at a minimum mass

These solutions are the only regime where CODA Tier 2 genuinely departs
from GR in the strong-field sector. Full analysis in
`phenomenology/black_hole_phenomenology.md`.

**Limitation:** The Yukawa hair is confined to sub-Planckian distances
from the horizon for EFT-consistent $\xi < 1/4$. The non-Schwarzschild
branch is observationally inaccessible at astrophysical scales.

---

## Tier 2 — Krylov Complexity Framework

### Avdoshkin, A., Dymarsky, A. & Smolkin, M. (2022/2024) `[FOUNDATION]`
**"Krylov Complexity in Quantum Field Theory, and Beyond"**  
*JHEP* (2024), arXiv:2212.14429

Foundational extension of Krylov complexity to local operators in
continuum QFT. CODA draws on:

- Lanczos coefficient growth $b_n \sim n$ for local operators in
  continuous QFT, controlled by UV cutoff
- The relation between the spectral density $f_2(\omega)$, its
  moments $\mu_k$, and the Lanczos coefficients $\{b_n\}$
- The demonstration that Krylov complexity in QFT is a global,
  not local, quantity — the key obstacle to CODA's Tier 1 construction

**Limitation for CODA:** All results are for global Hilbert space
operators on flat or highly symmetric backgrounds. No covariant
local density is defined or attempted.

---

### Caputa, P. et al. (2023-2024) `[FOUNDATION]`
**Modular Krylov complexity — multiple papers**

Extension of Krylov complexity to modular Hamiltonians $K_A = -\log\rho_A$
of boundary subregions, using Tomita-Takesaki theory. This is the
closest existing framework to CODA's Tier 1 construction:

- Replaces global Hamiltonian with the covariant modular Hamiltonian
- Localises complexity to a region $A$, not yet to a point
- Works on arbitrary Lorentzian backgrounds
- Has been used to extract geometric data (area operators, islands)
  in holographic settings

**CODA's Tier 1 proposal** is to take the continuum limit of modular
Krylov complexity as $A$ shrinks to a point — the $\epsilon \to 0$
limit that is currently not known to exist (see `covariant_ck.md`).

---

### Susskind, L. & Brown, A.R. et al. (2016) `[FOUNDATION]`
**"Complexity Equals Action"**  
*Phys. Rev. Lett.* **116**, 191301 and *Phys. Rev. D* **93**, 086006

Susskind's "Complexity=Action" (CA) conjecture: the quantum complexity
of the holographic boundary state equals the gravitational action of
the Wheeler-DeWitt patch. CODA extends this by coupling the complexity
back to the Einstein Field Equations — the action is no longer just
a measure of complexity but is modified by it.

---

### Bisognano, J.J. & Wichmann, E.H. (1975/1976) `[FOUNDATION]`
**"On the Duality Condition for a Hermitian Scalar Field" and
"On the Duality Condition for Quantum Fields"**  
*J. Math. Phys.* **16**, 985 and **17**, 303

Establishes the connection between modular flow and spacetime geometry
for Rindler wedges in Minkowski space (Bisognano-Wichmann theorem).
This is the rigorous mathematical foundation for the claim that
modular Hamiltonians are the covariant replacement for global time
evolution in algebraic QFT — a key assumption in CODA's Tier 1
construction. Extension to general curved spacetimes is an open
problem noted as Priority 7 in `covariant_ck.md` §7.

---

### Almheiri, A., Dong, X. & Harlow, D. (2015) `[FOUNDATION]`
**"Bulk Locality and Quantum Error Correction in AdS/CFT"**  
*JHEP* **2015**, 163.

Quantum error-correcting code structure of holographic spacetime.
Establishes that bulk locality emerges from quantum error correction
in the boundary theory. Provides conceptual grounding for the idea
that local spacetime properties — including complexity density — are
encoded in the quantum information structure of the boundary state.

---

### Maldacena, J., Shenker, S.H. & Stanford, D. (2016) `[FOUNDATION]`
**"A Bound on Chaos"**  
*JHEP* **2016**, 106.

The Lyapunov exponent bound $\lambda_L \leq 2\pi T$ in quantum chaotic
systems. CODA draws on this in two distinct roles:

**Role 1 — Scrambling time:** The scrambling time $t_s \sim \beta\log S$
sets the timescale for information to spread across a black hole, relevant
to the BH information paradox discussion in `phenomenology/black_hole_phenomenology.md`.

**Role 2 — DSSYK chaos bound route to $a_0$:** The DSSYK holographic dual
to de Sitter is maximally chaotic at temperature $T_{dS} = H_0/2\pi$,
saturating this bound with Lyapunov exponent $\lambda_K = 2\pi T_{dS} = H_0$.
This defines a characteristic timescale $\tau^* = H_0^{-1}$ and hence the
acceleration scale $a_0 = c/\tau^* = cH_0$ — Route 1 of the three
independent derivations in `phenomenology/mond_thread.md` §5.2.
[ESTABLISHED from Aguilar-Gutierrez 2024, §4.1]

---

### Aguilar-Gutierrez, S.E. (2024) `[FOUNDATION]`
**"Towards Complexity in de Sitter Space from the Double-Scaled
Sachdev-Ye-Kitaev Model"**  
*JHEP* **10** (2024), 107. arXiv:2403.13186

The paper that provides CODA's most concrete Krylov complexity results
in a de Sitter holographic setting. CODA draws directly on:

- **Eq. 4.10** — Explicit Lanczos coefficients for physical operators
  in the DSSYK/LdS2/SdS3 triality:
  $b_n = n\sqrt{(n^2 - \nu^2/4)/(4n^2-1)} \to n/2$ for large $n$
- **Eq. 4.15** — Late-time exponential Krylov complexity
  $C_K(\tau \gg 1) \propto e^{H_0\tau}$, saturating the MSS chaos bound
- **Eq. 4.13-4.14** — Closed-form exact result for $\nu = 1/2$:
  $b_n = n/2$, $C_K(\tau) = \sinh^2(\tau/2)$
- The identification $\lambda_K = H_0$ (Lyapunov exponent equals
  the Hubble parameter) — Route 1 of the $a_0 \sim cH_0$ derivation

**Role in CODA:** Provides the established Lanczos growth rate
$\alpha = H_0/2$ that CODA's Phase 3a programme required. Confirms
that in the correct (holographic, chaotic) dS setting, Krylov
complexity saturates the chaos bound with exponent $H_0$. This is
the missing element that the Q4 free-scalar analysis could not provide.

**Limitation for CODA:** Results are in the DSSYK boundary QM dual to
2D/3D de Sitter. The lift to a local density in 4D dS is the Priority 1
open problem in `covariant_ck.md` §7.

---

### Heller, M.P., Ori, F., Papalini, J., Schuhmann, T. & Wang, M.-T. (2025) `[FOUNDATION]`
**"De Sitter Holographic Complexity from Krylov Complexity in DSSYK"**  
arXiv:2510.13986. (Submitted October 2025)

The paper establishing the first explicit duality between cosmological
holographic complexity and microscopic boundary Krylov complexity. CODA
draws directly on:

- **Eq. 21** — The dS complexity dictionary:
  $2|\log q|\,C_K(\chi)_{\theta\approx\pi} = -i\,L_{dS}(\chi)$
- **Eq. 20** — Classical dS Krylov complexity function:
  $C_K(\chi) \propto \log[\cosh(\chi\theta/2)] - \log\theta$
  — quadratic-to-linear transition at $\chi \sim \ell_{dS}$
- **Eq. 23** — Higher-dimensional holographic complexity proposal
  in $dS_{d+1}$: extremal timelike volumes anchored at $\mathcal{I}^\pm$
- **Eq. 70** — Late-time growth rate proportional to $S_{dS} \cdot T_{dS}
  = S_{dS} \cdot H_0/(2\pi)$ in all dimensions
- **Supplemental §3** — Volume integrand of the timelike extremal slice:
  the candidate local complexity density (Route 2 of $a_0$ derivation)

**Role in CODA:** Provides the explicit dS Krylov function whose
quadratic-to-linear transition at $\chi \sim \ell_{dS}$ gives
$a_{\rm transition} = c^2/\ell_{dS} = cH_0 = a_0$ (Route 2 of the
three-route derivation in `phenomenology/mond_thread.md` §5.2).
Also provides the limiting extremal surface as the DSSYK-informed
candidate for a state-independent $\mathcal{C}_K(x)$ in the bulk
(see `theory/covariant_ck.md` §4.3).

The authors identify *"microscopic realizations in higher dimensions"*
as the most pressing open question — precisely CODA's Priority 1 problem.

**Limitation for CODA:** Microscopic derivation from DSSYK only in 2D.
Higher-dimensional extension (Eq. 23) holds for the integrated complexity;
the local density construction is the remaining open step.

---

### Blommaert, A., Mertens, T.G. & Papalini, J. (2024) `[FOUNDATION]`
**"The Dilaton Gravity Hologram of Double-Scaled SYK"**  
arXiv:2404.03535

Establishes the precise duality between disk-level sine dilaton gravity
and the DSSYK model — the backbone of the Heller et al. (2025) dS
complexity construction. CODA draws on this for:

- The holographic dictionary $\hat{H}_{\rm grav} = \hat{T}_{\rm DSSYK}$
  (gravitational Hamiltonian = DSSYK transfer matrix)
- The Weyl rescaling that maps the effective AdS2 geometry to the original
  dS2 geometry (the mechanism underlying the dS complexity derivation)
- The temperature formula $\beta(\theta)$ and its dS limit $\theta \approx \pi$

**Role in CODA:** Background infrastructure for the DSSYK/dS holographic
programme. Understanding the sine dilaton / DSSYK dictionary is
prerequisite for extending DSSYK Krylov results to 4D de Sitter.

---

## Tier 3 — MOND and Modified Gravity Frameworks

### Milgrom, M. (1983) `[BRIDGE]`
**"A modification of the Newtonian dynamics as a possible alternative
to the hidden mass hypothesis"**  
*Astrophys. J.* **270**, 365.

Original MOND papers establishing the interpolating relation
$a = \mu(a_N/a_0)a_N$, the Milgrom scale
$a_0 \approx 1.2 \times 10^{-10}$ m/s², and the deep-MOND limit.
The observational target CODA's MOND thread must reproduce.

---

### Bekenstein, J. & Milgrom, M. (1984) `[TEMPLATE]`
**"Does the missing mass problem signal the breakdown of Newtonian
gravity?"**  
*Astrophys. J.* **286**, 7.

AQUAL (Aquadratic Lagrangian) — the nonlinear kinetic scalar template
for covariant MOND. The action:

$$S_{\rm AQUAL} = \int d^4x\sqrt{-g}\,\frac{a_0^2}{8\pi G}\,
F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)$$

with $F(y) \to y$ for $y \gg 1$ and $F(y) \to \frac{2}{3}y^{3/2}$
for $y \ll 1$ is the structural template for how $\mathcal{C}_K(x)$
should enter CODA's MOND sector. CODA's proposal is that the
function $F$ is derived from the modular Lanczos structure rather
than postulated.

---

### Bekenstein, J.D. (2004) `[TEMPLATE]`
**"Relativistic gravitation theory for the modified Newtonian dynamics
paradigm"**  
*Phys. Rev. D* **70**, 083509. (TeVeS)

First relativistic covariant MOND theory (Tensor-Vector-Scalar).
Demonstrates that the AQUAL structure can be elevated to a fully
covariant theory but requires an auxiliary timelike vector field.
This motivates CODA's identification of the Krylov flow vector
$u^\mu$ as the natural candidate for this role.

**Known failures:** Gravitational wave speed deviations ruled out
by GW170817; ghost instabilities in some parameter ranges; struggles
with CMB and large-scale structure.

---

### Skordis, C. & Złośnik, T. (2021) `[TARGET]`
**"A New Relativistic Theory for Modified Newtonian Dynamics"**  
*Phys. Rev. Lett.* **127**, 161302. (AeST)

The current state-of-the-art covariant MOND theory. Ghost-free at
second order, compatible with CMB power spectrum and matter power
spectrum, replaces Milgrom's dimensionful $a_0$ with a dimensionless
coupling $K_B$ whose cosmological value reproduces the
$a_0 \sim cH_0$ coincidence.

**Role in CODA:** AeST is the **structural target** for CODA's MOND
thread. CODA claims the AeST field content (scalar + timelike vector
+ metric) maps onto objects that arise naturally from the Tier 1
Krylov construction, providing a first-principles derivation of the
AeST structure rather than postulating it.

**Mapping:**

| AeST field | CODA Tier 1 candidate |
|------------|----------------------|
| Scalar $\phi$ | $\mathcal{C}_K(x)$ |
| Timelike vector $A^\mu$ | Krylov flow vector $u^\mu$ |
| Kinetic function $F$ | Modular Lanczos structure |
| Scale $K_B$ | De Sitter modular transition |

[This mapping is a CODA hypothesis — not yet derived.]

---

### Verlinde, E. (2017) `[BRIDGE]`
**"Emergent Gravity and the Dark Universe"**  
*SciPost Phys.* **2**, 016. (arXiv:1611.02269)

Information-theoretic derivation of MOND phenomenology from de Sitter
entanglement entropy. The key result for CODA:

$$a_0 \sim cH_0$$

emerges from the de Sitter horizon surface gravity — the point where
volume-law entanglement entropy overtakes area-law contributions.
This is the strongest existing bridge between an entropy/information
concept and the Milgrom scale.

**Role in CODA:** Provides the conceptual framework for CODA's $a_0$
derivation programme (see `phenomenology/mond_thread.md` §5.2).
The hypothesis is that CODA's $\mathcal{C}_K(x)$ captures the
volume-law/area-law transition via the modular Krylov construction.

**Limitations:** Not a covariant local field theory; applies cleanly
only to isolated spherical systems; under-predicts cluster lensing
by factor $\sim 3$.

---

### Jacobson, T. (1995) `[BRIDGE]`
**"Thermodynamics of Spacetime: The Einstein Equation of State"**  
*Phys. Rev. Lett.* **75**, 1260.

Derives Einstein's equations from the Clausius relation
$\delta Q = T\,dS$ applied to local Rindler horizons with area-law
entropy. Shows GR is an equation of state, not a fundamental law.

**Role in CODA:** Conceptual grounding for the mean-field treatment
of state-dependent $\mathcal{C}_K(x)$. CODA's state-dependence
problem (documented in `covariant_ck.md` §3.2) may be resolved by
treating $\mathcal{C}_K$ as an equation-of-state quantity rather
than a fundamental field — analogous to Jacobson's treatment of
$T_{\mu\nu}$.

---

## Tier 4 — Observational Constraints

### LIGO-Virgo-KAGRA Collaboration (2021/2025) `[CONSTRAINT]`
**GW250114 — detection and spectroscopy papers**

The most clearly recorded gravitational wave signal to date (SNR 80).
The LVK spectroscopy paper shows:
- Ringdown fully consistent with Kerr QNMs (220 and 221 modes)
- Residual network SNR ≤ 6.86 at 90% credibility (p = 0.34)
- No unexplained spectral features at 355 Hz or any other frequency

This ruled out CODE-GEO's empirical claims and establishes that any
CODA prediction involving GW phenomenology must be testable against
genuinely anomalous residuals in future high-SNR events.

---

### McGaugh, S., Lelli, F. & Schombert, J. (2016) `[CONSTRAINT]`
**"Radial Acceleration Relation in Rotationally Supported Galaxies"**  
*Phys. Rev. Lett.* **117**, 201101.

The Radial Acceleration Relation (RAR/MDAR): a tight empirical
correlation between observed centripetal acceleration and baryonic
Newtonian acceleration across 153 galaxies, with scatter at the
level of observational uncertainty. Any MOND-compatible theory must
reproduce this without fine-tuning. CODA's MOND predictions, once
developed, will be tested against this dataset.

---

### Famaey, B. & McGaugh, S. (2012) `[CONSTRAINT]`
**"Modified Newtonian Dynamics (MOND): Observational Phenomenology
and Relativistic Extensions"**  
*Living Rev. Relativ.* **15**, 10. (arXiv:1112.3960)

Comprehensive review of MOND observational successes and failures.
The definitive reference for MOND constraints. CODA's MOND thread
uses this as the primary source for the observational target
specification in `phenomenology/mond_thread.md` §1.

---

## Ruled Out or Superseded

### Mannheim, P.D. & Kazanas, D. (1989) `[RULED OUT for CODA Tier 2]`
**"Exact vacuum solution to conformal Weyl gravity and galactic rotation
curves"**  
*Astrophys. J.* **342**, 635.

The Mannheim-Kazanas solution $B(r) = 1 - 2GM/r + \gamma r - \kappa r^2$
is a vacuum solution of **pure conformal gravity** (no Einstein-Hilbert
term). CODA's Tier 2 action includes the EH term, which breaks
conformal invariance and eliminates the $\gamma r$ term from the
vacuum structure.

**Ruled out for Tier 2 by:** Three independent model responses (CODA
research session Q-two) + Stelle (1977) consistency + direct derivation
showing only Yukawa corrections for Einstein-Weyl gravity.

**Status for Tier 1:** Not ruled out as a limiting case.
Pure conformal gravity ($G \to \infty$ limit) may be recoverable
from CODA Tier 1 if the EH coupling is emergent rather than fundamental.

---

### CODE-GEO V3.1 (2026) `[SUPERSEDED]`
**"Formalizing the Hilbert-Complexity Action to resolve the BH
Information Paradox"**  
github.com/Darian-Frey/CODE-GEO

CODA's predecessor. CODE-GEO's empirical claim — a 2.816 ms echo in
GW250114 at 355 Hz — was not supported by the LVK analysis
(residual SNR 6.86, p = 0.34). Several theoretical steps were
reverse-engineered from desired results.

CODA retains from CODE-GEO:
- The Hilbert-Complexity Action form $S = \int\sqrt{-g}[R/16\pi G + \alpha\mathcal{C}_K]$
- The Planck-scale motivated coupling $\alpha \sim \ell_P^2/(8\pi)$
- The MOND-as-computational-latency intuition

CODA discards from CODE-GEO:
- The GW250114 empirical claims
- The ad-hoc $(R_s/r)^6$ nonlinear gate
- The asserted Large-N enhancement without derivation
- The Mannheim-Kazanas connection for the Einstein-Weyl action

---

## Open Literature — Being Monitored

The following active research areas are relevant to CODA and should
be monitored for new results:

| Area | Relevance | Status | Key workers |
|------|-----------|--------|-------------|
| DSSYK / dS holography extensions to 4D | Priority 1 open problem — 4D local density lift | **Active** — Heller et al. (2025) identify this as most pressing open question | Blommaert, Mertens, Papalini (Ghent); Verlinde (Princeton) |
| Modular Krylov complexity | Tier 1 construction — $\epsilon \to 0$ limit | Active — Caputa group | Caputa, Magan, Patramanis |
| Modular flow in curved spacetime | Tier 1 foundation — Bisognano-Wichmann extensions | Active | Casini-Huerta-Myers programme |
| AeST phenomenology tests | MOND thread structural target | Active — new CMB data constraints | Skordis, Złośnik, Famaey |
| Wide binary MOND tests (Gaia DR3) | Galactic-scale constraint on MOND | Active — contested results | Pittordis, Sutherland; Banik |
| Galaxy cluster MOND tests | Known failure regime | Ongoing | McGaugh, Banik, Kroupa |
| dS/CFT — higher-dimensional | $a_0 \sim cH_0$ mechanism extension | Active | Anninos, Strominger |

---

*End of document. Version 0.2.*