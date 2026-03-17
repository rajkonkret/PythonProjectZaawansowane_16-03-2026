from functools import wraps


def dekorator(funkcja):
    @wraps(funkcja)  # przekazuje dodatkowe infoemacje o funkcji do wrappera
    def wrapper(*args, **kwargs):
        print("inforacja:abc")
        wynik = funkcja(*args, **kwargs)
        print("Zakończenie")
        return wynik

    return wrapper
