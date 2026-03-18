import gc
from weakref import WeakKeyDictionary


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({self.name!r})"

    def __del__(self):
        print(f'USUWAM obiekt: {self.name}')


