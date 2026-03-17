"""
Trzy przypadki użycia funkcji __call__
1. Licznik wywołań funkcji
2. Walidacja danych wejściowych
3. implementacja cache
"""
from counter_zad1 import CallCounter

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
