from z3 import *

s = Solver()

x,y,z = Bools('x y z')

Wolf = Function('Wolf', BoolSort(), BoolSort())
Fox = Function('Fox', BoolSort(), BoolSort())
Bird = Function('Bird', BoolSort(), BoolSort())
Caterpillar = Function('Caterpillar', BoolSort(), BoolSort())
Snail = Function('Snail', BoolSort(), BoolSort())
Grain = Function('Grain', BoolSort(), BoolSort())
Animal = Function('Animal', BoolSort(), BoolSort())
Plant = Function('Plant', BoolSort(), BoolSort())
Eats = Function('Eats', BoolSort(), BoolSort(), BoolSort())
Smaller = Function('Smaller', BoolSort(), BoolSort(), BoolSort())

s.add(Exists(x, Wolf(x)))
s.add(Exists(x, Fox(x)))
s.add(Exists(x, Bird(x)))
s.add(Exists(x, Caterpillar(x)))
s.add(Exists(x, Snail(x)))
s.add(Exists(x, Grain(x)))

s.add(ForAll(x, Implies(Animal(x), 
	Or(
		ForAll(y, Implies(Plant(y), Eats(x,y))),
		ForAll(z, Implies(And(Animal(z), Smaller(z,x), Exists(y, And(Plant(y), Eats(z,y)))), Eats(x,z)))
	)
)))

s.add(Implies(And(Caterpillar(x), Bird(y)), Smaller(x,y)))
s.add(Implies(And(Snail(x), Bird(y)), Smaller(x,y)))
s.add(Implies(And(Bird(x), Fox(y)), Smaller(x,y)))
s.add(Implies(And(Fox(x), Wolf(y)), Smaller(x,y)))
s.add(Implies(And(Bird(x), Caterpillar(y)), Eats(x,y)))

s.add(Implies(Caterpillar(x), Exists(y, And(Plant(y), Eats(x,y)))))
s.add(Implies(Snail(x), Exists(y, And(Plant(y), Eats(x,y)))))

s.add(Implies(And(Wolf(x), Fox(y)), Eats(x,y)))
s.add(Implies(And(Wolf(x), Grain(y)), Eats(x,y)))
s.add(Implies(And(Bird(x), Snail(y)), Eats(x,y)))

s.add(Exists(x, Exists(y, And(Animal(x), Animal(y), Eats(x,y), ForAll(z, Implies(Grain(z), Eats(y,z)))))))

print(s.check())
