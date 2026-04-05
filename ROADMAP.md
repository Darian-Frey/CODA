# CODA Research Roadmap

**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Last updated:** April 2026

This roadmap records the phased research plan for CODA, tracks completed
milestones, and states explicitly what is blocked and why. It is a living
document — updated as work progresses and as open problems are resolved
or reframed.

---

## Current State Summary

The **theory layer** (Phase 1) is complete and internally consistent.
All numerical factors are verified against Stelle (1977). The Tier 2
working theory is fully characterised: field equations, propagator,
ghost mass, Newtonian potential, and all key limits are derived and
documented.

The **phenomenology layer** (Phase 2) is partially complete. The MOND
thread is written as a working hypothesis; it is not a prediction of
Tier 2, and awaits Tier 1 development. The weak-field limit document
is pending.

**The primary blocker for all phenomenological predictions is the
Tier 1 covariant $\mathcal{C}_K(x)$ construction** — the unsolved
problem documented in `theory/covariant_ck.md`. Nothing in Phase 3
or later can proceed without meaningful progress on this.

---

## Phase 1 — Theoretical Foundations ✓ COMPLETE

**Goal:** Establish the CODA action, derive the field equations from
first principles, verify all results against primary sources, and
document the core open problem ($\mathcal{C}_K(x)$ construction).

| Task | Document | Status | Notes |
|------|----------|--------|-------|
| Define covariant $\mathcal{C}_K(x)$ — problem statement | `theory/covariant_ck.md` | ✓ Complete | Tier 1 open; Tier 2 proxy established |
| CODA action and field equations | `theory/action_principle.md` v0.2 | ✓ Complete | Corrected: $\Lambda_C = 32\pi G\xi$ |
| Linearisation, propagator, ghost mass | `theory/field_equations.md` v0.2 | ✓ Complete | All factors verified vs. Stelle (1977) |
| Correction of Mannheim-Kazanas error | Both theory docs | ✓ Complete | $\gamma r$ belongs to pure conformal gravity only |

**Key results established in Phase 1:**
- Ghost mass $m_2^2 = 1/(32\pi G\xi)$ — Stelle (1977) confirmed
- EFT condition $\xi < 1/4$ — analytically derived
- Newtonian potential: Yukawa correction $-\frac{4}{3}e^{-m_2 r}/r$ — Stelle (1977) confirmed
- All GR vacuum solutions are exact CODA Tier 2 solutions
- FLRW cosmology unmodified
- UV/IR polarity problem identified: Tier 2 cannot produce MOND

---

## Phase 2 — Phenomenology (IN PROGRESS)

**Goal:** Characterise what CODA predicts in accessible physical regimes,
identify where MOND phenomenology could emerge from Tier 1, and establish
the Solar System constraints.

| Task | Document | Status | Notes |
|------|----------|--------|-------|
| MOND thread — observational target and structural requirements | `phenomenology/mond_thread.md` | ✓ v0.1 hypothesis | Requires Tier 1; AeST identified as structural target |
| Solar System and PPN constraints | `phenomenology/weak_field_limit.md` | 🔲 Pending | Next priority |
| Galaxy rotation curve phenomenology | `phenomenology/mond_thread.md` §6 | 🔲 Pending | Blocked on Tier 1 |
| Cosmological perturbation analysis | TBD | 🔲 Pending | FLRW background exact GR; perturbations differ |

**Phase 2 near-term target:**  
Complete `phenomenology/weak_field_limit.md` — establishing exactly what
CODA Tier 2 predicts for PPN parameters $\gamma$, $\beta$, perihelion
advance, and gravitational wave speed. This document is achievable now
without Tier 1.

---

## Phase 3 — The Tier 1 Construction Programme (BLOCKED — primary blocker)

**Goal:** Formally define $\mathcal{C}_K(x)$ as a covariant scalar field,
establish the $\epsilon \to 0$ limit of the modular Krylov density,
and derive the MOND-relevant nonlinear kinetic structure.

