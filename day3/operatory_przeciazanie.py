# class Value:
#     def __init__(self, value):
#         self.value = value
#
#
# kw1 = Value(10)
# kw2 = Value(5)
# print(kw1 + kw2) @ TypeError: unsupported operand type(s) for +: 'Value' and 'Value'
from functools import total_ordering


class Value:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


kw1 = Value(10)
kw2 = Value(5)
print(kw1 + kw2)  # 15


# __lt__, __le__, __gt__, __ge__
# __eq__, __ne__
@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


alice = Student("Alice", 90)
alice2 = Student("Alice", 90)

print(alice == alice2)  # False, po nadpisaniu __eq__ True
bob = Student("Bob", 76)

print(alice < bob)  # False
print(alice > bob)  # True
