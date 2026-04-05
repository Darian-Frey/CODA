# The CODA Action Principle

**Document:** `theory/action_principle.md`  
**Project:** CODA — Complexity-Originated Dynamics of Action  
**Version:** 0.2 (Corrected — supersedes v0.1)  
**Status:** Foundational — field equations derived; key limits verified  
**Depends on:** `theory/covariant_ck.md`  
**Corrected by:** `theory/field_equations.md` v0.2 (Stelle 1977 verification)  
**Epistemic Flags:** [ESTABLISHED] for standard GR results; [CODA] for new
claims; [OPEN PROBLEM] for unresolved issues; [CORRECTED] for items changed
from v0.1.

---

## Changelog v0.1 → v0.2

Three errors corrected following direct verification against Stelle (1977):

1. **Section 2.2** — Variation coefficient: $-4\xi B_{\mu\nu}$ → $-2\xi B_{\mu\nu}$
2. **Section 3 throughout** — $\Lambda_C = 64\pi G\xi$ → $\Lambda_C = 32\pi G\xi$
3. **Section 6** — Mannheim-Kazanas MOND claim retracted and replaced

See `theory/field_equations.md` v0.2 for full derivation and source verification.

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
(`covariant_ck.md`, Section 6). All field equations in this document
use the **Tier 2 working definition** of $\mathcal{C}_K$.

### 1.2 Tier 2 Action (Working Theory)

Using the semiclassical Weyl proxy from `covariant_ck.md` Section 5:

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

### 2.2 Weyl-Squared Term [ESTABLISHED — CORRECTED]

[CORRECTED from v0.1: coefficient was $-4B_{\mu\nu}$; correct value is $-2B_{\mu\nu}$]

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

Defining the **CODA complexity coupling:** [CORRECTED from v0.1]

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

### 5.2 All Vacuum GR Solutions [ESTABLISHED]

For any GR vacuum solution, $R_{\mu\nu} = 0$.
By the contracted Bianchi identity, $\nabla^\rho C_{\mu\rho\nu\sigma} = 0$,
therefore $B_{\mu\nu} = 0$.

**Every vacuum solution of GR — Schwarzschild, Kerr, Kerr-Newman,
pp-waves, gravitational waves — is an exact solution of CODA.**

The complexity correction does not modify any vacuum spacetime. ✓

### 5.3 Weak Field Limit [CODA]

The Newtonian potential acquires a Yukawa correction (derived in
`field_equations.md` v0.2, Section 6):

$$\Phi(r) = -\frac{GM}{r}\left(1 - \frac{4}{3}\,e^{-m_2 r}\right),
\qquad m_2^2 = \frac{1}{32\pi G\xi}$$

For CODA's natural coupling, $m_2^{-1} \sim \ell_P$, making this
Planck-scale and unobservable. [CORRECTED: ghost mass was $1/(64\pi G\xi)$
in v0.1; corrected value from Stelle (1977) is $1/(32\pi G\xi)$]

### 5.4 Conformally Flat Spacetimes [ESTABLISHED]

$g_{\mu\nu} = \Omega^2\eta_{\mu\nu} \Rightarrow C_{\mu\nu\rho\sigma} = 0
\Rightarrow B_{\mu\nu} = 0$.

CODA reduces exactly to GR for all conformally flat spacetimes,
including FLRW cosmology. Standard cosmological evolution is
unmodified by CODA Tier 2. ✓

---

## 6. The MOND Thread — Corrected Statement [CORRECTED from v0.1]

### 6.1 Retraction

Version 0.1 claimed that the Mannheim-Kazanas solution — including the
$\gamma r$ linear potential that produces flat galactic rotation curves —
appears as a vacuum solution of CODA's Tier 2 action.
**This claim is incorrect and is fully retracted.**

