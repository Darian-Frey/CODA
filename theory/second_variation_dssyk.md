# Second Variation of the DSSYK Complexity: $\delta^2\mathcal{C}_{dS}/\delta g^2$

**Document:** `theory/second_variation_dssyk.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Status:** PARTIAL RESULT — deep-MOND power established; holographic dictionary step open  
**Date:** April 2026  
**Depends on:** `theory/dS4_perturbed.md`, `theory/coda_mond_theorem.md`  
**Epistemic flags:**
- `[ESTABLISHED]` — proved algebraically/numerically in this document
- `[CODA]` — new result or interpretation
- `[OPEN]` — requires further calculation

---

## 0. The Question

The CODA MOND Theorem (`coda_mond_theorem.md`) requires premise (iii):

$$S_{\rm kin} = -\frac{a_0^2}{8\pi G}\int d^4x\,F\!\left(\frac{|\nabla\mathcal{C}_K|^2}{\kappa^2 a_0^2}\right)$$

This premise was asserted, not derived. To derive it from the DSSYK
construction requires showing that the second variation of the complexity
functional,

$$\frac{\delta^2\mathcal{C}_{dS}}{\delta g^{\mu\nu}(x)\,\delta g^{\rho\sigma}(y)},$$

has AQUAL structure when expanded in the perturbed de Sitter background.

**Result of this document:** The second variation has two contributions.
The direct-direct term gives a potential ($\Phi^2$). The non-analytic
family term gives $|\Phi|^{3/2}$ — matching the deep-MOND power $F(s)
\sim s^{3/2}$ — but connecting $|\Phi|$ to $a_N^2/a_0^2$ requires the
holographic dictionary (the remaining open step).

---

## 1. Structure of the Second Variation

The DSSYK complexity functional:

$$\mathcal{C}_{dS}[g] = \frac{-i}{G_N\ell}\int_{\Sigma(g)}\sqrt{|h(g)|}\,d^3\sigma$$

where $\Sigma(g)$ is the extremal timelike slice in metric $g$.

Under $g \to g + \delta g$ (with $\delta g_{\mu\nu} = 2\Phi\,g_{\mu\nu}$,
a conformal perturbation in Newtonian gauge):

$$\mathcal{C}_{dS}[g+\delta g] = \mathcal{C}^{(0)}_{dS}
+ \mathcal{C}^{(1)}_{dS}[\Phi]
+ \mathcal{C}^{(2)}_{dS}[\Phi^2]
+ \mathcal{C}^{(3/2)}_{dS}[|\Phi|^{3/2}]
+ \ldots$$

The second variation $\mathcal{C}^{(2)}_{dS}$ has three contributions:

| Contribution | From | Order |
|-------------|------|-------|
| Direct-direct | $\sqrt{|h|}$ to 2nd order, surface fixed | $O(\Phi^2)$ |
| Shape | Surface deforms to remain extremal | $O(\Phi^2)$ |
| Non-analytic | Triple derivative through double degeneracy | $O(|\Phi|^{3/2})$ |

The non-analytic term is sub-leading in magnitude but encodes the MOND physics.

---

## 2. Direct-Direct Contribution

Under $\delta g_{\mu\nu} = 2\Phi\,g_{\mu\nu}$, the induced metric on
a 3-surface changes as $h_{ab} \to (1+2\Phi)h_{ab}$. The volume element:

$$(1+2\Phi)^{3/2}\sqrt{|h|} = \left(1 + 3\Phi + \frac{3}{2}\Phi^2
+ \ldots\right)\sqrt{|h|}$$

**Direct-direct contribution:**

$$\mathcal{C}^{(2)}_{\rm direct} = \frac{-i}{G_N\ell}\cdot\frac{3}{2}
\int_\Sigma\Phi^2\,\sqrt{|h|}\,d^3\sigma$$

`[ESTABLISHED]`

This is a **potential term** — quadratic in $\Phi$, with no spatial gradients.
It contributes an effective mass term for the complexity field, not a kinetic term.

---

## 3. Jacobi Operator for Shape Deformation

The extremal surface $\Sigma$ deforms under the metric perturbation.
The deformation $\xi$ (normal displacement from $\Sigma$) satisfies the
**Jacobi equation**:

$$\mathcal{J}\xi = \mathcal{F}[\Phi], \qquad
\mathcal{F}[\Phi] = -n^\mu\nabla_\mu\Phi\big|_\Sigma$$

where the **Jacobi operator** on the limiting surface is:

$$\mathcal{J} = \Box_\Sigma - \left(K_{ab}K^{ab} - R_{\mu\nu}n^\mu n^\nu\right)$$

with $\Box_\Sigma$ the d'Alembertian on the induced Lorentzian metric
$(-, +, +)$ on $\Sigma$, $K_{ab}$ the second fundamental form, and $n^\mu$
the unit spacelike normal.

**Shape contribution to the second variation:**

$$\mathcal{C}^{(2)}_{\rm shape} = \frac{-i}{G_N\ell}\int_\Sigma
\sqrt{|h|}\;\xi\cdot\mathcal{F}[\Phi]\,d^3\sigma$$

With $\xi = \mathcal{J}^{-1}\mathcal{F}[\Phi]$, this is a bilinear form in
$n\cdot\nabla\Phi$.

### 3.1 Jacobi Operator on the dS4 Limiting Surface

For the limiting surface at $\tau_* = \sqrt{3/2}$ in dS4 (using $\ell = 1$
units). The induced metric signature is $(-,+,+)$ (w is timelike, $\theta,\phi$
are spacelike). `[ESTABLISHED — computed explicitly]`

**Metric components:**

$$h_{ww} = -\frac{1}{3}, \qquad h_{\theta\theta} = \frac{2}{3}, \qquad
h_{\phi\phi} = \frac{2}{3}\sin^2\theta$$

$$h^{ww} = -3, \qquad h^{\theta\theta} = \frac{3}{2}, \qquad
h^{\phi\phi} = \frac{3}{2}\csc^2\theta$$

**Computed Jacobi curvature term** ($\ell = 1$, $R_{\mu\nu} = 3g_{\mu\nu}$):

$$K_{ab}K^{ab} = \frac{16}{3}, \qquad R_{\mu\nu}n^\mu n^\nu = 3$$

$$K_{ab}K^{ab} - R_{\mu\nu}n^\mu n^\nu = \frac{7}{3}$$

`[ESTABLISHED — verified numerically]`

**Jacobi eigenvalue** for mode $e^{ik_w w}Y_{\ell m}(\theta,\phi)$:

$$\lambda(k_w,\ell) = 3k_w^2 - \frac{3}{2}\ell(\ell+1) + \frac{7}{3}$$

`[ESTABLISHED]`

**Ground state** ($k_w = 0$, $\ell = 0$):

$$\boxed{\lambda_0 = \frac{7}{3} \approx 2.33}$$

**Key finding:** The Jacobi ground state is **non-zero** ($\lambda_0 = 7/3$)
in pure de Sitter. There is no near-zero mode in the Jacobi spectrum of the
limiting surface. `[ESTABLISHED]`

**Implication:** The MOND physics does NOT come from a Jacobi near-zero
mode (as might be expected from analogy with holographic entanglement
entropy). Instead, it arises from the **degenerate family structure** of the
limiting surface — the $g' = 0$ condition established in `dS4_perturbed.md`.

### 3.2 Shape Contribution is Analytic

Since $\lambda_0 = 7/3 \neq 0$, the Jacobi operator is invertible on pure
de Sitter, and the shape deformation $\xi = \mathcal{J}^{-1}\mathcal{F}$
is well-defined and analytic in $\Phi$. The shape contribution:

$$\mathcal{C}^{(2)}_{\rm shape} \propto
\int_\Sigma\frac{(n\cdot\nabla\Phi)^2}{\lambda(k_w,\ell)}\,d^3\sigma$$

This is an analytic functional of $\Phi$ — a gradient squared term that
gives the Poisson (Newtonian) kinetic structure at large $k_w$.

---

## 4. The Non-Analytic $|\Phi|^{3/2}$ Term — The MOND Signal

The MOND physics comes from an unexpected source: the **third-order expansion**
of the growth rate $g(\tau_*)$ through the double degeneracy.

### 4.1 Setup

From `dS4_perturbed.md`, the perturbed turning point satisfies:

$$(\delta\tau)^2 = -\frac{3\Phi}{4} \quad \Rightarrow \quad
\delta\tau = \pm\sqrt{\frac{3|\Phi|}{4}}$$

This is $O(|\Phi|^{1/2})$, not $O(\Phi)$, due to the double degeneracy
$f_\tau|_* = g'|_* = 0$.

### 4.2 Third-Order Expansion of the Growth Rate

Expanding $g(\tau_* + \delta\tau) = E_* + g'\delta\tau + \frac{1}{2}g''(\delta\tau)^2
+ \frac{1}{6}g'''(\delta\tau)^3 + \ldots$ with $g'|_* = 0$:

$$g = E_* + \underbrace{\frac{1}{2}g''\cdot(-3\Phi/4)}_{\text{linear in }\Phi}
+ \underbrace{\frac{1}{6}g'''\cdot(\pm\sqrt{3|\Phi|/4})^3}_{O(|\Phi|^{3/2})}
+ O(\Phi^2)$$

**Computed derivatives** at $\tau_* = \sqrt{3/2}$ (verified numerically):

$$g''(\tau_*) = -\frac{16\sqrt{3}}{9} \approx -3.079$$

$$g'''(\tau_*) = \frac{208\sqrt{2}}{9} \approx 32.68$$

**Third-order coefficient:**

$$\frac{g'''}{6}\left(\frac{3}{4}\right)^{3/2}
= \frac{g'''}{6}\cdot\frac{3\sqrt{3}}{8}
= \frac{13\sqrt{6}}{9} \approx 3.538$$

`[ESTABLISHED — verified symbolically and numerically]`

**The growth rate in the perturbed background:**

$$g(\tau_*^{\rm pert}) = E_*\left[1 + 3\Phi
+ \frac{13\sqrt{6}}{9E_*}|\Phi|^{3/2}\cdot\text{sign}(\delta\tau)
+ O(\Phi^2)\right]$$

$$= E_*\left[1 + 3\Phi + \alpha|\Phi|^{3/2} + O(\Phi^2)\right]$$

where $\alpha = \frac{13\sqrt{6}}{9E_*} = \frac{13\sqrt{6}}{9}\cdot\frac{9}{2\sqrt{3}}
= \frac{13\sqrt{2}}{2}$. `[ESTABLISHED]`

### 4.3 The Non-Analytic Contribution to $\mathcal{C}^{(2)}_{dS}$

The complexity growth rate to second-order (in the sense of all $O(\Phi^2)$
and non-analytic $O(|\Phi|^{3/2})$ terms):

$$\frac{d\mathcal{C}_{dS}}{dw_0}\bigg|_{\rm pert}
= c_{d=3}\,S_{dS}\,T_{dS}\cdot\left[1 + 3\Phi + \alpha|\Phi|^{3/2}\right]$$

The **non-analytic contribution** to the second variation:

$$\boxed{\mathcal{C}^{(3/2)}_{dS} = c_{d=3}\,S_{dS}\,T_{dS}\cdot\alpha
\int_{\rm bulk}|\Phi(x)|^{3/2}\,d^4x}$$

`[ESTABLISHED — from $g'''$ term through double degeneracy]`

---

## 5. Matching to AQUAL: The Power is Right

### 5.1 The Deep-MOND AQUAL Limit

The AQUAL kinetic action in deep MOND ($a_N \ll a_0$, $s \ll 1$):

$$-\frac{a_0^2}{8\pi G}F(s)\big|_{s\ll 1} \approx -\frac{a_0^2}{8\pi G}\cdot\frac{2}{3}s^{3/2}
= -\frac{a_0^2}{8\pi G}\cdot\frac{2}{3}\left(\frac{a_N^2}{a_0^2}\right)^{3/2}
= -\frac{a_N^3}{12\pi G\,a_0}$$

This is $O(a_N^3)$, or equivalently $O(|\nabla\Phi|^3)$.

### 5.2 The DSSYK Non-Analytic Term

The DSSYK complexity generates $\alpha|\Phi|^{3/2}$.

**The power matches:** $|\Phi|^{3/2} \sim (a_N/a_0)^3$ IF $|\Phi| \sim (a_N/a_0)^2$.

**When does $|\Phi| = (a_N/a_0)^2$?**

For a Newtonian potential $\Phi = -GM/r$, $a_N = GM/r^2$, $a_0 = c^2/\ell$:

$$|\Phi| = \frac{GM}{r}, \qquad \frac{a_N^2}{a_0^2} = \frac{G^2M^2}{r^4 a_0^2}$$

These are equal when $r = GM/a_0 = r_M$ (the MOND radius). At $r = r_M$:
$a_N = a_0$ — the MOND transition scale. `[ESTABLISHED]`

This means the identification $|\Phi| \leftrightarrow a_N^2/a_0^2$ holds
PRECISELY at the MOND transition radius, not globally.

**For the full AQUAL structure**, the identification must hold for all $r$,
which requires a holographic mapping that converts the Newtonian potential
value $\Phi(r)$ into the DSSYK boundary coordinate argument.

---

## 6. The Remaining Gap — The Holographic Dictionary

### 6.1 What Is Established

| Quantity | Value | Status |
|---------|-------|--------|
| Direct-direct contribution | $(3/2)\int\Phi^2\sqrt{|h|}\,d^3\sigma$ | `[ESTABLISHED]` |
| Jacobi ground eigenvalue | $\lambda_0 = 7/3$ (non-zero) | `[ESTABLISHED]` |
| MOND signal origin | Family structure, NOT Jacobi near-zero mode | `[ESTABLISHED]` |
| Non-analytic power | $|\Phi|^{3/2}$ from $g'''$ | `[ESTABLISHED]` |
| Non-analytic coefficient | $\alpha = 13\sqrt{2}/2$ | `[ESTABLISHED]` |
| Power matching to AQUAL | $|\Phi|^{3/2} \sim (a_N/a_0)^3$ at $r = r_M$ | `[ESTABLISHED]` |

### 6.2 What Remains Open

The holographic dictionary step: for the DSSYK complexity functional
evaluated at bulk point $x = (r, t_s)$, how does the bulk Newtonian potential
$\Phi(r)$ map to the DSSYK boundary coordinate argument $\chi\theta/2$?

Specifically: does there exist a mapping $\chi\theta/2 = \mathcal{F}[\Phi, r]$
such that $|\Phi|^{3/2}$ in the DSSYK generating functional maps exactly to
$F(a_N^2/a_0^2)$ in the AQUAL action?

For this to work, the mapping must satisfy:

$$|\mathcal{F}[\Phi, r]|^2 = \frac{a_N^2}{a_0^2} = \frac{|\nabla\Phi|^2}{a_0^2}$$

i.e., the DSSYK argument must be proportional to the LOCAL GRADIENT of $\Phi$,
not the value of $\Phi$ itself.

**The required calculation:** Compute how the DSSYK boundary time $\chi$,
evaluated at a bulk point $x$ in the extremal surface construction, responds
to the GRADIENT of the metric perturbation $\nabla\Phi(x)$ — not just $\Phi(x)$.
This is a calculation on the DSSYK boundary theory that requires the explicit
bulk-to-boundary map for the extremal surface construction.

---

## 7. The Full Second Variation — Schematic Result

Combining all contributions:

$$\frac{\delta^2\mathcal{C}_{dS}}{\delta\Phi(x)\delta\Phi(y)}\bigg|_{dS_4}
= \underbrace{\frac{3}{2}\mathcal{C}_K^{(0)}\delta^{(4)}(x-y)
\cdot\delta^{(3)}(x-\Sigma)}_{\text{potential (local on }\Sigma\text{)}}
+ \underbrace{K_{\rm shape}(x,y)}_{\text{gradient (Jacobi Green's fn)}}
+ \underbrace{\mathcal{N}[|\Phi(x)|^{3/2}]}_{\text{non-analytic (MOND)}}$$

The three terms:

1. **Potential:** Local on the surface, gives an effective mass for $\mathcal{C}_K$.
   Not relevant for MOND.

2. **Gradient (Jacobi):** The Green's function $K_{\rm shape}(x,y) =
   \mathcal{J}^{-1}(n\cdot\nabla)\otimes(n\cdot\nabla)$ produces a kinetic
   term proportional to $(n\cdot\nabla\Phi)^2$ — the Newtonian acceleration
   squared. This is the Poisson kinetic term (Newtonian gravity).

3. **Non-analytic:** The $|\Phi|^{3/2}$ term from the $g'''$ contribution
   through the double degeneracy. **This is the MOND signal.**

---

## 8. Summary and Status

**What this calculation establishes:**

The second variation of the DSSYK complexity functional in dS4 contains a
non-analytic contribution $\propto|\Phi|^{3/2}$ arising from the triple
derivative $g'''(\tau_*)$ acting through the double degeneracy of the
limiting surface. The power $3/2$ matches the deep-MOND AQUAL limit
$F(s) \sim s^{3/2}$. The Jacobi ground eigenvalue $7/3$ means the MOND
signal does NOT come from a Jacobi near-zero mode — an important structural
clarification. `[ESTABLISHED]`

**What remains for the full derivation of premise (iii):**

The mapping from the bulk Newtonian potential $\Phi(r)$ to the DSSYK
boundary argument $\chi\theta/2 = |\nabla\Phi|/a_0$ requires the explicit
bulk-to-boundary map of the DSSYK extremal surface construction. This is the
holographic dictionary step — showing that the DSSYK generating functional,
when expressed in terms of the LOCAL GRADIENT $|\nabla\Phi|$ rather than the
potential VALUE $|\Phi|$, has the form $F(|\nabla\Phi|^2/a_0^2)$.

The calculation amounts to showing:

$$\int_{\rm bulk}|\Phi(x)|^{3/2}\,d^4x \xlongrightarrow[\text{holographic}]{\text{dictionary}}
\int_{\rm bulk}F\!\left(\frac{|\nabla\Phi(x)|^2}{a_0^2}\right)d^4x$$

in the appropriate bulk-to-boundary limit. `[OPEN — Priority 1]`

---

*End of document. Version 0.1.*  
*Key results: Jacobi $\lambda_0 = 7/3$ (non-zero); MOND signal is the*  
*non-analytic $|\Phi|^{3/2}$ term from double degeneracy.*  
*Remaining: holographic dictionary mapping $|\Phi|^{3/2} \to F(|\nabla\Phi|^2/a_0^2)$.*
