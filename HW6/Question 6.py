from z3 import *

f = open("input.txt", "r")
in_a = int(f.readline())
m = int(f.readline())
in_b = int(f.readline())
n = int(f.readline())

# print("in_a:", in_a, "m:", m, "in_b:", in_b, "n:", n)

s = Solver()

# Simulate power
out_a = in_a
for i in range(m):
	out_a = out_a * in_a

# Simulate power_new
out_b = in_b
for i in range(n):
	out_b = out_b * out_b

s.add(Not(out_a == out_b))

if s.check() == unsat:
	print("Equal")
else:
	print("Not equal")