This is the hardest theoretical problem in CODA and the gate that all
subsequent phases pass through. It is documented in full in
`theory/covariant_ck.md`.

### Phase 3a — de Sitter Krylov Complexity (REVISED — see audit/llm_synthesis/Q4_dS_Krylov.md)

**Status:** Programme revised following Q4 research session (April 2026).
The original formulation (free scalar, modular flow, Lanczos transition)
was found to be insufficient. A free scalar in the dS static patch has
**bounded** Lanczos coefficients — no linear growth, no $a_0$ emergence.
The calculation must target strongly-coupled holographic de Sitter
(DSSYK) rather than free fields.

**Key finding from Q4:** The exact modular Krylov calculation in the dS
static patch has not been done for any system. For free scalars, $b_n$
is bounded by $\sim H_0$ and $K(t)$ saturates at $t \sim H_0^{-1}$.
For chaotic/holographic dS, $b_n \sim H_0 n$ (chaos bound at $T_{dS}$),
which would give $a_0 \sim cH_0$ — but this calculation doesn't yet exist.
The DSSYK holographic programme (arXiv:2510.13986, 2403.13186) is the
correct computational target.

| Task | Priority | Notes |
|------|----------|-------|
| Read DSSYK holographic dS papers (arXiv:2510.13986, 2403.13186, 2508.10093) | **1 — immediate** | Most relevant existing Krylov-dS results |
| Identify modular Krylov spectrum in DSSYK boundary QM | **2** | Tractable with existing DSSYK technology |
| Check whether rate $\alpha \sim H_0$ appears in modular evolution | **3** | Follows from chaos bound if theory is chaotic |
| Determine whether AQUAL nonlinear structure emerges from $K(t)$ | **4** | Core CODA prediction — key step |
| Free scalar modular Krylov in dS static patch (parallel track) | **5** | Worthwhile but insufficient for $a_0$ derivation |

**What has been ruled out:** The free-scalar modular Krylov calculation
cannot produce $a_0 \sim cH_0$. This is recorded in the ruled-out table.

**Closest existing result:** Adhikari et al. (arXiv:2203.14330) computed
Krylov complexity for inflationary-patch scalar perturbations (Heisenberg
evolution, not modular) and found $\alpha \sim H$ — partial evidence that
the Hubble scale governs complexity rates in dS, but not the required
modular static-patch calculation.

### Phase 3b — Covariant Construction (REQUIRES RESEARCH BREAKTHROUGHS)

| Task | Priority | Status |
|------|----------|--------|
| Prove/disprove existence of $\epsilon \to 0$ limit of modular Krylov density | **1** | Open — may be fundamentally obstructed |
| Establish covariant renormalisation scheme for $\mathcal{C}_K(x)$ | **2** | Open |
| Fix preferred-foliation problem — derive canonical $u^\mu$ from field equations | **3** | Open |
| Extend Bisognano-Wichmann theorem to curved spacetimes | **4** | Partially established |

**Honest assessment:** Phase 3b may not be solvable in its strong form.
The Reeh-Schlieder theorem and type-III factor structure of local algebras
present fundamental obstacles to a pointwise density. CODA's fallback
position is the two-tier structure: use Tier 2 for all calculable results,
and treat Tier 1 as a theoretical target whose non-existence would also
be a publishable result.

---

## Phase 4 — Simulations and Verification (PENDING PHASE 3)

**Goal:** Build Python simulation suite to verify analytical results and
test MOND predictions against galactic data.

| Task | Document | Depends on |
|------|----------|-----------|
| de Sitter Krylov complexity simulator | `simulations/dS_krylov.py` | Phase 3a |
| MOND interpolation function from Tier 1 action | `simulations/mond_fit.py` | Phase 3b |
| Galaxy rotation curve fits | `simulations/rotation_curves.py` | Phase 3b + MOND action |
| PPN parameter calculator | `simulations/ppn_params.py` | Phase 2 weak-field doc |
| ADM mass verification | `simulations/adm_mass.py` | Phase 1 (available now) |

