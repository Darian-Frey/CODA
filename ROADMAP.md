# CODA Research Roadmap

**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.3  
**Last updated:** April 2026

This roadmap records the phased research plan for CODA, tracks completed
milestones, and states explicitly what is blocked and why. It is a living
document — updated as work progresses and as open problems are resolved
or reframed.

---

## Current State Summary

**Phase 3b is substantially complete.** Six documents were produced in
the current research session establishing:

1. The pure dS4 Krylov density: $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2)$
   — all four checks passed (finite, covariant, correct dimensions, state-independent)
2. The perturbed dS4 result: double degeneracy of limiting surface, $(\delta\tau)^2 = -3\Phi/4$,
   $\delta\mathcal{C}_K/\mathcal{C}_K^{(0)} = 3\Phi$, $|\nabla\mathcal{C}_K| = \kappa a_N$
3. The CODA MOND interpolating function: $\mu = \tanh$, derived from $d(\log\cosh)/dx$
4. The identification theorem: $x_{\rm eff} = a_N/a_0$ — proved from perturbed dS result
5. **The CODA MOND Theorem** (proved): $\nabla\cdot[\tanh(a_N/a_0)\nabla\Phi] = 4\pi G\rho_b$
6. The second variation: Jacobi $\lambda_0 = 7/3$ (non-zero); $|\Phi|^{3/2}$ non-analytic
   MOND signal identified from triple derivative through double degeneracy

**The CODA MOND Theorem is proved**, given premise (iii) of the theorem
statement. The $\kappa$ cancellation closes the proof without requiring the
holographic dictionary.

**One structural gap remains** before premise (iii) is fully derived: the
holographic dictionary connecting $|\Phi|^{3/2}$ in the DSSYK generating
functional to $F(|\nabla\Phi|^2/a_0^2)$ in the AQUAL action. This requires
showing the DSSYK boundary time responds to $|\nabla\Phi|$ (gradient) rather
than $|\Phi|$ (value) at each bulk point.

**Phase 4 (simulations) is now unblocked.** The MOND equation
$\nabla\cdot[\tanh(a_N/a_0)\nabla\Phi] = 4\pi G\rho_b$ is a concrete
prediction testable against the SPARC rotation curve dataset (175 galaxies).
This is the immediate next priority.

---

## Phase 1 — Theoretical Foundations ✓ COMPLETE

**Goal:** Establish the CODA action, derive the field equations from
first principles, verify all results against primary sources, and
document the core open problem ($\mathcal{C}_K(x)$ construction).

| Task | Document | Status | Notes |
|------|----------|--------|-------|
| Define covariant $\mathcal{C}_K(x)$ — problem statement | `theory/covariant_ck.md` v0.2 | ✓ Complete | DSSYK evidence added; 4D lift is Priority 1 |
| CODA action and field equations | `theory/action_principle.md` v0.3 | ✓ Complete | Correction flags removed; Bach-flat theorem added |
| Linearisation, propagator, ghost mass | `theory/field_equations.md` v0.3 | ✓ Complete | Full solution catalogue; conservation identity proved |
| Correction of Mannheim-Kazanas error | Both theory docs | ✓ Complete | $\gamma r$ belongs to pure conformal gravity only |

**Key results established in Phase 1:**
- Ghost mass $m_2^2 = 1/(32\pi G\xi)$ — Stelle (1977) confirmed
- EFT condition $\xi < 1/4$ — analytically derived
- Newtonian potential: Yukawa correction $-\frac{4}{3}e^{-m_2 r}/r$ — Stelle (1977) confirmed
- Conservation identity $\nabla^\mu B_{\mu\nu} = 0$ — proved from diffeomorphism invariance
- **Bach-flat theorem:** All conformally flat and all Einstein metrics satisfy
  $B_{\mu\nu} = 0$ and are exact CODA Tier 2 solutions — proved
- Full solution catalogue: Schwarzschild, Kerr, Schwarzschild-dS/AdS,
  Kerr-dS/AdS, FLRW, gravitational waves — all exact CODA solutions
