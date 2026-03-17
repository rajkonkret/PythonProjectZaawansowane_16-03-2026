class CacheFunction:

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print(f"Wynik w cache dla argumentów: {args}")
            return self.cache[args]

        print(f"Wynik obliczeń dla argumentó: {args}")
        result = self.func(*args)
        self.cache[args] = result
        return result
