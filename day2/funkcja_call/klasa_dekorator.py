class debug:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"[{self.name}] calling {func.__name__}")
            return func(*args, **kwargs)

        return wrapper


def f(x):
    return x + 1

print(f(10))