- Non-Schwarzschild branch (Lu et al. 2015) — the only genuine Tier 2
  departure from GR; confined to sub-Planckian scales
- UV/IR polarity problem identified: Tier 2 cannot produce MOND
- DSSYK evidence for Tier 1 structure: limiting extremal surface as
  candidate for state-independent $\mathcal{C}_K(x)$

---

## Phase 2 — Phenomenology ✓ COMPLETE

**Goal:** Characterise what CODA predicts in accessible physical regimes,
identify where MOND phenomenology could emerge from Tier 1, and establish
the Solar System and cosmological constraints.

| Task | Document | Status | Notes |
|------|----------|--------|-------|
| MOND thread — observational target and structural requirements | `phenomenology/mond_thread.md` v0.1 | ✓ Complete | §5 updated with DSSYK $a_0$ derivation |
| Solar System and PPN constraints | `phenomenology/weak_field_limit.md` v0.1 | ✓ Complete | $\gamma=\beta=1$ exactly; all tests passed |
| Cosmological background and perturbations | `phenomenology/cosmological_background.md` v0.1 | ✓ Complete | FLRW exact GR; perturbations $\sim(k/M_P)^2$ |
| Black hole phenomenology | `phenomenology/black_hole_phenomenology.md` v0.1 | ✓ Complete | GR solutions exact; non-Schwarzschild branch analysed |

**Key results established in Phase 2:**
- PPN parameters: $\gamma = \beta = 1$ exactly — no Solar System tension
- Yukawa deviation at 50 μm: $\sim e^{-10^{30}} \approx 0$ — no sub-mm gravity tension
- CMB power spectra: identical to GR; Bach tensor correction $\sim(k/M_P)^2 \sim 10^{-114}$
- GW speed: $c_{GW} = c$ exactly — GW170817 constraint trivially satisfied
- All Einstein metrics Bach-flat: Schwarzschild, Kerr, Schwarzschild-dS/AdS
  are exact CODA solutions with no observable modification
- Non-Schwarzschild branch: Weyl hair confined to $r \lesssim \ell_P$ — unobservable

---

## Phase 3 — The Tier 1 Construction Programme

**Goal:** Formally define $\mathcal{C}_K(x)$ as a covariant scalar field,
establish the $\epsilon \to 0$ limit of the modular Krylov density,
and derive the MOND-relevant nonlinear kinetic structure.

### Phase 3a — de Sitter Krylov Complexity ✓ COMPLETE

**Status:** All six steps complete. The $a_0 \sim cH_0/2\pi$ derivation
has three independent routes. The AQUAL functional form is established from
the DSSYK Krylov function. The 4D local density is computed.

| Step | Task | Status | Source |
|------|------|--------|--------|
| 3a-i | Read DSSYK holographic dS papers | ✓ Complete | Heller et al. (2025), Aguilar-Gutierrez (2024) |
| 3a-ii | Confirm $b_n \sim H_0 n/2$ in DSSYK | ✓ Complete | Aguilar-Gutierrez Eq. 4.10: $b_n \to n/2$ for large $n$ |
| 3a-iii | Confirm $\alpha \sim H_0$, chaos bound saturated | ✓ Complete | Lyapunov $\lambda_K = H_0$; $C_K \propto e^{H_0 t}$ |
| 3a-iv | Derive $a_0 \sim cH_0$ from complexity | ✓ Complete | Three independent routes; $a_0 = cH_0/2\pi$ observationally preferred |
| 3a-v | AQUAL functional form from $C_K$ | ✓ Complete | $F'(s) = \tanh(\sqrt{s})$; $F$ from $\log\cosh$ — `coda_interpolating_function.md` |
| 3a-vi | 4D local density in $d=3$ | ✓ Complete | $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2)$ — `dS4_krylov_density.md` |

**Three established routes to $a_0 = cH_0/2\pi$ (de Sitter temperature):**

