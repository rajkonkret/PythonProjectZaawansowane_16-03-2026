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
        yield i  # zwraca wartość, zapamiętuje krok w którym zakończył


print(gen_liczby())  # <generator object gen_liczby at 0x0000023ACE598FB0>

print(list(gen_liczby()))

for p in gen_liczby():
    print(p)
    # time.sleep(1)

gen = gen_liczby()
print(next(gen))
print(next(gen))
print("Inna operacja")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# StopIteration

def wznowienie(n, k):
    print("Wstrzymanie działania")
    yield 3005

    print("Wznowienie działania 1")
    yield n + k

    print("Wznowienie działania 2")
    n = 8 * k - 4
    yield n - k

    print("Wznowienie działanai 3")
    yield n * k

    print("Wznowienie działania 4")
    yield n / k

    print("Wznowienie działania 5")


print(wznowienie(8, 4))

print(list(wznowienie(8, 4)))


# <generator object wznowienie at 0x0000025B39D98FB0>
# Wstrzymanie działania
# Wznowienie działania 1
# Wznowienie działania 2
# Wznowienie działanai 3
# Wznowienie działania 4
# Wznowienie działania 5
# [3005, 12, 24, 112, 7.0]

def gen2():
    n = 1
    while True:
        result = yield n
        print(result)
        if result == "stop":
            break
        n += 1
        print(n)
        print(50 * "-")


g2 = gen2()
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

g2.send("OK")  # OK

print(next(g2))

try:
    g2.send("stop")  # StopIteration
except StopIteration as e:
    print("Koniec danych:", e)


# Koniec danych:

def send_gen():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x + 1
        else:
            x = 3 * y


g = send_gen()
print("_" * 60)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(122))
print(next(g))
print(next(g))
print(g.send(15))
print(next(g))
print(g.send("a"))
# 5
# 366
# 367
# 368
# 45
# 46
# aaa