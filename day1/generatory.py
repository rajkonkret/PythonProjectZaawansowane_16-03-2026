# generatory
import time


def liczby():
    wynik = []
    for i in range(31):
        wynik.append(i)

    return wynik


print(liczby())


def gen_liczby():
    for i in range(31):
        yield i


print(gen_liczby())  # <generator object gen_liczby at 0x0000023ACE598FB0>

print(list(gen_liczby()))

for p in gen_liczby():
    print(p)
    time.sleep(1)
