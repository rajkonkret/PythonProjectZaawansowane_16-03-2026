from problem_cache import memoizacja
from problem_cache import fiboacci


# @memoizacja
# def fun():
#     print("Radek")

# fiboacci(5)


def funkcja():
    print(fiboacci(5))


print(fiboacci(4))
funkcja()
# ID cache: 2764463180032
# {(1,): 1}
# {(1,): 1, (0,): 0}
# {(1,): 1, (0,): 0, (2,): 1}
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# {(1,): 1, (0,): 0, (2,): 1, (3,): 2}
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((2,) -> 1)
# Używam cache o ID: 2764463180032
# {(1,): 1, (0,): 0, (2,): 1, (3,): 2, (4,): 3}
# 3
# Zwracamy wynik z cache dla argumentów: (4,)
# Zwracamy wynik z cache dla argumentów: (3,)
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((2,) -> 1)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((3,) -> 2)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((2,) -> 1)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((4,) -> 3)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (3,)
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((2,) -> 1)
# Używam cache o ID: 2764463180032
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2764463180032
# Funkcja: fiboacci((3,) -> 2)
# Używam cache o ID: 2764463180032
# {(1,): 1, (0,): 0, (2,): 1, (3,): 2, (4,): 3, (5,): 5}
# 5
