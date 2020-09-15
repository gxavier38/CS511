from z3 import *

x, y, z = Bools('x y z')

phi = Or(And(x,y), And(y,z), And(x,z))
psi = And(Or(x,y), Or(x,z), Or(y,z))
f = phi == psi

s = Solver()
s.add(Not(f))

if s.check() == unsat:
	print("Tautology")
else:
	print("Not tautology")