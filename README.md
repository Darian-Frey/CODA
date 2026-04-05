# Project CODA

**Complexity-Originated Dynamics of Action**

> *A covariant field-theoretic extension of General Relativity via Krylov
> Complexity Density, with derived field equations and phenomenological
> threads targeting MOND rotation curves and Planck-to-macroscopic scale
> bridging.*

---

## What CODA Is

CODA is an attempt to build a rigorous bridge between quantum information
theory and macroscopic gravitational dynamics. It extends the
Einstein-Hilbert action by coupling spacetime curvature to a covariant
**Krylov Complexity Density** $\mathcal{C}_K(x)$ — a local scalar field
encoding the quantum computational depth required to describe the local
spacetime geometry.

The central action is:

$$S_{\rm CODA} = \int d^4x\,\sqrt{-g}
\left[\frac{R}{16\pi G} + \alpha\,\mathcal{C}_K(x) + \mathcal{L}_m\right]$$

The field equations are:

$$G_{\mu\nu} - \Lambda_C\,B_{\mu\nu} = 8\pi G\,T_{\mu\nu}$$

where $B_{\mu\nu}$ is the Bach tensor and $\Lambda_C = 32\pi G\xi$ is the
CODA complexity coupling. All numerical factors are verified against
Stelle (1977).

---

## What CODA Is Not

CODA does not claim to be a completed theory. The central object
$\mathcal{C}_K(x)$ — a diffeomorphism-covariant scalar with units
$[L^{-4}]$ — **does not yet have a rigorous construction**. No paper in
the existing literature has built such an object. The construction problem
is documented explicitly in `theory/covariant_ck.md` with all obstacles
stated.

CODA does not claim observational validation. The Tier 2 working proxy
(Weyl-squared action) is a semiclassical stand-in used to derive field
equations, propagator structure, and consistency properties — not a claim
about observable physics. All speculative proposals are clearly marked
with epistemic flags.

---

## Epistemic Architecture

All CODA documents use explicit epistemic tags:

| Tag | Meaning |
|-----|---------|
| `[ESTABLISHED]` | Standard result from the literature, independently verified |
| `[CODA]` | Result derived within CODA; not previously published |
| `[CODA-HYPOTHESIS]` | CODA proposal, plausible but unverified |
| `[SPECULATIVE]` | Conjecture requiring formal development |
| `[OPEN PROBLEM]` | Unresolved question with explicit priority ranking |
| `[CORRECTED]` | Supersedes an error in a prior document version |

This is not decoration. Epistemic tagging is how CODA avoids the failure
mode of its predecessor CODE-GEO, which conflated established results with
speculative claims.

---

## The Two-Tier Structure

### Tier 2 — Working Theory (available now)

The **Weyl-squared proxy** $\mathcal{C}_K(x) \approx \frac{\ell_P^4}{8\pi}
C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}$ gives a tractable
working theory. Its properties are fully derived:

- Field equations: $G_{\mu\nu} - 32\pi G\xi\,B_{\mu\nu} = 8\pi G T_{\mu\nu}$
- Ghost mass: $m_2^2 = 1/(32\pi G\xi)$, above $M_P$ for $\xi < 1/4$ ✓
- All GR vacuum solutions (Schwarzschild, Kerr) are exact CODA solutions ✓
- FLRW cosmology is unmodified ✓
- Newtonian potential: $\Phi = -GM/r\,(1 - \frac{4}{3}e^{-m_2 r})$
- **MOND phenomenology: absent** (Tier 2 is a UV modification; MOND requires IR)

### Tier 1 — Target Theory (open problem)

The **formal modular Krylov construction** — defined via shrinking causal
diamonds and the modular Hamiltonian — is what CODA ultimately targets.
If this construction succeeds, it is expected to produce:

- A natural AQUAL-like nonlinear kinetic structure for $\mathcal{C}_K$
- The Milgrom scale $a_0 \sim cH_0$ from the de Sitter horizon
- The AeST (Skordis-Złośnik 2021) field structure derived from first principles
- A ghost-free modification of gravity at galactic scales

