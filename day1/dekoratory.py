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
