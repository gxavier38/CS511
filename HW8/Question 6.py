from z3 import *

# Read input graph
filename = sys.argv[1]
with open(filename, "r") as f:
	file = f.readlines()
w = eval(file[0])
c = eval(" ".join(file[1:]))
assert(len(w) == len(c))
assert(len(c) == len(c[0]))
num_nodes = len(w)

s = Solver()

# Create variables
x = [Int("x" + str(i)) for i in range(num_nodes)]
for i in range(num_nodes):
	s.add(Or(x[i] == 1, x[i] == 0))

# Add weight constraints
max_weight = max(w)
total = Int("total")
temp = 0
for i in range(num_nodes):
	temp2 = 0
	for j in range(i+1,num_nodes):
		temp2 += c[i][j] * x[i] * x[j]
	temp += w[i] * x[i] - (1 + max_weight) * temp2
s.add(total == temp)

# Solve
if s.check() == unsat:
	print("Unsatisfiable!")
	quit()
while s.check() == sat:
	model = s.model()
	s.add(total > model[total])
print(model)