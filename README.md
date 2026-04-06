# CODA Research Roadmap

**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.2  
**Last updated:** April 2026

This roadmap records the phased research plan for CODA, tracks completed
milestones, and states explicitly what is blocked and why. It is a living
document — updated as work progresses and as open problems are resolved
or reframed.

---

## Current State Summary

The **theory layer** (Phase 1) is complete and internally consistent.
All numerical factors verified against Stelle (1977). The Tier 2 working
theory is fully characterised: field equations, propagator, ghost mass,
Newtonian potential, Bach-flat theorem, conservation identity, and full
solution catalogue.

The **phenomenology layer** (Phase 2) is now complete. All four
documents are written and cross-referenced: weak field limit (PPN
parameters, Solar System tests), cosmological background (FLRW exact GR,
perturbation suppression), MOND thread (updated with DSSYK $a_0$
derivation), and black hole phenomenology (non-Schwarzschild branch).

**Phase 3a is substantially advanced.** Reading of the DSSYK primary
sources (Heller et al. 2025, Aguilar-Gutierrez 2024) established three
independent derivation routes giving $a_0 = cH_0$ from holographic
Krylov complexity in de Sitter. Steps 3a-i through 3a-iv are complete.
The remaining gap is the 4D local density lift (3a-vi) — identified by
Heller et al. themselves as the most pressing open problem in the field.

**The primary blocker for full phenomenological predictions remains the
Tier 1 covariant $\mathcal{C}_K(x)$ construction** — specifically the
4D lift of the DSSYK Krylov density to a local spacetime scalar.

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

### Phase 3a — de Sitter Krylov Complexity ✓ SUBSTANTIALLY COMPLETE

**Status:** Steps i–iv complete following direct reading of DSSYK primary
sources (April 2026). The $a_0 \sim cH_0$ derivation now has three
independent routes from established results. Step v (AQUAL structure)
is partially complete. Step vi (4D local density) is the primary open
problem for the next phase of research.

See `audit/llm_synthesis/Q4b_DSSYK_papers.md` for full session log.

| Step | Task | Status | Source |
|------|------|--------|--------|
| 3a-i | Read DSSYK holographic dS papers | ✓ Complete | Heller et al. (2025), Aguilar-Gutierrez (2024) |
| 3a-ii | Confirm $b_n \sim H_0 n/2$ in DSSYK | ✓ Complete | Aguilar-Gutierrez Eq. 4.10: $b_n \to n/2$ for large $n$ |
| 3a-iii | Confirm $\alpha \sim H_0$, chaos bound saturated | ✓ Complete | Lyapunov $\lambda_K = H_0$; $C_K \propto e^{H_0 t}$ |
| 3a-iv | Derive $a_0 \sim cH_0$ from complexity | ✓ Complete | Three independent routes — see below |
| 3a-v | AQUAL functional form from $C_K$ | 🔶 Partial | Transition scale correct; exact interpolating function open |
| 3a-vi | 4D local density lift | 🔲 Open | Heller et al.'s "most pressing question"; CODA Priority 1 |

**Three established routes to $a_0 = cH_0$:**

1. **Chaos bound route** — Lyapunov exponent $\lambda_K = H_0$ defines
   $\tau^* = H_0^{-1}$; acceleration $a_0 = c/\tau^* = cH_0$
   [Aguilar-Gutierrez 2024, §4.1 — ESTABLISHED]

2. **Complexity transition route** — Quadratic-to-linear transition in
   $C_K(\chi) \propto \log\cosh(\chi\theta/2)$ at $\chi_* \sim \ell_{dS}$;
   acceleration at transition $= c^2/\ell_{dS} = cH_0$
   [Heller et al. 2025, Eq. 20 — ESTABLISHED]

3. **Growth rate route** — Late-time rate $\propto S_{dS} \cdot T_{dS}
   = S_{dS} \cdot H_0/2\pi$; transition scale $\sim cH_0$
   [Heller et al. 2025, Eq. 70 — ESTABLISHED]

All three give $a_0 = cH_0$ with $O(1)$ factor $\eta = 1/(2\pi)$ from
$T_{dS} = H_0/2\pi$, matching Verlinde (2016) exactly.

**What was ruled out:** Free scalar modular Krylov in dS produces bounded
$b_n$ and no $a_0$ — recorded in ruled-out table below.

**The 4D local density problem (3a-vi) in detail:**  
Heller et al. (2025) provide the timelike extremal slice volume integrand
$\mathcal{V}(\tau)$ as a candidate local bulk complexity density. The
challenge is lifting this 2D construction to a covariant local scalar
in 4D de Sitter — the "microscopic realizations in higher dimensions"
that the authors identify as the most pressing open question. CODA's
specific next calculation is: does Heller et al.'s Eq. 23 (the
$dS_{d+1}$ holographic complexity proposal) produce a well-defined
integrand that survives as a covariant local density in the $d=3$ case?

