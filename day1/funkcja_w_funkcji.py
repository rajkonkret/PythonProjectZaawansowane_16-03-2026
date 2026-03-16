from typing import Any

print("Kilka przykładów funkcji")


def witaj(imie: str) -> str:
    return f"Miło Cię widzieć {imie}"


def konkurs(imie: str, punkty: int, miejsca: int) -> str:
    return f"Uczestnik konkuru {imie}, liczba punktów: {punkty}, zajęte miejsca: {miejsca}"


def bonus(punkty: int, bonus: float) -> float:
    return punkty * bonus


def osoba(funkcja: Any, *args) -> Any:
    return funkcja(*args)


# funkcje wyższego rzędu
print(osoba(witaj, "leon"))
print(osoba(konkurs, "Anna", 78, 9))
print(osoba(bonus, 66, 0.2))


# Kilka przykładów funkcji
# Miło Cię widzieć leon
# Uczestnik konkuru Anna, liczba punktów: 78, zajęte miejsca: 9
# 13.200000000000001

# dekorator
# przyjmuje inną funkcję
# zwraca wynik tej funkci plus dodakowe działanie

def startstop(funkcja):
    def wrapper(*args, **kwargs):
        print(60 * "-")
        print("Startowanie procesu...")
        funkcja(*args, **kwargs)
        print("Kończenie procesu....")

    return wrapper  # zwróći adres, referencję


def zawijanie(w_co):
    print(f"Zawijanie czekoladek w {w_co}")


zw = startstop(zawijanie)
print(zw)  # <function startstop.<locals>.wrapper at 0x0000013A4976D7A0>
print(type(zw))  # <class 'function'>
zw("sreberka")


# ------------------------------------------------------------
# Startowanie procesu...
# Zawijanie czekoladek w sreberka
# Kończenie procesu....

@startstop
def dmuchanie(czego):
    print(f"Dmuchanie {czego} na urodziny")


dmuchanie("baloników")
# ------------------------------------------------------------
# Startowanie procesu...
# Dmuchanie baloników na urodziny
# Kończenie procesu....

dmuchanie("Świeczek na torcie")
# ------------------------------------------------------------
# Startowanie procesu...
# Dmuchanie Świeczek na torcie na urodziny
# Kończenie procesu....

liczby = [45, 262, 5, 8, 49, -3, 53, 25, 22, 12, 48, 90, 32, 8, 7, 3, 2]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)

cube = list(map(lambda x: x ** 2, liczby))
print(cube)
# [2025, 68644, 25, 64, 2401, 9, 2809, 625, 484, 144, 2304, 8100, 1024, 64, 49, 9, 4]

# list coprehension
dane = [i ** 2 for i in range(100)]
print(dane)
