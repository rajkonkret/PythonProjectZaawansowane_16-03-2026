import sys
import math
from joblib import Parallel, delayed

# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

sys.set_int_max_str_digits(1_000_000)


def compute_tactorial(n):
    print(f"Obliczenia silnii {n}")
    return math.factorial(n)


numbers = [5, 7, 19, 112, 180, 260, 400, 10000]

# standardowo na procesach
# result = Parallel(n_jobs=4)(
#     delayed(compute_tactorial)(n) for n in numbers
# )

# result = Parallel(n_jobs=4, backend="threading")(
#     delayed(compute_tactorial)(n) for n in numbers
# )

# -1 wszystkie dostępne rdzenie CPU
result = Parallel(n_jobs=-1)(
    delayed(compute_tactorial)(n) for n in numbers
)
print("wyniki silnia:", result)
