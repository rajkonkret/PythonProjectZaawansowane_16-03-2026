import sys


class Normal:
    def __init__(self, x, y):
        self.x = x
        self.y = y


n = Normal(1, 2)

print("Normal na __dict__:", hasattr(n, "__dict__"))  # Normal na __dict__: True
print(n.__dict__)  # {'x': 1, 'y': 2}

n.z = 9999
print("Normal.z", n.z)  # Normal.z 9999


class Slotted:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Slotted(1, 2)
print("Slotted na __dict__:", hasattr(s, "__dict__"))  # Slotted na __dict__: False
# s.z = 9999 # AttributeError: 'Slotted' object has no attribute 'z' and no __dict__ for setting new attributes

print("Rozmiar Normal", sys.getsizeof(n))
print("Rozmiar Slotted", sys.getsizeof(s))


# Rozmiar Normal 48
# Rozmiar Slotted 48

class Next(Slotted):
    # __slots__ = () # AttributeError: 'Next' object has no attribute 'z' and no __dict__ for setting new attributes


    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


a = Next(1, 2, 3)
print(a.z)
