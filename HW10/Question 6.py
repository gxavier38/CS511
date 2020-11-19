from z3 import *
from itertools import combinations

(m,n) = (6,10)
PierP = [(1,1),(2,7),(3,3),(3,8),(6,8)]
BlockedP = [(2,3),(2,5),(2,8),(4,4),(4,5),(4,9),(5,5),(6,1)]

# (m,n) = (5,1)
# PierP = [(1,1),(5,1)]
# BlockedP = []

# (m,n) = (1,5)
# PierP = [(1,1),(1,5)]
# BlockedP = []

# (m,n) = (5,5)
# PierP = [(1,1),(5,5)]
# BlockedP = []

# (m,n) = (5,1)
# PierP = [(1,1),(5,1)]
# BlockedP = [(3,1)]

# (m,n) = (5,1)
# PierP = [(1,1),(3,1),(5,1)]
# BlockedP = []

# (m,n) = (0,0)
# PierP = []
# BlockedP = []

# (m,n) = (1,5)
# PierP = [(1,1)]
# BlockedP = []

# (m,n) = (1,5)
# PierP = []
# BlockedP = []

s = Solver()
total = Int("total")

def getLocation(location):
	(i,j) = location
	return arr[i-1][j-1]

def getAdjacent(location):
	(i,j) = location
	res = []
	if i > 1:
		res = res + [arr[i-2][j-1]]
	if i < m:
		res = res + [arr[i][j-1]]
	if j > 1:
		res = res + [arr[i-1][j-2]]
	if j < n:
		res = res + [arr[i-1][j]]
	return res

def difference(arr, elems):
	return list(set(arr) - set(elems))

def printMap(true_model):
	arr = [[" " for j in range(n)] for i in range(m)]
	for location in true_model:
		arr[location[0]-1][location[1]-1] = "+"
	for location in PierP:
		arr[location[0]-1][location[1]-1] = "P"
	for location in BlockedP:
		arr[location[0]-1][location[1]-1] = "█"
	res = [".".join(x) for x in arr]
	res = ["|" + x + "|" for x in res]
	res = "\n".join(res)
	print(res)

# All positions
P = [(i+1,j+1) for i in range(m) for j in range(n)]
# Free positions
FreeP = difference(P, PierP + BlockedP)

# Construct variables
arr = [[Bool("X" + str(i+1) + "," + str(j+1)) for j in range(n)] for i in range(m)]

# Add PierP constraint
for location in PierP:
	current = getLocation(location)
	s.add(current == True)

# Add BlockedP contraint
for location in BlockedP:
	current = getLocation(location)
	s.add(current == False)

# PierP has exactly one set neighbour
for location in PierP:
	neighbours = getAdjacent(location)
	s.add(Or(*neighbours))
	for neighbour in neighbours:
		other_neighbours = difference(neighbours, [neighbour])
		s.add(Implies(neighbour, Not(Or(other_neighbours))))

# If FreeP is set then it has at least two set neighbours
for location in FreeP:
	current = getLocation(location)
	neighbours = getAdjacent(location)
	subsets = combinations(neighbours, 2)
	s.add(Implies(current, Or([And(subset) for subset in subsets])))

# Add weights
weight = 0
for location in P:
	weight = weight + IntSort().cast(Not(getLocation(location)))
s.add(total == weight)

# Solve
if s.check() == unsat:
	print("Unsatisfiable!")
	quit()
while s.check() == sat:
	model = s.model()
	s.add(total > model[total])

# Print
true_model = [location for location in P if model[getLocation(location)] == True]
false_model = [location for location in P if model[getLocation(location)] == False]
print("Tree is", true_model, "with weight", model[total])
printMap(true_model)