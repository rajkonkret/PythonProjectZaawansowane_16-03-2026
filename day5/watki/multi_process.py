import multiprocessing
import os


# CPU Bound


def compute_square(n):
    print(f"Proces {os.getpid()} oblicza kwadrat {n}")
    return n ** 2


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 11, 13, 24, 28, 30]

    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(compute_square, numbers)

    print(f"Kwadraty n: {result}")
# Kwadraty n: [1, 4, 9, 16, 25, 121, 169, 576, 784, 900]
