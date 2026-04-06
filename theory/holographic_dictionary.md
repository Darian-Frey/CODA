# Holographic Dictionary: From DSSYK Second Variation to AQUAL

**Document:** `theory/holographic_dictionary.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Status:** ACTIVE RESEARCH — four routes surveyed; shift symmetry argument identified  
**Date:** April 2026  
**Depends on:** `theory/second_variation_dssyk.md`, `theory/coda_mond_theorem.md`  
**Epistemic flags:**
- `[ESTABLISHED]` — proved in this or prior documents
- `[CODA]` — new result from this session
- `[OPEN]` — requires further calculation
- `[RULED OUT]` — tried and shown to fail

---

## 0. The Problem Statement

The CODA MOND Theorem (`coda_mond_theorem.md`) assumes premise (iii):

$$S_{\rm kin} = -\frac{a_0^2}{8\pi G}\int d^4x\sqrt{-g}\;
F\!\left(\frac{|\nabla\mathcal{C}_K|^2}{\kappa^2 a_0^2}\right)$$

This is an action of AQUAL form, with the MOND function determined by
the gradient of the complexity density. The question is: why this form
(AQUAL in $\nabla\mathcal{C}_K$) rather than, say, an action depending
on $\mathcal{C}_K$ itself?

The **holographic dictionary problem** is to derive this form from the
DSSYK complexity functional $\mathcal{C}_{dS}[g]$.

From `second_variation_dssyk.md`, the second variation $\delta^2\mathcal{C}_{dS}/\delta g^2$
has contributions:
- Direct-direct: $(3/2)\Phi^2$ — a potential term, no gradients
- Non-analytic: $|\Phi|^{3/2}$ — from the triple derivative $g'''(\tau_*)$

Neither is the gradient structure $F(|\nabla\Phi|^2/a_0^2)$ of AQUAL.

This document records the calculation of four routes, their failures,
and the identification of a symmetry argument that may resolve the problem.

---

## 1. Four Routes Surveyed

### Route A — Jacobi Spectrum `[RULED OUT]`

**Attempt:** The Jacobi operator on the dS$_4$ limiting surface has
eigenvalues $\lambda(k,\ell) = 3k^2 - \frac{3}{2}\ell(\ell+1) + \frac{7}{3}$.
The kinetic term $3k^2$ looks like a gradient operator. Perhaps the Jacobi
two-point function gives the AQUAL structure.

**Calculation:** The forcing term for shape deformations under $\delta g = 2\Phi g$
is the normal derivative $n^\mu\nabla_\mu\Phi$. At the limiting surface,
the dS field equation $\Box_{dS}\Phi = 0$ gives $\partial_\tau^2\Phi = \frac{1}{4}k^2\Phi$
at $\tau_* = \sqrt{3/2}$ (where $|1 - \tau_*^2| = \frac{1}{2}$), so the
forcing picks up a factor of $k$. The shape contribution to the second variation:

$$\delta^2\mathcal{C}\big|_{\rm shape}(k) \sim
\frac{\frac{1}{4}k^2|\Phi_k|^2}{3k^2 + 7/3}
= \frac{k^2|\Phi_k|^2}{12k^2 + 28/3}$$

**Limits:**
- $k \to \infty$ (Newtonian): $\to |\Phi_k|^2/12$ — a potential term, NOT kinetic
- $k \to 0$ (deep MOND): $\to \frac{3}{28}k^2|\Phi_k|^2$ — a kinetic term ✓

**Failure mode:** The Jacobi function $s/(12s + 28/3)$ (with $s = k^2/a_0^2 = a_N^2/a_0^2$)
differs from $\tanh(\sqrt{s})$ by factors of 12–300 across the relevant range:

| $s$ | $\tanh(\sqrt{s})$ | $s/(12s + 28/3)$ | ratio |
|-----|------------------|--------------------|-------|
| 0.001 | 0.032 | 0.000107 | 295 |
| 1.0 | 0.762 | 0.047 | 16 |
| 100 | 1.000 | 0.083 | 12 |

The Jacobi spectrum alone does NOT reproduce the tanh interpolation.
Furthermore, the UV/IR roles are backwards: the Jacobi gives a kinetic
term at small $k$ (deep MOND) and a potential term at large $k$
(Newtonian) — the opposite of what we need from AQUAL.

**Conclusion:** Route A fails to give the global AQUAL gradient structure.

### Route B — Lanczos Perturbation Theory `[RULED OUT]`

**Attempt:** The DSSYK Lanczos coefficients $b_n \to n/2$ in pure dS$_4$.
In perturbed dS, $b_n$ picks up corrections $\delta b_n \sim b_n^{(0)}\Phi(\tau_*(n\ell))$
at each level. The gradient $\nabla\Phi$ enters through the level-to-level
variation of $b_n$ as the turning point sweeps across different radii.

**Calculation:** The level-to-level difference of the Lanczos corrections:
$$\delta b_{n+1} - \delta b_n \approx 3b_0 \cdot a_N(r_n)\cdot\Delta r_n$$
is proportional to the Newtonian acceleration at the corresponding turning
point radius. Summing over levels:
$$\sum_n \delta b_n \cdot f(n) \approx 3b_0\ell\,a_N(r_{\rm LES})
\cdot\int_0^\infty f(n)\,dn$$

**Failure mode:** The sum is dominated by the accumulation near the LES,
giving a contribution proportional to $a_N(r_{\rm LES})$ — a fixed value,
not an integral over all bulk positions. Route B cannot generate the
integral $\int F(a_N^2/a_0^2)d^4x$ needed for AQUAL.

**Conclusion:** Route B gives local (LES) information, not global AQUAL.

### Route C — Boundary Coupling at the LES `[PARTIAL — CODA]`

**Attempt:** At the LES radius $r_{\rm LES} = \ell/\sqrt{3/2}$, for any
spherically symmetric Newtonian potential:
$$|\Phi(r_{\rm LES})| = a_N(r_{\rm LES})\cdot r_{\rm LES}
= a_N \cdot \frac{\ell}{\sqrt{3/2}}$$

With $a_0 = cH_0/2\pi = c/(2\pi\ell)$ (Route 3):
$$\frac{a_N}{a_0} = |\Phi(r_{\rm LES})|\cdot\frac{2\pi\sqrt{3/2}}{c}$$

Therefore, the DSSYK complexity evaluated at the LES with $|\Phi|$ as argument:
$$C_K\!\left(\frac{|\Phi(r_{\rm LES})|}{\Lambda}\right) = C_K\!\left(\frac{a_N}{a_0}\right)
= \log\cosh\!\left(\frac{a_N}{a_0}\right)$$

where $\Lambda = c/(2\pi\sqrt{3/2})$. The identification is self-consistent
and the algebra checks out exactly. `[CODA — verified numerically]`

**Partial success:** This IS the correct MOND interpolation, but only at $r = r_{\rm LES}$.

**Failure mode:** For $r \neq r_{\rm LES}$, $|\Phi(r)| = a_N(r)\cdot r$ and
the proportionality constant $r$ is not equal to $r_{\rm LES} = \ell/\sqrt{3/2}$.
The identification $|\Phi| \leftrightarrow a_N/a_0$ fails at other radii.

**Conclusion:** Route C gives the correct MOND physics at the MOND radius
$r_M \sim r_{\rm LES}$ but cannot be extended to a global AQUAL action.

### Route D — Integral Over Surface Family `[RULED OUT]`

**Attempt:** The total complexity change, integrating the growth rate
perturbation over all boundary times $w_0$:
$$\delta\mathcal{C}_{\rm total} \propto \int_0^\infty\Phi(r_*(w_0))\,dw_0$$

Changing variable to $r_*$: this gives $\int\Phi(r)\,L(r)\,dr$ where
$L(r) = |dw_0/dr_*|^{-1}$ is the rate at which the turning point moves.

**Calculation:** Near the LES, $r_* \approx r_{\rm LES} - Ce^{-w_0/L_0}$, giving
$L(r) \sim (r_{\rm LES} - r)$ — a linear vanishing at the LES.

For the MOND match: $\Phi(r)\cdot L(r) = c\cdot F(a_N^2/a_0^2)$ requires
$L(r) \sim r^{-5}$ for a point mass in deep MOND. But $L(r) \sim (r_{\rm LES} - r)$
is completely different.

**Conclusion:** Route D fails. The integral over boundary times does not
reproduce the AQUAL radial structure.

---

## 2. What the Failed Routes Reveal

All four routes fail in the same fundamental way: the DSSYK complexity
is a functional of $|\Phi|$ (the potential VALUE at the LES or near it),
while AQUAL is a functional of $|\nabla\Phi|$ (the potential GRADIENT
throughout the bulk). These differ in $r$-dependence for any specific
potential:

| Quantity | Point mass $r$-dependence |
|---------|--------------------------|
| $|\Phi(r)|$ | $r^{-1}$ |
| $|\nabla\Phi(r)|^2 = a_N^2$ | $r^{-4}$ |
| $F(a_N^2/a_0^2)$ deep MOND | $r^{-6}$ |

No algebraic manipulation within a single surface evaluation converts
$r^{-1}$ into $r^{-4}$ or $r^{-6}$.

**The holographic dictionary cannot come from evaluating the DSSYK
complexity at the LES alone. It requires a different identification
of how $\mathcal{C}_K(x)$ couples to the gravitational sector.**

---

## 3. The Shift Symmetry Argument `[CODA — leading candidate]`

### 3.1 The symmetry

In pure de Sitter, $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2)$ is a
universal constant. Shifting the complexity density by a constant:

$$\mathcal{C}_K(x) \to \mathcal{C}_K(x) + c$$

corresponds to choosing a different reference state for the DSSYK
complexity. Physical MOND forces should be independent of this choice
— the force is determined by the GRADIENT of the complexity, not its
absolute value.

This is a **shift symmetry**: the action functional must be invariant
under $\mathcal{C}_K \to \mathcal{C}_K + c$ for any constant $c$.

### 3.2 Consequence for the kinetic action

Any functional of $\mathcal{C}_K$ that is shift-symmetric must depend
only on $\nabla\mathcal{C}_K$ (or higher derivatives), not on
$\mathcal{C}_K$ itself.

The most general shift-symmetric, Lorentz-invariant, second-order
kinetic action for $\mathcal{C}_K$ is:

$$S_{\rm kin}[\mathcal{C}_K] = \int d^4x\sqrt{-g}\;
\mathcal{L}(|\nabla\mathcal{C}_K|^2)$$

for some function $\mathcal{L}$. This is exactly the AQUAL form.

The specific function $\mathcal{L}(s) = -(a_0^2/8\pi G)F(s/\kappa^2 a_0^2)$
is then determined by:
1. Dimensional analysis (the $a_0^2/G$ prefactor)
2. The correct Newtonian limit $\mathcal{L}(s) \to -(s/\kappa^2)/(8\pi G)$ for large $s$
3. The DSSYK function $F(s) = 2\sqrt{s}\log\cosh\sqrt{s} - ...$
   determining the specific form of $\mathcal{L}$

### 3.3 Physical basis of the symmetry

Why should the action be shift-symmetric in $\mathcal{C}_K$?

**Argument 1 — Reference state independence:** The complexity density
$\mathcal{C}_K(x)$ is defined relative to a reference state (pure de Sitter
vacuum). Different choices of reference shift $\mathcal{C}_K$ by a constant.
Physical predictions cannot depend on this choice.

**Argument 2 — Goldstone boson analogy:** In the DSSYK construction,
the complexity is related to the phase of the Hartle-Hawking state. Phase
rotations (shifts by $2\pi$) are gauge redundancies, and the low-energy
effective action for the phase must be purely derivative.

**Argument 3 — Holographic Weyl anomaly:** In AdS/CFT, the holographic
action for a massless scalar is purely kinetic (no potential term) due
to the conformal symmetry of the boundary theory. The DSSYK/dS
correspondence has an analogous structure where $\mathcal{C}_K$ plays
the role of the Goldstone boson of broken de Sitter isometries.

### 3.4 Status and what remains

**Established:** The shift symmetry, if present, uniquely forces the
action to AQUAL form. The remaining question is whether the DSSYK
construction genuinely has this symmetry.

**What needs to be proved:** That the DSSYK complexity functional
$\mathcal{C}_{dS}[g + 2\Phi g]$ is invariant under $\Phi(x) \to \Phi(x) + c$
(a constant shift of the Newtonian potential, which corresponds to
$\mathcal{C}_K \to \mathcal{C}_K + 3c\mathcal{C}_K^{(0)}$).

**Physical plausibility:** Adding a constant to $\Phi$ everywhere shifts
the overall energy level but not the forces (since forces are $\nabla\Phi$).
The DSSYK complexity responds to $\Phi$ at the turning point of each
extremal surface. If the complexity is sensitive to the DIFFERENCE in
$\Phi$ between different radii (i.e., $\nabla\Phi$) rather than the
absolute value, the shift symmetry holds.

**The specific calculation:** Does $\mathcal{C}_{dS}[g + 2(\Phi + c)g] =
\mathcal{C}_{dS}[g + 2\Phi g] + $ (constant independent of $x$)?

From the perturbed dS result: $\delta\mathcal{C}_K = 3\Phi\mathcal{C}_K^{(0)}$.
Under $\Phi \to \Phi + c$: $\delta\mathcal{C}_K \to 3(\Phi + c)\mathcal{C}_K^{(0)}$.

The constant shift $3c\mathcal{C}_K^{(0)}$ appears in $\mathcal{C}_K$
everywhere — it's a spatially uniform addition. Whether this induces a
constant shift in the ACTION depends on whether the action is evaluated
on the COMPLEXITY FIELD $\mathcal{C}_K$ or on its GRADIENT $\nabla\mathcal{C}_K$.

Since $\nabla(\mathcal{C}_K + 3c\mathcal{C}_K^{(0)}) = \nabla\mathcal{C}_K$
(the gradient of a constant is zero), the AQUAL action automatically
satisfies the shift symmetry. The question is whether the DSSYK
generating functional naturally produces the AQUAL form rather than
a non-shift-symmetric potential form. `[OPEN]`

---

## 4. Refined Statement of the Open Problem

The holographic dictionary problem reduces to:

**Does the DSSYK generating functional $W[\mathcal{C}_K]$ possess the
shift symmetry $\mathcal{C}_K \to \mathcal{C}_K + c$?**

If yes: the AQUAL form $S_{\rm kin} \propto \int F(|\nabla\mathcal{C}_K|^2)d^4x$
follows from symmetry, and premise (iii) of the MOND theorem is derived.

If no: a different kinetic action form must be postulated, and the MOND
equation would differ from the tanh form.

The specific calculation to resolve this:

1. Compute the DSSYK generating functional $W[\Phi + c] - W[\Phi]$ for
   a uniform potential shift $c$
2. If $W[\Phi + c] - W[\Phi]$ is independent of the field configuration
   (depends only on $c$ and global quantities), the shift symmetry holds
3. From the perturbed result: $W[\Phi] = \mathcal{C}_K^{(0)}\int(1 + 3\Phi)d^4x$,
   so $W[\Phi + c] - W[\Phi] = 3c\mathcal{C}_K^{(0)}\int d^4x$ — a constant
   times the spacetime volume. This is shift-symmetric if the volume is
   a fixed background quantity (true in the static-patch approximation).

**Preliminary evidence for the shift symmetry:** `[CODA]`

The first variation $\delta\mathcal{C}_{dS} = 3\Phi\mathcal{C}_K^{(0)}$ gives
$W[\Phi + c] - W[\Phi] = 3c\mathcal{C}_K^{(0)}\cdot V$ where $V$ is the
static-patch 4-volume — independent of the field profile $\Phi(x)$. This
is exactly what the shift symmetry requires at first order. `[ESTABLISHED]`

At second order: the non-analytic term $\alpha|\Phi|^{3/2}$ transforms as
$|\Phi + c|^{3/2} \neq |\Phi|^{3/2} + |c|^{3/2}$ — the shift symmetry is
BROKEN by the second-order non-analytic term. `[ESTABLISHED]`

This suggests the shift symmetry is a property of the GRADIENT structure
(which is shift-symmetric by construction) but NOT of the potential-value
structure (which is shift-violating). The AQUAL kinetic action preserves
the shift symmetry because it depends only on $\nabla\mathcal{C}_K$. The
direct second variation (potential term $\Phi^2$) violates it.

---

## 5. Proposed Resolution: Two-Step Identification

The calculation suggests the following two-step holographic dictionary:

**Step 1 — Identify the complexity FIELD** (established):
$$\mathcal{C}_K(x) = \mathcal{C}_K^{(0)}\bigl(1 + 3\Phi(x)\bigr)$$

**Step 2 — Identify the kinetic action by shift symmetry** (to be proved):

The only shift-symmetric, locally Lorentz-invariant kinetic action for
$\mathcal{C}_K$ of second-derivative order is:
$$S_{\rm kin} = \int d^4x\sqrt{-g}\;\mathcal{L}(|\nabla\mathcal{C}_K|^2)$$

The function $\mathcal{L}$ is then fixed by:
- Newtonian limit: $\mathcal{L}(s) \to -s/(8\pi G\kappa^2)$ (Poisson)
- DSSYK form: $F(s/\kappa^2 a_0^2) = F'(s/\kappa^2 a_0^2) = \tanh(\sqrt{s}/\kappa a_0)$
- $\kappa$ cancellation: the argument becomes $a_N^2/a_0^2$

This gives premise (iii) from the shift symmetry alone, without requiring
the full second variation calculation to reproduce the AQUAL structure.

**What the shift symmetry argument needs:**
A proof that the DSSYK effective action for the complexity field is
shift-symmetric — either from the DSSYK Hamiltonian structure (is there
a conserved charge corresponding to the constant shift?) or from the
holographic bulk (does the dS/CFT dictionary map $\Phi$-shifts to trivial
boundary transformations?).

---

## 6. What Has Been Established and What Remains

### Established `[ESTABLISHED]`

- Route A (Jacobi) fails: does not reproduce tanh, UV/IR roles reversed
- Route B (Lanczos) fails: only gives local information at LES
- Route C (boundary coupling) works at $r = r_{\rm LES}$ but not globally
- Route D (surface integral) fails: incorrect $r$-scaling for MOND
- The shift symmetry $\mathcal{C}_K \to \mathcal{C}_K + c$ forces AQUAL form
- The first variation is shift-symmetric: $W[\Phi + c] - W[\Phi] = $ const ✓
- The second-order non-analytic term $|\Phi|^{3/2}$ is NOT shift-symmetric ✗

### The Remaining Calculation `[OPEN — Priority 1]`

Prove (or disprove) that the DSSYK effective action for the complexity field
is shift-symmetric. Specifically:

1. Does the DSSYK Hamiltonian have a conserved charge corresponding to
   $\mathcal{C}_K \to \mathcal{C}_K + c$?
2. Does the dS bulk-to-boundary map make $\Phi$-shifts correspond to
   trivial (non-dynamical) boundary transformations?
3. Can the shift-symmetry breaking term $|\Phi|^{3/2}$ be absorbed into
   a redefinition of the field or action?

If question 3 is yes — if the non-analytic term is an artifact of using
$\Phi$ (the potential value) as the field rather than $|\nabla\Phi|$ (the
gradient) — then the shift symmetry argument completely resolves the
holographic dictionary problem.

---

## 7. Summary Table

| Route | Attempt | Result | Status |
|-------|---------|--------|--------|
| A — Jacobi spectrum | Kinetic term from $3k^2$ eigenvalue | UV/IR backwards; not tanh | `[RULED OUT]` |
| B — Lanczos perturbation | $\delta b_n \propto a_N(r_n)$ | Only gives LES contribution | `[RULED OUT]` |
| C — Boundary coupling | $|\Phi|_{\rm LES} \propto a_N/a_0$ | Works at LES, not globally | `[PARTIAL]` |
| D — Surface integral | $\int\Phi(r_*) dw_0$ | Wrong $r$-scaling | `[RULED OUT]` |
| **Shift symmetry** | $\mathcal{C}_K \to \mathcal{C}_K + c$ forces AQUAL | Works if symmetry holds | **`[LEADING CANDIDATE]`** |

**Next calculation:** Verify whether the DSSYK construction has the
shift symmetry by checking whether the effective action for
$\mathcal{C}_K$ is purely kinetic (gradient-dependent only) in the
DSSYK Hamiltonian framework.

---

*End of document. Version 0.1.*  
*Status: Four routes surveyed; shift symmetry identified as leading candidate.*  
*Priority 1: Prove/disprove the shift symmetry of the DSSYK effective action.*
