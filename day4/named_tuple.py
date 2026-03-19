from collections import namedtuple

# tupla zawiera nazwy parametrow - podobnie jak nazwy kluczy w słowniku
Point = namedtuple("Point", ['x', 'y'])

p = Point(10, 20)

print(p[0])
print(p[1])
# 10
# 20

print(p.x)
print(p.y)
# 10
# 20

# niemutowalna
p.x = 100  # AttributeError: can't set attribute
