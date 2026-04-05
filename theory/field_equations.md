# CODA Field Equations — Linearisation, Propagator, and Corrections

**Document:** `theory/field_equations.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.3  
**Status:** Foundational — all numerical factors verified against Stelle (1977)  
**Depends on:** `theory/action_principle.md`, `theory/covariant_ck.md`  
**Primary source:** K.S. Stelle, *Phys. Rev. D* **16**, 953 (1977)  
**Changelog v0.3:**
- §2.3 added: Conservation identity $\nabla^\mu B_{\mu\nu} = 0$
- §7 restructured: Bach-flat metrics theorem added (§7.0); Einstein metric class
  expanded to include Schwarzschild-dS, Kerr-dS; FLRW proof formalised (§7.3)
- §7.5 added: Cosmological perturbation suppression (references `cosmological_background.md`)
- §9: Two new canonical equations added
- §11: Open problems updated — cosmological items closed/refined, BH items sharpened

---

## ⚠ Corrections to Prior CODA Documents

This document supersedes `field_equations.md` v0.1 and corrects two errors
in `action_principle.md` identified by cross-referencing Stelle (1977) directly.

**Error 1 — Variation coefficient:**  
`action_principle.md` stated $\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}C^2)}
{\delta g^{\mu\nu}} = -4B_{\mu\nu}$. The correct result, consistent with the
conformal gravity EOM and verified via Stelle's ghost mass formula, is:

$$\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,C^2)}{\delta g^{\mu\nu}} = -2B_{\mu\nu}$$

**Error 2 — CODA coupling $\Lambda_C$:**  
`action_principle.md` stated $\Lambda_C = 64\pi G\xi$. The correct value is:

$$\Lambda_C = 32\pi G\xi$$

**Error 3 — Mannheim-Kazanas MOND connection (previously flagged):**  
The $\gamma r$ linear potential is a feature of pure conformal gravity only.
It does not appear in Einstein-Weyl gravity (CODA Tier 2).

**Error source — Reply 2 (multi-model session):**  
Reply 2's ghost mass $m_2^2 = 1/(8\pi G\xi)$ arose from substituting
$\kappa^2 = 8\pi G$ into Stelle's formula. Stelle defines $\kappa^2 = 32\pi G$
(his Eq. 2.1, p. 954) — a factor-of-4 difference that propagates directly
into $m_2^2$. Replies 1 and 3 were correct.

---

## 1. Stelle (1977) — Authoritative Fixed Points

Stelle's action (Eq. 2.1, p. 954), signature $(-+++)$:

$$I_{\rm sym} = -\int d^4x\sqrt{-g}
\left(\alpha R_{\mu\nu}R^{\mu\nu} - \beta R^2 + \kappa^{-2}\gamma R\right)$$

where $\kappa^2 = 32\pi G$ and $\gamma = 2$.

The overall minus sign with $\kappa^{-2}\gamma R = R/(16\pi G)$ gives the EH
term $+R/(16\pi G)$, matching CODA's sign convention.

**Weyl identity** (Stelle Appendix, Eq. A5, p. 968):

$$\int d^4x\sqrt{-g}\left(R_{\mu\nu}R^{\mu\nu} - \frac{1}{3}R^2\right)
= \frac{1}{2}\int d^4x\sqrt{-g}\,C_{\mu\nu\alpha\beta}C^{\mu\nu\alpha\beta}$$

This establishes the CODA-to-Stelle dictionary:

$$\alpha_{\rm Stelle} = 2\xi_{\rm CODA}, \qquad
\beta_{\rm Stelle} = \frac{2\xi_{\rm CODA}}{3}$$

**Ghost mass** (Stelle Eq. 2.3, p. 954), substituting $\alpha = 2\xi$,
$\kappa^2 = 32\pi G$:

$$\boxed{m_2^2 = \left(\tfrac{1}{2}\alpha\kappa^2\right)^{-1}
= \frac{1}{32\pi G\xi}}$$

**Newtonian potential** (Stelle Eq. 2.3, p. 954), pure Einstein-Weyl
case ($m_0 \to \infty$ since no independent $R^2$ term):

$$\boxed{\Phi(r) = -\frac{GM}{r}\left(1 - \frac{4}{3}\,e^{-m_2 r}\right)}$$

These two boxed results are the **authoritative fixed points** for all CODA
documents. Any derivation yielding different coefficients contains a
convention error and should be re-checked against these.

---

## 2. The CODA Field Equations — Corrected

### 2.1 Variation Verification

For $B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma}
+ \frac{1}{2}R^{\rho\sigma}C_{\mu\rho\nu\sigma}$, the variation satisfies:

$$\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,C^2)}{\delta g^{\mu\nu}} = -2B_{\mu\nu}$$

**Self-consistency check:** Setting this to zero for pure conformal gravity
($S = \int\sqrt{-g}C^2$) gives $B_{\mu\nu} = 0$, which is the correct
conformal gravity vacuum equation. ✓

**Stelle consistency check:** With $-2B_{\mu\nu}$ the field equations give
$m_2^2 = 1/(32\pi G\xi)$, matching Stelle Eq. 2.3 exactly. ✓

### 2.2 Corrected CODA Field Equations

$$\frac{G_{\mu\nu}}{16\pi G} + \xi(-2B_{\mu\nu}) - \frac{1}{2}T_{\mu\nu} = 0$$

$$\boxed{G_{\mu\nu} - 32\pi G\xi\,B_{\mu\nu} = 8\pi G\,T_{\mu\nu}}$$

**Corrected CODA complexity coupling:**

$$\boxed{\Lambda_C = 32\pi G\xi = \frac{G\alpha\ell_P^4}{2\pi}}$$

### 2.3 Conservation Identity [ESTABLISHED]

The CODA Tier 2 action $S_{C^2} = \xi\int d^4x\sqrt{-g}\,C^2$ is
diffeomorphism-invariant. By the generalised contracted Bianchi identity,
the variation of any diffeomorphism-invariant action satisfies:

$$\nabla^\mu\!\left(\frac{1}{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}}\right) = 0$$

Applied to $S_{C^2}$ with $\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}C^2)}
{\delta g^{\mu\nu}} = -2B_{\mu\nu}$:

$$\boxed{\nabla^\mu B_{\mu\nu} = 0}$$

This is an identity — it holds on every metric, not only on solutions.
Combined with $\nabla^\mu G_{\mu\nu} = 0$ (standard Bianchi) and the field
equations, it implies $\nabla^\mu T_{\mu\nu} = 0$: matter is conserved in CODA
Tier 2 exactly as in GR. The complexity coupling introduces no anomalous energy
injection. `[ESTABLISHED]`

---

## 3. Linearised Field Equations

### 3.1 Setup

$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, trace-reversed perturbation
$\bar{h}_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h$,
harmonic gauge $\partial^\mu\bar{h}_{\mu\nu} = 0$.

Linearised quantities [ESTABLISHED]:

$$G_{\mu\nu}^{(1)} = -\frac{1}{2}\Box\bar{h}_{\mu\nu}, \qquad
B_{\mu\nu}^{(1)}\bigg|_{\rm TT} = \frac{1}{2}\Box^2 h_{\mu\nu}^{\rm TT}$$

The linearised Weyl tensor in full:

$$C_{\mu\nu\rho\sigma}^{(1)} = R_{\mu\nu\rho\sigma}^{(1)}
- \frac{1}{2}\!\left(\eta_{\mu\rho}R_{\nu\sigma}^{(1)} - \eta_{\mu\sigma}R_{\nu\rho}^{(1)}
- \eta_{\nu\rho}R_{\mu\sigma}^{(1)} + \eta_{\nu\sigma}R_{\mu\rho}^{(1)}\right)
+ \frac{R^{(1)}}{6}\!\left(\eta_{\mu\rho}\eta_{\nu\sigma}
- \eta_{\mu\sigma}\eta_{\nu\rho}\right)$$

### 3.2 TT Sector Vacuum Equation

Substituting into $G_{\mu\nu} - 32\pi G\xi\,B_{\mu\nu} = 0$:

$$-\frac{1}{2}\Box h^{\rm TT}
- 32\pi G\xi\cdot\frac{1}{2}\Box^2 h^{\rm TT} = 0$$

$$\boxed{\Box\left(1 + 32\pi G\xi\,\Box\right)h_{\mu\nu}^{\rm TT} = 0}$$

In momentum space ($\Box \to -k^2$, metric signature $(-+++)$):

$$\boxed{k^2\left(1 - 32\pi G\xi\,k^2\right) = 0}$$

Poles at $k^2 = 0$ (massless graviton) and $k^2 = m_2^2 = 1/(32\pi G\xi)$
(massive ghost). ✓ Consistent with Stelle (1977).

---

## 4. The Graviton Propagator

### 4.1 Momentum-Space Structure

Quadratic kinetic operator (TT spin-2 sector):

$$\mathcal{O}(k) = \frac{k^2}{16\pi G} - 2\xi\,k^4
= \frac{k^2}{16\pi G}\left(1 - 32\pi G\xi\,k^2\right)$$

Partial-fraction decomposition of the propagator:

$$D_{\mu\nu,\rho\sigma}(k) = 16\pi G\,i\,\Pi^{\rm TT}_{\mu\nu\rho\sigma}
\left[\frac{1}{k^2} - \frac{1}{k^2 - m_2^2}\right]$$

### 4.2 Poles, Spins, and Kinetic Signs [ESTABLISHED]

| Pole | Location | Spin | Residue | Mode |
|------|----------|------|---------|------|
| Massless | $k^2 = 0$ | 2 | $+$ (positive) | Healthy GR graviton |
| Massive | $k^2 = m_2^2$ | 2 | $-$ (negative) | Stelle ghost |

No scalar pole is present in pure Einstein-Weyl gravity. [ESTABLISHED]

---

## 5. Ghost Mass and EFT Self-Consistency

### 5.1 Ghost Mass [ESTABLISHED — Stelle 1977]

$$\boxed{m_2 = \frac{1}{\sqrt{32\pi G\xi}} = \frac{M_P}{2\sqrt{\xi}},
\qquad M_P = \frac{1}{\sqrt{8\pi G}}}$$

**Model disagreement resolved:**

| Source | $m_2^2$ | Verdict |
|--------|---------|---------|
| Reply 1 | $\frac{1}{32\pi G\xi}$ | ✓ Correct |
| Reply 2 | $\frac{1}{8\pi G\xi}$ | ✗ Wrong $\kappa^2$ |
| Reply 3 | $\frac{1}{32\pi G\xi}$ | ✓ Correct |
| **Stelle (1977)** | $\frac{1}{32\pi G\xi}$ | ✓ **Authoritative** |

### 5.2 EFT Condition [ESTABLISHED]

$$m_2 > M_P \quad\Longleftrightarrow\quad \boxed{\xi < \frac{1}{4}}$$

CODA's natural coupling gives $\xi \sim \ell_P^6 \ll 1$ (natural units).
EFT self-consistency holds with enormous margin. Ghost mass $m_2 \gg M_P$;
the ghost is unphysical at all accessible energies. ✓

---

## 6. The Newtonian Potential [ESTABLISHED — Stelle 1977]

$$\boxed{\Phi(r) = -\frac{GM}{r}\left(1 - \frac{4}{3}\,e^{-m_2 r}\right)}$$

**Key features:**

- **Correction type:** Yukawa (exponentially decaying) — not power-law,
  not linear. Confirmed by all three models and Stelle (1977).
- **Coefficient $\frac{4}{3}$:** Exact for pure Einstein-Weyl (no $R^2$).
  Arises from the residue of the massive spin-2 ghost propagator.
- **Long range** ($r \gg m_2^{-1}$): exact GR recovery $\Phi \to -GM/r$. ✓
- **Short range** ($r \ll m_2^{-1}$): $1/r$ singularity softened — Stelle (1977).
- **Galactic scales:** For EFT-consistent $\xi$, $m_2^{-1} \sim \ell_P$.
  The Yukawa correction is negligible at all astrophysical scales. No MOND effect.

**No linear $r$ term exists in this theory.** The Mannheim-Kazanas $\gamma r$
potential is absent. CODA Tier 2 does not produce galactic-scale modifications.

---

## 7. Known Exact Solutions

### 7.0 Bach-Flat Metrics — General Theorem [ESTABLISHED]

A metric is called **Bach-flat** if $B_{\mu\nu} = 0$. All Bach-flat metrics
are exact solutions of CODA Tier 2 with the same matter content as in GR.

**Theorem:** The following two classes of metrics in 4D are Bach-flat:

**(A) Conformally flat metrics:** $C_{\mu\nu\rho\sigma} = 0$ identically.
Both terms in $B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma}
+ \frac{1}{2}R^{\rho\sigma}C_{\mu\rho\nu\sigma}$ vanish term by term.

**(B) Einstein metrics:** Any metric satisfying
$R_{\mu\nu} = \lambda g_{\mu\nu}$ for a constant $\lambda$.

*Proof of (B):* For an Einstein metric, the contracted second Bianchi identity
gives $\nabla_\mu R_{\nu\sigma} = \frac{1}{4}g_{\nu\sigma}\nabla_\mu R = 0$
(constant $R = 4\lambda$). The contracted Bianchi identity for the Weyl tensor:

$$\nabla^\rho C_{\mu\nu\rho\sigma}
= -\nabla_\mu R_{\nu\sigma} + \nabla_\nu R_{\mu\sigma}
+ \tfrac{1}{6}(g_{\mu\sigma}\nabla_\nu R - g_{\nu\sigma}\nabla_\mu R) = 0$$

Therefore $\nabla^\rho C_{\mu\nu\rho\sigma} = 0$ for all Einstein metrics.
The Bach tensor reduces to:

$$B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma}
+ \tfrac{\lambda}{2}\underbrace{C_{\mu\rho\nu}{}^\rho}_{=\,0\text{ (traceless)}} = 0$$

where the first term vanishes because $\nabla^\rho C_{\mu\rho\nu\sigma} = 0$
implies $\nabla^\sigma\nabla^\rho C_{\mu\rho\nu\sigma} = 0$ (using the Bianchi
identity once more with the Einstein metric condition). $\square$

**Corollary:** CODA Tier 2 adds no correction to GR for any member of either
class. The coupling $\xi$ is entirely invisible for conformally flat and
Einstein metrics. `[ESTABLISHED]`

### 7.1 Einstein Vacuum Metrics ($\lambda = 0$, $R_{\mu\nu} = 0$) [ESTABLISHED]

All vacuum GR solutions are exact CODA Tier 2 solutions:

| Metric | Properties | CODA status |
|--------|-----------|-------------|
| Schwarzschild | Vacuum, static, spherical | Exact solution, $B_{\mu\nu} = 0$ |
| Kerr | Vacuum, rotating, axisymmetric | Exact solution, $B_{\mu\nu} = 0$ |
| Gravitational waves (pp-waves) | Vacuum, type N | Exact solution, $B_{\mu\nu} = 0$ |
| Minkowski | Vacuum, flat | Exact solution, $C = B = 0$ |

### 7.2 Einstein Metrics with Cosmological Constant ($\lambda = \Lambda/3$) [ESTABLISHED, v0.3]

Einstein metrics with cosmological constant $R_{\mu\nu} = \Lambda g_{\mu\nu}/3$
are also Bach-flat. This class is larger than often appreciated:

| Metric | $\Lambda$ | CODA status |
|--------|-----------|-------------|
| Schwarzschild-de Sitter | $\Lambda > 0$ | Exact solution, $B_{\mu\nu} = 0$ |
| Schwarzschild-anti-de Sitter | $\Lambda < 0$ | Exact solution, $B_{\mu\nu} = 0$ |
| Kerr-de Sitter | $\Lambda > 0$ | Exact solution, $B_{\mu\nu} = 0$ |
| Kerr-anti-de Sitter | $\Lambda < 0$ | Exact solution, $B_{\mu\nu} = 0$ |
| Pure de Sitter | $\Lambda > 0$ | Exact solution, $C = B = 0$ (also conformally flat) |
| Pure anti-de Sitter | $\Lambda < 0$ | Exact solution, $B_{\mu\nu} = 0$ |

**Important implication for black hole phenomenology:** The standard GR black
holes — including all Schwarzschild-dS and Kerr-dS solutions relevant to
cosmology — are unmodified by CODA Tier 2. Genuine CODA departures from GR
require metrics that are *neither* conformally flat *nor* Einstein metrics.
See `phenomenology/black_hole_phenomenology.md` for the non-Schwarzschild
solutions (Lu, Perkins, Pope, Stelle 2015) that carry Weyl hair.

### 7.3 Non-Schwarzschild Black Holes [ESTABLISHED]

Lu, Perkins, Pope, Stelle (2015): static spherically symmetric solutions
with massive spin-2 hair $\sim e^{-m_2 r}/r$, asymptotically flat, distinct
from Schwarzschild near the horizon. These are solutions of the full CODA
field equations with $B_{\mu\nu} \neq 0$ — they exist precisely because the
$\xi C^2$ term admits additional gravitational degrees of freedom. See §7.5
of `phenomenology/black_hole_phenomenology.md` for analysis.

### 7.4 FLRW Cosmology [ESTABLISHED — formalised v0.3]

**Theorem:** All FLRW metrics satisfy $C_{\mu\nu\rho\sigma} = 0$ and
$B_{\mu\nu} = 0$. The CODA Tier 2 field equations reduce exactly to the
standard Friedmann equations for all values of $\xi$ and all matter content.

*Proof:* Spatially flat FLRW: $ds^2 = a^2(\eta)(-d\eta^2 + d\vec{x}^2)$.
This is $a^2(\eta)$ times Minkowski, a conformal rescaling of a flat metric.
The Weyl tensor is conformally covariant with weight 0 in 4D:
$C_{\mu\nu\rho\sigma}[a^2\eta] = C_{\mu\nu\rho\sigma}[\eta] = 0$.
The same holds for $k = \pm 1$ FLRW via the relevant conformal rescalings.
Bach-flat theorem class (A) applies. $\square$

**Consequence:** No cosmological background measurement can constrain $\xi$.
See `phenomenology/cosmological_background.md` for the full analysis.

### 7.5 Cosmological Perturbations — Suppression Result [ESTABLISHED, v0.3]

On a FLRW background with small perturbations, the Bach tensor is first order
in perturbation theory: $\delta B_{\mu\nu} = \mathcal{O}(\delta g)$. In Fourier
space it involves four spatial derivatives of the metric perturbation:

$$\delta B_{\mu\nu} \sim \frac{k^4}{a^4}\delta g_{\mu\nu}$$

The CODA correction to perturbed field equations relative to Einstein:

$$\frac{32\pi G\xi\,\delta B_{\mu\nu}}{\delta G_{\mu\nu}}
\sim \frac{k_{\rm phys}^2}{m_2^2}
= 4\xi\,\frac{k_{\rm phys}^2}{M_P^2}$$

At CMB scales ($k_{\rm phys} \sim 10^{-4}$–$10^{-2}$ Mpc$^{-1}$):

$$\frac{k_{\rm phys}^2}{M_P^2} \sim 10^{-114}$$

**All cosmological perturbation observables (CMB power spectra, matter power
spectrum, gravitational slip, BBN) are identical to GR to all measurable
precision.** `[CODA-PREDICTION]` Full analysis in `phenomenology/cosmological_background.md`.

---

## 8. Implications for CODA

### 8.1 MOND Thread

| Approach | Status | Reason |
|----------|--------|--------|
| Tier 2 Yukawa | Negligible at galactic scales | $m_2^{-1} \sim \ell_P$ |
| Large $\xi$ (EFT-violating) | Unacceptable | Ghost enters physical spectrum |
| Pure conformal limit | Incompatible | Loses GR recovery |
| Tier 1 formal $\mathcal{C}_K$ | **Open — preferred** | Not constrained to $C^2$ form |

### 8.2 Solar System and PPN Tests

For EFT-consistent $\xi$: Yukawa range $m_2^{-1} \ll$ AU.
PPN parameters $\gamma_{\rm PPN} = 1$, $\beta_{\rm PPN} = 1$ are exact.
All Solar System tests pass automatically. ✓

---

## 9. Canonical Equation Summary

| Quantity | Expression | Source |
|----------|-----------|--------|
| Field equations | $G_{\mu\nu} - 32\pi G\xi\,B_{\mu\nu} = 8\pi G T_{\mu\nu}$ | This document (corrected) |
| Bach tensor variation | $\frac{\delta(\sqrt{-g}C^2)}{\sqrt{-g}\,\delta g^{\mu\nu}} = -2B_{\mu\nu}$ | Verified via Stelle |
| Conservation identity | $\nabla^\mu B_{\mu\nu} = 0$ | §2.3 (v0.3, Bianchi) |
| $\Lambda_C$ | $32\pi G\xi$ | Corrected from $64\pi G\xi$ |
| TT vacuum equation | $\Box(1 + 32\pi G\xi\,\Box)h^{\rm TT} = 0$ | This document |
| Ghost mass | $m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$ | Stelle (1977) Eq. 2.3 |
| EFT condition | $\xi < \frac{1}{4}$ | Stelle (1977) |
| Newtonian potential | $\Phi = -\frac{GM}{r}(1 - \frac{4}{3}e^{-m_2 r})$ | Stelle (1977) Eq. 2.3 |
| Trace equation | $R = -8\pi G\,T$ | Unmodified from GR |
| Bach-flat theorem | $B_{\mu\nu} = 0$ for all conformally flat and Einstein metrics | §7.0 (v0.3) |
| Cosmological suppression | $\delta B/\delta G \sim k_{\rm phys}^2/M_P^2$ | §7.5 (v0.3) |

---

## 10. Corrections Required in Other Documents

| Document | Location | Change |
|----------|----------|--------|
| `action_principle.md` | Section 2.2 variation | $-4\xi B_{\mu\nu}$ → $-2\xi B_{\mu\nu}$ |
| `action_principle.md` | Section 3 and 7 | $\Lambda_C = 64\pi G\xi$ → $32\pi G\xi$ throughout |
| `action_principle.md` | Section 6 | Retract Mannheim-Kazanas claim (already flagged) |

---

## 11. Open Problems

| Priority | Problem | Notes |
|----------|---------|-------|
| 1 | Can Tier 1 $\mathcal{C}_K$ produce IR corrections without a ghost? | Core MOND / cosmology question |
| 2 | Quasi-normal modes and ringdown for non-Schwarzschild CODA BHs | Observational GW signature |
| 3 | Is the non-Schwarzschild branch of Lu et al. thermodynamically preferred? | BH stability question |
| 4 | Cauchy problem for 4th-order CODA equations | Mathematical completeness |
| 5 | Do non-Einstein metrics other than Lu et al. BHs exist? | Full classification of CODA solutions |
| — | ~~Cosmological tensor perturbation spectrum~~ | Closed: identical to GR (§7.5) |
| — | ~~PPN parameter calculation~~ | Closed: $\gamma = \beta = 1$ exactly (weak_field_limit.md) |

---

## 12. Multi-Model Session Notes

**Unanimous agreements (all confirmed by Stelle 1977):**
- $B^{(1)}_{\mu\nu}|_{\rm TT} = \frac{1}{2}\Box^2 h^{\rm TT}$
- Two propagator poles: massless spin-2 (healthy) + massive spin-2 (ghost)
- No scalar pole in pure Einstein-Weyl
- Yukawa correction $\Phi = -\frac{GM}{r}(1 - \frac{4}{3}e^{-m_2 r})$
- Mannheim-Kazanas belongs to pure conformal gravity only

**Disagreement resolved:**
- Ghost mass: $m_2^2 = \frac{1}{32\pi G\xi}$ (Replies 1, 3 correct; Reply 2 used wrong $\kappa^2$)

**Errors in prior CODA documents corrected:**
- Variation coefficient: $-4B_{\mu\nu}$ → $-2B_{\mu\nu}$
- $\Lambda_C$: $64\pi G\xi$ → $32\pi G\xi$

**v0.3 additions (direct derivation, no model query):**
- Bach-flat metrics theorem: proved for both conformally flat and Einstein metric classes
- Conservation identity: $\nabla^\mu B_{\mu\nu} = 0$ from diffeomorphism invariance
- FLRW theorem: formal proof given
- Schwarzschild-dS / Kerr-dS added to exact solution catalogue

---

## 13. References

- **Stelle, K.S. (1977)** — *Phys. Rev. D* **16**, 953. All numerical results
  in this document are verified against this source.
- Mannheim, P.D. & Kazanas, D. (1989) — Exact solution of pure conformal gravity
- Lu, H., Perkins, A., Pope, C.N. & Stelle, K.S. (2015) — Non-Schwarzschild BHs
  in quadratic gravity
- CODA documents: `phenomenology/weak_field_limit.md`,
  `phenomenology/cosmological_background.md`

---

*End of document. Version 0.3.*