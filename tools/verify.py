#!/usr/bin/env python3
"""Independent verifier for multicolour Ramsey colourings (standard library only).

Usage:
    python3 verify.py matrix FILE k1,k2,...,kr       # FILE = N lines of N digits (colour of edge {i,j}, '0' on the diagonal)
    python3 verify.py firstrow FILE k1,k2,...,kr     # FILE = N-1 digits: edge {i,j} has the colour written at position |i-j|
    python3 verify.py firstrow FILE k1,k2,...,kr --full   # same, but search cliques through EVERY vertex (very slow in Python)

For a first row the colouring is linear (the colour of {i,j} depends only on |i-j|), so a clique can be translated by subtracting its smallest vertex:
if a monochromatic clique exists, one exists that contains vertex 0. The default therefore searches cliques through vertex 0 only. Use --full (or the C++ verifier,
verify.cpp, which is fast enough to check every vertex) if you prefer not to rely on this argument.

Colours are numbered 0..r-1; colour c must contain no clique K_{k_c}. If the check succeeds for a colouring of N vertices,
then R(k1,...,kr) >= N + 1. The program exits with status 0 on success and 1 on failure.
"""
import sys, time

def load_matrix(path, r):
    rows = [l.strip() for l in open(path) if l.strip()]
    n = len(rows)
    if any(len(x) != n for x in rows):
        sys.exit("FAILURE: the matrix is not square")
    col = [[int(ch) for ch in row] for row in rows]
    for i in range(n):
        for j in range(n):
            if col[i][j] != col[j][i]:
                sys.exit("FAILURE: the matrix is not symmetric at (%d,%d)" % (i, j))
            if i != j and not (0 <= col[i][j] < r):
                sys.exit("FAILURE: colour out of range at (%d,%d)" % (i, j))
    return n, col

def load_firstrow(path, r):
    s = "".join(open(path).read().split())
    n = len(s) + 1
    row = [int(ch) for ch in s]
    if any(not (0 <= x < r) for x in row):
        sys.exit("FAILURE: colour out of range in the first row")
    col = [[0 if i == j else row[abs(i - j) - 1] for j in range(n)] for i in range(n)]
    return n, col

def has_clique(adj, cand, need):
    """True if the vertex set 'cand' (bitset) contains a clique of 'need' vertices in the graph 'adj'."""
    if need == 0:
        return True
    if bin(cand).count("1") < need:
        return False
    while cand:
        low = cand & -cand
        v = low.bit_length() - 1
        cand ^= low
        if bin(cand).count("1") < need - 1:
            return False
        if has_clique(adj, cand & adj[v], need - 1):
            return True
    return False

def main():
    if len(sys.argv) not in (4, 5) or sys.argv[1] not in ("matrix", "firstrow"):
        sys.exit(__doc__)
    ks = [int(x) for x in sys.argv[3].split(",")]
    full = len(sys.argv) == 5 and sys.argv[4] == "--full"
    only0 = (sys.argv[1] == "firstrow") and not full
    r = len(ks)
    t0 = time.time()
    n, col = (load_matrix if sys.argv[1] == "matrix" else load_firstrow)(sys.argv[2], r)
    print("order N = %d, %d colours, limits %s" % (n, r, ks))
    ok = True
    for c in range(r):
        adj = [0] * n
        for i in range(n):
            m = 0
            for j in range(n):
                if i != j and col[i][j] == c:
                    m |= 1 << j
            adj[i] = m
        edges = sum(bin(a).count("1") for a in adj) // 2
        found = False
        for v in (range(1) if only0 else range(n)):
            higher = adj[v] >> (v + 1) << (v + 1)          # neighbours with a larger index only (each clique is found once)
            if has_clique(adj, higher, ks[c] - 1):
                found = True
                break
        print("  colour %d: %d edges, K_%d %s" % (c, edges, ks[c], "FOUND (failure)" if found else "absent"))
        ok = ok and not found
    if ok:
        print("SUCCESS: no colour contains its forbidden clique, hence R(%s) >= %d  (%.0f s)" % (",".join(map(str, ks)), n + 1, time.time() - t0))
        sys.exit(0)
    print("FAILURE")
    sys.exit(1)

main()
