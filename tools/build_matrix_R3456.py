#!/usr/bin/env python3
"""Builds the 1064 x 1064 colouring for R(3,4,5,6) >= 1065 from the 266-vertex linear block 'base_3_4_3_5_n266_firstrow.txt'
by one quadrupling step in the sense of Xu, Xie, Exoo and Radziszowski ("Constructive lower bounds on classical multicolor Ramsey numbers", Electron. J. Combin. 11 (2004) #R35).

Base block B on N0 = 266 vertices, 4 colours with limits (3,4,3,5), the colour of {i,j} being the digit at position |i-j|.
Four copies of B (indexed 0..3) are glued as follows (vertex = copy*N0 + j):
  - same copy                                 : colour of B;
  - copies on different sides ({0,1} versus {2,3}) : colour 2 if the two vertices have the same index j, colour of B otherwise;
  - different copies on the same side           : colour 3 if the same index j, colour 2 otherwise.
The result has no K3 in colour 0, no K4 in colour 1, no K5 in colour 2 and no K6 in colour 3: limits (3,4,5,6).
"""
import sys
seq = "".join(open("base_3_4_3_5_n266_firstrow.txt").read().split())
n0 = len(seq) + 1
a, b = 3, 2                       # colour a gains one in its limit (5 -> 6); the merged colour b goes from 3 to 5
n = 4 * n0
out = open("R_3_4_5_6_n1064_matrix.txt", "w")
for u in range(n):
    i1, j1 = divmod(u, n0)
    row = []
    for v in range(n):
        i2, j2 = divmod(v, n0)
        if u == v:
            c = 0
        elif i1 == i2:
            c = int(seq[abs(j1 - j2) - 1]) if j1 != j2 else 0
        elif (i1 < 2) != (i2 < 2):
            c = b if j1 == j2 else int(seq[abs(j1 - j2) - 1])
        else:
            c = a if j1 == j2 else b
        row.append(str(c))
    out.write("".join(row) + "\n")
out.close()
print("matrix written: %d x %d" % (n, n))
