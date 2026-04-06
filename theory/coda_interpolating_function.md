# Phase 3b — The CODA Interpolating Function: F from DSSYK

**Document:** `theory/coda_interpolating_function.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Status:** CALCULATION RESULT  
**Date:** April 2026  
**Depends on:** `theory/dS4_krylov_density.md`, `theory/dS4_perturbed.md`  
**Epistemic flags:**
- `[ESTABLISHED]` — verified algebraically and confirmed numerically
- `[CODA]` — new identification or derivation
- `[HYPOTHESIS]` — well-motivated but not yet fully derived
- `[OPEN]` — requires further calculation

---

## 0. The Question

From `theory/dS4_perturbed.md`: the perturbed complexity density satisfies
$|\nabla\mathcal{C}_K| \propto a_N$. For the CODA MOND action to have
AQUAL structure, it must contain a nonlinear kinetic term of the form:

$$S_{\rm kin} \propto \int d^4x\sqrt{-g}\;F\!\left(\frac{|\nabla\mathcal{C}_K|^2}{\Lambda^2}\right)
= \int d^4x\sqrt{-g}\;F\!\left(\frac{a_N^2}{a_0^2}\right)$$

**This document determines $F$ from the DSSYK Krylov complexity function.**

---

## 1. The DSSYK Krylov Complexity Function

From Heller et al. (2025) Eq. 20 and Aguilar-Gutierrez (2024) Eq. 4.14,
the DSSYK Krylov complexity in the de Sitter holographic setting is:

$$\boxed{C_K(x) = \log\cosh(x)}$$

where $x = \chi\theta/2$ is the dimensionless DSSYK boundary coordinate
(with $\chi$ the spacelike boundary coordinate and $\theta \approx \pi$
the dS spectral parameter). `[ESTABLISHED from primary sources]`

Two supporting results:

**Result A** (Heller et al., classical limit, Eq. 20): the dS complexity
function in the $q \to 1$ limit is explicitly $C_K \propto \log\cosh(\chi\theta/2)$.

**Result B** (Aguilar-Gutierrez, exact for $\nu = 1/2$, Eq. 4.14):
$C_K(\tau) = \sinh^2(\tau/2)$, whose late-time form $\frac{1}{4}e^\tau$
is the exponential growth controlled by $\log\cosh$.

---

## 2. The Derivative — The Interpolating Function

Taking the derivative of the DSSYK complexity function with respect to
its argument $x$:

$$\boxed{\frac{dC_K}{dx} = \tanh(x)}$$

`[ESTABLISHED — elementary]`

**Claim:** This derivative IS the MOND interpolating function $\mu$.

**Verification of MOND limits for $\mu(x) = \tanh(x)$:**

| Regime | $x = a_N/a_0$ | $\mu(x) = \tanh(x)$ | Required |
|--------|--------------|---------------------|---------|
| Newtonian | $x \to \infty$ | $\to 1$ | $\mu \to 1$ ✓ |
| Deep MOND | $x \to 0$ | $\to x$ | $\mu \to x$ ✓ |

`[ESTABLISHED — verified symbolically]`

The function $\mu(x) = \tanh(x)$ is a valid MOND interpolating function.
It belongs to the same family as the standard choices ($\mu = x/\sqrt{1+x^2}$,
$\mu = 1 - e^{-x}$) and satisfies both asymptotic MOND conditions exactly.

---

## 3. Deriving $F$ from $\mu$

In AQUAL, the kinetic function $F(s)$ relates to the interpolating function
$\mu$ via:

$$\mu(\sqrt{s}) = F'(s) = \frac{dF}{ds}$$

(since the AQUAL equation of motion $\nabla\cdot[\mu(a_N/a_0)\nabla\Phi]
= 4\pi G\rho$ requires $\mu(\sqrt{s}) = F'(s)$ where $s = a_N^2/a_0^2$).

With $\mu(\sqrt{s}) = \tanh(\sqrt{s})$:

$$F'(s) = \tanh(\sqrt{s})$$

$$F(s) = \int_0^s \tanh(\sqrt{s'})\,ds'$$

**Substitution** $u = \sqrt{s'}$, $ds' = 2u\,du$:

$$F(s) = 2\int_0^{\sqrt{s}} u\tanh(u)\,du$$

**Integration by parts** ($\int u\tanh u\,du = u\log\cosh u - \int\log\cosh u\,du$):

$$\boxed{F(s) = 2\sqrt{s}\,\log\cosh(\sqrt{s})
- 2\int_0^{\sqrt{s}}\log\cosh(u)\,du}$$

`[ESTABLISHED — elementary integration]`

Recognising $C_K(x) = \log\cosh(x)$:

$$\boxed{F(s) = 2\sqrt{s}\cdot C_K(\!\sqrt{s})
- 2\int_0^{\sqrt{s}} C_K(u)\,du}$$

**$F$ is an explicit integral transform of the DSSYK Krylov complexity
function.** `[CODA — key identification]`

---

## 4. Verification of the AQUAL Limits

### 4.1 Deep-MOND Limit ($s \ll 1$, $a_N \ll a_0$)

Taylor expansion: $\log\cosh(x) = x^2/2 - x^4/12 + \mathcal{O}(x^6)$

$$2\sqrt{s}\cdot\frac{s}{2} - 2\int_0^{\sqrt{s}}\frac{u^2}{2}\,du
= s^{3/2} - \frac{s^{3/2}}{3} = \frac{2}{3}s^{3/2}$$

$$\boxed{F(s) \to \frac{2}{3}s^{3/2} \quad (s \ll 1)}$$

This is exactly the deep-MOND AQUAL limit. `[ESTABLISHED]` ✓

### 4.2 Newtonian Limit ($s \gg 1$, $a_N \gg a_0$)

For large $x$: $\log\cosh(x) \approx x - \log 2$

$$2\sqrt{s}(\sqrt{s} - \log 2) - 2\int_0^{\sqrt{s}}(u-\log 2)\,du$$
$$= 2s - 2\sqrt{s}\log 2 - \left(s - 2\sqrt{s}\log 2\right) = s$$

$$\boxed{F(s) \to s \quad (s \gg 1)}$$

This is exactly the Newtonian AQUAL limit. `[ESTABLISHED]` ✓

### 4.3 Numerical Verification

| $s = a_N^2/a_0^2$ | $F(s)$ | $\frac{2}{3}s^{3/2}$ | $F/(\frac{2}{3}s^{3/2})$ | Regime |
|------|------|------|------|------|
| $10^{-3}$ | $2.11\times10^{-5}$ | $2.11\times10^{-5}$ | $0.9998$ | Deep MOND |
| $10^{-2}$ | $6.65\times10^{-4}$ | $6.67\times10^{-4}$ | $0.9980$ | MOND |
| $10^{-1}$ | $2.07\times10^{-2}$ | $2.11\times10^{-2}$ | $0.9806$ | Transition |
| $10^{0}$ | $5.62\times10^{-1}$ | $6.67\times10^{-1}$ | — | Transition |

| $s = a_N^2/a_0^2$ | $F(s)$ | $s$ (Newton) | $F/s$ | Regime |
|------|------|------|------|------|
| $10$ | $9.19$ | $10$ | $0.919$ | Near-Newton |
| $10^2$ | $99.18$ | $100$ | $0.992$ | Newtonian |
| $10^3$ | $999.18$ | $1000$ | $0.999$ | Newtonian |

The transition from MOND to Newtonian behaviour occurs at $s \sim 1$,
i.e. $a_N \sim a_0$. `[ESTABLISHED — numerically verified]`

---

## 5. The CODA MOND Action

The CODA MOND action with the determined $F$:

$$\boxed{S_{\rm CODA}^{(\rm MOND)} = -\int d^4x\sqrt{-g}
\;\frac{a_0^2}{8\pi G}\;F\!\left(\frac{a_N^2}{a_0^2}\right)}$$

where:

$$F(s) = 2\sqrt{s}\,\log\cosh(\sqrt{s}) - 2\int_0^{\sqrt{s}}\log\cosh(u)\,du$$

$$\quad a_0 = cH_0 \quad (\text{established via three DSSYK routes, Phase 3a})$$

**The equation of motion** (varying the full CODA + matter action):

$$\nabla\cdot\!\left[\tanh\!\left(\frac{a_N}{a_0}\right)\nabla\Phi\right] = 4\pi G\rho_b$$

where $\rho_b$ is the baryonic matter density.

This is the AQUAL MOND equation with interpolating function $\mu = \tanh$.
`[CODA — derived from DSSYK Krylov complexity]`

---

## 6. Comparison with Existing MOND Interpolating Functions

The literature has considered several functional forms for $\mu$.
The CODA derivation yields $\mu = \tanh$, which can be compared:

| Name | $\mu(x)$ | Deep MOND $\mu \to x$? | Newton $\mu \to 1$? |
|------|----------|----------------------|---------------------|
| Simple | $x/\sqrt{1+x^2}$ | ✓ | ✓ |
| Standard | $x/(1+x)$ | ✓ | ✓ |
| **CODA (tanh)** | $\tanh(x)$ | ✓ | ✓ |
| Exponential | $1 - e^{-x}$ | ✓ | ✓ |

All four are compatible with rotation curve data (the observational
distinction between interpolating functions requires very precise data
at the MOND transition scale, $a_N \sim a_0$). The CODA derivation
selects $\tanh$ from first principles rather than by fit. `[CODA]`

**Observational discriminant:** The interpolating functions differ most
at intermediate accelerations $a_N \sim a_0$. For example, at $x = 1$:
- Simple: $\mu(1) = 1/\sqrt{2} \approx 0.707$
- CODA (tanh): $\mu(1) = \tanh(1) \approx 0.762$
- Standard: $\mu(1) = 1/2 = 0.500$

Current rotation curve data cannot cleanly discriminate between these,
but upcoming Euclid weak-lensing data may be able to. `[OPEN — observational]`

---

## 7. The Identification Step and Its Status

The derivation depends on identifying the DSSYK argument $\chi\theta/2$
with $a_N/a_0$. This identification proceeds in two steps:

**Step A — Established:** The gradient of the bulk complexity density is
proportional to the Newtonian acceleration:

$$|\nabla\mathcal{C}_K| = \frac{2}{\sqrt{3}\,G_N\ell^2}\,a_N$$

(from `theory/dS4_perturbed.md`, all four checks passed). `[ESTABLISHED]`

**Step B — Hypothesis:** The DSSYK boundary coordinate $\chi\theta/2$
maps to $a_N/a_0$ at the bulk point $x$ via:

$$\frac{\chi\theta}{2} = \frac{|\nabla\mathcal{C}_K|}{|\nabla\mathcal{C}_K|_{\rm threshold}}
= \frac{a_N}{a_0}$$

where the threshold is set by the de Sitter background:
$|\nabla\mathcal{C}_K|_{\rm threshold} = (2/\sqrt{3}G_N\ell^2)\cdot a_0$.

This step makes physical sense: the DSSYK argument $\chi\theta/2$
parametrizes the "relative complexity" at a bulk point, which in the
perturbed background scales as $a_N/a_0$. But the precise identification
requires the full covariant perturbation theory, not just the linearised
calculation of `dS4_perturbed.md`. `[HYPOTHESIS]`

**What would make Step B rigorous:** Computing how the DSSYK complexity
functional $\mathcal{C}_{dS}[g]$ changes when $g$ is the perturbed de Sitter
metric at each bulk point, and showing that the local rate of change maps
to $\tanh(a_N/a_0)$. This is the next calculation. `[OPEN]`

---

## 8. Summary of the Three-Step Derivation

The complete derivation of the CODA MOND action:

**Step 1** — Pure dS4 result (`dS4_krylov_density.md`):
$$\mathcal{C}_K^{(0)} = \frac{2}{3\sqrt{3}\,G_N\ell^2} \approx 0.385\,M_P^2H_0^2$$

**Step 2** — Perturbed dS4 result (`dS4_perturbed.md`):
$$\mathcal{C}_K(x) = \mathcal{C}_K^{(0)}[1 + 3\Phi(x)],
\qquad |\nabla\mathcal{C}_K| \propto a_N$$

**Step 3** — $F$ from DSSYK (this document):
$$\mu = \frac{d}{dx}C_K(x)\bigg|_{x=a_N/a_0} = \tanh\!\left(\frac{a_N}{a_0}\right)$$

$$F(s) = 2\sqrt{s}\,\log\cosh(\sqrt{s})
- 2\int_0^{\sqrt{s}}\log\cosh(u)\,du$$

**Resulting MOND equation:**
$$\nabla\cdot\!\left[\tanh\!\left(\frac{a_N}{a_0}\right)\nabla\Phi\right]
= 4\pi G\rho_b$$

with $a_0 = cH_0$.

---

## 9. Epistemic Status

| Claim | Status | Source |
|-------|--------|--------|
| DSSYK Krylov function is $\log\cosh(x)$ | `[ESTABLISHED]` | Heller et al. Eq. 20 |
| $d(\log\cosh)/dx = \tanh(x)$ | `[ESTABLISHED]` | Elementary |
| $\tanh(x)$ is a valid MOND $\mu$ | `[ESTABLISHED]` | Verified both limits |
| $F(s)$ has correct deep-MOND and Newton limits | `[ESTABLISHED]` | Numerically verified |
| $|\nabla\mathcal{C}_K| \propto a_N$ | `[ESTABLISHED]` | `dS4_perturbed.md` |
| DSSYK argument $\chi\theta/2 \leftrightarrow a_N/a_0$ | `[HYPOTHESIS]` | Requires full covariant treatment |
| The CODA MOND equation is $\nabla\cdot[\tanh(a_N/a_0)\nabla\Phi]=4\pi G\rho_b$ | `[CODA]` | Follows from hypothesis |

The established portion is substantially stronger than the hypothesis.
The hypothesis ($\chi\theta/2 = a_N/a_0$) is well-motivated and dimensionally
consistent but requires a further calculation to be placed on rigorous footing.

---

## 10. Open Problems

| Priority | Problem | Notes |
|----------|---------|-------|
| 1 | Derive the identification $\chi\theta/2 = a_N/a_0$ rigorously | Full covariant perturbation theory |
| 2 | Test $\mu = \tanh$ against SPARC rotation curve dataset | Observational constraint |
| 3 | Vector field $A^\mu$ — identify CODA analogue | Required for full relativistic covariance |
| 4 | CMB compatibility check for $\mu = \tanh$ CODA | Required before claiming AeST-level status |
| 5 | Non-spherically-symmetric case (galactic disk) | Breaks $S^2$ symmetry of construction |

---

*End of document. Version 0.1.*  
*Key result: $F(s) = 2\sqrt{s}\log\cosh(\sqrt{s}) - 2\int_0^{\sqrt{s}}\log\cosh(u)du$*  
*from $\mu = d(\log\cosh)/dx = \tanh$. Deep-MOND: $F \to \frac{2}{3}s^{3/2}$.*  
*Newtonian: $F \to s$. Transition at $s \sim 1$, i.e. $a_N \sim a_0 = cH_0$.*
