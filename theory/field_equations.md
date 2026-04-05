# CODA Field Equations — Linearisation, Propagator, and Corrections

**Document:** `theory/field_equations.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.2 (Corrected — supersedes v0.1)  
**Status:** Foundational — all numerical factors verified against Stelle (1977)  
**Depends on:** `theory/action_principle.md`, `theory/covariant_ck.md`  
**Primary source:** K.S. Stelle, *Phys. Rev. D* **16**, 953 (1977)

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

## 7. Known Solutions Beyond Flat Space

### 7.1 All GR Vacuum Solutions [ESTABLISHED]

$R_{\mu\nu} = 0 \Rightarrow B_{\mu\nu} = 0$. Every vacuum solution of GR
(Schwarzschild, Kerr, gravitational waves) is an exact solution of CODA Tier 2.

### 7.2 Non-Schwarzschild Black Holes [ESTABLISHED]

Lu, Perkins, Pope, Stelle (2015): static spherically symmetric solutions
with massive spin-2 hair $\sim e^{-m_2 r}/r$, asymptotically flat, distinct
from Schwarzschild near the horizon.

### 7.3 FLRW Cosmology [ESTABLISHED]

$C_{\mu\nu\rho\sigma} = 0$ for all FRW backgrounds (conformally flat).
$B_{\mu\nu} = 0$. Background cosmology is exactly GR. ✓

### 7.4 Mannheim-Kazanas — Belongs to Pure Conformal Gravity [ESTABLISHED]

The solution $B(r) = 1 - 2GM/r + \gamma r - \kappa r^2$ solves only the
pure $\int\sqrt{-g}C^2$ action (no EH term). Adding the EH term restores
Schwarzschild asymptotics and removes the $\gamma r$ term entirely.

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
| $\Lambda_C$ | $32\pi G\xi$ | Corrected from $64\pi G\xi$ |
| TT vacuum equation | $\Box(1 + 32\pi G\xi\,\Box)h^{\rm TT} = 0$ | This document |
| Ghost mass | $m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$ | Stelle (1977) Eq. 2.3 |
| EFT condition | $\xi < \frac{1}{4}$ | Stelle (1977) |
| Newtonian potential | $\Phi = -\frac{GM}{r}(1 - \frac{4}{3}e^{-m_2 r})$ | Stelle (1977) Eq. 2.3 |
| Trace equation | $R = -8\pi G\,T$ | Unmodified from GR |

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
| 1 | Can Tier 1 $\mathcal{C}_K$ produce linear-$r$ corrections without a ghost? | Core MOND question |
| 2 | Linearised perturbations around Schwarzschild in CODA Tier 2 | Strong-field corrections |
| 3 | Cauchy problem for 4th-order CODA equations | Mathematical completeness |
| 4 | Explicit PPN parameter calculation | Solar system verification |
| 5 | Cosmological tensor perturbation spectrum | CMB observables |

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

---

## 13. References

- **Stelle, K.S. (1977)** — *Phys. Rev. D* **16**, 953. All numerical results
  in this document are verified against this source: ghost mass (Eq. 2.3),
  Newtonian potential (Eq. 2.3), Weyl identity (Appendix Eq. A5),
  $\kappa^2$ convention (Eq. 2.1).
- Mannheim, P.D. & Kazanas, D. (1989) — Exact solution of pure conformal gravity
- Lu, H., Perkins, A., Pope, C.N. & Stelle, K.S. (2015) — Non-Schwarzschild BHs

---

*End of document. Version 0.2.*  
*Next: `phenomenology/mond_thread.md` — MOND thread reconstruction via Tier 1.*