---

## Key Results (Verified)

All the following are verified against primary sources and documented
with full derivations:

- **Ghost mass** (Stelle 1977): $m_2^2 = \frac{1}{32\pi G\xi}$
- **EFT condition**: $\xi < \frac{1}{4}$ for ghost above $M_P$
- **Newtonian potential** (Stelle 1977): Yukawa correction $\propto \frac{4}{3}e^{-m_2 r}/r$
- **Vacuum solutions**: All GR vacuum spacetimes are exact CODA Tier 2 solutions
- **Bach tensor variation**: $\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}C^2)}{\delta g^{\mu\nu}} = -2B_{\mu\nu}$
- **Trace equation**: Unmodified from GR — $R = -8\pi G T$

## Key Open Problems (Prioritised)

1. Prove or disprove the $\epsilon \to 0$ limit of the modular Krylov density
2. Compute Krylov complexity in de Sitter vacuum — does it produce $a_0 \sim cH_0$?
3. Establish whether the Krylov flow vector $u^\mu$ maps to the AeST vector field
4. Derive the AQUAL nonlinear kinetic structure from modular Lanczos coefficients
5. Establish the Cauchy problem for the 4th-order CODA Tier 2 field equations

---

## Repository Structure

```
CODA/
├── README.md                          ← This file
├── ROADMAP.md                         ← Phased research plan
├── CITATION.cff                       ← Citation metadata
├── LITERATURE_MAP.md                  ← Theoretical lineage
│
├── theory/
│   ├── covariant_ck.md                ← Defining C_K(x): the core open problem
│   ├── action_principle.md            ← The CODA action and field equations (v0.2)
│   └── field_equations.md             ← Linearisation, propagator, ghost mass (v0.2)
│
├── phenomenology/
│   ├── mond_thread.md                 ← MOND reconstruction via Tier 1 (hypothesis)
│   └── weak_field_limit.md            ← Solar System and PPN constraints (pending)
│
├── simulations/                       ← Python verification scripts (pending)
├── derivations/                       ← LaTeX working documents
└── audit/
    └── llm_synthesis/                 ← Four-model research session logs
```

**Reading order:** `covariant_ck.md` → `action_principle.md` →
`field_equations.md` → `mond_thread.md`

---

## Research Methodology

CODA uses a **four-model synthesis methodology** for all major theoretical
questions. Before writing any document, a research query is distributed to
four independent large language models. Their responses are synthesised —
agreements increase confidence, disagreements are investigated and resolved
against primary sources. All synthesis sessions are logged in
`audit/llm_synthesis/` with explicit records of what was agreed, disputed,
and corrected.

This methodology caught the following errors before they propagated:
- Incorrect $\Lambda_C = 64\pi G\xi$ (corrected to $32\pi G\xi$ via Stelle 1977)
- Incorrect Mannheim-Kazanas MOND claim for Einstein-Weyl gravity
- Factor-of-4 error in ghost mass from one model (traced to wrong $\kappa^2$ convention)

---

## Lineage

CODA is a complete rebuild of Project CODE-GEO (v3.1), which attempted to
connect quantum information complexity to gravitational wave observations.
CODE-GEO's empirical claim — a 2.816 ms echo in GW250114 — was not
supported by published LIGO analysis, and several of its theoretical steps
were reverse-engineered from desired results rather than derived.

CODA retains CODE-GEO's core instinct (Krylov complexity as a gravitational
source term) and its strongest original idea (interpreting the Milgrom
acceleration as vacuum-computational latency), while rebuilding the
theoretical framework from scratch with rigorous derivations, primary
source verification, and explicit epistemic tagging throughout.

---

## Citation

If you use CODA in your work, please cite:

```
@software{hartley2026coda,
  author    = {Hartley, Shane},
  title     = {Project CODA: Complexity-Originated Dynamics of Action},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/Darian-Frey/CODA}
}
```

---

## License

MIT License — see LICENSE file.

---

*Project CODA — Version 0.1 (Theory Layer Complete)*  
*Lead researcher: Shane Hartley*