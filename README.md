# Eight new lower bounds for multicolour classical Ramsey numbers, and an Atlas of lower bounds

Julien Courties, November 2026.

**Abstract.** We give explicit edge colourings (or, for the two largest, explicit recipes) that improve the best lower bounds known to us for eight multicolour classical Ramsey numbers, and we publish an *Atlas* of lower bounds for 6,426 parameter sets R(k<sub>1</sub>,…,k<sub>r</sub>) (2 to 7 colours, limits up to 10) together with a three-colour extension up to limits 15. Six of the eight colourings are verified exhaustively by programs that are independent of the programs that found them. The constructions combine F. Rowley's template-and-atom composition, the quadrupling of Xu, Xie, Exoo and Radziszowski, circulant colourings found by SAT, and one non-linear colouring found by tabu search.

## 1. Results

R(k<sub>1</sub>,…,k<sub>r</sub>) is the least N such that every r-colouring of the edges of K<sub>N</sub> contains, for some i, a monochromatic K<sub>k<sub>i</sub></sub> in colour i. A colouring of K<sub>N</sub> in which colour i contains no K<sub>k<sub>i</sub></sub> for every i proves R(k<sub>1</sub>,…,k<sub>r</sub>) ≥ N + 1.

| Number | New bound | Order N of the colouring | Previous best known to us | Certificate | Verified |
| --- | --- | --- | --- | --- | --- |
| R(3,5,5) | **≥ 140** | 139 | 139 (published, Radziszowski rev. 18, Table XIb) | [`R_3_5_5_n139_firstrow.txt`](records/R_3_5_5_n139_firstrow.txt) | exhaustive |
| R(3,5,6) | **≥ 192** | 191 | 181 (published, Table XIb) | [`R_3_5_6_n191_firstrow.txt`](records/R_3_5_6_n191_firstrow.txt) | exhaustive |
| R(3,5,7) | **≥ 267** | 266 | 241 (published, Table XIb) | [`R_3_5_7_n266_firstrow.txt`](records/R_3_5_7_n266_firstrow.txt) | exhaustive |
| R(4,5,5) | **≥ 241** | 240 | 217 (deduced from published values by quadrupling; no value published for these exact parameters) | [`R_4_5_5_n240_matrix.txt`](records/R_4_5_5_n240_matrix.txt) (matrix) | exhaustive |
| R(3,4,5,5) | **≥ 770** | 769 | 729 (Rowley 2022, arXiv:2203.13476; survey) | [`R_3_4_5_5_n769_firstrow.txt`](records/R_3_4_5_5_n769_firstrow.txt) | exhaustive |
| R(3,4,5,6) | **≥ 1065** | 1064 | 865 (deduced from published values by quadrupling; no value published for these exact parameters) | [`R_3_4_5_6_n1064_matrix.txt`](records/R_3_4_5_6_n1064_matrix.txt) (matrix) | exhaustive |
| R(5,5,5,5,5) | **≥ 44,338** | 44,337 | 41,626 (survey Table XIa; Rowley 2022) | [`R_5_5_5_5_5_n44337_firstrow.txt`](records/R_5_5_5_5_5_n44337_firstrow.txt) | exhaustive (vertex 0) |
| R<sub>7</sub>(5) = R(5,5,5,5,5,5,5) | **≥ 4,344,970** | 4,344,969 | 3,974,441 (Rowley 2022, Table 2) | [`R_5x5x5x5x5x5x5_n4344969_firstrow.txt`](records/R_5x5x5x5x5x5x5_n4344969_firstrow.txt) | composition theorem (see §4) |

"Exhaustive" means that the clique search was run on the whole colouring by the verifiers of this repository. "Previous best known to us" is the best value in the tables we used; our search of the literature was not exhaustive (see §6).

## 2. Conventions

Colours are numbered 0,…,r−1 in increasing order of their limits (for R(3,4,5,6): colour 0 has no K<sub>3</sub>, colour 1 no K<sub>4</sub>, colour 2 no K<sub>5</sub>, colour 3 no K<sub>6</sub>).
A **linear** colouring on the vertices 0,…,N−1 gives the edge {i,j} the colour that depends only on |i−j|; it is stored as its **first row**: N−1 digits, the digit at position d being the colour of the length d. A **non-linear** colouring is stored as its full **matrix** (N lines of N digits, 0 on the diagonal).

## 3. Methods

**Composition (Rowley).** A *template* is a period of m−1 digits in which 0,1,… are colours of the template and `J` is a *joker*, a triangle-free length reserved for a colour of the base; φ is the number of lengths before the first joker. Composing a template with a linear colouring V on n vertices (the *base* or *atom*) gives a linear colouring on N = (m−1)(n−1) + 1 + φ vertices: for μ = 1,…,n−1 write the period once, each joker being replaced by the colour of the length μ of V, then append the first φ digits of the period. The limits of the result are those of the template followed by those of V (F. Rowley, *A generalised linear Ramsey graph construction*, Australasian J. Combin., 2021; arXiv:2203.13476, 2022). [`tools/compose.py`](tools/compose.py) is our re-implementation; [`tools/build_all.py`](tools/build_all.py) rebuilds six of the certificates from their ingredients in [`ingredients/`](ingredients/) and checks that they are identical to the stored files.

