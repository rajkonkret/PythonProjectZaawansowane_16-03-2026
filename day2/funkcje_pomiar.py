import time
import operator
from functools import partial
import numpy as np


def pomiarczasu(funkcja):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        funkcja(*args, **kwargs)
        end_time = time.time()
        wynik = end_time - start_time
        print(f"Czas wykonania funkcji: {wynik} s.")

    return wrapper


@pomiarczasu
def my_wait(num):
    time.sleep(2)


# zsumowac liczby od 0 do 14_999_999


@pomiarczasu
def my_for_sum(num):
    total = 0
    for i in range(num):
        total += i
    print("sum is:", total)


@pomiarczasu
def my_sum_without_for(num):
    total = sum(range(num))
    print("sum is:", total)


@pomiarczasu
def my_sum_np(num):
    total = np.sum(np.arange(num), dtype=np.int64)
    print("Sum is:", total)


num = 150_000_000
my_wait(150_000_000)  # Czas wykonania funkcji: 2.000502824783325 s.
my_for_sum(150_000_000)
my_sum_without_for(150_000_000)
my_sum_np(150_000_000)
# Czas wykonania funkcji: 2.000542640686035 s.
# sum is: 112499992500000
# Czas wykonania funkcji: 1.2687098979949951 s.
# sum is: 112499992500000
# Czas wykonania funkcji: 0.2558426856994629 s.
# Sum is: 112499992500000
# Czas wykonania funkcji: 0.06603813171386719 s.

# dla 150_000_000
# Czas wykonania funkcji: 2.000274658203125 s.
# sum is: 11249999925000000
# Czas wykonania funkcji: 6.8767735958099365 s.
# sum is: 11249999925000000
# Czas wykonania funkcji: 2.1878318786621094 s.
# Sum is: 11249999925000000
# Czas wykonania funkcji: 0.5510263442993164 s.
print(6.876 / 0.5010)  # 12.47912885662432
print(1.268 / 0.066)  # 19.21212121212121

print(50 * "-")
lista = list(range(1_000_000))


@pomiarczasu
def my_for_mul():
    l = []
    for i in lista:
        l.append(i * 2)


funkcja = lambda x: x * 2


@pomiarczasu
def my_for_with_map_mul():
    l_map = list(map(funkcja, lista))


@pomiarczasu
def my_for_list_compre():
    l = [i * 2 for i in lista]


@pomiarczasu
def my_for_with_map_operator():
    l_map = list(map(partial(operator.mul, 2), lista))


my_for_mul()
my_for_with_map_mul()
my_for_list_compre()
# --------------------------------------------------
# Czas wykonania funkcji: 0.09656953811645508 s.
# Czas wykonania funkcji: 0.11460494995117188 s.
# Czas wykonania funkcji: 0.0792994499206543 s.
my_for_with_map_operator()
# --------------------------------------------------
# Czas wykonania funkcji: 0.09587359428405762 s.
# Czas wykonania funkcji: 0.11596465110778809 s.
# Czas wykonania funkcji: 0.08292293548583984 s.
# Czas wykonania funkcji: 0.08803892135620117 s.