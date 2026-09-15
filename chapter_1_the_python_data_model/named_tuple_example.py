from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "profession"])

p = Person("Jarjish", 22, "Developer")

print(p.name)
print(p.age)
print(p.profession)

p2 = Person("Parth", 22, "Dancer")
print(p2.name)
print(p2.age)
print(p2.profession)