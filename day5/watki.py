import threading


def print_cube(num):
    print(f"Sześcian wrtości {num} wynosi: {num ** 3}")


def print_square(num):
    print(f'Kwadrat wartości {num} wynosi: {num ** 2}')


t1 = threading.Thread(target=print_cube, args=(1000,))
t2 = threading.Thread(target=print_square, args=(100,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Zakończone")
# Sześcian wrtości 1000 wynosi: 1000000000
# Kwadrat wartości 100 wynosi: 10000
# Zakończone
# https://towardsdatascience.com/python-3-14-and-the-end-of-the-gil/
