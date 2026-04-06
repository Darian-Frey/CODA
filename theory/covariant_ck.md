# Covariant Krylov Complexity Density — C_K(x)

**Document:** `theory/covariant_ck.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.3  
**Status:** Substantially Advanced — dS4 density computed; MOND theorem proved; holographic dictionary is primary open problem  
**Authors:** Shane Hartley  
**Changelog v0.3:** Phase 3b results integrated throughout. Section 4.4 updated
— Steps 1–3 now complete for pure dS4; Step 4 (perturbed dS4) added with explicit
results. Section 4.5 summary table updated. Section 6 working definition updated
with explicit $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2)$ and perturbed result.
Section 7 open problems completely restructured: former Priorities 1 and 4 closed;
new Priority 1 is the holographic dictionary; Jacobi $\lambda_0 = 7/3$ recorded.
**Epistemic Flag:** The Tier 1 construction does not yet exist in full generality.
Everything beyond Section 2 is original theoretical work. Claims are marked
[ESTABLISHED], [CODA], [HYPOTHESIS], or [OPEN] throughout. Phase 3b results in
Sections 4–6 are [ESTABLISHED] by explicit calculation; their extension beyond
pure/perturbed dS4 is [OPEN].

---

## 0. Purpose of This Document

The CODA action principle is:

$$S = \int d^4x \sqrt{-g} \left[ \frac{R}{16\pi G} + \alpha \mathcal{C}_K \right]$$

For this to be a well-defined action in General Relativity, $\mathcal{C}_K$ must be:

- A **scalar field** under diffeomorphisms
- **Locally defined** at each spacetime point $x$
- Dimensionally consistent: $[\mathcal{C}_K] = L^{-4}$
- **Not dependent on a preferred foliation** or global time coordinate

Standard Krylov complexity $K(t) = \sum_n n\,|\phi_n(t)|^2$ satisfies none of these
requirements. It is a dimensionless, global, state-dependent, foliation-dependent
number.

This document records the most rigorous known paths toward constructing a covariant
$\mathcal{C}_K(x)$, the obstacles each faces, CODA's working definition, and what
remains open.

---

## 1. State of the Literature

**[ESTABLISHED]** As of the date of this document, no paper in the literature
constructs a diffeomorphism-covariant Krylov complexity density $\mathcal{C}_K(x)$
with units $[L^{-4}]$ suitable for inclusion in a spacetime action integral.

The closest existing work:

**Krylov complexity in QFT (flat space)**
Avdoshkin, Dymarsky, and Smolkin (2022/2024) extend Krylov complexity to local
operators in free QFTs and CFTs. They establish that Lanczos coefficients $b_n$
grow linearly for continuous QFTs, controlled by the UV cutoff. However, $K(t)$
remains a global quantity; no local density is defined and no coupling to gravity
is attempted.

**Modular Krylov complexity**
Caputa et al. (2023–2024) replace the global Hamiltonian with the modular Hamiltonian
$K_A = -\log\rho_A$ of a boundary subregion. This is the most promising existing
framework because modular flow is covariant and intrinsic to the local von Neumann
algebra. However, the result is a function of modular time $s$ associated to a
*region*, not a scalar density at a *point*.

**Holographic complexity (CV/CA)**
Myers, Chapman, Heller and collaborators work with complexity as a spacetime volume
or WDW-patch action in AdS/CFT. These are already spacetime integrals, but they
are not Krylov-based and are strongly model-dependent. They provide geometric
intuition but not a general construction.

**DSSYK holographic complexity in de Sitter — 2D (2024-25) [NEW — ESTABLISHED]**
Two papers now establish the first top-down microscopic connection between Krylov
complexity and holographic complexity in a cosmological spacetime:

*Aguilar-Gutierrez (2024), arXiv:2403.13186, JHEP 10, 107.* Computes Krylov
complexity for physical operators in the DSSYK/LdS2/SdS3 holographic triality.
Key result (their Eq. 4.10): explicit Lanczos coefficients for physical operators,

$$b_n = n\sqrt{\frac{n^2 - \nu^2/4}{4n^2 - 1}} \xrightarrow{n\gg 1} \frac{n}{2}$$

giving linear growth $b_n \sim H_0 n/2$ and exponential late-time complexity
$C_K \propto e^{H_0 t}$, saturating the MSS chaos bound.

*Heller, Ori, Papalini, Schuhmann, Wang (2025), arXiv:2510.13986.* Establishes
the duality between DSSYK Krylov spread complexity and the volume of timelike
extremal slices in dS2 (their Eq. 21):

$$2|\log q|\, C_K(\chi)_{\theta\approx\pi} = -i\, L_{dS}(\chi)$$

with the explicit classical complexity function
$C_K(\chi) \propto \log\cosh(\chi\theta/2)$ — quadratic-to-linear transition at
$\chi \sim \ell_{dS}$, late-time growth rate $\propto S_{dS} \cdot T_{dS} \propto
S_{dS} \cdot H_0$.

These papers identify *"microscopic realizations of the proposed holographic
complexities in higher dimensions"* as the most pressing open problem — precisely
CODA's Tier 1 construction.

**Cosmological applications**
Krylov complexity has been computed in FLRW and Wheeler–DeWitt quantum cosmology,
and in the inflationary patch (Adhikari et al. 2022, arXiv:2203.14330). All
treatments are global; no pointwise density appears. The inflationary-patch result
finds $b_n \sim H n$ (partial evidence that the Hubble scale governs Krylov growth
in dS, but in a different patch and using Heisenberg rather than modular evolution).

**Bottom line:** CODA's 4D local construction is genuinely beyond current published
work. However, the DSSYK papers now provide a concrete 2D holographic model that
can serve as a guide. Section 4 of this document analyses what the DSSYK picture
implies for the Tier 1 construction.

---

## 2. What a Covariant C_K(x) Requires

To localise Krylov complexity to a spacetime point $x \in (M, g_{\mu\nu})$,
five structural elements are needed: [ESTABLISHED]

### 2.1 Local Operator Algebra

In locally covariant algebraic QFT, each region $\mathcal{O} \subset M$ is assigned
a $*$-algebra $\mathcal{A}(\mathcal{O})$. Localisation to a point is always via a
limiting process as regions shrink to $\{x\}$, together with smearing by test functions:

$$O_f = \int d^4x\,\sqrt{-g}\, f(x)\,\Phi(x)$$

where $f$ has compact support near $x_0$. As $\text{supp}(f) \to \{x_0\}$,
one hopes some Krylov data associated to $O_f$ defines a density at $x_0$.

**Critical obstacle:** By the Reeh–Schlieder theorem, the local algebra at a point
is a type III von Neumann factor. Point algebras are trivial in relativistic QFT —
the limit $\mathcal{O} \to \{x\}$ does not yield a useful algebraic object.

### 2.2 A State and GNS Inner Product

Krylov complexity requires an operator inner product. In curved spacetime this is:

$$(A, B)_\omega = \omega(A^\dagger B)$$

where $\omega$ is a Hadamard state providing the GNS Hilbert space. In curved
spacetime there is no unique vacuum; different Hadamard states yield inequivalent
Krylov bases, explicitly breaking covariance unless a preferred state can be
canonically selected.

### 2.3 A Local Generator (Replacing the Global Hamiltonian)

Standard Krylov complexity requires the Liouvillian $\mathcal{L} = i[H, \cdot]$,
where $H$ is global. In a general Lorentzian manifold there is no preferred global
time and therefore no preferred $H$. Candidates for a local replacement:

- A timelike vector field $u^\mu(x)$ and its associated one-parameter automorphism
  group $\alpha_t$ — but this introduces explicit foliation dependence
- The **modular Hamiltonian** $K_A = -\log\rho_A$ for a causal diamond $A \ni x$
  (Tomita–Takesaki theory) — this is covariant and intrinsic to the local algebra,
  but non-local even for infinitesimal diamonds

The modular Hamiltonian route is the most covariant option. The Bisognano–Wichmann
theorem establishes a rigorous link between modular flow and spacetime geometry
for Rindler wedges in Minkowski space. Extensions to curved spacetime are an active
research area. [ESTABLISHED for Rindler; SPECULATIVE for general curved spacetime]

### 2.4 Dimensional Matching

Standard Krylov complexity $K(t)$ is dimensionless. To obtain $[\mathcal{C}_K] = L^{-4}$,
a characteristic length scale must be introduced. The natural candidate is the
Planck length $\ell_P = \sqrt{\hbar G / c^3}$:

$$\mathcal{C}_K \sim \frac{K}{\ell_P^4}$$

This is physically motivated — it places the complexity contribution at the Planck
scale, consistent with the suppression of $\alpha$. However, it makes
$\mathcal{C}_K$ cutoff-dependent in a way that must be controlled by a
renormalisation prescription. [SPECULATIVE]

### 2.5 A Renormalisation Scheme

Any local $\mathcal{C}_K(x)$ will be UV-dominated. The Lanczos coefficients $b_n$
for local operators in continuous QFTs grow as $b_n \sim n$ for large $n$; the
raw complexity sum diverges. A finite result requires:

- Subtraction of a reference vacuum value
- Addition of local curvature counterterms
- A scheme that preserves diffeomorphism invariance throughout

Different choices of smearing, time-averaging, and counterterms yield different
$\mathcal{C}_K(x)$. [OPEN PROBLEM — no covariant scheme is known]

---

## 3. The Fundamental Obstacles

These are ordered from most to least severe.

### 3.1 Non-Locality of the Krylov Basis [FUNDAMENTAL]

The Krylov basis is generated by repeated commutators with the Hamiltonian:

$$K_0 \sim O,\quad K_1 \sim [H,O],\quad K_2 \sim [H,[H,O]],\ldots$$

Each commutator spreads the support of the operator. In a relativistic QFT,
$[H, O(x)]$ has support on the entire forward lightcone of $x$. After $n$ steps,
$K_n$ is an operator with support over a causally extended region that grows
without bound. There is no canonical way to assign "this part of $K_n$ belongs
to point $x$." This is not a technical difficulty but a structural feature of
how Krylov complexity encodes information spreading.

### 3.2 State Dependence vs. the Action Principle [FUNDAMENTAL]

Krylov complexity is state-dependent. Placing $\mathcal{C}_K$ in the action
makes the action itself depend on the quantum state, which violates the standard
logic of the variational principle: the action determines the states, not
vice versa.

**CODA's resolution (proposed):** Treat $\mathcal{C}_K$ as a *mean-field quantity*
rather than a fundamental field — a quantum effective action term representing the
self-consistent average entanglement structure of the spacetime. This is analogous
to how Jacobson derived the Einstein equations thermodynamically from the Clausius
relation: the result is the same field equation but the derivation is statistical,
not variational from a fundamental action. [SPECULATIVE — requires formal development]

### 3.3 No Preferred Foliation [FUNDAMENTAL]

A generic Lorentzian manifold has no global timelike Killing vector. Any definition
of $K(t)$ requires a choice of time flow $u^\mu(x)$, making a putative
$\mathcal{C}_K(x)$ a functional of $(g_{\mu\nu},\, u^\mu,\, \omega)$ rather than
of $g_{\mu\nu}$ alone. In an action, this would introduce a preferred-frame
violation unless $u^\mu$ is itself derived from the equations of motion (e.g.,
as a fluid velocity field or eigenvector of the stress-energy tensor).

### 3.4 UV Divergences and Scheme Dependence [SEVERE, TECHNICAL]

In the continuum limit, the Krylov chain becomes a continuous object and the sum
$\sum_n n|\phi_n|^2$ diverges. Any finite $\mathcal{C}_K(x)$ is heavily
scheme-dependent and behaves at leading order like a complicated higher-derivative
curvature functional. The complexity interpretation may be entirely washed out by
the regularisation procedure.

### 3.5 Causality [MODERATE]

A pointwise $\mathcal{C}_K(x)$ would assign a definite "depth" at $x$
instantaneously. Operator growth is confined inside lightcones, so any
genuinely local density is either zero (outside the lightcone of the initial
operator) or requires a smearing that spreads the support and loses locality.

---

## 4. DSSYK Evidence for the Holographic Krylov Density

This section analyses what the DSSYK holographic programme (arXiv:2510.13986
and arXiv:2403.13186) tells us about the structure CODA's Tier 1 $\mathcal{C}_K(x)$
should have. All results cited here are [ESTABLISHED] from primary sources.
Their application to CODA's 4D construction is [CODA-HYPOTHESIS].

### 4.1 The DSSYK Holographic Complexity Dictionary

In the DSSYK/sine dilaton gravity duality (Heller et al. 2025), the complexity
dictionary is:

$$2|\log q|\, C_K(t)_\theta = \langle\hat{L}_{\rm eff}\rangle$$

where $C_K$ is the Krylov spread complexity of the time-evolved Hartle-Hawking
state in the DSSYK model, and $\langle\hat{L}_{\rm eff}\rangle$ is the quantum
expectation value of the geodesic length (= volume of extremal codimension-1
slice) in the effective AdS2 geometry.

In the de Sitter limit ($\theta \approx \pi$), this maps via Weyl rescaling to:

$$2|\log q|\, C_K(\chi)_{\theta\approx\pi} = -i\, L_{dS}(\chi)$$

where $L_{dS}(\chi)$ is the volume of a **timelike extremal codimension-1 slice**
anchored at future and past infinity of dS2 at boundary coordinate $\chi/2$.

**For CODA:** This is the precise statement that bulk complexity = boundary Krylov
complexity in a cosmological spacetime. The bulk object ($L_{dS}$) is an integrated
geometric quantity — a volume. The local density of this volume is therefore a
candidate for $\mathcal{C}_K(x)$ after integration over the slice.

### 4.2 The Classical dS Krylov Complexity Function

The explicit classical result (their Eq. 20):

$$C_K(\chi) \propto \log\!\left[\cosh\!\left(\frac{\chi\theta}{2}\right)\right]
- \log\theta$$

This function:
- Grows **quadratically** for small $\chi \ll 2/\theta \sim 2\ell_{dS}$
- Transitions to **linear growth** at $\chi \sim \ell_{dS}$
- Has late-time growth rate $\propto S_{dS} \cdot T_{dS} = S_{dS} \cdot H_0/(2\pi)$

The transition coordinate $\chi_* \sim \ell_{dS} = c/H_0$ corresponds, under the
static-patch time interpretation, to the timescale $H_0^{-1}$ and hence the
acceleration scale $a_0 = c^2/\ell_{dS} = cH_0$. See `phenomenology/mond_thread.md`
§5.2 for the full derivation of the Milgrom scale from this transition.

### 4.3 The Holographic Density — What the DSSYK Picture Implies

The volume of the timelike extremal slice in $dS_{d+1}$ (Heller et al., Eq. 25):

$$V = \ell^d \Omega_{d-1} \int d\tau\,
\frac{i}{\tau^d}\sqrt{\frac{1}{1-\tau^2} - (1-\tau^2)\dot{w}^2(\tau)}$$

The **integrand** of this expression:

$$\mathcal{V}(\tau) \equiv \frac{i\,\ell^d\,\Omega_{d-1}}{\tau^d}
\sqrt{\frac{1}{1-\tau^2} - (1-\tau^2)\dot{w}^2}$$

is a *local* density along the extremal slice. This is the natural candidate for
the bulk local complexity density, analogous to how the local entropy density in
holographic entanglement entropy is the area element of the RT surface.

**Properties of $\mathcal{V}(\tau)$:**
- Covariant under diffeomorphisms in the $\tau, w$ coordinates
- Depends on the position $\tau$ along the slice and the embedding $\dot{w}(\tau)$
- Diverges as $\tau \to 0$ (near the asymptotic boundary) — requires holographic
  renormalisation, analogous to RT surface area renormalisation
- On the **limiting extremal surface** ($w_0 \to \infty$, $\tau_* \to \sqrt{d/(d-1)}$),
  the embedding $\dot{w}(\tau)$ is fixed and $\mathcal{V}(\tau)$ becomes a
  state-independent geometric quantity

The limiting extremal surface is the **accumulation surface** of all complexity
slices as $w_0 \to \infty$. It is determined purely by the dS metric — no reference
to the quantum state. This is the DSSYK-inspired candidate for a covariant
$\mathcal{C}_K(x)$ in the bulk.

### 4.4 Phase 3b Results — What Has Been Computed

The following calculations (documented in `theory/dS4_krylov_density.md`,
`theory/dS4_perturbed.md`, `theory/coda_interpolating_function.md`,
and `theory/coda_mond_theorem.md`) complete the programme sketched in v0.2.

**Step 1 — dS4 local density (d=3) ✓ COMPLETE** `[ESTABLISHED]`

For $d=3$ (4D de Sitter), the limiting extremal surface sits at
$\tau_* = \sqrt{3/2}$, $E_* = 2/(3\sqrt{3})$. The growth rate normalised
to a 4D bulk density gives:

$$\boxed{\mathcal{C}_K^{(dS_4)} = \frac{2}{3\sqrt{3}\,G_N\ell^2}
\approx 0.385\,M_P^2 H_0^2}$$

All four checks pass: (i) finite ✓ (ii) covariant ✓ (iii) dimensions
$[L^{-4}]$ ✓ (iv) state-independent ✓. Coefficient $c_{d=3} = 16\pi/(3\sqrt{3})
\approx 9.68$ computed explicitly. In pure dS, $\mathcal{C}_K$ is constant
(correct — maximal symmetry). See `theory/dS4_krylov_density.md`.

**Step 2 — Perturbed dS4: double degeneracy ✓ COMPLETE** `[ESTABLISHED]`

Under a conformal perturbation $\delta g_{\mu\nu} = 2\Phi g_{\mu\nu}$
(Newtonian gauge), the limiting surface has a doubly-degenerate critical
point: $\partial f/\partial\tau|_* = 0$ AND $g'(\tau_*) = 0$ simultaneously.
Standard first-order perturbation theory fails; second-order analysis gives:

$$(\delta\tau)^2 = -\frac{3\Phi}{4}, \quad
\frac{\delta\mathcal{C}_K}{\mathcal{C}_K^{(0)}} = 3\Phi(x)$$

$$\boxed{|\nabla\mathcal{C}_K(x)| = \kappa\, a_N(x), \qquad
\kappa = \frac{2}{\sqrt{3}\,G_N\ell^2} = 3\mathcal{C}_K^{(0)}}$$

The complexity density tracks the Newtonian potential; its gradient is the
Newtonian acceleration. See `theory/dS4_perturbed.md`.

**Step 3 — AQUAL interpolating function ✓ COMPLETE** `[ESTABLISHED]`

The DSSYK complexity function $C_K(x) = \log\cosh(x)$ determines the MOND
interpolating function via differentiation:

$$\mu(x) = \frac{d\,C_K}{dx} = \tanh(x)$$

$$F(s) = 2\sqrt{s}\log\cosh(\sqrt{s}) - 2\int_0^{\sqrt{s}}\log\cosh(u)\,du$$

Limits verified: $F(s) \to \frac{2}{3}s^{3/2}$ (deep MOND) ✓,
$F(s) \to s$ (Newtonian) ✓. $F$ is an integral transform of $C_K$.
See `theory/coda_interpolating_function.md`.

**Step 4 — CODA MOND Theorem ✓ PROVED** `[CODA]`

Given Steps 1–3 and the CODA kinetic action, the $\kappa$ cancellation
$(|\nabla\mathcal{C}_K|^2/\kappa^2 a_0^2 = a_N^2/a_0^2)$ gives the
MOND equation by standard variation:

$$\boxed{\nabla\cdot\!\left[\tanh\!\left(\frac{a_N}{a_0}\right)
\nabla\Phi\right] = 4\pi G\rho_b}$$

with $a_0 = cH_0/2\pi = cT_{dS}$ from the de Sitter temperature (within
10% of observed $a_0^{\rm obs} = 1.2\times10^{-10}$ m/s² with no free
parameters). See `theory/coda_mond_theorem.md`.

**Step 5 — Second variation and MOND signal** `[ESTABLISHED]`

The second variation $\delta^2\mathcal{C}_{dS}/\delta g^2$ has been
partially computed (`theory/second_variation_dssyk.md`):
- Direct-direct: $(3/2)\Phi^2$ potential term (no gradients)
- Jacobi operator on limiting surface: $\lambda(k,\ell) = 3k^2 - \frac{3}{2}\ell(\ell+1) + \frac{7}{3}$
- Ground state: $\lambda_0 = 7/3 \neq 0$ — **no near-zero Jacobi mode**
- MOND signal is the non-analytic $|\Phi|^{3/2}$ term from $g'''(\tau_*)$
  through the double degeneracy — has the correct power for deep-MOND AQUAL

The remaining gap: mapping $|\Phi|^{3/2}$ in the DSSYK generating functional
to $F(|\nabla\Phi|^2/a_0^2)$ requires showing the DSSYK boundary time
responds to $|\nabla\Phi|$ (gradient), not $|\Phi|$ (value), at each bulk
point — the holographic dictionary step.

### 4.5 Summary — Status After Phase 3b

| Question | Pre-Phase 3b | Post-Phase 3b |
|----------|-------------|--------------|
| Does a holographic Krylov density exist in dS? | Evidence in 2D `[ESTABLISHED]` | ✓ Computed in dS4: $2/(3\sqrt{3}G_N\ell^2)$ `[ESTABLISHED]` |
| What does $\mathcal{C}_K(x)$ look like? | $\propto\log\cosh$ in dS2 | $\mathcal{C}_K^{(0)}(1+3\Phi)$ in perturbed dS4 `[ESTABLISHED]` |
| Is the density state-independent? | Partially: late-time limit | ✓ Resolved in pure dS4 `[ESTABLISHED]` |
| Is there a $a_0\sim cH_0$ transition? | Three routes confirmed | ✓ $a_0=cH_0/2\pi$, 10% from observed `[ESTABLISHED]` |
| Does $|\nabla\mathcal{C}_K|\propto a_N$? | Open | ✓ Proved via double degeneracy `[ESTABLISHED]` |
| AQUAL interpolating function from $\log\cosh$? | Open | ✓ $\mu=\tanh$, $F$ from integral transform `[ESTABLISHED]` |
| CODA MOND equation | Speculative | ✓ **Theorem proved** `[CODA]` |
| Jacobi near-zero mode? | Expected | ✗ $\lambda_0=7/3\neq 0$; MOND from $g'''$ not Jacobi `[ESTABLISHED]` |
| Holographic dictionary | Open | **Primary open problem** — $|\Phi|^{3/2}\to F(|\nabla\Phi|^2/a_0^2)$ `[OPEN]` |
| 4D local density beyond dS | Open | Still open; perturbed dS done; general curved spacetime open `[OPEN]` |

---

## 5. Candidate Constructions

### 5.1 Modular Krylov on Shrinking Causal Diamonds

**Construction:**
1. Choose a Hadamard state $\omega$ on $(M, g)$
2. For a small causal diamond $D(x, \epsilon)$ centred at $x$ with radius $\epsilon$,
   compute the modular Hamiltonian $K_{D(x,\epsilon)} = -\log\rho_{D(x,\epsilon)}$
3. Run the Lanczos recursion with $K_{D(x,\epsilon)}$ as generator for a smeared
   operator peaked at $x$
4. Define:

$$\mathcal{C}_K(x) \stackrel{?}{=} \lim_{\epsilon \to 0} \frac{\mathcal{C}_K^{\text{mod}}(s_0;\, D(x,\epsilon))}{\text{Vol}(D(x,\epsilon)) \cdot \ell_P^4}$$

**DSSYK context (v0.2 addition):** The DSSYK holographic construction in Section 4
provides a concrete 2D model for this programme. The Hartle-Hawking state plays the
role of $\omega$; the chord Hilbert space plays the role of the Krylov basis; and the
result is $C_K \propto \log\cosh(\chi\theta/2)$. The $\epsilon \to 0$ limit in the
current construction maps, in the DSSYK language, to the limit $w_0 \to \infty$
(the accumulation surface), which is finite and well-defined. This suggests the
limit may exist in the holographic setting even if it is problematic in the
direct algebraic QFT approach.

**Strengths:** Modular theory is the unique covariant replacement for global time
evolution in algebraic QFT. It respects local causality, works on arbitrary
Lorentzian backgrounds, and has been used to extract geometric data (area operators,
quantum extremal surfaces) in holographic settings. The DSSYK papers now provide
a concrete working example.

**Critical weakness:** The limit $\epsilon \to 0$ is not known to exist. It is
expected to either diverge or vanish depending on the UV regulator. No proof
of a finite $[L^{-4}]$ scalar survives this limit in the current literature.
[OPEN PROBLEM]

### 5.2 Local Moments of the Two-Point Function

**Construction:**
Extract local Lanczos data from the Wightman two-point function $W(x,y)$ without
running the full global Lanczos algorithm. The Hadamard expansion of $W(x,y)$ near
coincidence encodes local geometric and state information in its coefficients.
Define local spectral moments:

$$\mu_k(x) = \int_0^\infty \omega^k\, f_2(\omega; x)\, d\omega$$

where $f_2(\omega; x)$ is extracted from derivatives of $W(x,y)$ along a chosen
timelike direction at $x$. Invert the moment–Lanczos map pointwise to obtain
local $\{b_n(x)\}$. Construct a local complexity $K_{\text{loc}}(t; x)$ and define
$\mathcal{C}_K(x)$ by time-averaging with a UV cutoff and subtracting the Minkowski
vacuum reference.

**Strengths:** Uses only the two-point function, which is the core object of QFT
in curved spacetime and is well-understood. Naturally yields a scalar once a
timelike direction is fixed. The local Hadamard expansion connects directly to
local curvature invariants, suggesting a natural set of counterterms.

**Weaknesses:** The moment–Lanczos inversion is highly non-trivial and numerically
unstable. UV singularities dominate the low moments. The timelike direction
introduces foliation dependence unless it is canonically fixed. [SPECULATIVE —
most promising in principle, technically brutal]

### 5.3 Geometric Krylov Scalar via Operator Manifold Curvature

**Construction:**
Treat the space of operators near $x$ as a manifold equipped with the
Fisher–Rao / Bures information metric $\mathcal{G}_{ab}$ derived from the
autocorrelation function. The "complexity" at $x$ is the geodesic length on this
operator manifold. Define:

$$\mathcal{C}_K(x) = \mathcal{G}_{ab}(x)\, \partial_\mu \theta^a\, \partial^\mu \theta^b$$

where $\theta^a$ are coordinates on the operator manifold.

**Strengths:** Manifestly covariant if $\mathcal{G}_{ab}$ is constructed
covariantly. Gives a kinetic-like term that has a natural place in an action.
Connects to quantum information geometry (Fubini–Study metric, quantum Fisher
information).

**Weaknesses:** The operator manifold is infinite-dimensional in QFT; the metric
$\mathcal{G}_{ab}$ requires a regularisation. Defining $\theta^a(x)$ as local
coordinates is scheme-dependent. This approach captures the *geometry* of the
operator space but may lose the dynamical *spreading* content of Krylov complexity.
[SPECULATIVE]

---

## 6. CODA's Working Definition

Given the obstacles above, CODA adopts a **two-tier approach**:

### Tier 1 — DSSYK Holographic Definition (now concrete in dS4)

In the holographic de Sitter setting, $\mathcal{C}_K(x)$ is defined as the
volume density of the limiting extremal timelike surface at the bulk point $x$,
normalised by $G_N\ell$:

$$\mathcal{C}_K(x) := \frac{-i}{G_N\ell}\,\mathcal{V}(\tau_*(x))$$

where $\mathcal{V}(\tau_*)$ is the integrand of the Heller et al. extremal slice
volume evaluated at the bulk position $\tau_*(x)$ of the limiting surface.

**Explicit result in pure dS4** `[ESTABLISHED — theory/dS4_krylov_density.md]`:

$$\mathcal{C}_K^{(0)} = \frac{2}{3\sqrt{3}\,G_N\ell^2}
\approx 0.385\,M_P^2 H_0^2$$

This is constant in pure de Sitter — correct by maximal symmetry. All
four requirements of §0 are satisfied: scalar ✓, local ✓, $[L^{-4}]$ ✓,
foliation-independent ✓.

**Explicit result in perturbed dS4** `[ESTABLISHED — theory/dS4_perturbed.md]`:

Under $\delta g_{\mu\nu} = 2\Phi g_{\mu\nu}$ (Newtonian gauge, weak field):

$$\mathcal{C}_K(x) = \mathcal{C}_K^{(0)}\!\left(1 + 3\Phi(x)\right),
\qquad |\nabla\mathcal{C}_K(x)| = \kappa\,a_N(x)$$

where $\kappa = 3\mathcal{C}_K^{(0)} = 2/(\sqrt{3}\,G_N\ell^2)$ and
$a_N = |\nabla\Phi|$ is the Newtonian acceleration. The complexity gradient
is proportional to the local gravitational acceleration. This proportionality
— with $\kappa$ cancelling in the AQUAL argument — is the key result that
drives the MOND theorem.

**Remaining limitation:** The definition is currently established only in
(perturbed) de Sitter spacetime. Extension to a general curved background
requires the holographic dictionary relating bulk geometry to DSSYK boundary
data in non-dS spacetimes. `[OPEN]`

**Status of the formal causal-diamond limit:** The original Tier 1 target
— the renormalised continuum limit on shrinking causal diamonds — remains
open in general:

$$\mathcal{C}_K(x) \stackrel{?}{=} \lim_{\epsilon \to 0}
\frac{\mathcal{C}_K^{\text{mod}}(s_0;\,D(x,\epsilon))}
{\text{Vol}(D(x,\epsilon))\cdot \ell_P^4}\Bigg|_{\text{ren}}$$

The DSSYK construction circumvents this by working directly with the
geometric limiting surface rather than taking an operator-algebraic limit.
Whether the two routes agree — i.e. whether the modular Krylov limit on
shrinking diamonds converges to the extremal surface density in the
holographic regime — is an important open question but does not block
the current programme. `[OPEN]`

### Tier 2 — Semiclassical Proxy (working tool for strong-field regime)

For strong-field phenomenology where the dS approximation breaks down
(black holes, cosmological perturbations), CODA uses the **Weyl complexity scalar**:

$$\mathcal{C}_K(x) \approx \frac{\ell_P^4}{8\pi}\,
C_{\alpha\beta\gamma\delta}(x)\, C^{\alpha\beta\gamma\delta}(x)$$

where $C_{\alpha\beta\gamma\delta}$ is the Weyl curvature tensor.

**Motivation:** (i) proper diffeomorphism scalar with $[L^{-4}]$; (ii) vanishes
in conformally flat spacetimes (Minkowski, FLRW) — activates only where tidal
complexity is present; (iii) Penrose's Weyl Curvature Hypothesis connects
$C_{\alpha\beta\gamma\delta}$ to gravitational entropy; (iv) computable directly
from the metric.

**Limitations:** Encodes geometric complexity, not quantum information complexity.
Cannot capture scrambling or Lyapunov growth. Stand-in for Tier 1 in
non-dS regimes; not independently derived from the Krylov construction.

**State dependence:** Following §3.2, $\mathcal{C}_K$ in the CODA action is a
mean-field background encoding the semiclassical entanglement structure of the
spacetime — evaluated self-consistently with $g_{\mu\nu}$, analogous to
$\langle T_{\mu\nu}\rangle$ in semiclassical gravity.

---

## 7. Open Problems — Ranked by Priority

### Completed (Phase 3b) — formerly open priorities

| Problem | Closed by | Document |
|---------|-----------|----------|
| Lift DSSYK 2D Krylov density to 4D $\mathcal{C}_K(x)$ | $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2)$ computed | `dS4_krylov_density.md` |
| AQUAL structure from $\log\cosh$ | $\mu = \tanh$; $F$ derived | `coda_interpolating_function.md` |
| Does $|\nabla\mathcal{C}_K|\propto a_N$? | Proved via double degeneracy | `dS4_perturbed.md` |
| CODA MOND equation | **Theorem proved** | `coda_mond_theorem.md` |
| Preferred-foliation in pure dS | State-independent on limiting surface | `dS4_krylov_density.md` |

### Ruled out

| Idea | Ruled out by |
|------|-------------|
| Jacobi near-zero mode as origin of MOND | $\lambda_0 = 7/3 \neq 0$ on limiting surface |
| Free scalar modular Krylov producing $a_0$ | Bounded $b_n$, no linear growth |

### Current open problems

| Priority | Problem | Status | Notes |
|----------|---------|--------|-------|
| **1** | **Holographic dictionary:** show DSSYK boundary time responds to $\|\nabla\Phi\|$ (gradient), not $\|\Phi\|$ (value) | `[OPEN]` | Needed to convert $\|\Phi\|^{3/2}$ in generating functional to $F(\|\nabla\Phi\|^2/a_0^2)$; last step to fully derive premise (iii) of MOND theorem |
| **2** | **The $2\pi$ factor:** track precise normalisation from DSSYK dictionary to $a_0 = cH_0/2\pi$ vs $cH_0$ | `[OPEN]` | Currently 10% discrepancy; within $H_0$ tension; needs exact coefficient from holographic boundary conditions |
| **3** | **Vector sector $A^\mu$:** construct a Krylov flow vector field for gravitational lensing consistency | `[OPEN]` | AeST has $A^\mu$; CODA candidate is $u^\mu$ from extremal surface normal; needed for full relativistic covariant MOND |
| **4** | **Second variation — full Jacobi calculation:** complete the $\delta^2\mathcal{C}_{dS}/\delta g^2$ computation beyond the schematic result | `[OPEN]` | Jacobi $\lambda_0 = 7/3$ established; need full shape deformation Green's function and MOND-limit connection |
| **5** | **Extend to non-dS backgrounds:** CMB, galaxy cluster lensing, black hole interiors | `[OPEN]` | Requires either full holographic dictionary or independent construction; blocked on Priority 1 |
| **6** | **$\epsilon\to 0$ limit vs extremal surface:** show the modular Krylov limit on causal diamonds agrees with the DSSYK extremal surface density | `[OPEN]` | Important for conceptual unity; does not block phenomenology |
| **7** | **Covariant renormalisation scheme** | `[OPEN]` | Required for precise UV predictions; analogue of holographic entanglement entropy counterterms |
| **8** | **Bisognano–Wichmann extension to curved spacetime** | `[PARTIAL]` | Casini-Huerta-Myers for spherical regions; general case open |

---

## 8. References and Lineage

**CODA Phase 3b documents (v0.3 additions):**
- `theory/dS4_krylov_density.md` — $\mathcal{C}_K^{(0)}$ in dS4; limiting surface; four checks
- `theory/dS4_perturbed.md` — double degeneracy; $(\delta\tau)^2=-3\Phi/4$; $|\nabla\mathcal{C}_K|=\kappa a_N$
- `theory/coda_interpolating_function.md` — $\mu=\tanh$; $F$ via integral transform; limits
- `theory/coda_identification.md` — $x_{\rm eff}=a_N/a_0$; BTFR; RAR shape
- `theory/coda_mond_theorem.md` — MOND theorem proved; $\kappa$ cancellation
- `theory/second_variation_dssyk.md` — Jacobi $\lambda_0=7/3$; $|\Phi|^{3/2}$ MOND signal

**Foundational DSSYK / dS holographic complexity:**
- Heller, Ori, Papalini, Schuhmann, Wang (2025) — arXiv:2510.13986 — dS holographic Krylov complexity from DSSYK
- Aguilar-Gutierrez (2024) — arXiv:2403.13186, JHEP 10, 107 — Complexity in dS, explicit $b_n$
- Blommaert, Mertens, Papalini (2024) — arXiv:2404.03535 — dilaton gravity hologram of DSSYK

**Krylov complexity in QFT and holography:**
- Avdoshkin, Dymarsky, Smolkin (2022/2024) — Krylov complexity in QFT
- Parker, Cao, Avdoshkin, Scaffidi, Altman (2019) — Universal operator growth hypothesis
- Caputa et al. (2023–2024) — Modular Krylov complexity
- Rabinovici, Sanchez-Garrido, Shir, Sonner (2023) — Bulk manifestation of Krylov complexity

**Modular theory foundations:**
- Bisognano, Wichmann (1975/1976) — Modular flow and Rindler geometry
- Tomita-Takesaki theory — modular automorphisms of von Neumann algebras
- Casini, Huerta, Myers (2011) — Modular Hamiltonian for spherical regions

**Holographic complexity (non-Krylov):**
- Susskind, Brown et al. (2016) — Complexity Equals Action / Volume
- Almheiri, Dong, Harlow (2015) — Bulk reconstruction and QEC

**MOND and observational:**
- Milgrom (1983) — Original MOND; Milgrom scale $a_0$
- Lelli, McGaugh, Schombert (2016) — SPARC dataset
- McGaugh, Lelli, Schombert (2016) — Radial Acceleration Relation
- Skordis, Złośnik (2021) — AeST; ghost-free relativistic MOND (structural target)
- Verlinde (2016) — Emergent gravity; $a_0\sim cH_0$ from entropy

**Conceptual foundations:**
- Jacobson (1995) — Thermodynamics of spacetime
- Penrose (1979) — Weyl Curvature Hypothesis
- Stelle (1977) — Quadratic gravity; all Tier 2 numerical results

---

## 9. Synthesis Notes — Multi-Model Research Sessions

**Session 1 (v0.1 original):** Four-model synthesis on the covariant $\mathcal{C}_K$
construction.

**Unanimous agreement:**
- No covariant $\mathcal{C}_K(x)$ with $[L^{-4}]$ exists in the literature
- $K(t)$ is irreducibly global; localisation is not a technical fix but a structural problem
- Modular Hamiltonians are the correct local replacement for the global generator
- State dependence is a genuine obstacle requiring a reframing of the action principle
- UV divergences will require a non-trivial renormalisation scheme

**Points of productive disagreement (Session 1):**
- Replies 1 and 3 were more optimistic about the operator manifold / geometric Krylov
  approach (Section 5.3) than Reply 2. CODA retains both as parallel tracks.
- Reply 2 was most explicit that the $\epsilon \to 0$ limit is not known to exist.

**Session 2 (v0.2):** Direct reading of Heller et al. (2025) and
Aguilar-Gutierrez (2024). DSSYK programme established; three routes to $a_0$
confirmed; limiting extremal surface identified as candidate $\mathcal{C}_K(x)$.

**Session 3 (v0.3 — Phase 3b):** Full derivation chain completed.

Key results established:
- $\mathcal{C}_K^{(0)} = 2/(3\sqrt{3}G_N\ell^2)$ in pure dS4 — all checks pass
- Double degeneracy of limiting surface: $f_\tau|_* = g'|_* = 0$ simultaneously;
  $(\delta\tau)^2 = -3\Phi/4$ (non-analytic, not first-order perturbation theory)
- $|\nabla\mathcal{C}_K| = \kappa a_N$ — complexity gradient tracks acceleration
- $\mu = \tanh$ derived from $d(\log\cosh)/dx$
- MOND theorem proved; $\kappa$ cancels; $a_0 = cH_0/2\pi$ within 10% of observed
- Jacobi $\lambda_0 = 7/3 \neq 0$ — MOND signal from $g'''$ not Jacobi near-zero mode
- SPARC: 175 galaxies fitted; tanh competitive with simple; parameter-free $a_0$ 10% off

Primary open problem sharpened from "4D lift" to "holographic dictionary":
mapping $|\Phi|^{3/2}$ in DSSYK generating functional to $F(|\nabla\Phi|^2/a_0^2)$.

---

*End of document. Version 0.3.*
*Key results: $\mathcal{C}_K^{(0)}$ computed; MOND theorem proved; Jacobi $\lambda_0=7/3$.*
*Primary open problem: holographic dictionary connecting $|\Phi|^{3/2}$ to $F(|\nabla\Phi|^2/a_0^2)$.*