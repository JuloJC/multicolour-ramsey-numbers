// Exhaustive verifier for LINEAR colourings (first row), searching cliques through vertex 0 only (standard C++11, no dependencies).
//   g++ -O2 -o verify_linear0 verify_linear0.cpp
//   ./verify_linear0 FILE k1,k2,...,kr        FILE = N-1 digits: the edge {i,j} has the colour written at position |i-j|; colour c must contain no K_{k_c}.
// Why vertex 0 is enough: the colour of {i,j} depends only on |i-j|, so a monochromatic clique {x_0 < x_1 < ...} can be translated by -x_0 into the vertex set {0,...,N-1};
// hence a monochromatic clique exists iff one exists through vertex 0. (To examine EVERY vertex use verify.cpp, which is slower.)
// For each colour c the program lists the neighbours S of vertex 0 in colour c and searches a clique K_{k_c - 1} inside S (bitset recursion). Exit status 0 = success.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>
using namespace std;
typedef unsigned long long u64;
static int W;
static bool hasClique(const vector<vector<u64>>& adj, const vector<u64>& cand, int need) {
    if (need == 0) return true;
    int pc = 0; for (int i = 0; i < W; i++) pc += __builtin_popcountll(cand[i]);
    if (pc < need) return false;
    vector<u64> c = cand, nx(W, 0);
    for (int i = 0; i < W; i++) while (c[i]) {
        int b = __builtin_ctzll(c[i]); c[i] &= c[i] - 1; int x = (i << 6) + b; pc--;
        if (pc < need - 1) return false;
        if (need == 1) return true;
        bool any = false; for (int j = 0; j < i; j++) nx[j] = 0; for (int j = i; j < W; j++) { nx[j] = c[j] & adj[x][j]; if (nx[j]) any = true; }
        if (any && hasClique(adj, nx, need - 1)) return true;
    }
    return false;
}
int main(int argc, char** argv) {
    if (argc != 3) { fprintf(stderr, "usage: verify_linear0 FILE k1,k2,...,kr\n"); return 2; }
    vector<int> ks; { string s = argv[2], t; for (char ch : s + ",") { if (ch == ',') { if (!t.empty()) ks.push_back(atoi(t.c_str())); t.clear(); } else t += ch; } }
    int r = (int)ks.size(); ifstream f(argv[1]); if (!f) { fprintf(stderr, "cannot open %s\n", argv[1]); return 2; }
    string s, l; while (getline(f, l)) for (char ch : l) if (ch >= '0' && ch <= '9') s += ch; int N = (int)s.size() + 1; auto t0 = chrono::steady_clock::now();
    for (char ch : s) if (ch - '0' >= r) { puts("FAILURE: colour out of range"); return 1; }
    printf("order N = %d, %d colours\n", N, r); bool ok = true;
    for (int c = 0; c < r; c++) {
        vector<int> S; for (int d = 1; d < N; d++) if (s[d - 1] - '0' == c) S.push_back(d); int n = (int)S.size(); W = (n + 63) >> 6;
        vector<vector<u64>> adj(n, vector<u64>(W, 0));
        for (int a = 0; a < n; a++) for (int b = a + 1; b < n; b++) if (s[S[b] - S[a] - 1] - '0' == c) { adj[a][b >> 6] |= 1ULL << (b & 63); adj[b][a >> 6] |= 1ULL << (a & 63); }
        vector<u64> all(W, 0); for (int i = 0; i < n; i++) all[i >> 6] |= 1ULL << (i & 63);
        bool found = hasClique(adj, all, ks[c] - 1);
        double dt = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
        printf("  colour %d: degree of vertex 0 = %d, K_%d %s  (%.0f s)\n", c, n, ks[c], found ? "FOUND (failure)" : "absent", dt); fflush(stdout); ok = ok && !found;
    }
    if (ok) { printf("SUCCESS: no colour contains its forbidden clique, hence R("); for (int i = 0; i < r; i++) printf("%s%d", i ? "," : "", ks[i]); printf(") >= %d\n", N + 1); return 0; }
    puts("FAILURE"); return 1;
}
