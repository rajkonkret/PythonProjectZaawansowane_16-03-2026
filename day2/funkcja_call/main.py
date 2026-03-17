"""
Trzy przypadki użycia funkcji __call__
1. Licznik wywołań funkcji
2. Walidacja danych wejściowych
3. implementacja cache
"""
from counter_zad1 import CallCounter
from validator import RangeValidator
from cache import CacheFunction

print(70 * "-")
counter = CallCounter()
counter()
counter()
counter()
counter()
counter()
# ----------------------------------------------------------------------
# Funkcję __call__ wywołąno 1 razy
# Funkcję __call__ wywołąno 2 razy
# Funkcję __call__ wywołąno 3 razy
# Funkcję __call__ wywołąno 4 razy
# Funkcję __call__ wywołąno 5 razy

print(70 * "-")
valid = RangeValidator(2, 20)
valid(3)
valid(17)
valid(8)
valid(44)
# ----------------------------------------------------------------------
# Wartość 3 mieści się w przedziale (min:2, max:20)
# Wartość 17 mieści się w przedziale (min:2, max:20)
# Wartość 8 mieści się w przedziale (min:2, max:20)
# Wartość 44 jest poza przedziałęm (min:2, max:20)

print(70 * "-")


def efunction(x, y):
    return x ** y + y ** x


cache_func = CacheFunction(efunction)
print(cache_func(2, 3))
print(cache_func(2, 3))
print(cache_func(2, 3))
print(cache_func(2, 3))
print(cache_func(2, 3))
# ----------------------------------------------------------------------
# Wynik obliczeń dla argumentó: (2, 3)
# 17
# Wynik w cache dla argumentów: (2, 3)
# 17
# Wynik w cache dla argumentów: (2, 3)
# 17
# Wynik w cache dla argumentów: (2, 3)
# 17
# Wynik w cache dla argumentów: (2, 3)
# 17

print(cache_func(12, 1))
# Wynik obliczeń dla argumentó: (12, 1)
# 13

print(cache_func(2, 3))
# Wynik w cache dla argumentów: (2, 3)
# 17
