import time
import concurrent.futures
import multiprocessing

from funkcja_prime import find_the_sum_pime_nums

numbers = [(1, 10_000), (3, 50_000), (5_000, 100_000), (4, 9_000), (8_000, 15_000), (95_000, 133_000), (200, 67_540)]


def run_haveat_function(params):
    return find_the_sum_pime_nums(*params)


def multi():
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(run_haveat_function, numbers)
    end_time = time.time()
    print(f"Całkowity czas wykonania wszystkich sum (mulitiprocessing): {end_time - start_time} s")


def asynchronicznie():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        result = executor.map(run_haveat_function, numbers)
    end_time = time.time()
    print(f"Całkowity czas wykonania wszystkich sum (ProcessPoolExecutor): {end_time - start_time} s")


def main():
    multi()
    asynchronicznie()


if __name__ == '__main__':
    main()
# Całkowity czas wykonania wszystkich sum (mulitiprocessing): 11.013286113739014 s
# Całkowity czas wykonania wszystkich sum (ProcessPoolExecutor): 10.559108257293701 s
