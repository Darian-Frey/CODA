# Covariant Krylov Complexity Density — C_K(x)

**Document:** `theory/covariant_ck.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1 (Foundational)  
**Status:** Open Problem — Working Definition Proposed  
**Authors:** Shane Hartley  
**Epistemic Flag:** The construction below does not yet exist in the literature.
Everything beyond Section 2 is original theoretical work in progress.
Claims are marked [ESTABLISHED], [SPECULATIVE], or [OPEN PROBLEM] throughout.

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

**Cosmological applications**
Krylov complexity has been computed in FLRW and Wheeler–DeWitt quantum cosmology.
All treatments are global; no pointwise density appears.

**Bottom line:** What CODA requires is genuinely beyond current published work.
The analysis below is extrapolation from first principles and must be treated as such.

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

## 4. Candidate Constructions

### 4.1 Modular Krylov on Shrinking Causal Diamonds

**Construction:**
1. Choose a Hadamard state $\omega$ on $(M, g)$
2. For a small causal diamond $D(x, \epsilon)$ centred at $x$ with radius $\epsilon$,
   compute the modular Hamiltonian $K_{D(x,\epsilon)} = -\log\rho_{D(x,\epsilon)}$
3. Run the Lanczos recursion with $K_{D(x,\epsilon)}$ as generator for a smeared
   operator peaked at $x$
4. Define:

$$\mathcal{C}_K(x) \stackrel{?}{=} \lim_{\epsilon \to 0} \frac{\mathcal{C}_K^{\text{mod}}(s_0;\, D(x,\epsilon))}{\text{Vol}(D(x,\epsilon)) \cdot \ell_P^4}$$

**Strengths:** Modular theory is the unique covariant replacement for global time
evolution in algebraic QFT. It respects local causality, works on arbitrary
Lorentzian backgrounds, and has been used to extract geometric data (area operators,
quantum extremal surfaces) in holographic settings.

**Critical weakness:** The limit $\epsilon \to 0$ is not known to exist. It is
expected to either diverge or vanish depending on the UV regulator. No proof
of a finite $[L^{-4}]$ scalar survives this limit in the current literature.
[OPEN PROBLEM]

### 4.2 Local Moments of the Two-Point Function

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

### 4.3 Geometric Krylov Scalar via Operator Manifold Curvature

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

## 5. CODA's Working Definition

Given the obstacles above, CODA adopts a **two-tier approach**:

### Tier 1 — Formal Definition (target)

$\mathcal{C}_K(x)$ is defined as the renormalised continuum limit of modular
Krylov complexity on shrinking causal diamonds (Section 4.1), regularised by
$\ell_P^4$, with counterterms fixed by requiring the weak-field limit reproduces
Newtonian gravity without correction:

$$\mathcal{C}_K(x) := \lim_{\epsilon \to 0} \frac{\mathcal{C}_K^{\text{mod}}(s_0;\,D(x,\epsilon))}{\text{Vol}(D(x,\epsilon))\cdot \ell_P^4}\Bigg|_{\text{ren}}$$

**Status:** [OPEN PROBLEM] — the limit is not known to exist. This is the
construction CODA aims to formalise. Establishing existence (or proving
non-existence) is the primary theoretical task of this research programme.

### Tier 2 — Semiclassical Proxy (working tool)

For phenomenological work and simulation while Tier 1 is developed, CODA uses
the **Weyl complexity scalar**:

$$\mathcal{C}_K(x) \approx \frac{\ell_P^4}{8\pi}\, C_{\alpha\beta\gamma\delta}(x)\, C^{\alpha\beta\gamma\delta}(x)$$

where $C_{\alpha\beta\gamma\delta}$ is the Weyl curvature tensor.

**Motivation:**
- $C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}$ is a proper diffeomorphism
  scalar with units $[L^{-4}]$ — no construction needed
- It vanishes in conformally flat spacetimes (including Minkowski and FLRW),
  activating only where gravitational complexity (tidal distortion, anisotropy)
  is present — this mirrors the desired activation property
- Penrose's Weyl Curvature Hypothesis already interprets $C_{\alpha\beta\gamma\delta}$
  as encoding gravitational entropy; there is a natural conceptual link to
  informational complexity
- In the Schwarzschild geometry it is non-zero only near the source, providing
  the correct localisation behaviour
- It is computable from the metric without additional field content

**Limitations of the proxy:** The Weyl scalar encodes geometric complexity, not
directly quantum information complexity. It cannot capture scrambling dynamics or
the Lyapunov growth of Krylov complexity in chaotic systems. It is a stand-in
pending Tier 1 construction, not a derivation of $\mathcal{C}_K$ from quantum theory.

**State dependence resolution:** Following the mean-field interpretation in Section
3.2, $\mathcal{C}_K$ in the CODA action is treated as a *background field*
representing the semiclassical average complexity of the quantum state consistent
with the metric $g_{\mu\nu}$. This is analogous to the treatment of $\langle T_{\mu\nu}\rangle$
in semiclassical gravity: state-dependent, but evaluated self-consistently.

---

## 6. Open Problems — Ranked by Priority

| Priority | Problem | Status |
|----------|---------|--------|
| 1 | Prove or disprove the existence of the $\epsilon \to 0$ limit in Section 4.1 | OPEN |
| 2 | Establish a covariant renormalisation scheme for $\mathcal{C}_K(x)$ | OPEN |
| 3 | Derive the Weyl proxy from the modular Krylov construction in the semiclassical limit | OPEN |
| 4 | Fix the preferred-foliation problem — identify a canonical $u^\mu(x)$ from the equations of motion | OPEN |
| 5 | Extend Bisognano–Wichmann to curved spacetimes as the foundation for modular Krylov | PARTIAL |
| 6 | Compute local moments $\mu_k(x)$ from the Hadamard expansion explicitly for Schwarzschild | OPEN |

---

## 7. References and Lineage

- Avdoshkin, Dymarsky, Smolkin (2022/2024) — Krylov complexity in QFT
- Caputa et al. (2023–2024) — Modular Krylov complexity
- Bisognano, Wichmann (1975/1976) — Modular flow and Rindler geometry
- Susskind, Brown et al. (2016) — Complexity Equals Action
- Almheiri, Dong, Harlow (2015) — Bulk reconstruction and QEC
- Jacobson (1995) — Thermodynamics of spacetime
- Penrose (1979) — Weyl Curvature Hypothesis

---

## 8. Synthesis Notes — Multi-Model Research Session

*This document was produced using a four-model synthesis methodology. The following
records areas of agreement and disagreement across the research session.*

**Unanimous agreement:**
- No covariant $\mathcal{C}_K(x)$ with $[L^{-4}]$ exists in the literature
- K(t) is irreducibly global; localisation is not a technical fix but a structural problem
- Modular Hamiltonians are the correct local replacement for the global generator
- State dependence is a genuine obstacle requiring a reframing of the action principle
- UV divergences will require a non-trivial renormalisation scheme

**Points of productive disagreement:**
- Replies 1 and 3 were more optimistic about the operator manifold / geometric Krylov
  approach than Reply 2, which rated it less rigorous than the two-point moment approach.
  CODA retains both as parallel tracks (Sections 4.2 and 4.3)
- Reply 2 was most explicit that the $\epsilon \to 0$ limit is not known to exist —
  this is now flagged as Priority 1 open problem rather than an assumed construction

**Added by synthesis not present in any single model:**
- The Weyl curvature scalar as a semiclassical proxy (Tier 2 working definition)
- The mean-field reframing of the state dependence problem via analogy with
  semiclassical gravity
- Explicit priority ranking of open problems

---

*End of document. Version 0.1 — subject to revision as Tier 1 construction is developed.*