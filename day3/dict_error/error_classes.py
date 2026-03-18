# https://naukapythona.com.pl/
class InFloatValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Wartość {self.value} jest niewłaściwa! Akceptowalne są tylko wartośći w typie: int i float!"


class KeyValueConstructorError(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return (f"""
                Klucze i wartości winny być przekazane do słownika w listach lub krotkach...
                klucz: {self.key} jest w typie {type(self.key)},
                wartość: {self.value} jest w typie {type(self.value)}.
                """)
