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


def weak_dict_example():
    print("--- WeakKeyDictionary ---")
    d = WeakKeyDictionary()

    u = User("Adam")
    d[u] = "dane Adama"

    print("Przed usunięciem zmiennej")
    print(dict(d))

    u = None
    gc.collect()  # uruchomienie garbage collectora

    print("Po u = None i gc.collect():")
    print(dict(d))
    print("Wpis znika, WeakKeyDictionary nie trzyma klucza przy życiu ")


normal_dict_example()
# --- Zwykły dict ---
# Przed usunięciem zmiennej
# {User('Jan'): 'dane Jana'}
# Po u = None i gc.collect():
# {User('Jan'): 'dane Jana'}
# Obiekt nadal żyje
# USUWAM obiekt: Jan

weak_dict_example()
# --- WeakKeyDictionary ---
# Przed usunięciem zmiennej
# {User('Adam'): 'dane Adama'}
# USUWAM obiekt: Adam
# Po u = None i gc.collect():
# {}
# Wpis znika, WeakKeyDictionary nie trzyma klucza przy życiu
