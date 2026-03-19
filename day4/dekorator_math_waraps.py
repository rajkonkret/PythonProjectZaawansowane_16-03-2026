from functools import wraps


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Pełna nazwa metody: {func.__qualname__}')
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for key, val in vars(cls).items():
        print(key, val)
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


@debugmethods
class Calc:
    def add(self, x, y):
        return (x + y) * 10

    def mul(self, x, y):
        return x * y * 100

    def div(self, x, y):
        return x / (y + 10)

    @property
    def wart(self):
        return self.add(5, 6) + self.mul(5, 2)

    @property
    def stala(self):
        return 9.81


mc = Calc()

print(mc.add(4, 7))
# Pełna nazwa metody: Calc.add
# 110
print(mc.mul(4, 7))
# Pełna nazwa metody: Calc.mul
# 2800
print(mc.div(4, 7))
# Pełna nazwa metody: Calc.div
# 0.23529411764705882

print(mc.wart)
# Pełna nazwa metody: Calc.add
# Pełna nazwa metody: Calc.mul
# 1110

print(mc.stala)  # 9.81 -> to nie jest funkcja
