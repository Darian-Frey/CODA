# Covariant Krylov Complexity Density — C_K(x)

**Document:** `theory/covariant_ck.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.2  
**Status:** Open Problem — Working Definition Proposed; DSSYK Evidence Added  
**Authors:** Shane Hartley  
**Changelog v0.2:** Section 1 literature updated with DSSYK holographic papers
(2024–25); Section 4 added (DSSYK holographic picture); open problems table
updated; references updated.  
**Epistemic Flag:** The Tier 1 construction does not yet exist in the literature.
Everything beyond Section 2 is original theoretical work in progress.
Claims are marked [ESTABLISHED], [SPECULATIVE], or [OPEN PROBLEM] throughout.
DSSYK results in Section 4 are [ESTABLISHED] from primary sources for 2D dS;
their relevance to CODA's 4D construction is [CODA-HYPOTHESIS].

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

### 4.4 The Remaining Step: 4D Local Density

The DSSYK construction provides a 2D (dS2) result. To lift it to CODA's 4D
covariant density $\mathcal{C}_K(x)$, three steps are required:

**Step 1 — Higher-dimensional extremal surface.**
Heller et al. (2025) propose the holographic complexity in $dS_{d+1}$ is given
by their Eq. 23:

$$\mathcal{C}_{dS} \equiv \frac{-i\,V}{G_N\, \ell_{dS}}$$

where $V$ is the volume of the timelike extremal codimension-1 slice anchored at
$\mathcal{I}^\pm$. The late-time growth rate in all dimensions $d \geq 2$ is
$\propto S_{dS} \cdot T_{dS}$. The 4D case ($d = 3$) is included in their
numerical results (Fig. 3). [ESTABLISHED for the integrated quantity; extension
to a local density is [OPEN PROBLEM]]

**Step 2 — Covariant local density from the surface volume element.**
The volume element of the limiting extremal surface at position $x$ in the bulk
would define $\mathcal{C}_K(x)$ as the "complexity per unit proper volume." In the
dS2 case this is $\sim \tau_*^{-d}$ per unit $\tau$ — a well-defined geometric
quantity on the limiting surface. Generalizing to a local density in the 4D bulk
requires specifying how this surface is embedded in the full 4D geometry and how
to project off the surface into the bulk. [OPEN PROBLEM]

**Step 3 — State independence.**
The limiting extremal surface is state-independent (it depends only on the dS
metric, not the quantum state). This would resolve Obstacle 3.2 (state dependence):
$\mathcal{C}_K(x)$ would be a metric functional, not a state functional. In the
DSSYK language, this corresponds to the Krylov complexity at late times
($w_0 \to \infty$) saturating to the complexity of the accumulated extremal surface.
[CODA-HYPOTHESIS — the state independence at late times is established; the
pointwise bulk construction is not]

### 4.5 Summary — What DSSYK Adds to CODA's Construction Programme

| Question | Pre-DSSYK status | Post-DSSYK status |
|----------|-----------------|------------------|
| Does a holographic Krylov density exist? | Speculative | Evidence in 2D dS [ESTABLISHED] |
| What does $C_K(x)$ look like? | Unknown | $\propto \log\cosh(\cdot)$ in dS2 [ESTABLISHED] |
| Is there a $a_0 \sim cH_0$ transition? | Speculative | Three routes confirmed [ESTABLISHED] |
| Is the density state-independent? | Obstacle (§3.2) | Partially: late-time limit is state-independent [EVIDENCE] |
| 4D local density | Open | Still open; limiting extremal surface is candidate [OPEN] |
| Microscopic 4D realization | Open | Identified as Heller et al.'s "most pressing question" [OPEN] |

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

### Tier 1 — Formal Definition (target)

$\mathcal{C}_K(x)$ is defined as the renormalised continuum limit of modular
Krylov complexity on shrinking causal diamonds (Section 5.1), regularised by
$\ell_P^4$, with counterterms fixed by requiring the weak-field limit reproduces
Newtonian gravity without correction:

$$\mathcal{C}_K(x) := \lim_{\epsilon \to 0}
\frac{\mathcal{C}_K^{\text{mod}}(s_0;\,D(x,\epsilon))}
{\text{Vol}(D(x,\epsilon))\cdot \ell_P^4}\Bigg|_{\text{ren}}$$

**Status:** [OPEN PROBLEM] — the limit is not known to exist in general.

**DSSYK-informed refinement (v0.2):** In the holographic setting, the natural
replacement for the $\epsilon \to 0$ limit is the limiting extremal surface
construction of Section 4.3:

$$\mathcal{C}_K(x) \approx \mathcal{V}(\tau_*(x)) \cdot \ell_P^{-4}$$

where $\mathcal{V}(\tau_*)$ is the volume density of the limiting extremal surface
(the accumulation surface of the timelike holographic complexity slices, Section
4.3) evaluated at the bulk point $x$ corresponding to static patch position $\tau_*$.

This DSSYK-informed definition has three advantages over the direct causal diamond
limit: (i) it is state-independent (the limiting surface depends only on the dS
metric); (ii) it is well-defined as a geometric quantity without needing a
limit that may not exist; (iii) it has an explicit 2D prototype in the DSSYK
calculation. The primary limitation is that it is currently only defined in dS
backgrounds and requires the higher-dimensional DSSYK extension to be applicable
in a general curved spacetime. [CODA-HYPOTHESIS]

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

## 7. Open Problems — Ranked by Priority

| Priority | Problem | Status | Notes |
|----------|---------|--------|-------|
| 1 | Lift DSSYK 2D Krylov density to 4D covariant $\mathcal{C}_K(x)$ | OPEN | Paper 1's "most pressing question"; Step 2 of Section 4.4 |
| 2 | Prove or disprove the existence of the $\epsilon \to 0$ limit (Section 5.1) | OPEN | DSSYK suggests finite in holographic setting; unclear in AQFT |
| 3 | Establish a covariant renormalisation scheme for $\mathcal{C}_K(x)$ | OPEN | Analogous to holographic entanglement entropy renormalisation |
| 4 | Verify AQUAL structure from $\log\cosh$ complexity function in field equations | OPEN | Does $C_K \propto \log\cosh$ produce correct MOND interpolating function? |
| 5 | Derive the Weyl proxy from the modular Krylov construction in semiclassical limit | OPEN | Required for Tier 2 / Tier 1 consistency |
| 6 | Fix the preferred-foliation problem — canonical $u^\mu(x)$ from equations of motion | OPEN | DSSYK partial resolution: state-independent at late times |
| 7 | Extend Bisognano–Wichmann to curved spacetimes | PARTIAL | Active area; Casini-Huerta-Myers made progress for spherical regions |
| 8 | Compute local moments $\mu_k(x)$ from Hadamard expansion for Schwarzschild | OPEN | Section 5.2 programme |

---

## 8. References and Lineage

**Foundational DSSYK / dS holographic complexity (v0.2 additions):**
- Heller, Ori, Papalini, Schuhmann, Wang (2025) — arXiv:2510.13986 — dS holographic complexity from Krylov in DSSYK
- Aguilar-Gutierrez (2024) — arXiv:2403.13186, JHEP 10, 107 — Complexity in dS from DSSYK, explicit $b_n$
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

**Conceptual foundations:**
- Jacobson (1995) — Thermodynamics of spacetime
- Penrose (1979) — Weyl Curvature Hypothesis

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

**Session 2 (v0.2 additions):** Direct reading of Heller et al. (2025) and
Aguilar-Gutierrez (2024).

**What the DSSYK papers add to CODA:**
- First concrete example of Krylov complexity = holographic bulk volume in dS (2D)
- Explicit Lanczos formula $b_n \sim n/2$ and three routes to $a_0 \sim cH_0$
- The limiting extremal surface as a state-independent candidate for $\mathcal{C}_K(x)$
- The $\epsilon \to 0$ limit maps to $w_0 \to \infty$ in the holographic setting,
  where the result is finite (the accumulation surface)
- Priority 1 open problem sharpened to: lift 2D DSSYK Krylov density to 4D

---

*End of document. Version 0.2. All DSSYK results established and verified
against primary sources. The 4D local density construction remains the
primary open problem.*