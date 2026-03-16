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
