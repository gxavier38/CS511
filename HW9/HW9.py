from z3 import *

def add_variable(var):
	if var not in var_map:
		var_map[var] = Int(str(var))
		s.add(Or(var_map[var] == 0, var_map[var] == 1))

def MPE(cpt, obs):
	total = Real("total")
	total_prob = 1

	# Add variables
	for i in range(len(cpt)):
		var_row = cpt[i]
		curr_var = var_row[0]
		add_variable(curr_var)
		var_prob = 0
		sum_prob = 0

		# Add variable's CPT
		for j in range(len(var_row[1])):
			curr_row = var_row[1][j]
			conditions = curr_row[0]
			value = curr_row[1][1]
			sum_prob += curr_row[2]
			probability = RealVal(curr_row[2])

			assert(value == 0 or value == 1)
			assert(curr_var == curr_row[1][0])

			if value == 1:
				probability = probability * var_map[curr_var]
			else:
				probability = probability * (1 - var_map[curr_var])

			# Add conditions
			for k in range(len(conditions)):
				cond_var = conditions[k][0]
				val = conditions[k][1]
				assert(val == 0 or val == 1)
				add_variable(cond_var)
				if val == 1:
					probability *= var_map[cond_var]
				else:
					probability *= (1 - var_map[cond_var])
			var_prob += probability
		assert(sum_prob == 1)
		total_prob *= var_prob
	s.add(total == total_prob)

	# Add observations
	for i in range(len(obs)):
		var = obs[i][0]
		val = obs[i][1]
		assert(val == 0 or val == 1)
		add_variable(var)
		s.add(var_map[var] == val)

	# Solve
	if s.check() == unsat:
		print("Unsatisfiable!")
		return None
	while s.check() == sat:
		model = s.model()
		s.add(total > model[total])

	# Output var_map
	res = [[var, model[var_map[var]]] for var in var_map]
	return res

def MAP(cpt, obs, vs):
	return [x for x in MPE(cpt, obs) if x[0] in vs]

# Read input
filename = sys.argv[1]
with open(filename, "r") as f:
	file = f.readlines()
cpt = eval(" ".join(file[:-2]))
obs = eval(file[-2])
vs = eval(file[-1])

s = Solver()
var_map = {}

res = MPE(cpt, obs)
# res = MAP(cpt, obs, vs)
print(res)