| Record | Template | Base | Origin of the ingredients |
| --- | --- | --- | --- |
| R(3,5,5) | (5,5,3 ; 99) | K<sub>2</sub> (one length) | template found by our SAT searches |
| R(3,5,6) | (5,6,3 ; 136) | K<sub>2</sub> | template found by our SAT searches |
| R(3,5,7) | (5,7,3 ; 188) | K<sub>2</sub> | template found by our SAT searches |
| R(3,4,5,5) | (5,3 ; 10) | circulant atom (3,4,5 ; 86) | template from Rowley's tables; atom found by our SAT search |
| R(3,4,5,6) | (3,3,5,3 ; 112) × K<sub>3</sub> → linear block (3,4,3,5 ; 266), then one quadrupling | – | template found by our SAT searches |
| R(5,5,5,5,5) | (5,5,3 ; 99) | atom (5,5,5 ; 453) | atom: Exoo, R<sub>3</sub>(5) ≥ 454 (published) |
| R<sub>7</sub>(5) | (5,5,3 ; 99) | the colouring of R(5,5,5,5,5) | – |

**Quadrupling.** Four copies of a base colouring are glued as in Xu, Xie, Exoo and Radziszowski, *Constructive lower bounds on classical multicolor Ramsey numbers*, Electron. J. Combin. 11 (2004) #R35; the rule is written out in [`tools/build_matrix_R3456.py`](tools/build_matrix_R3456.py), which rebuilds the 1064 × 1064 matrix of R(3,4,5,6) from the 266-vertex block [`ingredients/base_3_4_3_5_n266_firstrow.txt`](ingredients/base_3_4_3_5_n266_firstrow.txt).

**Tabu search.** The 240-vertex colouring for R(4,5,5) is non-linear: it was found by a tabu search that starts from a linear colouring and minimises the number of monochromatic forbidden cliques.

**Templates and atoms found by SAT.** Circulant atoms are found by a counterexample-guided SAT search: the solver colours the N/2 distinct distances and an exact clique search returns violated constraints. Templates are searched with the same engine under the template conditions.

## 4. Verification

All verifiers use only the standard library of Python or C++ and are independent of the programs that produced the colourings. Compile with `g++ -O2 -o verify tools/verify.cpp` and `g++ -O2 -o verify_linear0 tools/verify_linear0.cpp`.

```bash
# exhaustive, EVERY vertex examined (no symmetry argument)
./verify firstrow records/R_3_5_5_n139_firstrow.txt 3,5,5          # SUCCESS ... R(3,5,5) >= 140
./verify firstrow records/R_3_5_6_n191_firstrow.txt 3,5,6          # SUCCESS ... R(3,5,6) >= 192
./verify firstrow records/R_3_5_7_n266_firstrow.txt 3,5,7          # SUCCESS ... R(3,5,7) >= 267
./verify matrix   records/R_4_5_5_n240_matrix.txt   4,5,5          # SUCCESS ... R(4,5,5) >= 241
./verify firstrow records/R_3_4_5_5_n769_firstrow.txt 3,4,5,5      # SUCCESS ... R(3,4,5,5) >= 770   (about 30 s)
./verify matrix   records/R_3_4_5_6_n1064_matrix.txt 3,4,5,6       # SUCCESS ... R(3,4,5,6) >= 1065  (about 10 s)

# linear colourings: cliques through vertex 0 only (see the translation argument below); much faster, needed for large N
./verify_linear0 records/R_5_5_5_5_5_n44337_firstrow.txt 5,5,5,5,5   # R(5,5,5,5,5) >= 44338

python3 tools/verify.py firstrow records/R_3_4_5_5_n769_firstrow.txt 3,4,5,5   # the same check in Python (vertex 0 only), a few seconds
python3 tools/build_all.py                                                       # rebuilds six certificates from their ingredients
```

*Translation argument.* In a linear colouring the colour of {i,j} depends only on |i−j|, so a monochromatic clique with smallest vertex x can be translated by −x into {0,…,N−1}. Hence a monochromatic clique exists if and only if one exists through vertex 0, and it suffices to search the neighbourhood of vertex 0.

**Status of the two largest colourings.**

