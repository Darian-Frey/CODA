# Research Session Log — Q4: de Sitter Krylov Complexity

**File:** `audit/llm_synthesis/Q4_dS_Krylov.md`  
**Session:** Phase 3a — de Sitter Krylov Complexity  
**Date:** April 2026  
**Query target:** Whether Krylov complexity in de Sitter static patch
produces a natural acceleration scale $a_0 \sim cH_0$  
**Models consulted:** Claude Sonnet 4.6 + 3 independent LLMs  
**Documents updated by this session:** `phenomenology/mond_thread.md`,
`ROADMAP.md`

---

## Query Summary

We asked for a technical calculation of Krylov complexity $K(t)$ for a
free massive scalar operator evolved under the modular Hamiltonian of the
de Sitter static patch, using the Bunch-Davies vacuum. Specifically:

1. Wightman function and spectral density $f_2(\omega)$
2. Lanczos coefficients $\{b_n\}$ and growth law
3. Transitions in Lanczos behaviour at scale $\sim H_0^{-1}$
4. Long-time behaviour of $K(t)$
5. Any existing result linking Krylov to $a_0 \sim cH_0$

---

## Model Responses — Summary Table

| Question | Reply 1 | Reply 2 | Reply 3 | Assessment |
|----------|---------|---------|---------|------------|
| Exact calculation exists in literature? | Implicit yes | No | No — explicitly | **Not done** |
| Free scalar $b_n$ linearly growing? | **Yes** — "rigorous" | **No** — bounded | **No** — bounded | Reply 1 wrong |
| Growth rate if linear | $\alpha = H_0/2$ — "solid" | N/A | N/A | Not applicable to free field |
| Transition at $H_0^{-1}$ scale? | UV cutoff only | No sharp transition | No — conjectural only | **No known transition** |
| $K(t)$ long-time behaviour | Exponential $e^{H_0 t}$ | Saturation/oscillation | Saturation $\sim H_0^{-1}$ | **Bounded for free field** |
| Existing $a_0 \sim cH_0$ from Krylov? | Speculative argument | No | No | **None exists** |

---

## Key Disagreement and Resolution

### The Disagreement

Reply 1 claimed $b_n = \frac{H_0}{2}n$ and $K(t) \sim e^{H_0 t}$ are
"rigorous results" with "solid" epistemic status. Replies 2 and 3 both
stated that for a **free scalar** the Lanczos coefficients are
**bounded** (not linearly growing) and $K(t)$ saturates rather than
grows exponentially.

This is a direct contradiction on the most basic feature of the system.

### Resolution

Reply 1 made a specific error: **conflating thermal structure with
chaotic dynamics**.

The de Sitter static patch has a thermal temperature $T_{dS} = \hbar
H_0/2\pi k_B$ (Gibbons-Hawking effect), producing a KMS Wightman
function. Reply 1 applied the result $b_n \sim \pi n/\beta = (H_0/2)n$
as if the system were chaotic. But this result holds only for systems
that saturate the Maldacena-Shenker-Stanford chaos bound — which
requires strong interactions and maximal chaos.

A **free scalar** is integrable. Its Lanczos coefficients do not grow
linearly. The linear growth $b_n \sim \alpha n$ is a hallmark of
interacting, chaotic many-body systems with broad, smooth spectral
densities. A free field has a gapped, effectively discrete spectrum
in the static patch — producing bounded or oscillatory $b_n$.

Reply 1's Wightman function $W(t) \propto 1/\sinh^2(H_0 t/2)$ is the
form for a 2D CFT on a thermal circle — not a free massive scalar in
4D de Sitter. Replies 2 and 3 gave the correct spectral density
(involving Gamma functions with scale $H_0$) and correctly concluded
that $b_n$ is bounded.

**Verdict: Replies 2 and 3 are correct. Reply 1's "rigorous results"
are wrong for the stated system.**

---

## What Was Actually Established

### Established with high confidence

**The exact modular Krylov calculation in the dS static patch has not
been done.** All three models confirm: no paper in the literature
computes $K(t)$ for a local operator evolved under the modular
Hamiltonian of the de Sitter static patch with Bunch-Davies vacuum.
This is a genuine open calculation.

**For a free scalar, $b_n$ is bounded** (not linearly growing), with
magnitude set by $\sim H_0$. $K(t)$ saturates or oscillates on
timescales $\sim H_0^{-1}$. There is no linear or exponential growth.

**There is no existing result** linking a Krylov transition or
saturation to $a_0 \sim cH_0$ in any field theory setting. All three
models agree on this unanimously.

### Established with medium confidence

The spectral density for a free massive scalar at $r=0$ in the dS
static patch has the form (Reply 2):

$$f_2(\omega) \propto \left|\Gamma\!\left(\frac{\Delta_+}{2}
+ i\frac{\omega}{2H_0}\right)\Gamma\!\left(\frac{\Delta_-}{2}
+ i\frac{\omega}{2H_0}\right)\right|^2$$

where $\Delta_\pm = \frac{3}{2} \pm \nu$, $\nu = \sqrt{9/4 - m^2/H_0^2}$.
This is continuous, decays exponentially at large $\omega$ with scale
$H_0$, and satisfies KMS with $\beta = 2\pi/H_0$. However, transforming
to modular time coordinates has not been done explicitly.

