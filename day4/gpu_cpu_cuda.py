import numpy as np
from numba import cuda
from timeit import default_timer as timer


@cuda.jit
def gpu_function(a):
    i = cuda.grid(1)
    if i < a.size:
        a[i] += 1


n = 10_000_000
a = np.ones(n, dtype=np.float64)

a_gpu = cuda.to_device(a)

threads_per_block = 256
blocks_per_grid = (n + threads_per_block - 1) // threads_per_block

start = timer()
gpu_function[blocks_per_grid, threads_per_block](a_gpu)
cuda.synchronize()  # czekanie na koniec działąń na karcie graficznej
print("GPU CUDA:", timer() - start)

# kopiowanie danych z gpu
a = a_gpu.copy_to_host()
# GPU CUDA: 0.04906726299998354
# https://colab.research.google.com/drive/1-IQ9TGtZL7phJNWv2xhpkjXPm7UMJRYs#scrollTo=oKKdsoJoXyYM
