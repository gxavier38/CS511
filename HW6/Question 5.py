from z3 import *

m = Function('m', IntSort(), IntSort(), IntSort())
i = Function('i', IntSort(), IntSort())
x,y,z,e = Ints('x y z e')

s = Solver()

# Axioms of group theory
s.add(m(m(x,y), z) == m(x, m(y,z)))  # m is associative
s.add(m(x, e) == x)                  # e is a right identity
s.add(m(x, i(x)) == e)               # i(x) is right inverse of x

# Find Abelian group
s.add(Not(m(x,y) == m(y,x)))

if s.check() == unsat:
	print("Tautology")
else:
	print("Not tautology")