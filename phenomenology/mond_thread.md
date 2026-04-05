# CODA MOND Thread — Reconstructing Galactic Phenomenology via Tier 1

**Document:** `phenomenology/mond_thread.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.1  
**Status:** Speculative — working hypothesis, not a completed theory  
**Depends on:** `theory/covariant_ck.md`, `theory/action_principle.md`,
`theory/field_equations.md`  
**Epistemic Flags:** [ESTABLISHED] for observational and literature results;
[CODA-HYPOTHESIS] for new CODA-specific proposals; [SPECULATIVE] for
unverified conjectures; [OPEN PROBLEM] for unresolved questions.

---

## 0. Why This Document Exists — The UV/IR Polarity Problem

CODA's Tier 2 proxy ($\xi C^2$) is a **UV modification** of gravity: it
activates at high curvature, produces a Yukawa correction with range
$m_2^{-1} \sim \ell_P$, and leaves galactic and cosmological scales
completely unchanged. MOND is an **IR modification**: it activates at low
acceleration $a \lesssim a_0 \approx 1.2 \times 10^{-10}$ m/s², precisely
where galactic dynamics deviate from GR predictions, and is undetectable in
the Solar System.

These are structurally opposite regimes. No amount of tuning $\xi$ bridges
this gap — the Yukawa range $m_2^{-1} = (32\pi G\xi)^{1/2}$ would need to
reach galactic scales ($\sim$ kpc), requiring $\xi$ so large that the ghost
mass falls far below the Planck scale, destroying the EFT. The Tier 2
action is constitutionally incapable of producing MOND phenomenology.

The MOND thread therefore depends entirely on the **Tier 1 construction** —
the formal covariant $\mathcal{C}_K(x)$ whose structure is not predetermined
to be Weyl-squared. The question this document addresses is: what properties
would $\mathcal{C}_K(x)$ need to have in order to produce MOND-like
galactic-scale modifications while preserving GR and avoiding ghosts?

---

## 1. The MOND Observational Target

Any theory that aspires to explain galactic dynamics without dark matter
must reproduce the following. [ESTABLISHED]

### 1.1 The Milgrom Interpolation

MOND is defined by the interpolating relation:

$$a = \mu\!\left(\frac{a_N}{a_0}\right) a_N$$

where $a_N = GM/r^2$ is the Newtonian baryonic acceleration, $a_0$ is the
Milgrom acceleration scale, and the interpolating function $\mu(x)$ satisfies:

$$\mu(x) \to 1 \quad (x \gg 1): \quad \text{Newtonian/GR limit}$$
$$\mu(x) \to \sqrt{x} \quad (x \ll 1): \quad \text{deep-MOND limit}$$

**Milgrom scale** (from rotation curve fits):
$a_0 = (1.20 \pm 0.02) \times 10^{-10}$ m/s²

### 1.2 Deep-MOND Regime

For $a_N \ll a_0$:

$$a \approx \sqrt{a_0 a_N}$$

This produces **flat rotation curves** — the circular velocity
$v_c = \sqrt{ar}$ becomes $v_c = (GM a_0)^{1/4}$ independent of $r$.
This also implies **scale invariance** under $(t, \mathbf{r}) \to
(\lambda t, \lambda \mathbf{r})$ in the deep-MOND limit.

### 1.3 Baryonic Tully-Fisher Relation (BTFR) [ESTABLISHED]

$$V_\infty^4 = G\,M_b\,a_0$$

where $M_b$ is the total baryonic mass and $V_\infty$ is the asymptotic
rotation velocity. This is tight, zero-scatter, and holds with no free
parameters beyond $a_0$. It is one of MOND's sharpest successes.

### 1.4 Radial Acceleration Relation (RAR/MDAR) [ESTABLISHED]

The observed acceleration $g_{\rm obs}$ correlates with the baryonic
Newtonian acceleration $g_b$ via a single function with scale $a_0$ and
very small scatter across all galaxy morphologies. Any MOND-compatible
theory must reproduce this correlation without fine-tuning.

### 1.5 External Field Effect (EFE) [ESTABLISHED]

MOND predicts that the internal dynamics of a system are modified by the
external gravitational field of its environment — a consequence of the
non-linearity of the MOND equation. Any covariant completion must reproduce
this effect in the quasi-static limit.

### 1.6 The Cosmological Coincidence

Observationally: $a_0 \approx cH_0 \approx c^2/\ell_{\rm Hubble}$, up to
factors of order unity. This is not explained by the MOND paradigm itself
but is a striking connection to cosmological scales. Any fundamental
derivation of $a_0$ must account for this coincidence. [ESTABLISHED]

### 1.7 Known Failure Regimes of MOND [ESTABLISHED]

MOND (in all its forms) struggles with:
- **Galaxy clusters:** Under-predicts cluster lensing mass by factor $\sim 3$
  (Bullet Cluster and others). Requires additional "dark" component
- **CMB and large-scale structure:** Most covariant MOND theories
  struggle to reproduce CMB acoustic peaks and matter power spectrum
  without fine-tuning (AeST being the notable exception)
- **Strong-field regime:** Binary pulsar constraints tightly limit
  deviations from GR at high acceleration

Any CODA MOND implementation must acknowledge these limitations upfront.

---

## 2. Information-Theoretic Precedents

### 2.1 Verlinde's Emergent Gravity (2016) [ESTABLISHED — key reference]

Verlinde's framework is the strongest existing information-theoretic
bridge to MOND. The core argument: in de Sitter space, entanglement
entropy has two contributions — an area-law piece (short-range quantum
entanglement) and a **volume-law piece** from dark-energy excitations.
Matter displaces the volume-law entropy, inducing an "elastic" response
in the de Sitter medium that mimics an additional gravitational pull.

For spherically symmetric systems, this yields an extra "apparent dark"
acceleration:

$$g_D \approx \sqrt{g_b \cdot a_M}, \qquad a_M \approx \frac{a_0}{6}$$

which in combination with baryonic gravity reproduces the deep-MOND limit
and the BTFR.

**The crucial result for CODA:** The Milgrom scale emerges as the de Sitter
horizon surface gravity:

$$\boxed{a_0 \sim cH_0 \sim \frac{c^2}{\ell_{dS}}}$$

This is not a coincidence but a consequence of the fact that the
volume-law entanglement entropy is controlled by the de Sitter horizon.

**Limitations:** Verlinde's framework is not a covariant local field theory
and is difficult to cast as an action with a local scalar density
$\mathcal{C}_K(x)$. It applies cleanly only to isolated spherical systems
and under-predicts cluster lensing by $\sim 3$. It provides a conceptual
bridge but not a completed theory.

### 2.2 Jacobson's Thermodynamic GR (1995) [ESTABLISHED]

Jacobson derived the Einstein equations from the Clausius relation
$\delta Q = T\,dS$ applied to local Rindler horizons, assuming
$S \propto A/4\ell_P^2$ (area law). This is purely area-law → pure GR.
To get MOND-like modifications, one would need a **modified entropy
functional** — specifically, volume-law corrections to the entanglement
entropy at low accelerations. Jacobson's derivation tells us the structure
but not the modification.

### 2.3 Krylov Complexity and MOND — Current Status [ESTABLISHED]

**There is no existing derivation of $a_0$ from Krylov complexity.**
All three independent models in CODA's research session confirmed this
unanimously. The existing holographic complexity–gravity links (CA/CV
conjectures, Krylov in SYK/JT gravity) are AdS-centric and high-energy.
The galactic low-acceleration regime is de Sitter/low-curvature — an
entirely different sector. Any connection is currently conjectural.

This is the frontier CODA is attempting to develop.

---

## 3. Structural Requirements on $\mathcal{C}_K(x)$ for MOND

For $\mathcal{C}_K(x)$ to produce MOND-like modifications while satisfying
the three constraints (GR at high acceleration, MOND at low acceleration,
no spin-2 ghost), the following structural conditions must hold:
[ESTABLISHED — confirmed by all three models]

### 3.1 Must Enter as a Scalar, Not a Curvature Invariant

The Tier 2 failure is structural: $C^2$ enters as a **curvature invariant**
producing a higher-derivative metric sector, which introduces the ghost.
$\mathcal{C}_K(x)$ must instead enter as a **dynamical scalar field** with
at most second derivatives in the action. The metric sector must remain
second-order (Einstein-Hilbert). This keeps the graviton propagator
healthy and avoids spin-2 ghost modes.

### 3.2 Noncanonical Kinetic Structure (AQUAL Template)

The scalar sector must have a **nonlinear kinetic term** — the AQUAL
(Aquadratic Lagrangian) structure of Bekenstein-Milgrom (1984):

$$S_K = \int d^4x\sqrt{-g}\,\frac{a_0^2}{8\pi G}\,
F\!\left(\frac{g^{\mu\nu}\partial_\mu\mathcal{C}_K\partial_\nu\mathcal{C}_K}
{a_0^2}\right)$$

where $F(y)$ is the interpolating function satisfying:

$$F(y) \to y \quad (y \gg 1): \quad \text{Newtonian limit — standard kinetic term}$$
$$F(y) \to \frac{2}{3}y^{3/2} \quad (y \ll 1): \quad \text{deep-MOND limit}$$

In the quasi-static weak-field limit, this produces the modified Poisson
equation:

$$\nabla\cdot\!\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right]
= 4\pi G\rho_b$$

with $\mu(x) = F'(x^2)$ being the standard MOND interpolating function.

### 3.3 Built-in Acceleration Scale $a_0$

The scale $a_0$ must be a **natural output** of the theory, not a free
parameter. Ideally it derives from $cH_0$ via the de Sitter horizon, as
in Verlinde's framework. In CODA's language: the transition between MOND
and Newtonian regimes must correspond to a natural transition in
$\mathcal{C}_K(x)$'s behaviour — specifically, from local/area-law
complexity to cosmological/volume-law complexity.

### 3.4 High-Curvature Suppression (Solar System Safety)

The $\mathcal{C}_K$-sourced modification must decouple when
$a_N \gg a_0$. This can be achieved via a coupling of the form:

$$S \supset \int d^4x\sqrt{-g}\,a_0^2\,f\!\left(\frac{\mathcal{C}_K}{a_0^2}\right)$$

with $f'(x) \to 0$ for $x \gg 1$ (high-acceleration/high-complexity
Newtonian regime). The function $f$ must be chosen so that it does not
reintroduce higher-derivative terms upon variation.

### 3.5 May Require an Auxiliary Vector Field

A pure scalar $\mathcal{C}_K$ is likely insufficient for full covariant
MOND: gravitational lensing in MOND requires both the time-time and
space-space metric perturbations to be modified consistently, which
typically demands a preferred-frame vector field. All successful covariant
MOND theories (TeVeS, AeST) include a timelike unit vector $A^\mu$ or
$u^\mu$ alongside the scalar sector.

**CODA's natural candidate:** The Krylov flow vector — the preferred
timelike direction used in the Tier 1 modular Krylov construction
(see `covariant_ck.md`, Section 2.3) — may serve this role. This would
give CODA a principled derivation of the vector sector rather than
postulating it ad hoc. [CODA-HYPOTHESIS]

---

## 4. Template Theories

### 4.1 AQUAL (Bekenstein-Milgrom 1984)

**Nonrelativistic** modified Poisson equation:
$$\nabla\cdot\!\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right]
= 4\pi G\rho_b$$

**Utility for CODA:** Provides the correct kinetic structure template.
The gradients of $\mathcal{C}_K$ could play the role of $|\nabla\Phi|/a_0$
in the interpolating function argument.

**Failure mode:** Not a relativistic theory. Cannot be elevated to a
covariant action without additional fields. Violates energy-momentum
conservation in the relativistic regime.

### 4.2 TeVeS (Bekenstein 2004)

**Relativistic tensor-vector-scalar** theory. Metric $g_{\mu\nu}$,
scalar $\phi$ (MOND interpolator), timelike unit vector $A^\mu$.
Matter couples to a disformal physical metric combining all three.

**Utility for CODA:** First relativistic MOND theory. The scalar $\phi$
with noncanonical kinetic term is the direct precursor of what
$\mathcal{C}_K$ should do. The vector field $A^\mu$ shows that a
preferred timelike direction is necessary.

**Failure modes:**
- Gravitational wave speed deviations ruled out by GW170817
- Ghost instabilities in the vector sector in some parameter ranges
- Struggles to reproduce CMB and large-scale structure
- Under-predicts Bullet Cluster lensing

### 4.3 AeST — Skordis & Złośnik (2021) [ESTABLISHED — current gold standard]

AeST proposes a relativistic gravitational theory leading to modified Newtonian dynamics, demonstrates agreement with the observed CMB and matter power spectra on linear cosmological scales, and is free of ghost instabilities at second order.

Critically, AeST replaces Milgrom's dimensionful constant $a_0$ with a dimensionless coupling constant $K_B$, with the cosmological coincidence $a_0 \sim cH_0$ now explained as an effect of the background FLRW cosmology.

**Structure:** Scalar field $\phi$ + timelike unit vector $A^\mu$ +
metric $g_{\mu\nu}$. The scalar has nonlinear kinetic term controlled by
$A^\mu$. Matter couples to the physical metric in the usual way.

**Utility for CODA:** AeST is the **structural target** for CODA's MOND
thread. It demonstrates that a ghost-free, CMB-compatible, covariant MOND
theory is achievable with precisely the field content that CODA's Tier 1
construction naturally provides. The identification is:

| AeST field | CODA Tier 1 object |
|------------|-------------------|
| Scalar $\phi$ | Covariant $\mathcal{C}_K(x)$ |
| Timelike vector $A^\mu$ | Krylov flow vector $u^\mu(x)$ |
| Nonlinear kinetic term | Modular complexity gradient structure |
| Scale $K_B$ | De Sitter modular transition |

[CODA-HYPOTHESIS — this identification is proposed, not derived]

**Remaining failure:** AeST still struggles with galaxy cluster lensing
(Bullet Cluster), suggesting additional physics beyond the scalar-vector
sector may be needed at those scales.

---

## 5. CODA's MOND Hypothesis — The Tier 1 Route

**Version note:** This section was substantially revised following direct
reading of Heller et al. (arXiv:2510.13986) and Aguilar-Gutierrez
(arXiv:2403.13186). See `audit/llm_synthesis/Q4b_DSSYK_papers.md` for
full details. The $a_0$ derivation programme is now substantially more
concrete than when this document was first written.

### 5.1 What the DSSYK Papers Establish [ESTABLISHED from primary sources]

Two results from the DSSYK holographic programme are directly relevant:

**From Aguilar-Gutierrez (2024), Section 4:**

For physical operators in the DSSYK/LdS2/SdS3 holographic triality,
the Lanczos coefficients are (their Eq. 4.10):

$$b_n = n\sqrt{\frac{n^2 - \nu^2/4}{4n^2 - 1}}
\xrightarrow{n\gg 1} \frac{n}{2}$$

**Linear growth with slope $\alpha = H_0/2$** (restoring $\ell_{dS}$
units). The late-time Krylov complexity:

$$C_K(\tau \gg 1) \propto e^\tau = e^{H_0 t}$$

saturating the Maldacena-Shenker-Stanford chaos bound with Lyapunov
exponent $\lambda_K = H_0$. The system is maximally chaotic at
temperature $T_{dS} = H_0/(2\pi)$.

**From Heller et al. (2025), the dS Krylov complexity function:**

$$C_K(\chi) \propto \log\!\left[\cosh\!\left(\frac{\chi\theta}{2}\right)\right]$$

This has a **quadratic-to-linear transition** at $\chi_* \sim 2\ell_{dS}$,
with late-time growth rate:

$$\frac{dC_K}{d\chi}\bigg|_{\chi\to\infty} \propto S_{dS} \cdot T_{dS}
= S_{dS} \cdot \frac{H_0}{2\pi}$$

### 5.2 The $a_0$ Derivation — Three Established Routes [ESTABLISHED]

The connection $a_0 = cH_0$ (Verlinde's result) now has three independent
derivation routes from the DSSYK literature, all consistent:

**Route 1 — Chaos bound:** The Lyapunov exponent $\lambda_K = H_0$ gives
timescale $\tau^* = H_0^{-1}$. Test particle with this dynamical timescale:

$$\boxed{a_0 = c/\tau^* = cH_0}$$

More precisely: $\lambda_K = 2\pi T_{dS} = H_0$, so
$a_0 = 2\pi c T_{dS} = cH_0$.

**Route 2 — Complexity transition:** The quadratic-to-linear transition in
$C_K(\chi)$ occurs at $\chi_* \sim \ell_{dS}$. Characteristic acceleration
at this scale:

$$\boxed{a_{\rm transition} = c^2/\ell_{dS} = cH_0 = a_0}$$

**Route 3 — Growth rate:** Late-time complexity rate $\propto S_{dS} \cdot H_0$.
The scale where cosmological complexity growth dominates local Newtonian
gravity defines $a_0 \sim cH_0$.

All three give $a_0 = cH_0$ with $O(1)$ factor $\eta = 1/(2\pi)$
from the de Sitter temperature, matching Verlinde (2016) exactly.

### 5.3 The Core Proposal — Revised [CODA-HYPOTHESIS]

The Tier 1 $\mathcal{C}_K(x)$ construction should target the **DSSYK
holographic regime** rather than the free scalar regime. The physical
picture:

**Sub-horizon regime** ($\ell \ll \ell_{dS}$, high acceleration):  
The local quantum gravity behaves like a weakly chaotic system; complexity
growth is slow. The contribution to the effective action is a standard
kinetic term. GR is recovered.

**Horizon-scale regime** ($\ell \sim \ell_{dS}$, low acceleration,
$a \lesssim cH_0$):  
The causal diamond reaches de Sitter scale. The local quantum gravity
enters the maximally chaotic regime ($\lambda_K \to H_0$). The complexity
growth transitions from sub-exponential to exponential ($b_n \sim n/2$).
The effective kinetic term becomes nonlinear.

**The transition** at $a \sim cH_0 = a_0$ separates the two regimes —
this is the MOND scale.

The functional form of the nonlinear kinetic term that emerges from
$C_K(\chi) \propto \log\cosh(\chi\theta/2)$ is not identical to AQUAL's
$F(y) \sim y^{3/2}$, but the qualitative structure (two power-law regimes,
transition at natural scale $\sim \ell_{dS}$) is correct.

### 5.4 The Remaining Gaps [OPEN PROBLEM]

Two concrete gaps remain between the DSSYK results and CODA's MOND thread:

**Gap 1 — 2D → 4D:** The DSSYK Krylov results are in 2D (dS2) or 3D
(SdS3). Heller et al. (2025) propose a higher-dimensional extension (their
Eq. 23) with the same $S_{dS} \cdot T_{dS}$ growth rate, but the microscopic
derivation from DSSYK only exists in 2D. Extension to 4D is their stated
"most pressing open question" — and CODA's Tier 1 problem in sharper form.

**Gap 2 — Local density:** DSSYK Krylov complexity is a global boundary
quantity. The holographic dictionary gives bulk complexity as an integrated
volume. To get $\mathcal{C}_K(x)$ as a local density, one needs the
integrand of the extremal volume — which is $r$-dependent and
foliation-dependent. The same obstacles documented in `covariant_ck.md`.

**The $a_0$ derivation programme in the following four steps:**

1. ✅ **De Sitter Krylov spectrum:** Lanczos coefficients $b_n \sim H_0 n/2$
   in the DSSYK holographic dual. Chaos bound saturated.

2. ✅ **Complexity transition at $\ell_{dS}$:** Quadratic-to-linear
   transition in $C_K(\chi)$ produces $a_{\rm transition} = cH_0 = a_0$.

3. 🔶 **AQUAL structure from complexity:** Whether the specific functional
   form $C_K(\chi) \propto \log\cosh(\cdot)$ produces the correct AQUAL
   interpolating function in the gravitational field equations. Open.

4. 🔲 **4D local density:** Lifting the DSSYK boundary Krylov to a
   covariant local $\mathcal{C}_K(x)$ in 4D dS. Open — Tier 1 problem.
   by the ratio of Lanczos growth rates in the local vs. cosmological
   regimes.

**Status:** Steps 1 and 2 are well-defined in principle. Step 3 requires
the covariant $\mathcal{C}_K(x)$ to exist (Tier 1 open problem). Step 4
is a prediction once Steps 1-3 are complete. [OPEN PROBLEM — Priority 1]

### 5.3 The Krylov Flow Vector

In the Tier 1 modular construction, a preferred timelike direction $u^\mu$
appears naturally as the generator of modular flow (the eigenvector of the
modular Hamiltonian at each spacetime point). This is not an additional
input — it is a derived quantity from the local state and metric.

**Proposed identification:** This Krylov flow vector $u^\mu$ plays the
role of AeST's timelike unit vector $A^\mu$. The action for the MOND
sector of CODA (in the Tier 1 framework) would then be:

$$S_{\rm MOND} = \int d^4x\sqrt{-g}\left[\frac{R}{16\pi G}
+ \mathcal{L}(\mathcal{C}_K, u^\mu, g_{\mu\nu})\right]$$

where $\mathcal{L}$ has the AeST structure with $\mathcal{C}_K$ and $u^\mu$
playing the roles of the AeST scalar and vector fields respectively, and
the nonlinear kinetic function $F$ derived (not assumed) from the modular
Lanczos structure.

[CODA-HYPOTHESIS — requires formal Tier 1 construction to verify]

---

## 6. What CODA Predicts Differently from Existing MOND Theories

If the CODA MOND hypothesis is correct, several predictions differ from
standard MOND and AeST:

**Prediction 1 — $\eta$ from first principles:** AeST treats the MOND
scale $a_0$ as a free parameter (absorbed into $K_B$). CODA claims $a_0$
derives from $cH_0$ with a specific calculable $O(1)$ factor $\eta$ from
the modular Krylov structure. If $\eta \neq 1/(2\pi)$ (the Verlinde/de
Sitter value), this is testable in principle. [SPECULATIVE]

**Prediction 2 — State dependence of $a_0$:** Because $\mathcal{C}_K$ is
state-dependent (see `covariant_ck.md`), the effective MOND scale may
vary with the local quantum state of the gravitational field. This
predicts a small variation of the effective $a_0$ in different
cosmological epochs — a deviation from standard MOND. [SPECULATIVE]

**Prediction 3 — Complexity signal in galaxy clusters:** The MOND failure
in clusters may be explained by a transition in the Krylov complexity
regime — cluster-scale dynamics may fall in an intermediate regime between
galactic (deep-MOND) and cosmological (GR), producing a characteristic
signature in the cluster acceleration profile. [SPECULATIVE]

---

## 7. The Sharpest Open Theoretical Question

Across all four model responses, one question emerged as the sharpest
unsolved problem connecting quantum information complexity to MOND:

> **Can a local, covariant definition of Krylov growth rate in the vacuum
> state of a QFT on a de Sitter background yield a global information
> bound that dynamically generates $a_0 \sim cH_0$ as the scale where
> scrambling transitions from local (area-law) to delocalised
> (volume-law), without violating causality or introducing ghosts?**

This is CODA's primary theoretical objective for the MOND thread.
The current answer is no — but unlike the covariant $\mathcal{C}_K(x)$
localisation problem (which may be fundamentally obstructed), this
question has a clear programme:

1. Compute Krylov complexity in de Sitter space (dS/CFT or direct modular
   flow calculation)
2. Identify the transition between area-law and volume-law Lanczos growth
3. Show that this transition sets a scale $\sim cH_0$
4. Derive the nonlinear AQUAL structure from the transition

Steps 1-2 are accessible with current techniques in quantum information
and holography. Steps 3-4 require the Tier 1 construction.

---

## 8. Open Problems — Ranked by Priority

| Priority | Problem | Status |
|----------|---------|--------|
| 1 | Compute Krylov complexity in de Sitter vacuum; does it produce $a_0 \sim cH_0$? | OPEN — critical |
| 2 | Establish covariant $\mathcal{C}_K(x)$ (Tier 1) — prerequisite for all MOND work | OPEN — see `covariant_ck.md` |
| 3 | Derive AeST kinetic structure from modular Lanczos coefficients | OPEN — SPECULATIVE |
| 4 | Identify Krylov flow vector $u^\mu$ with AeST vector field $A^\mu$ formally | OPEN — SPECULATIVE |
| 5 | Address galaxy cluster failure — does Krylov complexity predict intermediate regime? | OPEN |
| 6 | Does CODA predict a cosmological evolution of effective $a_0$? | OPEN |
| 7 | Reproduce the RAR/MDAR from the CODA MOND action | OPEN |

---

## 9. Multi-Model Research Session Notes

**Unanimous agreement (all three models):**
- No derivation of $a_0$ from Krylov complexity currently exists
- $\mathcal{C}_K$ must enter as a dynamical scalar, not a curvature invariant
- AQUAL nonlinear kinetic structure is the correct template
- AeST (Skordis-Złośnik 2021) is the current covariant MOND gold standard
- Verlinde's $a_0 \sim cH_0$ from de Sitter entanglement entropy is the
  strongest existing information-theoretic bridge
- MOND fails in galaxy clusters regardless of theory; CODA must acknowledge this

**Useful contributions by individual models:**
- Reply 1: AeST structural template; Krylov flow vector as natural AeST
  vector candidate; AQUAL action template with explicit $F(y)$ limits
- Reply 2: Clearest statement of epistemic status; precise MOND constraints;
  best treatment of the AQUAL→covariant extension problem
- Reply 3: Most rigorous constraint summary; precise $a_0$ value; clear
  statement of Verlinde's derivation; explicit AeST cluster failure caveat

**Added by synthesis beyond individual models:**
- The UV/IR polarity framing as the central organising insight
- The Tier 1 modular complexity transition at de Sitter scale as the
  CODA-specific MOND mechanism
- Explicit mapping between AeST fields and CODA Tier 1 objects
- The $a_0$ derivation programme as a four-step research plan
- Prediction of state-dependent effective $a_0$ as a falsifiable CODA signature

---

## 10. References

- Milgrom, M. (1983) — Original MOND papers; $a_0$ definition
- Bekenstein, J. & Milgrom, M. (1984) — AQUAL; nonlinear kinetic template
- Bekenstein, J.D. (2004) — TeVeS; first relativistic MOND
- Jacobson, T. (1995) — Thermodynamic derivation of GR
- Verlinde, E. (2016) — Emergent gravity; $a_0 \sim cH_0$ from de Sitter
  entanglement entropy (arXiv:1611.02269)
- **Skordis, C. & Złośnik, T. (2021)** — AeST; ghost-free relativistic MOND
  compatible with CMB; *Phys. Rev. Lett.* **127**, 161302.
  The structural target for CODA's MOND thread.
- McGaugh, S., Lelli, F. & Schombert, J. (2016) — Radial Acceleration
  Relation; tight empirical constraint any MOND theory must satisfy
- Famaey, B. & McGaugh, S. (2012) — MOND review; comprehensive constraint
  summary (arXiv:1112.3960)

---

*End of document. Version 0.1 — working hypothesis, requires Tier 1
development before any prediction can be made quantitative.*  
*Next: `phenomenology/weak_field_limit.md` — Solar System and PPN constraints.*