For **interacting/chaotic** quantum gravity in de Sitter — if such a
theory exists — the chaos bound gives $\alpha \lesssim 2\pi T_{dS}/\hbar
= H_0$, so $b_n \sim H_0 n$. Combined with $c$, this gives timescale
$H_0^{-1}$ and acceleration scale $\sim cH_0$. But this is AdS analogy
applied to dS — not a dS calculation.

### Closest existing results (flagged as non-exact)

**Adhikari et al. (arXiv:2203.14330):** Computed Krylov complexity
for cosmological scalar perturbations in the **inflationary patch**
(not static patch) using **Heisenberg evolution** (not modular flow).
Found $b_n = n/(2|\tau|)$ with $\alpha \sim H$. The rate is tied to
Hubble scale. Epistemic status: exact free-field calculation in a
related but different dS patch. Does not directly apply to CODA's
modular static-patch setup.

**DSSYK holographic duals to dS (arXiv:2510.13986, 2403.13186,
2508.10093 — 2024-25):** These compute Krylov complexity in
strongly-coupled boundary quantum mechanics dual to de Sitter geometry.
Find $K(t)$ growing with rate $\propto H_0 \cdot S_{dS}$ at late times.
Epistemic status: correct regime (chaotic, finite entropy), wrong
calculation type (boundary dual QM, not bulk free scalar). These are
the most relevant existing results for CODA.

---

## Critical Implication for CODA Phase 3a

The Phase 3a hypothesis — that a Krylov complexity transition at the
de Sitter scale produces $a_0 \sim cH_0$ through free-field modular
Krylov calculation — **cannot be realised with a free scalar**.

For free fields: $b_n$ bounded, $K(t)$ saturates, no transition,
no $a_0$ emergence.

For the hypothesis to work, CODA requires **quantum gravity in de Sitter
in the strongly coupled, maximally chaotic regime** — specifically:

1. A holographic de Sitter quantum gravity where $b_n \sim H_0 n$
   (rate set by chaos bound at $T = T_{dS}$)
2. A modular Krylov calculation in this theory — not done yet
3. A mechanism by which the complexity rate $\alpha \sim H_0$ produces
   the AQUAL nonlinear kinetic structure for $\mathcal{C}_K$

The DSSYK holographic programme (arXiv:2510.13986 etc.) is the most
natural place to attempt this calculation.

---

## Phase 3a Programme — Revised

The correct formulation of Phase 3a is:

> *Compute the Krylov complexity of a local operator in a holographic de
> Sitter quantum gravity (DSSYK or similar, strongly coupled, finite
> entropy $S_{dS}$) under modular flow of the static patch. Determine
> whether a transition or saturation at scale $\sim H_0^{-1}$ produces
> an effective nonlinear kinetic structure with scale $a_0 \sim cH_0$.*

### Revised priority ordering

| Step | Task | Status | Notes |
|------|------|--------|-------|
| 3a-i | Read DSSYK holographic dS papers (2024-25) | **Immediate** | arXiv:2510.13986, 2403.13186 |
| 3a-ii | Identify modular Krylov spectrum in DSSYK | **Near-term** | Tractable with existing technology |
| 3a-iii | Check whether rate $\alpha \sim H_0$ appears | **Near-term** | Follows from chaos bound if chaotic |
| 3a-iv | Determine whether AQUAL structure emerges from $K(t)$ transition | **Medium-term** | Key CODA prediction |
| 3a-v | Free scalar modular Krylov in dS static patch | **Parallel** | Worthwhile but won't give $a_0$ |

---

## Corrections to Prior CODA Documents

### `phenomenology/mond_thread.md` — Section 5.2 requires update

The $a_0$ derivation programme in §5.2 assumed the free scalar
modular Krylov calculation would be sufficient. This is incorrect.
The programme must be reframed around the DSSYK holographic approach.

Specific change: Step 2 ("Krylov complexity of a local field operator
under modular flow in the de Sitter vacuum state") must be amended to
specify that this requires an interacting/holographic theory, not a
free scalar. The Adhikari et al. inflationary-patch free-field result
is partial evidence but not sufficient.

### `ROADMAP.md` — Phase 3a description requires update

Phase 3a tasks should be reordered with DSSYK literature review as
the immediate first step, followed by modular Krylov in DSSYK.
The free-scalar calculation is useful but should be noted as
insufficient for the $a_0$ derivation.

---

## References Identified in This Session

- Adhikari, K. & Choudhury, S. (2022) — "Cosmological Krylov
  Complexity" (arXiv:2203.14330). Free scalar in inflationary patch;
  $\alpha \sim H$. Closest free-field dS result.

- Holographic DSSYK duals to dS (multiple 2024-25 papers):
  arXiv:2510.13986, arXiv:2403.13186, arXiv:2508.10093.
  Strongly coupled boundary QM dual to de Sitter; Krylov complexity
  with rate $\propto H_0$. **Most relevant existing results for CODA.**

- Maldacena, J., Shenker, S.H. & Stanford, D. (2016) — Chaos bound
  $\lambda_L \leq 2\pi T/\hbar$. Applied to $T = T_{dS}$, gives
  $\alpha \leq H_0$ for strongly coupled dS.

---

*End of session log. Phase 3a programme revised — DSSYK holographic
approach identified as the correct computational target.*
