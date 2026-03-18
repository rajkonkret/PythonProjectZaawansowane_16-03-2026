"""
Przygotuj obsługę błędu dla następujących przypadków:
Utwórz klasę CustomIntFloatDict za pomocą której bedziesz tworzyć nowe słowniki,
zadając klucze i wartości w odrębnych kolekcjach - jedyne dopuszczalne kolekcje to: list i tuple
typ wartości w słowniku to jedynie int lub float!
Utwórz do obsługi błędu dwie klasy błędu:
1. IntFloatValueError - reakcja na wartości słownika inne niż int i float
2. KeyValueConstruktorError - reakcja na przekazanie kluczy i wartości w niewłasciym typie (tylko list i tuple)
"""
from error_classes import InFloatValueError, KeyValueConstructorError


class CustomIntFloatDict(dict):

    def __init__(self, key=None, value=None):
        if key is None or value is None:
            return None
        elif not isinstance(key, (tuple, list)) or not isinstance(value, (tuple, list)):
            raise KeyValueConstructorError(key, value)
        else:
            zipped = zip(key, value)
            for k, val in zipped:
                if not isinstance(val, (int, float)):
                    raise InFloatValueError(val)
                # self[k] = val # moze doprowadzic do problemu zagnieżdzonej recursji
                # dict.__setitem__(self, k, val)
                super().__setitem__(k, val)


test_1 = CustomIntFloatDict()
print(test_1)  # {}

test_2 = CustomIntFloatDict(('a', 'b'))
print(test_2)

# test_3 = CustomIntFloatDict({'a', 'b'}, [6,3])
# print(test_3)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\AI\PythonProjectZaawansowane_16-03-2026\day3\dict_error\main.py", line 36, in <module>
#     test_3 = CustomIntFloatDict({'a', 'b'}, [6,3])
#   File "C:\Users\CSComarch\AI\PythonProjectZaawansowane_16-03-2026\day3\dict_error\main.py", line 19, in __init__
#     raise KeyValueConstructorError(key, value)
# error_classes.KeyValueConstructorError:
#                 Klucze i wartości winny być przekazane do słownika w listach lub krotkach...
#                 klucz: {'a', 'b'} jest w typie <class 'set'>,
#                 wartość: [6, 3] jest w typie <class 'list'>.

test_4 = CustomIntFloatDict(("x", "y", "z"), (10, 20, 30))
print(test_4)  # {'x': 10, 'y': 20, 'z': 30}
