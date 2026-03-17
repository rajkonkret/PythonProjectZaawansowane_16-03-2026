from func_wraps import dekorator
from cache import fibonacci
from obliczenia import podwojenie


def main():
    print("Przykład użycia dekoratora @wraps")

    @dekorator
    def wrap_przyklad():
        return "prosta funkcja"

    print(wrap_przyklad())
    # Przykład użycia dekoratora @wraps
    # inforacja:abc
    # Zakończenie
    # prosta funkcja

    print("_" * 50)
    print("Przykład użycia lru_cache")
    print(fibonacci(10))
    print(fibonacci.cache_info())
    # __________________________________________________
    # Przykład użycia lru_cache
    # 55
    # CacheInfo(hits=8, misses=11, maxsize=128, currsize=11)
    # hits - odczytał z cache
    # misses - liczył ponownie
    fibonacci.cache_clear()
    print(fibonacci.cache_info())
    # CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)

    print("_" * 50)
    print("Przykłąd użycia ** partial **")
    print(podwojenie(5))
    # __________________________________________________
    # Przykłąd użycia ** partial **
    # 10


if __name__ == '__main__':
    main()