**Near-term simulation (available now):** The Tier 2 Yukawa-corrected
Newtonian potential and ghost mass calculation can be verified
numerically without Tier 1.

---

## Phase 5 — Manuscripts and Dissemination (PENDING PHASES 3-4)

**Goal:** Produce publication-ready outputs from CODA's theoretical and
numerical work.

| Target | Content | Depends on |
|--------|---------|-----------|
| Paper 1: Preprint | "Ghost-free MOND from Covariant Krylov Complexity" | Phase 3a + 4 |
| Paper 2: Preprint | "Deriving the Milgrom Scale from de Sitter Modular Flow" | Phase 3a |
| Paper 3: Preprint | "The Covariant Krylov Complexity Density: Construction and Obstructions" | Phase 3b |

Paper 2 (the $a_0$ derivation) may be achievable independently of the
full Tier 1 construction and could be the first CODA paper to reach
preprint stage.

---

## Known Blockers

| Blocker | Affects | Severity | Notes |
|---------|---------|----------|-------|
| Tier 1 $\mathcal{C}_K(x)$ construction | Phases 3b, 4, 5 | **Critical** | May be fundamentally obstructed |
| de Sitter Krylov complexity calculation | Phases 3a, 5 (Paper 2) | **High** | Accessible now; should begin |
| AeST-CODA mapping verification | MOND thread §5.3 | **Medium** | Speculative; requires Tier 1 |
| Galaxy cluster failure (MOND general problem) | MOND predictions | **Medium** | Inherited from all covariant MOND theories |

---

## What Has Been Ruled Out

The following ideas were pursued and abandoned with documented reasons:

| Idea | Ruled out by | Document |
|------|-------------|----------|
| Mannheim-Kazanas $\gamma r$ term from CODA Tier 2 | Stelle (1977); all three independent models | `field_equations.md` v0.2 §7.4 |
| GW250114 echo prediction (CODE-GEO) | LVK spectroscopy paper; residual SNR 6.86 p=0.34 | CODE-GEO audit |
| $\Lambda_C = 64\pi G\xi$ | Stelle (1977) $\kappa^2$ convention | `field_equations.md` v0.2 §1 |
| $-4B_{\mu\nu}$ variation coefficient | Consistency with conformal gravity EOM and Stelle (1977) | `action_principle.md` v0.2 §2.2 |
| Free scalar modular Krylov in dS producing $a_0 \sim cH_0$ | Q4 session: free scalars have bounded $b_n$, no linear growth, no $a_0$ | `audit/llm_synthesis/Q4_dS_Krylov.md` |

---

## Theoretical Lineage (Literature Map Summary)

CODA's foundations rest on four research programmes:

1. **Holographic Complexity** (Susskind, Brown et al. 2016) — Complexity=Action
   conjecture; CODA extends this by coupling back to Einstein field equations
2. **Krylov Complexity in QFT** (Avdoshkin, Dymarsky, Smolkin 2022-24) —
   establishes Krylov complexity for local operators in continuum QFT
3. **Modular Krylov Complexity** (Caputa et al. 2023-24) — replaces global
   Hamiltonian with modular Hamiltonian; most covariant existing framework
4. **AeST / Covariant MOND** (Skordis-Złośnik 2021) — ghost-free relativistic
   MOND; structural target for CODA's Tier 1 MOND predictions
5. **Emergent Gravity / Verlinde** (2016) — information-theoretic derivation
   of $a_0 \sim cH_0$; closest existing bridge between entropy and MOND
6. **Quadratic Gravity** (Stelle 1977) — authoritative source for all Tier 2
   numerical results; ghost mass, Newtonian potential, Weyl identity

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | April 2026 | Initial release. Theory layer complete. Phase 1 verified against Stelle (1977). Phase 2 partially complete. |

---

*CODA ROADMAP v0.1 — maintained by Shane Hartley*