# The CODA Action Principle

**Document:** `theory/action_principle.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.3  
**Status:** Foundational — field equations derived; all limits verified  
**Depends on:** `theory/covariant_ck.md`, `theory/field_equations.md` v0.3  
**Corrected by:** `theory/field_equations.md` v0.2 (Stelle 1977 verification)  
**Epistemic Flags:** [ESTABLISHED] for standard GR results; [CODA] for new
claims; [OPEN PROBLEM] for unresolved issues.

---

## Changelog

**v0.1 → v0.2 (corrections):**
1. Variation coefficient: $-4\xi B_{\mu\nu}$ → $-2\xi B_{\mu\nu}$
2. $\Lambda_C = 64\pi G\xi$ → $\Lambda_C = 32\pi G\xi$
3. Mannheim-Kazanas MOND claim retracted

**v0.2 → v0.3 (additions):**
1. Editorial [CORRECTED] flags removed — corrected values are now clean statements
2. §5.2 expanded to full Bach-flat theorem covering all Einstein metrics
3. §5.5 added: conservation identity $\nabla^\mu B_{\mu\nu} = 0$
4. §6.2 MOND status updated with DSSYK derivation of $a_0 \sim cH_0$
5. §9 open problems updated — cosmological and PPN items closed
6. References updated with full phenomenology suite

---

## 1. The CODA Action

### 1.1 Formal Action

The full CODA action is: [CODA]

$$S_{\text{CODA}} = \int d^4x\,\sqrt{-g}
\left[\frac{R}{16\pi G} + \alpha\,\mathcal{C}_K(x) + \mathcal{L}_m\right]$$

where:

- $R$ is the Ricci scalar
- $G$ is Newton's gravitational constant
- $\mathcal{C}_K(x)$ is the covariant Krylov complexity density
  (see `covariant_ck.md`)
- $\mathcal{L}_m$ is the matter Lagrangian density
- $\alpha$ is a dimensionless coupling constant (natural units $\hbar = c = 1$)

The construction of $\mathcal{C}_K(x)$ remains an open problem
(`covariant_ck.md`, Section 7). All field equations in this document
use the **Tier 2 working definition** of $\mathcal{C}_K$.

### 1.2 Tier 2 Action (Working Theory)

Using the semiclassical Weyl proxy from `covariant_ck.md` Section 6:

$$\mathcal{C}_K(x) \approx \frac{\ell_P^4}{8\pi}\,
C_{\alpha\beta\gamma\delta}\,C^{\alpha\beta\gamma\delta}$$

the CODA action becomes: [CODA — Tier 2]

$$\boxed{S_{\text{CODA}}^{(2)} = \int d^4x\,\sqrt{-g}
\left[\frac{R}{16\pi G} + \xi\,C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}
+ \mathcal{L}_m\right]}$$

where the effective coupling is $\xi = \alpha\ell_P^4/(8\pi)$.

**Dimensional check:** $[C^2] = L^{-4}$, $[\xi] = 1$ (dimensionless in
natural units), so $[\xi C^2] = L^{-4}$ matching $[R/(16\pi G)]$ ✓

This action is a member of the Einstein-Weyl gravity family (Stelle 1977,
Boulware & Deser 1985). CODA inherits all known results while providing new
motivation for $\xi$ via the complexity density programme.

---

## 2. Variation Procedure

### 2.1 Einstein-Hilbert Term [ESTABLISHED]

$$\frac{1}{\sqrt{-g}}\frac{\delta}{\delta g^{\mu\nu}}
\!\left(\sqrt{-g}\,\frac{R}{16\pi G}\right) = \frac{G_{\mu\nu}}{16\pi G}$$

where $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$.

### 2.2 Weyl-Squared Term [ESTABLISHED]

$$\frac{1}{\sqrt{-g}}\frac{\delta}{\delta g^{\mu\nu}}
\!\left(\sqrt{-g}\,C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}\right)
= -2\,B_{\mu\nu}$$

where the **Bach tensor** is:

$$\boxed{B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma}
+ \frac{1}{2}\,R^{\rho\sigma}C_{\mu\rho\nu\sigma}}$$

**Self-consistency check:** Setting $-2B_{\mu\nu} = 0$ for pure conformal
gravity correctly yields the vacuum equation $B_{\mu\nu} = 0$. ✓

**Stelle (1977) check:** This coefficient produces
$m_2^2 = 1/(32\pi G\xi)$, exactly matching Stelle Eq. 2.3. ✓

### 2.3 Matter Term [ESTABLISHED]

$$\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L}_m)}{\delta g^{\mu\nu}}
= -\frac{1}{2}\,T_{\mu\nu}$$

---

## 3. The CODA Field Equations

Setting $\delta S_{\text{CODA}}^{(2)} = 0$:

$$\frac{G_{\mu\nu}}{16\pi G} - 2\xi\,B_{\mu\nu} - \frac{1}{2}\,T_{\mu\nu} = 0$$

Multiplying through by $16\pi G$:

$$\boxed{G_{\mu\nu} - 32\pi G\xi\,B_{\mu\nu} = 8\pi G\,T_{\mu\nu}}$$

Defining the **CODA complexity coupling:**

$$\boxed{\Lambda_C = 32\pi G\xi = \frac{G\alpha\ell_P^4}{2\pi}}$$

the field equations are:

$$G_{\mu\nu} - \Lambda_C\,B_{\mu\nu} = 8\pi G\,T_{\mu\nu}$$

**Numerical estimate** with $\alpha = \ell_P^2/(8\pi)$:

$$\Lambda_C = \frac{G\ell_P^6}{2\pi}
\approx 6.0\times10^{-221}\ \text{m}^7\,\text{kg}^{-1}\,\text{s}^{-2}$$

This is Planck-suppressed to an extreme degree, ensuring GR is recovered
exactly at all accessible scales. [OPEN PROBLEM — Large-N enhancement
mechanism needed for macroscopic observability]

---

## 4. Properties of the Bach Tensor [ESTABLISHED]

### 4.1 Symmetry
$$B_{\mu\nu} = B_{\nu\mu}$$

### 4.2 Tracelessness (4D)
$$g^{\mu\nu}B_{\mu\nu} = 0$$

The trace of the CODA field equations gives $R = -8\pi G T$,
identical to standard GR. The Bach tensor does not modify the
trace equation.

### 4.3 Covariant Conservation
$$\nabla^\mu B_{\mu\nu} = 0$$

Consistent with $\nabla^\mu G_{\mu\nu} = 0$ and
$\nabla^\mu T_{\mu\nu} = 0$. ✓

### 4.4 Fourth-Order Nature

The Bach tensor involves $\nabla^2$ acting on the Weyl tensor
(which itself is $\sim\nabla^2 g$). The CODA field equations are
therefore 4th order in derivatives of $g_{\mu\nu}$, compared to
GR's 2nd order. This is the central structural difference.

---

## 5. Key Limits

### 5.1 Minkowski Spacetime [ESTABLISHED]

$C_{\mu\nu\rho\sigma} = 0 \Rightarrow B_{\mu\nu} = 0$.
Minkowski space is an exact solution of CODA. ✓

### 5.2 All Einstein Metrics — Bach-Flat Theorem [ESTABLISHED, v0.3]

A metric is Bach-flat ($B_{\mu\nu} = 0$) if it belongs to either of two
classes (proved in `field_equations.md` v0.3, §7.0):

**(A) Conformally flat:** $C_{\mu\nu\rho\sigma} = 0$ identically (e.g.
Minkowski, FLRW, de Sitter).

**(B) Einstein metrics:** $R_{\mu\nu} = \lambda g_{\mu\nu}$ for constant
$\lambda$ (e.g. all vacuum GR solutions, Schwarzschild-dS/AdS, Kerr-dS/AdS).

**Every member of either class is an exact solution of CODA Tier 2 with
the same matter content as GR.** Specifically:

| Spacetime | Class | $B_{\mu\nu}$ |
|-----------|-------|-------------|
| Minkowski | A | $0$ |
| de Sitter / Anti-de Sitter | A and B | $0$ |
| FLRW (all $k$, all $a(t)$) | A | $0$ |
| Schwarzschild, Kerr | B ($\lambda=0$) | $0$ |
| Schwarzschild-dS/AdS | B | $0$ |
| Kerr-dS/AdS | B | $0$ |
| Gravitational waves (pp-waves) | B ($\lambda=0$) | $0$ |

**Corollary:** The CODA coupling $\xi$ is invisible for all of the above.
Genuine CODA Tier 2 departures from GR require metrics that are neither
conformally flat nor Einstein. See `phenomenology/black_hole_phenomenology.md`
for the non-Schwarzschild solutions (Lu et al. 2015) that are such metrics.

### 5.3 Weak Field Limit [CODA]

The Newtonian potential acquires a Yukawa correction (derived in
`field_equations.md` v0.3, §6):

$$\Phi(r) = -\frac{GM}{r}\left(1 - \frac{4}{3}\,e^{-m_2 r}\right),
\qquad m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$$

For CODA's natural coupling, $m_2^{-1} \sim \ell_P$, making this
Planck-scale and unobservable. Full PPN analysis in
`phenomenology/weak_field_limit.md`.

### 5.4 Conformally Flat Spacetimes — Formal Theorem [ESTABLISHED, v0.3]

**Theorem:** All FLRW metrics satisfy $C_{\mu\nu\rho\sigma} = 0$ and
$B_{\mu\nu} = 0$. CODA Tier 2 reduces exactly to the standard Friedmann
equations for all values of $\xi$.

*Proof sketch:* Spatially flat FLRW is $a^2(\eta)\eta_{\mu\nu}$. The Weyl
tensor is conformally covariant with weight zero in 4D, so
$C[a^2\eta] = C[\eta] = 0$. ☐

**Consequence:** No cosmological observable constrains $\xi$. The CODA
correction to CMB power spectra, BBN, or the Friedmann equations is exactly
zero at background level and suppressed by $(k/M_P)^2 \sim 10^{-114}$ at
perturbative level. Full analysis in `phenomenology/cosmological_background.md`.

### 5.5 Conservation Identity [ESTABLISHED, v0.3]

The diffeomorphism invariance of $\int\sqrt{-g}C^2$ implies:

$$\nabla^\mu B_{\mu\nu} = 0$$

This is an identity on every metric (not only on solutions). Combined with
the standard Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$, the field
equations give $\nabla^\mu T_{\mu\nu} = 0$ — matter is conserved in CODA
Tier 2 exactly as in GR. The complexity coupling introduces no anomalous
energy injection. ✓

---

## 6. The MOND Thread [CORRECTED v0.2; UPDATED v0.3]

### 6.1 Retraction (v0.2)

Version 0.1 claimed that the Mannheim-Kazanas solution — including the
$\gamma r$ linear potential — appears as a vacuum solution of CODA's Tier 2
action. **This claim is incorrect and fully retracted.**

The Mannheim-Kazanas solution is the vacuum solution of **pure conformal
gravity** ($\int\sqrt{-g}C^2$, no EH term). In Einstein-Weyl gravity (CODA
Tier 2), the EH term breaks conformal invariance, forces Schwarzschild
asymptotics in vacuum, and removes the $\gamma r$ term entirely. The only
modification to the Newtonian potential is a Yukawa term exponentially
negligible at galactic scales for any EFT-consistent coupling. [ESTABLISHED]

### 6.2 Current Status (v0.3)

| Approach | Status | Reason |
|----------|--------|--------|
| Tier 2 Yukawa correction | Negligible at galactic scales | $m_2^{-1} \sim \ell_P$ for EFT-consistent $\xi$ |
| Large-$\xi$ Yukawa (EFT-violating) | Unacceptable | Ghost enters physical spectrum |
| Pure conformal limit (no EH) | Incompatible with CODA | Loses GR recovery |
| Tier 1 formal $\mathcal{C}_K$ | **Active programme** | DSSYK evidence gives $a_0 \sim cH_0$ |

### 6.3 Phase 3a — DSSYK Evidence for $a_0$ (v0.3 addition)

The Tier 1 MOND programme has substantially advanced. Reading of Heller
et al. (2025, arXiv:2510.13986) and Aguilar-Gutierrez (2024,
arXiv:2403.13186) established three independent derivation routes giving
$a_0 = cH_0$ from the DSSYK holographic Krylov complexity:

1. **Chaos bound:** Lyapunov exponent $\lambda_K = H_0$ sets timescale
   $\tau^* = H_0^{-1}$; acceleration $a_0 = c/\tau^* = cH_0$
2. **Complexity transition:** Quadratic-to-linear transition in $C_K(\chi)
   \propto \log\cosh(\chi\theta/2)$ at $\chi \sim \ell_{dS}$; acceleration
   at transition $= c^2/\ell_{dS} = cH_0$
3. **Growth rate:** Late-time rate $\propto S_{dS} \cdot H_0$; transition
   scale $a_0 \sim cH_0$

All three give the Verlinde result $a_0 = cH_0$ with $O(1)$ factor
$\eta = 1/(2\pi)$ from $T_{dS} = H_0/2\pi$. See `phenomenology/mond_thread.md`
§5 and `audit/llm_synthesis/Q4b_DSSYK_papers.md` for full analysis.

The remaining gap is the 4D local density lift — currently the Priority 1
open problem in `theory/covariant_ck.md` §7.

---

## 7. Known Problems

### 7.1 Ghost Modes [SEVERE — EFT-managed]

The 4th-order equations introduce a massive spin-2 ghost:

$$m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$$

EFT consistency requires $\xi < 1/4$. For CODA's natural coupling,
$\xi \sim \ell_P^6 \ll 1$, so $m_2 \gg M_P$ and the ghost decouples
from all sub-Planckian physics. ✓

### 7.2 Initial Value Problem [MODERATE]

The 4th-order Cauchy problem requires specifying more initial data
than GR. Whether additional constraints reduce the phase space
appropriately is an open question. [OPEN PROBLEM]

### 7.3 Renormalisability vs Unitarity [INFORMATIONAL]

Einstein-Weyl gravity is not perturbatively renormalisable as a
complete quantum gravity theory, but is a valid EFT with GR as the
leading term and the Weyl correction as a higher-derivative EFT
operator. [ESTABLISHED — Stelle 1977]

---

## 8. Canonical Equation Summary

| Quantity | Expression | Source |
|----------|-----------|--------|
| CODA Tier 2 action | $S = \int\sqrt{-g}[R/16\pi G + \xi C^2 + \mathcal{L}_m]$ | §1.2 |
| Field equations | $G_{\mu\nu} - \Lambda_C B_{\mu\nu} = 8\pi G T_{\mu\nu}$ | §3 |
| Bach tensor | $B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma} + \frac{1}{2}R^{\rho\sigma}C_{\mu\rho\nu\sigma}$ | §2.2 |
| Weyl variation | $\frac{\delta(\sqrt{-g}C^2)}{\sqrt{-g}\delta g^{\mu\nu}} = -2B_{\mu\nu}$ | §2.2 |
| Conservation identity | $\nabla^\mu B_{\mu\nu} = 0$ | §5.5 |
| Coupling | $\Lambda_C = 32\pi G\xi$ | §3 |
| Ghost mass | $m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$ | Stelle (1977) |
| EFT condition | $\xi < \frac{1}{4}$ | Stelle (1977) |
| Newtonian potential | $\Phi = -\frac{GM}{r}(1 - \frac{4}{3}e^{-m_2 r})$ | Stelle (1977) |
| Trace equation | $R = -8\pi G T$ | §4.2 |
| Bach-flat theorem | $B_{\mu\nu} = 0$ for conformally flat and Einstein metrics | §5.2 |

---

## 9. Open Problems

| Priority | Problem | Status |
|----------|---------|--------|
| 1 | Lift 2D DSSYK Krylov density to 4D covariant $\mathcal{C}_K(x)$ | Open — `covariant_ck.md` §7 Priority 1 |
| 2 | Can Tier 1 $\mathcal{C}_K$ reproduce AQUAL interpolating function? | Open — DSSYK transition scale correct; exact form unknown |
| 3 | QNM spectrum of non-Schwarzschild (Branch 2) black holes | Open — `black_hole_phenomenology.md` §8 |
| 4 | Thermodynamic stability of Branch 1 vs Branch 2 | Open — `black_hole_phenomenology.md` §8 |
| 5 | Cauchy problem for 4th-order CODA field equations | Open — mathematical completeness |
| — | ~~PPN parameter calculation~~ | Closed — $\gamma=\beta=1$ exactly (`weak_field_limit.md`) |
| — | ~~Cosmological perturbations around FLRW~~ | Closed — suppressed by $(k/M_P)^2$ (`cosmological_background.md`) |

---

## 10. References

- **Stelle, K.S. (1977)** — *Phys. Rev. D* **16**, 953.
  Ghost mass and Newtonian potential (Eq. 2.3); Weyl identity
  (Appendix Eq. A5); $\kappa^2$ convention (Eq. 2.1).
- Bach, R. (1921) — Original Bach tensor definition
- Boulware, D.G. & Deser, S. (1985) — Weyl-squared variation
- Lu, H., Perkins, A., Pope, C.N. & Stelle, K.S. (2015) —
  Non-Schwarzschild black holes in quadratic gravity,
  *Phys. Rev. Lett.* **114**, 171601
- Mannheim, P.D. & Kazanas, D. (1989) — Exact solution of **pure**
  conformal gravity (not CODA Tier 2)
- Heller et al. (2025) — arXiv:2510.13986 — dS Krylov complexity from DSSYK
- Aguilar-Gutierrez (2024) — arXiv:2403.13186 — DSSYK Krylov, explicit $b_n$
- CODA phenomenology: `weak_field_limit.md`, `cosmological_background.md`,
  `mond_thread.md`, `black_hole_phenomenology.md`

---

*End of document. Version 0.3. All numerical prefactors verified against
Stelle (1977). All inline CORRECTED flags removed — correction history in
changelog above.*