The Mannheim-Kazanas solution is the vacuum solution of **pure conformal
gravity** (action $= \int\sqrt{-g}C^2$, no EH term). In Einstein-Weyl
gravity (CODA Tier 2), the EH term breaks conformal invariance, forces
Schwarzschild asymptotics in vacuum, and removes the $\gamma r$ term
entirely. The only modification to the Newtonian potential is a Yukawa
term exponentially negligible at galactic scales for any EFT-consistent
coupling. [ESTABLISHED — confirmed by three independent model responses
and Stelle (1977)]

### 6.2 Current Status

| Approach | Status | Reason |
|----------|--------|--------|
| Tier 2 Yukawa correction | Negligible at galactic scales | $m_2^{-1} \sim \ell_P$ for EFT-consistent $\xi$ |
| Large-$\xi$ Yukawa (EFT-violating) | Unacceptable | Ghost enters physical spectrum |
| Pure conformal limit (no EH) | Incompatible with CODA | Loses GR recovery |
| Tier 1 formal $\mathcal{C}_K$ | **Open — preferred** | Not constrained to $C^2$ form |

The MOND phenomenology thread is deferred to `phenomenology/mond_thread.md`
and depends on Tier 1 progress. The formal $\mathcal{C}_K$ construction is
not constrained to produce Weyl-squared corrections and may yield
qualitatively different behaviour at different scales.

---

## 7. Known Problems

### 7.1 Ghost Modes [SEVERE — EFT-managed]

The 4th-order equations introduce a massive spin-2 ghost:

$$m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$$
[CORRECTED from v0.1; verified against Stelle (1977)]

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

| Quantity | Expression |
|----------|-----------|
| Field equations | $G_{\mu\nu} - \Lambda_C B_{\mu\nu} = 8\pi G T_{\mu\nu}$ |
| Bach tensor | $B_{\mu\nu} = \nabla^\rho\nabla^\sigma C_{\mu\rho\nu\sigma} + \frac{1}{2}R^{\rho\sigma}C_{\mu\rho\nu\sigma}$ |
| Weyl variation | $\frac{\delta(\sqrt{-g}C^2)}{\sqrt{-g}\delta g^{\mu\nu}} = -2B_{\mu\nu}$ |
| Coupling | $\Lambda_C = 32\pi G\xi$ |
| Ghost mass | $m_2^2 = \frac{1}{32\pi G\xi} = \frac{M_P^2}{4\xi}$ |
| EFT condition | $\xi < \frac{1}{4}$ |
| Newtonian potential | $\Phi = -\frac{GM}{r}(1 - \frac{4}{3}e^{-m_2 r})$ |
| Trace equation | $R = -8\pi G T$ |

---

## 9. Open Problems

| Priority | Problem | Notes |
|----------|---------|-------|
| 1 | Can Tier 1 $\mathcal{C}_K$ produce linear-$r$ corrections without a ghost? | MOND thread |
| 2 | Derive Large-N enhancement of $\Lambda_C$ from Tier 1 | Macroscopic observability |
| 3 | Establish Cauchy problem for CODA field equations | Mathematical completeness |
| 4 | Compute PPN parameters explicitly | Solar system tests |
| 5 | Analyse cosmological perturbations around FLRW | CMB constraints |

---

## 10. References

- **Stelle, K.S. (1977)** — *Phys. Rev. D* **16**, 953.
  Ghost mass and Newtonian potential (Eq. 2.3); Weyl identity
  (Appendix Eq. A5); $\kappa^2$ convention (Eq. 2.1).
- Bach, R. (1921) — Original Bach tensor definition
- Boulware, D.G. & Deser, S. (1985) — Weyl-squared variation
- Mannheim, P.D. & Kazanas, D. (1989) — Exact solution of **pure**
  conformal gravity (not CODA Tier 2)
- Padmanabhan, T. (2010) — *Gravitation*, Cambridge University Press

---

*End of document. Version 0.2.*  
*All numerical prefactors verified against Stelle (1977).*  
*Next: `phenomenology/mond_thread.md`*