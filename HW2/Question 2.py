from z3 import *

p1, p2, p3, p4 = Bools('p1 p2 p3 p4')

phi = Or(
	And(Not(p1), Not(p2), Not(p3), Not(p4)),
	And(Not(p1), Not(p2), p3, p4),
	And(Not(p1), p2, Not(p3), p4),
	And(Not(p1), p2, p3, Not(p4)),
	And(p1, Not(p2), Not(p3), p4),
	And(p1, Not(p2), p3, Not(p4)),
	And(p1, p2, Not(p3), Not(p4)),
	And(p1, p2, p3, p4)
)

psi = And(
	Or(p1, p2, p3, Not(p4)),
	Or(p1, p2, Not(p3), p4),
	Or(p1, Not(p2), p3, p4),
	Or(p1, Not(p2), Not(p3), Not(p4)),
	Or(Not(p1), p2, p3, p4),
	Or(Not(p1), p2, Not(p3), Not(p4)),
	Or(Not(p1), Not(p2), p3, Not(p4)),
	Or(Not(p1), Not(p2), Not(p3), p4),
)
theta = p1 == p2 == p3 == p4

f = phi == psi == theta

s = Solver()
s.add(Not(f))

if s.check() == unsat:
	print("Tautology")
else:
	print("Not, tautology")