# typy proste

import sys

# int, float, str, bool, complex
print()

# jaki zakres ma int
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# ctrl / - komentowanie kodu
# print((2024 ** 47 ** 2))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(47 ** 2024)
print(len(str(47 ** 2024)))  # rzutowanie na stringa, długosc 3385

# float
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
# max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15,
# mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# silne typowanie, nie zzamienai sam typów
# print("5" + 5) # TypeError: can only concatenate str (not "int") to str

# ctrl alt l - formatowanie kodu
print(5 + 5)  # 10
print("5" + "5")  # 55 - łączenie stringów

print(45 * "9")  # 999999999999999999999999999999999999999999999
print(45 * 9)  # 405
print(int(45) * int("9"))  # 405

# https://kariera.comarch.pl/blog/clean-code-15-krokow-do-stworzenia-czystego-kodu/
# https://peps.python.org/pep-0008/

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004

#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345

# decimal - ominięcie problemu błędu zaokrąglenia

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)  # 0.3

a = Decimal(0.1)
b = Decimal(0.2)
print(a + b)  # 0.3000000000000000166533453694
print(a, b)
# 0.1000000000000000055511151231257827021181583404541015625 0.200000000000000011102230246251565404236316680908203125

# bool
print(True)
print(False)

print(bool(0))  # False
print(bool(1))  # True

print(bool("radek"))  # True
print(bool(""))  # False
a = 100
b = 100
print(a == b)
print(a is b)

a = 1025
b = 1025
print(a is b)  # True

# powyżej 1024
a = int("1025")
b = int("1025")

print(a == b)  # True
print(a is b)  # False

a = int("100")
b = int("100")

print(a == b)  # True
print(a is b)  # True

print(True and False)  # False
print(True or False)  # True

print(True & False)  # porównanie bitowe

# 4 = 100
# 2 = 010
#     000

print(4 & 2)  # 0
print(4 and 2)  #
print(4 and 2)  # 2

# kolekcja
# lista, krotka (tuple), zbiór, słownik, frozenset

# lista - dowolne typy na raz, mutowalna, zachowuje kolejność
lista = list()
lista2 = []
lista = [9, 8, 8, 9, 9]
lista2 = [10, 20, 20, 20]

lista3 = lista  # kopia referencji, adresu
print(lista3)
print(lista)
print(id(lista))
print(id(lista3))  # 1693199552448
print(lista is lista3)  # True

lista_copy = lista.copy()  # kopia listy
print(id(lista_copy))  # 2274821684672
print(id(lista))  # 2274818969536

# teksty są niemutowalne
# pula tekstów
tekst = "Radek"
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Radek

# krotka (tuple)
# pozwala lepiej zarządzać pamięcią
a = ()
print(a)  # <class 'tuple'>
print(type(a))  # <class 'tuple'>

# del - usuniecie obiektu z pamięci

tupla = "tomek", "radek", "zenek", "marek"
print(type(tupla))  # <class 'tuple'>
print(tupla)  # ('tomek', 'radek', 'zenek', 'marek')

a = 1,
print(a)  # (1,)
print(type(a))  # <class 'tuple'>

a = (1,)
print(a)  # (1,)

# tupla[0] = "Roman"  # TypeError: 'tuple' object does not support item assignment
# del tupla
# print(tupla) # NameError: name 'tupla' is not defined. Did you mean: 'tuple'?

print(sorted(tupla))  # ['marek', 'radek', 'tomek', 'zenek']
print(tupla)  # ('tomek', 'radek', 'zenek', 'marek')