1. **Chaos bound route** — Lyapunov $\lambda_K = H_0$; $a_0 = c/\tau^* = cH_0$
   [Aguilar-Gutierrez 2024 — ESTABLISHED; factor $1/2\pi$ from temperature]

2. **Complexity transition route** — Quadratic-to-linear transition in
   $C_K \propto \log\cosh(\chi\theta/2)$ at $\chi_* \sim \ell_{dS}$;
   $a_0 = c^2/\ell_{dS} = cH_0$ [Heller et al. 2025 Eq. 20 — ESTABLISHED]

3. **Growth rate / temperature route** — Rate $\propto S_{dS}\cdot T_{dS}
   = S_{dS}\cdot H_0/2\pi$; $a_0 = cT_{dS} = cH_0/2\pi$
   [Heller et al. 2025 Eq. 70 — ESTABLISHED; observationally preferred]

**$a_0^{\rm CODA} = cH_0/2\pi \approx 1.08\times10^{-10}$ m/s²;
observed $a_0 \approx 1.2\times10^{-10}$ m/s² — agreement within 10%.** ✓

### Phase 3b — Covariant Construction ✓ SUBSTANTIALLY COMPLETE

Six documents produced. The CODA MOND Theorem is proved. One structural
gap remains before premise (iii) is fully derived from the DSSYK construction.

**Documents produced in Phase 3b:**

| Document | Key result | Status |
|----------|-----------|--------|
| `theory/dS4_krylov_density.md` | $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2) \approx 0.385\,M_P^2H_0^2$; all 4 checks pass | ✓ |
| `theory/dS4_perturbed.md` | Double degeneracy; $(\delta\tau)^2 = -3\Phi/4$; $\delta\mathcal{C}_K = 3\Phi\mathcal{C}_K^{(0)}$; $\|\nabla\mathcal{C}_K\| = \kappa a_N$ | ✓ |
| `theory/coda_interpolating_function.md` | $F'(s) = \tanh(\sqrt{s})$; $F = 2\sqrt{s}\log\cosh\sqrt{s} - 2\int\log\cosh$; limits verified | ✓ |
| `theory/coda_identification.md` | $x_{\rm eff} = a_N/a_0$ theorem; BTFR; RAR shape | ✓ |
| `theory/coda_mond_theorem.md` | **Theorem proved**: $\nabla\cdot[\tanh(a_N/a_0)\nabla\Phi] = 4\pi G\rho_b$; $\kappa$ cancels | ✓ |
| `theory/second_variation_dssyk.md` | Jacobi $\lambda_0 = 7/3$ (non-zero); $\|\Phi\|^{3/2}$ MOND signal from $g'''$ | ✓ |

**The CODA MOND Theorem (proved):**

$$\nabla\cdot\!\left[\tanh\!\left(\frac{a_N}{a_0}\right)\nabla\Phi\right] = 4\pi G\rho_b$$

**Proof structure:** (i) $\mathcal{C}_K = \mathcal{C}_K^{(0)}(1+3\Phi)$ → (ii)
$\nabla\mathcal{C}_K = \kappa\nabla\Phi$ → (iii) $\kappa$ cancels in the kinetic
action argument → (iv) AQUAL variation gives MOND equation directly.

**Key structural finding:** The Jacobi ground eigenvalue $\lambda_0 = 7/3 \neq 0$.
The MOND signal is NOT from a Jacobi near-zero mode. It arises from the
non-analytic $|\Phi|^{3/2}$ term generated by $g'''(\tau_*)$ through the
double degeneracy $f_\tau|_* = g'|_* = 0$.

**Remaining tasks in Phase 3b:**

