from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer


def cpu_function(a):
    for i in range(10_000_000):
        a[i] += 1


@jit(nopython=True)  # uzycie LLVM
def gpu_function(a):
    for i in range(10_000_000):
        a[i] += 1


if __name__ == '__main__':
    n = 10_000_000
    a = np.ones(n, dtype=np.float64)

    start = timer()
    cpu_function(a)
    print(f"Czas wykonania na CPU: {timer() - start}")

    start = timer()
    gpu_function(a)
    print(f"Czas wykonania na GPU: {timer() - start}")

    n = 20_000_000
    a = np.ones(n, dtype=np.float64)
    start = timer()
    gpu_function(a)
    print(f"Czas wykonania na GPU (2): {timer() - start}")

    start = timer()
    gpu_function(a)
    print(f"Czas wykonania na GPU (3): {timer() - start}")
