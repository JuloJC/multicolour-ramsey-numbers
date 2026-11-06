#!/usr/bin/env python3
"""Rowley's composition of a template with an atom (F. Rowley, 2021) -- independent re-implementation.

A TEMPLATE (k_1..k_p, 3 ; m) is a period of m-1 digits: 0..p-1 are its own colours, 'J' is the JOKER (a triangle-free length reserved for a colour of the base);
phi = number of lengths before the first joker. An ATOM V is a linear colouring of n vertices (n-1 digits, colours 0..r-1, limits l_1..l_r).
Composition: for mu = 1..n-1, write the period once, each joker being replaced by the colour of length mu of V (renumbered p + V[mu]); finally append the first phi digits of the period.
The result is a linear colouring on N = (m-1)(n-1) + 1 + phi vertices whose colours are, in this numbering, the p colours of the template followed by the r colours of V.
"""
def compose(T, phi, V, p):
    assert "J" not in T[:phi], "a joker occurs before position phi"
    out = []
    for ch_v in V:
        for ch in T:
            out.append(str(p + int(ch_v)) if ch == "J" else ch)
    out.append(T[:phi])
    return "".join(out)