| Task | Priority | Status | Notes |
|------|----------|--------|-------|
| Holographic dictionary: $|\Phi|^{3/2} \to F(|\nabla\Phi|^2/a_0^2)$ | **1** | 🔲 Open | Requires DSSYK boundary time response to $\nabla\Phi$, not $\Phi$ |
| Vector field $A^\mu$ (Krylov flow vector, AeST analogue) | **2** | 🔲 Open | Needed for full relativistic lensing consistency |
| CMB and large-scale structure compatibility | **3** | 🔲 Open | Requires vector sector first |
| Extend to non-spherical geometry (galactic disk) | **4** | 🔲 Open | Breaks $S^2$ symmetry of dS4 construction |
| ~~$\mathcal{C}_K^{(0)}$ in dS4~~ | — | ✓ Done | `dS4_krylov_density.md` |
| ~~AQUAL functional form~~ | — | ✓ Done | `coda_interpolating_function.md` |
| ~~MOND theorem~~ | — | ✓ Done | `coda_mond_theorem.md` |

---

## Phase 4 — Simulations and Verification ← ACTIVE

**Goal:** Test the CODA MOND prediction against observed galaxy rotation
curves. The MOND theorem is proved; Phase 4 is now unblocked.

**Immediate priority: SPARC rotation curve fits.**

The CODA MOND equation $a_N\tanh(a_N/a_0) = a_b$ with $a_0 = cH_0/2\pi$
is a concrete prediction with no free parameters. The SPARC dataset
(Lelli, McGaugh, Schombert 2016) provides baryonic mass profiles and
rotation curves for 175 galaxies. The test:

1. For each galaxy, compute $a_b(r) = GM_b(r)/r^2$ from measured mass profile
2. Solve $a_N\tanh(a_N/a_0) = a_b(r)$ at each $r$
3. Compute $v_c(r) = \sqrt{a_N\cdot r}$
4. Compare predicted vs. observed rotation curve
5. Compute residuals; compare $\mu = \tanh$ to $\mu = x/\sqrt{1+x^2}$ (simple)

The discriminant: at the transition ($a_N \sim a_0$), $\tanh(1) = 0.762$
vs. simple $\mu(1) = 0.707$ — a 7.7% difference potentially distinguishable
with Euclid weak-lensing data.

| Task | Document | Status | Depends on |
|------|----------|--------|-----------|
| **SPARC rotation curve fits** | `simulations/sparc_fits.py` | 🔲 **Next** | MOND theorem ✓ |
| RAR curve comparison ($\mu = \tanh$ vs data) | `simulations/rar_comparison.py` | 🔲 Next | SPARC fits |
| Tully-Fisher normalization check | `simulations/btfr_check.py` | 🔲 Next | MOND theorem ✓ |
| Holographic dictionary verification (numerical) | `simulations/dSd_krylov.py` | 🔲 Pending | Phase 3b Priority 1 |
| Tier 2 Yukawa potential verification | `simulations/adm_mass.py` | 🔲 Available now | Phase 1 ✓ |

---

## Phase 5 — Manuscripts and Dissemination

**Goal:** Produce publication-ready outputs from CODA's theoretical and
numerical work.

| Target | Content | Status | Depends on |
|--------|---------|--------|-----------|
| Paper 1 | "Krylov Complexity Density in de Sitter: Construction and MOND" | 🔶 Draftable now | Phase 3b complete; SPARC fits needed |
| Paper 2 | "The CODA MOND Theorem: AQUAL from DSSYK Holographic Complexity" | 🔶 Near-term | Theorem proved; holographic dict. open |
| Paper 3 | "SPARC Galaxy Rotation Curves from Tanh Interpolating Function" | 🔲 Pending | Phase 4 SPARC fits |

**Paper 1** is now draftable. The derivation chain from DSSYK sources
to $\nabla\cdot[\tanh(a_N/a_0)\nabla\Phi] = 4\pi G\rho_b$ is complete
across six documents. The SPARC fits would strengthen it significantly.

**Paper 2** (the $a_0$ derivation) has three-route content from Phase 3a.
The holographic dictionary (premise iii derivation) would close it fully.

**Paper 3** requires Phase 4 simulation output.

---

## Known Blockers

