from z3 import *

s = Solver()

# Add end time
End = Int('End')
s.add(End == 14)

# Add start times
A = Int('A')
B = Int('B')
C = Int('C')
D = Int('D')
E = Int('E')
F = Int('F')

s.add(A >= 0)
s.add(B >= 0)
s.add(C >= 0)
s.add(D >= 0)
s.add(E >= 0)
s.add(F >= 0)

# Add durations
At = Int('At')
Bt = Int('Bt')
Ct = Int('Ct')
Dt = Int('Dt')
Et = Int('Et')
Ft = Int('Ft')

s.add(At == 2)
s.add(Bt == 1)
s.add(Ct == 2)
s.add(Dt == 2)
s.add(Et == 7)
s.add(Ft == 5)

# Add end times
s.add(A + At <= End)
s.add(B + Bt <= End)
s.add(C + Ct <= End)
s.add(D + Dt <= End)
s.add(E + Et <= End)
s.add(F + Ft <= End)

# Add constraints
s.add(Or(A + At <= C, C + Ct <= A))
s.add(Or(B + Bt <= D , D + Dt <= B))
s.add(Or(B + Bt <= E, E + Et <= B))
s.add(Or(D + Dt <= E, E + Et <= D))
s.add(And(D + Dt <= F, E + Et <= F))
s.add(A + At <= B)

# Solve
if s.check() == sat:
	print("Satisfiable!")
	print(s.model())
else:
	print("Unsatisfiable!")