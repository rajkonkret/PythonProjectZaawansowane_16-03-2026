import time


def pomiarczasu(funkcja):
    def wrapper():
        start_time = time.time()
        funkcja()
        end_time = time.time()
        wynik = end_time - start_time
        print(f"Czas wykonania funkcji: {wynik} s.")

    return wrapper


# usypiacz. opóznia wykonanie o 3 sekundy, zwraca wynik działąnia funkcji
def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()

    return wrapper


# kolejność dekoratorów ma znaczenie
@pomiarczasu
@usypiacz
def big_lista():
    sum([i ** 5 for i in range(10_000_000)])


big_lista()


# Czas wykonania funkcji: 5.676693677902222 s.

def debug(funkcja):
    def wrapper(*args):
        print(f"Wołąna funkcja: {funkcja.__name__}")
        funkcja(*args)

    return wrapper


@debug
def info(i):
    print(f"Ważny kod: {i}")


info(8457375375934096)


# Wołąna funkcja: info
# Ważny kod: 8457375375934096

# dekarator z parametrami
def spradz_typy(typy):
    def dekorator(funkcja):

        def wrapper(*args, **kwargs):
            for (arg, typ) in zip(args, typy):  # zip() - łaczy w pary
                print(arg, typ)
                if not isinstance(arg, typ):
                    raise TypeError(f"Argument: {arg} nie jest typu: {typ}")
            return funkcja(*args, **kwargs)

        return wrapper

    return dekorator


@spradz_typy((int, int))
def mnozenie(a, b):
    return a * b


try:
    mnozenie(6, 8)
    mnozenie(6, "osiem")
except TypeError as e:
    print("Bład:", e)


# 6 <class 'int'>
# 8 <class 'int'>
# 6 <class 'int'>
# osiem <class 'int'>
# Bład: Argument: osiem nie jest typu: <class 'int'>

# zasymulowac cache dla funkcji
# jesli funkcja wywołąna z argumentami jakie znamy juz -> wynik z cache
# w przeciwnym wypadku dokonac nowego obliczenia i zwrócic wynik

def memoizacja(funkcja):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Zwracamy wynik z cache dla argumentów: {args}")
            print(f"Funkcja: {funkcja.__name__}({args} -> {funkcja(*args)})")
            return cache[args]
        else:
            wynik = funkcja(*args)
            cache[args] = wynik
            return wynik

    return wrapper


@memoizacja
def fiboacci(n):
    if n <= 1:
        return n
    else:
        return fiboacci(n - 1) + fiboacci(n - 2)


print(fiboacci(10))
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Zwracamy wynik z cache dla argumentów: (2,)
# Zwracamy wynik z cache dla argumentów: (1,)
# Funkcja: fiboacci((1,) -> 1)
# Zwracamy wynik z cache dla argumentów: (0,)
# Funkcja: fiboacci((0,) -> 0)
