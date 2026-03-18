# deskryptor
from weakref import WeakKeyDictionary


class LoggedPositiveInt:
    def __init__(self):
        # self._values = {}
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        print(f"{instance}")

    def __set__(self, instance, value):
        print("Ustawiasz pole")


class Product:
    stock = LoggedPositiveInt()

    def __init__(self, stock):
        self.stock = stock


p1 = Product(10)
p2 = Product(5)
# Ustawiasz pole
# Ustawiasz pole

print(p1.stock)  # <__main__.Product object at 0x00000136BF408D70>
p1.stock = 20
print(p2.stock)
# Ustawiasz pole
# <__main__.Product object at 0x000001FB110B8A50>
# None