| Blocker | Affects | Severity | Status |
|---------|---------|----------|--------|
| Holographic dictionary: $|\Phi|^{3/2} \to F(|\nabla\Phi|^2/a_0^2)$ | Premise (iii) of MOND Theorem; Paper 2 | **High** | Active research target; `second_variation_dssyk.md` identifies exact gap |
| SPARC rotation curve fits | Paper 1 and 3; observational validation | **High** | Unblocked — Phase 4 next |
| Vector sector $A^\mu$ (AeST analogue) | Gravitational lensing; CMB; full covariant MOND | **Medium** | Blocked on holographic dict. |
| Galaxy cluster MOND failure | All MOND predictions | **Medium** | Inherited from all covariant MOND theories |

---

## What Has Been Ruled Out

The following ideas were pursued and abandoned with documented reasons:

| Idea | Ruled out by | Document |
|------|-------------|----------|
| Mannheim-Kazanas $\gamma r$ term from CODA Tier 2 | Stelle (1977); all three independent models | `field_equations.md` v0.3 §7.6 |
| GW250114 echo prediction (CODE-GEO) | LVK spectroscopy paper; residual SNR 6.86 p=0.34 | CODE-GEO audit |
| $\Lambda_C = 64\pi G\xi$ | Stelle (1977) $\kappa^2$ convention | `field_equations.md` v0.3 §1 |
| $-4B_{\mu\nu}$ variation coefficient | Consistency with conformal gravity EOM and Stelle (1977) | `action_principle.md` v0.3 §2.2 |
| Free scalar modular Krylov in dS producing $a_0 \sim cH_0$ | Q4 session: free scalars have bounded $b_n$, no linear growth | `audit/llm_synthesis/Q4_dS_Krylov.md` |
| Jacobi near-zero mode as origin of MOND enhancement | Jacobi $\lambda_0 = 7/3 \neq 0$ on limiting surface | `second_variation_dssyk.md` §3.1 |

---

## Theoretical Lineage (Literature Map Summary)

CODA's foundations rest on seven research programmes:

1. **Holographic Complexity** (Susskind, Brown et al. 2016) — Complexity=Action
   conjecture; CODA extends this by coupling back to Einstein field equations
2. **Krylov Complexity in QFT** (Avdoshkin, Dymarsky, Smolkin 2022-24) —
   establishes Krylov complexity for local operators in continuum QFT
3. **Modular Krylov Complexity** (Caputa et al. 2023-24) — replaces global
   Hamiltonian with modular Hamiltonian; most covariant existing framework
4. **DSSYK / de Sitter Holography** (Heller et al. 2025; Aguilar-Gutierrez
   2024; Blommaert, Mertens, Papalini 2024) — first microscopic Krylov
   complexity in cosmological spacetime; three established routes to
   $a_0 \sim cH_0$; limiting extremal surface as candidate $\mathcal{C}_K(x)$
5. **AeST / Covariant MOND** (Skordis-Złośnik 2021) — ghost-free relativistic
   MOND; structural target for CODA's Tier 1 MOND predictions
6. **Emergent Gravity / Verlinde** (2016) — information-theoretic derivation
   of $a_0 \sim cH_0$; closest existing bridge between entropy and MOND
7. **Quadratic Gravity** (Stelle 1977; Lu et al. 2015) — authoritative source
   for all Tier 2 numerical results; non-Schwarzschild branch establishes
   the only genuine strong-field departure from GR in CODA Tier 2

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | April 2026 | Initial release. Theory layer complete. Phase 1 verified against Stelle (1977). Phase 2 partially complete. |
| 0.2 | April 2026 | Phase 2 complete. Phase 3a substantially complete (steps i–iv; three routes to $a_0$). Phase 3b reframed around 4D density lift. |
| 0.3 | April 2026 | Phase 3a complete (all six steps). Phase 3b substantially complete: six documents, MOND theorem proved, Jacobi $\lambda_0 = 7/3$ established, $\|\Phi\|^{3/2}$ MOND signal identified. Phase 4 unblocked. Holographic dictionary identified as remaining structural gap. |

---

*CODA ROADMAP v0.3 — maintained by Shane Hartley*