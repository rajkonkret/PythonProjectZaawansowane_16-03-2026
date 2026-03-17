# zasymulowac cache dla funkcji
# jesli funkcja wywołąna z argumentami jakie znamy juz -> wynik z cache
# w przeciwnym wypadku dokonac nowego obliczenia i zwrócic wynik

def memoizacja(funkcja):
    cache = {}
    print("ID cache:", id(cache))

    def wrapper(*args):
        if args in cache:
            print(f"Zwracamy wynik z cache dla argumentów: {args}")
            print(f"Funkcja: {funkcja.__name__}({args} -> {funkcja(*args)})")
            print(f"Używam cache o ID:", id(cache))
            return cache[args]
        else:
            wynik = funkcja(*args)
            cache[args] = wynik
            print(cache)
            return wynik

    return wrapper


@memoizacja
def fiboacci(n):
    if n <= 1:
        return n
    else:
        return fiboacci(n - 1) + fiboacci(n - 2)


@memoizacja
def fibonaci2(n):
    if n <= 1:
        return n
    else:
        return fibonaci2(n - 1) + fibonaci2(n - 2)

print(58 * "-")
print("Uzycie fibonacci 1")
print(fiboacci(3))
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)

print(58 * "-")
print("Uzycie fibonacci 2")
print(fiboacci(2))

print(58 * "-")
print("Uzycie fibonacci2")
print(fibonaci2(3))
# ID cache: 2223720034624
# ID cache: 2223720439168
# ----------------------------------------------------------
# Uzycie fibonacci 1
# {(1,): 1}
# {(1,): 1, (0,): 0}
# {(1,): 1, (0,): 0, (2,): 1}
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2223720034624
# {(1,): 1, (0,): 0, (2,): 1, (3,): 2}
# 2
# ----------------------------------------------------------
# Uzycie fibonacci 2
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Używam cache o ID: 2223720034624
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)
# Używam cache o ID: 2223720034624
# Funkcja: fiboacci((2,) -> 1)
# Używam cache o ID: 2223720034624
# 1
# ----------------------------------------------------------
# Uzycie fibonacci2
# {(1,): 1}
# {(1,): 1, (0,): 0}
# {(1,): 1, (0,): 0, (2,): 1}
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fibonaci2((1,) -> 1)
# Używam cache o ID: 2223720439168
# {(1,): 1, (0,): 0, (2,): 1, (3,): 2}
# 2