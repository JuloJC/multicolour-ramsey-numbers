// Independent exhaustive verifier for multicolour Ramsey colourings (standard C++11, no dependencies).
//   g++ -O2 -o verify verify.cpp
//   ./verify matrix   FILE k1,k2,...,kr     FILE = N lines of N digits (colour of the edge {i,j}; '0' on the diagonal)
//   ./verify firstrow FILE k1,k2,...,kr     FILE = N-1 digits: the edge {i,j} has the colour written at position |i-j|
// Colours are 0..r-1; colour c must contain no clique K_{k_c}. EVERY vertex is examined (no symmetry argument is used).
// If the check succeeds on N vertices then R(k1,...,kr) >= N+1. Exit status 0 = success, 1 = failure.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <chrono>
using namespace std;
typedef unsigned long long u64;
static int N, W;
static bool hasClique(const vector<vector<u64>>& adj, vector<u64> cand, int need) {
    if (need == 0) return true;
    int pc = 0; for (int i = 0; i < W; i++) pc += __builtin_popcountll(cand[i]);
    if (pc < need) return false;
    for (int i = 0; i < W; i++) while (cand[i]) {
        int b = __builtin_ctzll(cand[i]); cand[i] &= cand[i] - 1; int x = (i << 6) + b; pc--;
        if (pc < need - 1) return false;
        vector<u64> nx(W); for (int j = 0; j < W; j++) nx[j] = cand[j] & adj[x][j];
        if (hasClique(adj, nx, need - 1)) return true;
    }
    return false;
}
int main(int argc, char** argv) {
    if (argc != 4 || (string(argv[1]) != "matrix" && string(argv[1]) != "firstrow")) { fprintf(stderr, "usage: verify matrix|firstrow FILE k1,k2,...,kr\n"); return 2; }
    vector<int> ks; { string s = argv[3], t; for (char ch : s + ",") { if (ch == ',') { if (!t.empty()) ks.push_back(atoi(t.c_str())); t.clear(); } else t += ch; } }
    int r = (int)ks.size(); auto t0 = chrono::steady_clock::now();
    ifstream f(argv[2]); if (!f) { fprintf(stderr, "cannot open %s\n", argv[2]); return 2; }
    vector<string> rows; string l; while (getline(f, l)) { string z; for (char ch : l) if (ch >= '0' && ch <= '9') z += ch; if (!z.empty()) rows.push_back(z); }
    vector<vector<int>> col;
    if (string(argv[1]) == "matrix") {
        N = (int)rows.size(); col.assign(N, vector<int>(N, 0));
        for (int i = 0; i < N; i++) { if ((int)rows[i].size() != N) { puts("FAILURE: the matrix is not square"); return 1; } for (int j = 0; j < N; j++) col[i][j] = rows[i][j] - '0'; }
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) { if (col[i][j] != col[j][i]) { printf("FAILURE: not symmetric at (%d,%d)\n", i, j); return 1; } if (i != j && col[i][j] >= r) { printf("FAILURE: colour out of range at (%d,%d)\n", i, j); return 1; } }
    } else {
        string s; for (auto& x : rows) s += x; N = (int)s.size() + 1; col.assign(N, vector<int>(N, 0));
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) if (i != j) { int c = s[abs(i - j) - 1] - '0'; if (c >= r) { puts("FAILURE: colour out of range"); return 1; } col[i][j] = c; }
    }
    W = (N + 63) >> 6; printf("order N = %d, %d colours\n", N, r); bool ok = true;
    for (int c = 0; c < r; c++) {
        vector<vector<u64>> adj(N, vector<u64>(W, 0)); long long edges = 0;
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) if (i != j && col[i][j] == c) { adj[i][j >> 6] |= 1ULL << (j & 63); if (i < j) edges++; }
        bool found = false;
        for (int v = 0; v < N && !found; v++) {
            vector<u64> cand = adj[v]; for (int j = 0; j < W; j++) { if (j < (v >> 6)) cand[j] = 0; else if (j == (v >> 6)) cand[j] &= ~((2ULL << (v & 63)) - 1); }
            if (hasClique(adj, cand, ks[c] - 1)) found = true;
        }
        printf("  colour %d: %lld edges, K_%d %s\n", c, edges, ks[c], found ? "FOUND (failure)" : "absent"); ok = ok && !found;
    }
    double dt = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    if (ok) { printf("SUCCESS: no colour contains its forbidden clique, hence R("); for (int i = 0; i < r; i++) printf("%s%d", i ? "," : "", ks[i]); printf(") >= %d  (%.1f s)\n", N + 1, dt); return 0; }
    puts("FAILURE"); return 1;
}
