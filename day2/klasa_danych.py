from dataclasses import dataclass, field
from typing import List


class Liczba:
    def __init__(self, x, y):
        self.x = x
        self.y = y


liczba = Liczba(5, 3)
print(liczba)  # <__main__.Liczba object at 0x000002097DC00AD0>
print(liczba.x)  # 5
print(liczba.y)  # 3


@dataclass()
class DLiczba:
    x: int
    y: int
    z: float


dl = DLiczba(5, 3, 4.6)
print(dl)  # DLiczba(x=5, y=3, z=4.6)


@dataclass()
class Order:
    customer: str
    items: List[int] = field(default_factory=list)
    items_d: List[int] = field(default_factory=lambda: ["A", "B", "C"])
    status: str = "Pending"

ord = Order("A")
print(ord)
# Order(customer='A', items=[], items_d=['A', 'B', 'C'], status='Pending')
