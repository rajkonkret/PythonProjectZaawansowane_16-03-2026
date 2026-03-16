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
