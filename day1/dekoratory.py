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


