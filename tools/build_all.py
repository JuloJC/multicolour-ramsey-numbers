#!/usr/bin/env python3
"""Rebuilds the linear colourings of the records from their ingredients (templates and atoms in ../ingredients) with compose.py,
and checks that the result is identical to the certificate stored in ../records. Standard library only.
Colours of the composed graph are numbered: template colours first, then base colours; the final numbering orders the colours by increasing limit
(ties: template colours first), which is the numbering used in the certificates."""
import os, itertools, sys
from compose import compose
HERE = os.path.dirname(os.path.abspath(__file__)); ING = os.path.join(HERE, "..", "ingredients"); REC = os.path.join(HERE, "..", "records")

def read_template(name):
    lines = [l.strip() for l in open(os.path.join(ING, name)) if l.strip() and not l.startswith("#")]
    return int(lines[0]), lines[1]                       # phi, period with J
def read_atom(name):
    return "".join(l.strip() for l in open(os.path.join(ING, name)) if l.strip() and not l.startswith("#"))
def read_row(name):
    return "".join(open(os.path.join(REC, name)).read().split())

def check(title, tname, p, V, limits, certificate):
    phi, T = read_template(tname)
    s = compose(T, phi, V, p)
    ref = read_row(certificate)
    for perm in itertools.permutations(range(len(limits))):          # composed colour perm[c] becomes final colour c
        if [limits[perm[c]] for c in range(len(limits))] != sorted(limits):
            continue
        if "".join(str(perm.index(int(ch))) for ch in s) == ref:
            print("%-44s N = %-8d identical to %s" % (title, len(s) + 1, certificate)); return True
    print("%-44s MISMATCH" % title); return False

ok = True
ok &= check("R(3,5,5):  template (5,5,3;99) x K2",  "template_5_5_3_m99.txt",  2, "0", [5, 5, 3], "R_3_5_5_n139_firstrow.txt")
ok &= check("R(3,5,6):  template (5,6,3;136) x K2", "template_5_6_3_m136.txt", 2, "0", [5, 6, 3], "R_3_5_6_n191_firstrow.txt")
ok &= check("R(3,5,7):  template (5,7,3;188) x K2", "template_5_7_3_m188.txt", 2, "0", [5, 7, 3], "R_3_5_7_n266_firstrow.txt")
ok &= check("R(3,4,5,5): template (5,3;10) x atom (3,4,5;86)", "template_5_3_m10.txt", 1, read_atom("atom_3_4_5_n86_circulant_firstrow.txt"), [5, 3, 4, 5], "R_3_4_5_5_n769_firstrow.txt")
ok &= check("R(5,5,5,5,5): template (5,5,3;99) x atom (5,5,5;453)", "template_5_5_3_m99.txt", 2, read_atom("atom_5_5_5_n453_firstrow.txt"), [5] * 5, "R_5_5_5_5_5_n44337_firstrow.txt")
ok &= check("R_7(5): template (5,5,3;99) x the 5-colour graph", "template_5_5_3_m99.txt", 2, read_row("R_5_5_5_5_5_n44337_firstrow.txt"), [5] * 7, "R_5x5x5x5x5x5x5_n4344969_firstrow.txt")
print("ALL IDENTICAL" if ok else "DIFFERENCES FOUND")
sys.exit(0 if ok else 1)
