from z3 import *
from itertools import combinations
from random import choice

n = 6
p = 5
skip = 9

def difference(arr, elems):
	return list(set(arr) - set(elems))

def check(skip):
	s = Solver()

	# Variables
	Q = [[Bool("Q" + str(i+1) + "," + str(j+1)) for j in range(n)] for i in range(n)]
	R = [[Bool("R" + str(i+1) + "," + str(j+1)) for j in range(n)] for i in range(n)]

	# Constraint 1
	phi_1 = And([Or(Q[i]) for i in rows])

	# Constraint 2
	phi_2 = And([Or(R[i]) for i in other_rows])

	# Constraint 3
	phi_3 = And([Implies(Q[i][j], Not(R[i][j])) for i in all_rows for j in all_rows])

	# Constraint 4
	phi_4 = And([Implies(Q[i][j], And([And(Not(Q[i][l]), Not(R[i][l])) for l in all_rows if l != j])) for i in all_rows for j in all_rows])

	# Constraint 5
	phi_5 = And([Implies(Q[j][i], And([And(Not(Q[l][i]), Not(R[l][i])) for l in all_rows if l != j])) for i in all_rows for j in all_rows])

	# Constraint 6
	phi_6 = And([Implies(R[i][j], And([And(Not(Q[i][l]), Not(R[i][l])) for l in all_rows if l != j])) for i in all_rows for j in all_rows])

	# Constraint 7
	phi_7 = And([Implies(R[j][i], And([And(Not(Q[l][i]), Not(R[l][i])) for l in all_rows if l != j])) for i in all_rows for j in all_rows])

	# Constraint 8
	phi_8 = And([Implies(Q[i][j], And([And(Not(Q[k][l]), Not(R[k][l])) for k in all_rows for l in all_rows if k != i and l != j and k - l == i - j])) for i in all_rows for j in all_rows])

	# Constraint 9
	phi_9 = And([Implies(Q[i][j], And([And(Not(Q[k][l]), Not(R[k][l])) for k in all_rows for l in all_rows if k != i and l != j and k + l == i + j])) for i in all_rows for j in all_rows])

	# Add all constraints except skip
	phi = [phi_1, phi_2, phi_3, phi_4, phi_5, phi_6, phi_7, phi_8, phi_9]
	s.add(And([phi[x] for x in range(9) if x != skip]))
	assert(s.check() == sat)

	# Fix current assignments
	model = s.model()
	for i in range(n):
		for j in range(n):
			s.add(Q[i][j] == model[Q[i][j]])
			s.add(R[i][j] == model[R[i][j]])
	
	# Add skipped constraint and check whether assignment is still valid
	s.add(phi[skip])
	if s.check() == unsat:
		return True
	else:
		return False

assert(p <= n)

# Choose random rows
all_rows = [i for i in range(n)]
rows = choice(list(combinations(all_rows, p)))
other_rows = difference(all_rows, rows)

for i in range(9):
	if check(i) == True:
		print("Constraint", i+1, "is mandatory")
	else:
		print("Constraint", i+1, "is redundant")

# Mandatory
# 1,2,3,5,8,9
# Free
# 4,6,7