* **R(5,5,5,5,5) ≥ 44,338 (N = 44,337).** Verified exhaustively with `verify_linear0` (cliques through vertex 0, by the translation argument): no K<sub>5</sub> in any of the five colours (degrees of vertex 0: 14,484 in colour 0 and 4,636 in colour 4; total running time 1,361 s on one core of our machine).
* **R<sub>7</sub>(5) ≥ 4,344,970 (N = 4,344,969).** The colouring is the composition of the template (5,5,3 ; 99) with the 44,337-vertex colouring above. It has 4.3 million vertices and **cannot be verified by exhaustive search**: it rests on Rowley's composition theorem. We have **not** proved independently that our template (5,5,3 ; 99) satisfies the hypotheses of that theorem for every base. The evidence we have is that (i) its composition with K<sub>2</sub> (R(3,5,5), 139 vertices), (ii) its composition with the atom (5,5,5 ; 453) (R(5,5,5,5,5), 44,337 vertices) and (iii) the same double composition as for R<sub>7</sub>(5) but starting from K<sub>2</sub> (limits (5,5,5,5,3), 13,565 vertices) were all verified exhaustively. Treat this record as conditional on the composition theorem until an independent check of the template is available.

## 5. The Atlas

[`atlas/`](atlas/) contains the Atlas of lower bounds for multicolour Ramsey numbers R(k<sub>1</sub>,…,k<sub>r</sub>): one row per parameter set (3 ≤ k<sub>1</sub> ≤ … ≤ k<sub>r</sub> ≤ 10, 2 to 7 colours, 6,426 rows), the best bound we know, its origin (published, deduced from published values, built from published bricks, built with one of our bricks, tabu), the construction, and the published material used. Files: the workbook `Atlas_bornes_Ramsey_multicolore_EN_v13.xlsx`; the same data as CSV (`Atlas_up_to_10_colours_2-7.csv`, `Atlas_3_colours_limits_11-15.csv`, `Our_records.csv`, `Summary.csv`); [`bricks/bricks_vectors.txt`](bricks/bricks_vectors.txt) lists the vector of every atom, template and shifted template used.

An Atlas row labelled "Our bricks" or "Our bricks + published" is a candidate bound, not a claimed record: for most parameter sets no value is published. Only the eight rows above are presented as improvements, and only relative to the tables we used. The published values were copied by hand from Radziszowski's survey (rev. 18) and from Rowley's tables: a copying error is possible and should be checked before any citation. Only colourings with fewer than about 7,000 vertices are checked exhaustively; the other Atlas rows rely on the composition and quadrupling theorems.

## 6. Prior art and limits

* Our literature search was not exhaustive: it covered Radziszowski's *Small Ramsey Numbers* (DS1, rev. 18), Rowley's papers (arXiv:1912.01164, 2107.03560, 2203.13476), Xu–Xie–Exoo–Radziszowski (2004), Exoo–Tatarevic (2015) and a few 2026 preprints. If an earlier or better result exists, please open an issue and we will credit it and correct this file.
* The templates (5,5,3 ; 99), (5,6,3 ; 136), (5,7,3 ; 188) and (3,3,5,3 ; 112) were found by our searches; we compared (4,5,3) and (5,5,3) with Rowley's tables only.
* The atoms of this repository (the circulant (3,4,5 ; 86) and others) have sizes below or equal to published bounds for their own parameters; they are ingredients, not claims.
* These are computer-verified lower bounds on the order of explicit colourings, or colourings obtained from verified ingredients by published theorems. They have **not been peer reviewed**.

## 7. Repository layout

| Path | Content |
| --- | --- |
| `records/` | the certificates (first rows or matrices) of the eight records |
| `ingredients/` | the templates (`J` = joker, φ on the first line), atoms and the 266-vertex block used by the constructions |
| `tools/` | `verify.cpp`, `verify.py`, `verify_linear0.cpp`, `compose.py`, `build_all.py`, `build_matrix_R3456.py` |
| `atlas/` | the Atlas (xlsx and CSV) |
| `bricks/` | vectors of all bricks used by the Atlas |
| `results.json`, `SHA256SUMS`, `LICENSE` | the claims in machine-readable form; checksums (`sha256sum -c SHA256SUMS`); MIT for code, CC0 for data |

## References

* S. Radziszowski, *Small Ramsey Numbers*, Electron. J. Combin., Dynamic Survey DS1, rev. 18 (2026).
* F. Rowley, *Improved lower bounds for multicolour Ramsey numbers using SAT-solvers*, arXiv:2203.13476 (2022); *A generalised linear Ramsey graph construction*, Australasian J. Combin. (2021).
* X. Xu, Z. Xie, G. Exoo, S. Radziszowski, *Constructive lower bounds on classical multicolor Ramsey numbers*, Electron. J. Combin. 11(1) (2004) #R35.
* G. Exoo, M. Tatarevic, *New lower bounds for 28 classical Ramsey numbers*, Electron. J. Combin. 22(3) (2015) #P3.11.

## Acknowledgements

The search and verification programs were developed with the assistance of Claude (Anthropic). The author is responsible for the contents of this repository.

## Citation

J. Courties, *Eight new lower bounds for multicolour classical Ramsey numbers, and an Atlas of lower bounds*, GitHub repository, 2026.
