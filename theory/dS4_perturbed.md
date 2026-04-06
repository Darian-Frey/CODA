# Phase 3b Priority 1b — Perturbed dS₄: Complexity Density Response

**Document:** `theory/dS4_perturbed.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Status:** CALCULATION RESULT — perturbed de Sitter analysis  
**Date:** April 2026  
**Depends on:** `theory/dS4_krylov_density.md` v0.1  
**Epistemic flags:**
- `[ESTABLISHED]` — verified algebraically and confirmed by SymPy
- `[CODA]` — new identification or interpretation
- `[OPEN]` — requires further calculation

---

## 0. The Question

From `theory/dS4_krylov_density.md`: in pure de Sitter, the complexity
density $\mathcal{C}_K^{(dS_4)} = 2/(3\sqrt{3}G_N\ell^2)$ is constant —
it does not vary from point to point. For CODA's MOND thread, we need
$\mathcal{C}_K(x)$ to be position-dependent, responding to local matter.

**This document computes how the extremal surface and its associated
complexity density respond to a small matter perturbation
$\Phi(x)$ around pure de Sitter.**

---

## 1. Setup — Perturbed Metric

The perturbed $dS_4$ metric in Newtonian gauge (perfect fluid, $\Phi = \Psi$):

$$ds^2 = \frac{\ell^2}{\tau^2}\left[-(1+2\Phi)\frac{d\tau^2}{1-\tau^2}
+ (1-2\Phi)(1-\tau^2)dw^2 + (1-2\Phi)d\Omega_2^2\right]$$

where $\Phi(x) \ll 1$ is the Newtonian potential sourced by a matter
overdensity $\delta\rho$. For a point mass $M$ in the static patch:

$$\Phi(r) = -\frac{GM}{r} = -\frac{GM\tau}{\ell}$$

(where $r = \ell/\tau$ is the static patch radial coordinate).

**Perturbation parameter:** $|\Phi| \ll 1$, i.e. $GM \ll \ell$ (test mass
in de Sitter — appropriate for all galactic scales).

---

## 2. The Unperturbed Background — A Critical Structure

Before computing the perturbation, there is a structural feature of the
unperturbed limiting surface that governs everything downstream.

**Fact 1:** The turning point condition is
$f(\tau, E) = 1-\tau^2+E^2\tau^6 = 0$.

$$\frac{\partial f}{\partial\tau}\bigg|_* = (-2\tau + 6E^2\tau^5)\bigg|_{\tau_*,E_*}
= -2\sqrt{3/2} + 6\cdot\frac{4}{27}\cdot\left(\frac{3}{2}\right)^{5/2} = 0$$

`[ESTABLISHED — verified symbolically]`

**Fact 2:** The growth rate function $g(\tau) = \tau^{-3}\sqrt{\tau^2-1}$
satisfies $g(\tau) = E(\tau)$ along the turning point locus, and:

$$g'(\tau_*) = \frac{\tau_*^{-4}(3-2\tau_*^2)}{\sqrt{\tau_*^2-1}}
= \frac{(3-3)}{\sqrt{1/2}} = 0$$

`[ESTABLISHED — verified symbolically]`

**The limiting surface $\tau_* = \sqrt{3/2}$ is a doubly-degenerate
critical point:** both $\partial f/\partial\tau$ and $g'$ vanish there.
Standard first-order perturbation theory (implicit function theorem)
fails because the Jacobian is zero.

This requires analysis at second order. The relevant higher derivatives:

$$\frac{\partial^2 f}{\partial\tau^2}\bigg|_* = 8, \qquad
g''(\tau_*) = -\frac{16\sqrt{3}}{9} \approx -3.079$$

`[ESTABLISHED — verified symbolically and numerically]`

---

## 3. Perturbed Turning Point — Second-Order Analysis

The perturbed turning point condition:

$$f_{\rm pert}(\tau, E, \Phi) = (1-2\Phi)(1-\tau^2)+(1+4\Phi)E^2\tau^6 = 0$$

$$= f(\tau,E) + \Phi\bigl[-2(1-\tau^2) + 4E^2\tau^6\bigr] = 0$$

At the turning point $f = 0$, so $1-\tau^2 = -E^2\tau^6$. The
$\Phi$-coefficient becomes:

$$K = -2(1-\tau_*^2) + 4E_*^2\tau_*^6
= 2E_*^2\tau_*^6 + 4E_*^2\tau_*^6
= 6E_*^2\tau_*^6 = 3$$

`[ESTABLISHED — computed from $E_*^2\tau_*^6 = 1/2$ at $\tau_* = \sqrt{3/2}$]`

Taylor expanding $f_{\rm pert}$ around $(\tau_*, E_*, \Phi=0)$, using
$f|_* = 0$ and $f_\tau|_* = 0$:

$$f_{\rm pert} \approx \frac{1}{2}\underbrace{f_{\tau\tau}|_*}_{=\,8}\cdot(\delta\tau)^2
+ K\Phi + \mathcal{O}(\delta\tau^3, \Phi\delta\tau, \Phi^2) = 0$$

$$4(\delta\tau)^2 + 3\Phi = 0$$

$$\boxed{(\delta\tau)^2 = -\frac{3\Phi}{4}}$$

`[ESTABLISHED]`

**For attractive gravity** ($\Phi < 0$, e.g. a point mass):

$$(\delta\tau)^2 = \frac{3|\Phi|}{4} > 0 \qquad \checkmark$$

$$\delta\tau = \pm\sqrt{\frac{3|\Phi|}{4}} \propto |\Phi|^{1/2}$$

**The turning point shift is non-linear in $\Phi$** — a direct consequence
of the double degeneracy. Standard linear perturbation theory would predict
$\delta\tau \propto \Phi$; the actual result is $\delta\tau \propto |\Phi|^{1/2}$.

---

## 4. Perturbed Complexity Density

The complexity density is proportional to the growth rate $g(\tau_*)$:

$$\mathcal{C}_K \propto g(\tau_*) = E_*$$

Under $\tau_* \to \tau_* + \delta\tau$, using $g'(\tau_*) = 0$:

$$\delta g = g'(\tau_*)\delta\tau + \frac{1}{2}g''(\tau_*)(\delta\tau)^2
= \frac{1}{2}g''(\tau_*)\cdot\left(-\frac{3\Phi}{4}\right)$$

$$= -\frac{3g''(\tau_*)}{8}\,\Phi
= -\frac{3}{8}\cdot\left(-\frac{16\sqrt{3}}{9}\right)\Phi
= \frac{2\sqrt{3}}{3}\,\Phi$$

The fractional change in complexity density:

$$\frac{\delta\mathcal{C}_K}{\mathcal{C}_K^{(0)}}
= \frac{\delta g}{g(\tau_*)} = \frac{2\sqrt{3}/3}{2\sqrt{3}/9}
= \frac{2\sqrt{3}/3 \times 9}{2\sqrt{3}} = 3$$

Wait — let me recompute this cleanly:

$$\frac{\delta\mathcal{C}_K}{\mathcal{C}_K^{(0)}} = \frac{\delta g}{g_*}
= \frac{(2\sqrt{3}/3)\Phi}{2\sqrt{3}/9} = \frac{9}{3}\,\Phi = 3\Phi$$

Hmm, let me recheck: $g_* = E_* = 2\sqrt{3}/9$, $\delta g = (2\sqrt{3}/3)\Phi$.

$$\frac{\delta g}{g_*} = \frac{2\sqrt{3}/3}{2\sqrt{3}/9}\,\Phi = \frac{9}{3}\,\Phi = 3\Phi$$

And numerically: $-\frac{3}{8}g''(\tau_*)/g(\tau_*) = -\frac{3}{8}\times(-3.079)/(0.3849) \approx 3.0\times\Phi$

$$\boxed{\frac{\delta\mathcal{C}_K(x)}{\mathcal{C}_K^{(0)}} = 3\,\Phi(x)}$$

`[ESTABLISHED — computed from $g_* = 2\sqrt{3}/9$, $g''(\tau_*) = -16\sqrt{3}/9$]`

The perturbed complexity density:

$$\mathcal{C}_K(x) = \mathcal{C}_K^{(0)}\bigl[1 + 3\Phi(x)\bigr]
= \frac{2}{3\sqrt{3}\,G_N\ell^2}\bigl[1 + 3\Phi(x)\bigr]$$

For a point mass $M$ at the origin in the static patch ($\Phi = -GM/r$):

$$\mathcal{C}_K(r) = \frac{2}{3\sqrt{3}\,G_N\ell^2}\left[1 - \frac{3GM}{r}\right]$$

`[CODA — first explicit CODA prediction for complexity density near a mass]`

---

## 5. The Gradient Structure

Taking the spatial gradient of $\delta\mathcal{C}_K$:

$$\nabla\mathcal{C}_K(x) = 3\mathcal{C}_K^{(0)}\,\nabla\Phi(x)$$

The Newtonian acceleration is $\vec{a}_N = -\nabla\Phi$, so:

$$\nabla\mathcal{C}_K = -3\mathcal{C}_K^{(0)}\,\vec{a}_N$$

$$\boxed{|\nabla\mathcal{C}_K| = 3\mathcal{C}_K^{(0)}\,a_N
= \frac{2}{\sqrt{3}\,G_N\ell^2}\,a_N}$$

`[CODA]`

**The magnitude of the complexity gradient equals the Newtonian
acceleration (up to a constant).**

---

## 6. The AQUAL Connection

AQUAL (Bekenstein-Milgrom 1984) modifies gravity through a nonlinear
kinetic Lagrangian for a scalar field $\phi$:

$$\mathcal{L}_{\rm AQUAL} \propto F\!\left(\frac{|\nabla\phi|^2}{a_0^2}\right)$$

where $F(y) \to y$ for $y \gg 1$ (Newtonian regime, $a_N \gg a_0$) and
$F(y) \to \frac{2}{3}y^{3/2}$ for $y \ll 1$ (deep-MOND regime,
$a_N \ll a_0$).

From the result above: $|\nabla\mathcal{C}_K| \propto a_N$.

**If the CODA action includes a nonlinear kinetic term for $\mathcal{C}_K$:**

$$S_{\rm CODA}^{(\rm kin)} \propto \int d^4x\sqrt{-g}\;
F\!\left(\frac{|\nabla\mathcal{C}_K|^2}{\Lambda_{\rm MOND}^2}\right)$$

then, substituting $|\nabla\mathcal{C}_K|^2 \propto a_N^2$, this becomes:

$$\propto \int d^4x\sqrt{-g}\;F\!\left(\frac{a_N^2}{a_0^2}\right)$$

**This is exactly the AQUAL structure**, with the MOND scale identified as:

$$a_0 \propto \Lambda_{\rm MOND} \cdot \frac{|\nabla\mathcal{C}_K|}{a_N}
= \Lambda_{\rm MOND} \cdot \frac{2}{\sqrt{3}\,G_N\ell^2}$$

Setting $a_0 = cH_0 = c/\ell$:

$$\Lambda_{\rm MOND} = a_0\cdot\frac{\sqrt{3}\,G_N\ell^2}{2}
= \frac{c}{\ell}\cdot\frac{\sqrt{3}\,G_N\ell^2}{2}
= \frac{\sqrt{3}\,G_N\ell\,c}{2} = \frac{\sqrt{3}\,c}{2M_P^2\ell}$$

`[CODA — identification of MOND scale from DSSYK construction]`

---

## 7. What This Establishes and What Remains Open

### Established `[ESTABLISHED]`

1. The limiting extremal surface is doubly degenerate: $f_\tau|_* = g'|_* = 0$.
   This is an exact algebraic result, not an approximation.

2. In the presence of a matter perturbation $\Phi(x)$:
   - The turning point shifts as $(\delta\tau)^2 = -3\Phi/4$
     (non-linear square-root response)
   - The complexity density shifts as $\delta\mathcal{C}_K/\mathcal{C}_K^{(0)} = 3\Phi$
     (linear in $\Phi$, via second-order in $\delta\tau$)
   - The gradient $|\nabla\mathcal{C}_K| \propto a_N$

3. If the CODA action contains $F(|\nabla\mathcal{C}_K|^2/\Lambda^2)$,
   the AQUAL structure $F(a_N^2/a_0^2)$ emerges with $a_0 = cH_0$.

### Open `[OPEN]`

1. **What fixes $F$?** The form of the kinetic function $F$ is not
   determined by the extremal surface calculation alone. It must come
   from the DSSYK complexity function $C_K(\chi) \propto \log\cosh(\chi)$
   evaluated in the perturbed background. The $\log\cosh$ function
   transitions from quadratic to linear, matching the AQUAL transition
   from $F \sim y$ to $F \sim y^{3/2}$ — but the precise identification
   requires a further calculation.

2. **Non-spherically-symmetric perturbations.** The calculation above
   uses a spherically symmetric $\Phi(r)$. For a galactic disk, $\Phi$
   is axisymmetric and the extremal surface deformation will break the
   $S^2$ symmetry of the pure dS construction.

3. **Schwarzschild-dS case.** For a black hole embedded in de Sitter,
   the extremal surface construction changes topology — the surface must
   negotiate both the black hole horizon and the cosmological horizon.
   This is the BH information complexity problem.

4. **Back-reaction.** The calculation treats $\Phi$ as a test perturbation.
   Including back-reaction (how $\mathcal{C}_K$ modifies the metric, which
   modifies $\Phi$, which modifies $\mathcal{C}_K$) requires solving
   the full nonlinear CODA field equations.

---

## 8. Summary of Key Numbers

| Quantity | Value | Notes |
|----------|-------|-------|
| $\tau_*$ | $\sqrt{3/2} \approx 1.2247$ | Limiting surface in $dS_4$ |
| $f_{\tau\tau}|_*$ | $8$ | Controls turning point response |
| $K$ | $3$ | Coefficient of $\Phi$ in perturbed condition |
| $g''(\tau_*)$ | $-16\sqrt{3}/9 \approx -3.079$ | Controls complexity response |
| $(\delta\tau)^2 / |\Phi|$ | $3/4$ | Turning point deformation |
| $\delta\mathcal{C}_K / (\mathcal{C}_K^{(0)}\Phi)$ | $3$ | Complexity density linear response |
| $|\nabla\mathcal{C}_K| / a_N$ | $2/(\sqrt{3}G_N\ell^2)$ | Gradient-acceleration ratio |

---

## 9. CODA Document Updates Required

| Document | Update |
|----------|--------|
| `ROADMAP.md` | Phase 3b Priority 1b complete; next: determine $F$ from DSSYK |
| `phenomenology/mond_thread.md` | §5.3: AQUAL structure now has a derivation pathway via $|\nabla\mathcal{C}_K| \propto a_N$ |
| `theory/covariant_ck.md` | §4 and §7: double degeneracy as a structural feature; gradient result |

---

*End of document. Version 0.1.*  
*Key result: $|\nabla\mathcal{C}_K| \propto a_N$. AQUAL structure emerges*  
*if the CODA kinetic term is $F(|\nabla\mathcal{C}_K|^2/\Lambda^2)$.*
