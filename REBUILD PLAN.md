# Atlas Rebuild Plan — Book-Anchored Curriculum

**Trigger**: User uploaded 3 canonical texts (Hammack, Apostol I, Apostol II) and requested atlas rebuild anchored to these sources. Atlas becomes single source of truth (no book reading alongside), so lessons must be textbook-complete.

**Source PDFs** (local, gitignored, private):
- `References/Pure Math/Hammack - Book of Proof.pdf` (380 pages)
- `References/Pure Math/Apostol - Calculus Vol I.pdf` (686 pages)
- `References/Pure Math/Apostol - Calculus Vol II.pdf` (696 pages)

---

## Design principles (v2 — includes v0.1 L0 refinements)

1. Content in English, chat in Vietnamese
2. MFE-rigor (proofs + intuition + worked examples)
3. Concept IDs stable forever
4. Learning Outcomes (Bloom's taxonomy) at top of every lesson — **plus** "Why must you learn this?" motivation box with 4 quadrants: (a) Immediate use in this atlas, (b) Use in quant work, (c) Use in interviews, (d) Long-run payoff
5. Function families / concept families broken down: general form + description + domain/range + key property + application
6. Arrow diagrams for concepts, flow for composition, pseudocode before Python
7. Code corner as collapsible optional section
8. Atlas is single source of truth — lessons textbook-complete, no "see book X for details"
9. **NEW v0.1**: Each § starts with a mini "Why §N?" box (3 lines: what you'll learn / used later in this atlas / used in quant)
10. **NEW v0.1**: Cross-references between sections are hyperlinks (`<a href="#sN" class="xref">§N Title</a>`). Referenced target section has a `backlink-note` at top listing which sections cite it.
11. **NEW v0.1**: Each § ends with a `sec-nav` footer: `← §prev  |  ↑ Top  |  §next →`

---

## Book → Concept mapping

### Hammack Book of Proof → **L0 Proof Techniques** (new lesson)

| Hammack Ch | L0 Section | Priority |
|---|---|---|
| 1. Sets | §1 Sets & Set Operations | Must |
| 2. Logic | §2 Logic, Quantifiers, Truth Tables | Must |
| 3. Counting | §3 Counting Principles | Nice |
| 4. Direct Proof | §4 Direct Proof + Definitions | Must |
| 5. Contrapositive Proof | §5 Contrapositive Proof | Must |
| 6. Proof by Contradiction | §6 Proof by Contradiction | Must |
| 7. Non-Conditional | §7 Iff, Existence, Uniqueness Proofs | Must |
| 8. Proofs Involving Sets | §8 Set Proofs (∈, ⊆, =) | Must |
| 9. Disproof | §9 Counterexamples & Disproof | Must |
| 10. Induction | §10 Mathematical Induction (weak, strong, well-ordering) | Must |
| 11. Relations | §11 Relations & Equivalence Classes | Must |
| 12. Functions | Redirects to L1 (already covered) | — |
| 13. Proofs in Calculus | Redirects to L2 (limit ε-δ, sequences, series) | — |
| 14. Cardinality | §12 Cardinality: Countable vs Uncountable | Must (bridges to measure theory) |

**Estimated size**: ~600KB HTML, 12 sections, 25+ theorems with full proofs, 40+ worked examples, 30+ exercises with solutions.

### Apostol Vol I → Rebuild + Extend Math Foundations (L1-L11)

| Apostol I Ch | Current Atlas | Action |
|---|---|---|
| I. Real Number Axioms | (missing) | **NEW**: fold into L0 §0 or new L0.5 lesson |
| I. Induction | Covered in L0 §10 | Link L0 |
| I. Triangle Inequality | Covered in L0 §11 (Hammack Ch 13) | Link L0 |
| 1-2. Integral Calculus | L4 (planned) | **Rebuild L4** with Apostol integration-first sequence |
| 3. Continuous Functions | L2 (exists) | **Enrich L2** with Apostol Ch 3 proofs (basic limit theorems, IVT, EVT, uniform continuity, integrability) |
| 4. Differential Calculus | L3 (planned) | **Build L3** from Apostol Ch 4 |
| 5. FTC | L3-L4 bridge | Add to L4 |
| 6. Log/Exp/Inverse Trig | L1 (mentioned) or new L5 | **Build L5 Elementary Transcendental Functions** |
| 7. Taylor Polynomials | L6 (new) | **Build L6 Polynomial Approximations** |
| 8. Intro ODEs | L9 ODEs (planned) | **Build L9 First-order + Second-order Linear ODEs** |
| 9. Complex Numbers | (missing) | **NEW**: L7 Complex Numbers |
| 10. Sequences, Series, Improper Integrals | L8 (planned) | **Build L8 Sequences & Series** |
| 11. Sequences/Series of Functions | L8 subsection | Fold into L8 (uniform convergence) |
| 12-13. Vectors + Analytic Geometry | Linear Algebra pillar | Fold into new **LA1 Vector Spaces** |
| 14. Vector-Valued Functions | L10 (new) | **Build L10 Vector-Valued Functions & Curves** |
| 15. Linear Spaces | **LA1 Linear Spaces** | Build from Apostol II Ch 1 (more comprehensive) |
| 16. Linear Transformations | **LA2 Linear Transformations & Matrices** | Build |

### Apostol Vol II → Advanced Math (LA1-LA4, MV1-MV3, ODE2-ODE3)

**Part 1 Linear Algebra**:
- Ch 1-2 → **LA1** Linear Spaces + **LA2** Linear Transformations & Matrices
- Ch 3 → **LA3** Determinants
- Ch 4 → **LA4** Eigenvalues & Eigenvectors
- Ch 5 → **LA5** Symmetric Operators & Quadratic Forms
- Ch 6 → **ODE2** nth-order Linear ODEs (Legendre, Bessel)
- Ch 7 → **ODE3** Systems of ODEs (matrix exponential — critical for stochastic models)

**Part 2 Multivariable Calculus**:
- Ch 8 → **MV1** Differential Calculus of Scalar & Vector Fields
- Ch 9 → **MV2** Applications (extrema, Lagrange multipliers, PDE intro)
- Ch 10 → **MV3** Line Integrals
- Ch 11 → **MV4** Multiple Integrals + Green's Theorem
- Ch 12 → **MV5** Surface Integrals + Stokes + Divergence

**Part 3 Special Topics**:
- Ch 13-14 → mostly covered in Probability pillar (existing) — reference Apostol as source

---

## New atlas structure (revised — NO parallel structures)

**Principle**: Apostol/Hammack are SOURCES, not blueprints. Keep the original 1-tier lesson structure. Add L0 (proof, new), extend to L12 with missing pieces. Do NOT create parallel LA1-LA5 or MV1-MV5 — that would duplicate Apostol's TOC unnecessarily.

Math Foundations pillar — 12-13 concepts, one tier only:

| Concept ID | Lesson | Primary source | Status |
|---|---|---|---|
| `math-proof` | **L0** Proof Techniques | Hammack Ch 1-11, 14 | NEW |
| `math-functions` | **L1** Functions & Real Number System | Apostol I Intro + Ch 1 + Hammack Ch 12 | REBUILD (v1 exists) |
| `math-limits` | **L2** Limits & Continuity | Apostol I Ch 3 + Hammack Ch 13 | ENRICH (v1 exists) |
| `math-derivatives` | **L3** Differential Calculus | Apostol I Ch 4 | NEW |
| `math-integrals` | **L4** Integral Calculus | Apostol I Ch 1-2, 5 | NEW |
| `math-elementary-fns` | **L5** Elementary Transcendentals (log, exp, trig) | Apostol I Ch 6 | NEW |
| `math-taylor` | **L6** Taylor Polynomials & Approximations | Apostol I Ch 7 | NEW |
| `math-complex` | **L7** Complex Numbers | Apostol I Ch 9 | NEW (was missing) |
| `math-series` | **L8** Sequences, Series, Improper Integrals | Apostol I Ch 10-11 | NEW |
| `math-odes` | **L9** Ordinary Differential Equations | Apostol I Ch 8 + Apostol II Ch 6-7 | NEW |
| `math-linear-algebra` | **L10** Linear Algebra | Apostol I Ch 15-16 + Apostol II Ch 1-5 | NEW (may split into L10a/L10b if > 800KB) |
| `math-multivar` | **L11** Multivariable Calculus | Apostol II Ch 8-12 | NEW (may split L11a diff / L11b integrals) |
| `math-vector-valued` | **L12** Vector-Valued Functions & Curves (optional) | Apostol I Ch 14 | NEW |

**Total: 12-13 lessons**, no duplicates. Split/fold decisions per lesson at build time (target 300-800KB HTML per file).

**No new pillars added**. Everything under existing Math Foundations pillar.

---

## Phased build plan

### Phase 1: L0 Proof Techniques ⭐ START HERE
**Sessions**: 1-2 chats
**Deliverable**: `lessons/proof-techniques.html` — comprehensive L0 lesson
**Prerequisite**: none (entry point)
**Source**: Hammack Ch 1-11, 14
**Includes**:
- 12 sections covering all proof techniques
- 25+ theorems with full formal proofs
- 40+ worked examples with commentary
- 30+ exercises with complete solutions
- Learning Outcomes (Bloom's)
- Code corner: proof checkers in Python (optional)
- References: Hammack citations with page numbers

**After Phase 1**:
- Add `math-proof` node to Math Foundations pillar
- Wire prerequisite edges: L0 → L1, L0 → L2
- Update Quant-Roadmap.html PILLARS array
- Update references in L1 + L2 to link back to L0

### Phase 2: L0.5 Real Number System + Rebuild L1, L2
**Sessions**: 2-3 chats
**Deliverable**: `lessons/real-numbers.html` (NEW), rebuild `lessons/functions.html`, `lessons/limits.html`
**Source**: Apostol I Introduction + Ch 3
**Focus**:
- L0.5: field axioms, order axioms, completeness (LUB), Archimedean property, decimal representations
- L1 rebuild: Apostol-level rigor for functions
- L2 enrich: add Apostol Ch 3 proofs (basic limit theorems, IVT, EVT, uniform continuity, integrability of continuous functions)

### Phase 3: L3-L8 Single-Variable Calculus
**Sessions**: 4-6 chats
**Deliverable**: `lessons/derivatives.html`, `integrals.html`, `elementary-functions.html`, `taylor.html`, `complex-numbers.html`, `series.html`
**Source**: Apostol I Ch 4-11

### Phase 4: L9 ODEs + L10 Linear Algebra
**Sessions**: 3-4 chats
**Source**: Apostol I Ch 8 + Apostol II Part 1 & Ch 6-7
**Note**: L10 may split into L10a Linear Spaces + L10b Eigenvalues if content exceeds 800KB

### Phase 5: L11 Multivariable + L12 Vector-Valued
**Sessions**: 3-4 chats
**Source**: Apostol I Ch 14 + Apostol II Part 2
**Note**: L11 likely splits into L11a Diff (Ch 8-9) + L11b Integrals (Ch 10-12)

---

## Bootstrap prompt for each Phase chat

Paste into new Claude chat (project = Quant Practice):

```
Read D:\OneDrive\1. Quant\Quant-Practice\UPDATE MINDMAP.md and
D:\OneDrive\1. Quant\Quant-Practice\UPDATE PROGRESS.md and
D:\OneDrive\1. Quant\Quant-Practice\REBUILD PLAN.md first.

Today I want to execute: [Phase X — describe deliverable]

Source book chapters are in D:\OneDrive\1. Quant\Quant-Practice\References\Pure Math\
- Hammack - Book of Proof.pdf
- Apostol - Calculus Vol I.pdf
- Apostol - Calculus Vol II.pdf

Read only the specific chapters listed in REBUILD PLAN.md for this phase
to conserve tokens. Do not read whole books.

Rules (also in UPDATE MINDMAP.md):
- Atlas = single source of truth. Every lesson textbook-complete.
  No "see book for details", no "left as exercise".
- Content in English, chat in Vietnamese
- MFE-rigor with full proofs + intuition + worked examples
- Concept IDs stable, never rename
- Never touch *.notes.md, backup/, Notebooks/, PDF/, Data/, References/
- After ANY build, remind me to (1) commit+push code, (2) export progress
  JSON, (3) update REBUILD PLAN.md if scope changed
```

---

## Progress tracking

As phases complete, update this table:

| Phase | Deliverable | Status | Notes |
|---|---|---|---|
| 1 | L0 Proof Techniques | ⏳ Not started | Hammack Ch 1-11, 14 |
| 2 | Rebuild L1 (fold Real Numbers) + Enrich L2 | ⏳ | Apostol I Intro + Ch 1, 3 + Hammack Ch 12-13 |
| 3 | L3-L8 Single-var calculus | ⏳ | Apostol I Ch 4-11 |
| 4 | L9 ODEs + L10 Linear Algebra | ⏳ | Apostol I Ch 8, 15-16 + Apostol II Part 1, Ch 6-7 |
| 5 | L11 Multivariable + L12 Vector-Valued | ⏳ | Apostol I Ch 14 + Apostol II Part 2 |

---

## Estimates & timeline (revised — smaller scope, no parallel structures)

- Total build time (Claude): 60-90 hours across 10-14 chat sessions
- Realistic pace: 1-2 phases per week (assuming user has time to study between)
- Full rebuild timeline: **~3-4 months** from today

Deliverable count: **12-13 lesson files**, not 30+.

Study alongside build: after each phase completes, user should:
1. Study new lessons for 1-2 weeks
2. Mark mastery progress
3. Export JSON weekly
4. Note pain points → feed back in next phase chat

---

*Last updated: 2026-08-01 — initial rebuild plan based on Hammack + Apostol I & II uploads*
