import gc
from weakref import WeakKeyDictionary


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({self.name!r})"

    def __del__(self):
        print(f'USUWAM obiekt: {self.name}')


def normal_dict_example():
    print("--- Zwykły dict ---")
    d = {}

    u = User("Jan")
    d[u] = "dane Jana"

    print("Przed usunięciem zmiennej")
    print(d)

    u = None
    gc.collect()

    print("Po u = None i gc.collect():")
    print(d)
    print("Obiekt nadal żyje")

normal_dict_example()
# --- Zwykły dict ---
# Przed usunięciem zmiennej
# {User('Jan'): 'dane Jana'}
# Po u = None i gc.collect():
# {User('Jan'): 'dane Jana'}
# Obiekt nadal żyje
# USUWAM obiekt: Jan