### Phase 3b — Covariant Construction (ACTIVE — primary research target)

The core open problem is now sharply formulated: lift the DSSYK 2D Krylov
density to a covariant local scalar in 4D de Sitter, then to a general
curved spacetime.

| Task | Priority | Status | Notes |
|------|----------|--------|-------|
| Does Heller et al. Eq. 23 produce a well-defined local density integrand in $d=3$? | **1** | 🔲 Open | The specific narrow calculation — see Phase 5 |
| Prove/disprove $\epsilon \to 0$ limit of modular Krylov density in AQFT | **2** | 🔲 Open | DSSYK suggests finite in holographic setting; unclear in algebraic QFT |
| Establish covariant renormalisation scheme for $\mathcal{C}_K(x)$ | **3** | 🔲 Open | Analogous to holographic entanglement entropy renormalisation |
| Determine whether AQUAL structure emerges from $\log\cosh$ complexity function | **4** | 🔶 Partial | Transition scale correct; exact form open |
| Derive canonical $u^\mu(x)$ from field equations — fix preferred-foliation | **5** | 🔲 Open | DSSYK partial resolution: state-independent at late times |
| Extend Bisognano-Wichmann theorem to curved spacetimes | **6** | 🔶 Partial | Casini-Huerta-Myers made progress for spherical regions |

**Honest assessment:** The $\epsilon \to 0$ limit of modular Krylov density
remains potentially obstructed in the direct algebraic QFT approach. The
DSSYK holographic route (Priority 1 above) circumvents this by working
in a regime where the limit is finite and geometrically well-defined.
If Priority 1 succeeds, it resolves Priority 2 in the holographic sector
and sets the agenda for extending to general spacetimes.

---

## Phase 4 — Simulations and Verification (PENDING PHASE 3b)

**Goal:** Build Python simulation suite to verify analytical results and
test MOND predictions against galactic data.

| Task | Document | Status | Depends on |
|------|----------|--------|-----------|
| DSSYK Krylov complexity: extremal surface integrand in $d=3$ | `simulations/dSd_krylov.py` | 🔲 Pending | Phase 3b Priority 1 — **next calculation** |
| MOND interpolation function from Tier 1 action | `simulations/mond_fit.py` | 🔲 Pending | Phase 3b AQUAL structure |
| Galaxy rotation curve fits | `simulations/rotation_curves.py` | 🔲 Pending | Phase 3b + MOND action |
| Tier 2 Yukawa potential and ghost mass verification | `simulations/adm_mass.py` | 🔲 Available now | Phase 1 complete |

---

## Phase 5 — Manuscripts and Dissemination

**Goal:** Produce publication-ready outputs from CODA's theoretical and
numerical work.

| Target | Content | Status | Depends on |
|--------|---------|--------|-----------|
| Paper 1 | "The Covariant Krylov Complexity Density: Construction and Obstructions" | 🔲 Pending | Phase 3b |
| Paper 2 | "Deriving the Milgrom Scale from de Sitter Krylov Complexity" | 🔶 Near-term | Phase 3b Priority 1 — has concrete content |
| Paper 3 | "Ghost-free MOND from Covariant Krylov Complexity" | 🔲 Pending | Phase 3b + AQUAL structure |

**Paper 2 is the immediate target.** Three independent derivation routes
for $a_0 = cH_0$ are established from the DSSYK literature. The specific
CODA contribution is the 4D lift of the DSSYK extremal surface integrand
to a covariant local density — if that calculation succeeds, Paper 2 has
a genuine new result.

---

## Known Blockers

| Blocker | Affects | Severity | Status |
|---------|---------|----------|--------|
| 4D local density lift (DSSYK Eq. 23 in $d=3$) | Phase 3b Priority 1, Paper 2 | **Critical** | Active research target — tractable calculation |
| AQUAL functional form from $\log\cosh$ complexity | MOND thread §5.3, Paper 1 | **High** | Transition scale correct; exact form open |
| AeST-CODA mapping verification | MOND thread §5.3 | **Medium** | Speculative; requires Tier 1 completion |
| Galaxy cluster failure (MOND general problem) | MOND predictions | **Medium** | Inherited from all covariant MOND theories |

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
| 0.2 | April 2026 | Phase 2 complete (all four phenomenology documents). Phase 3a substantially complete (steps i–iv done; three routes to $a_0 = cH_0$ established from DSSYK primary sources). Phase 3b reframed around 4D density lift as Priority 1. Lineage updated with DSSYK programme. |

---

*CODA ROADMAP v0.2 — maintained by Shane Hartley*