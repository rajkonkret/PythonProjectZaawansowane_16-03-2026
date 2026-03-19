"""
Dekorator do zarządzania stanem obiektu: np.: status aktywności
__getattribute__
"""


def state_manager(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            self._state = "inactive"
            super().__init__(*args, **kwargs)

        def activate(self):
            self._state = "active"

        def deactivate(self):
            self._state = "inactive"

        def get_state(self):
            return self._state

        def __getattribute__(self, item):
            value = super().__getattribute__(item)
            if item == 'run_fast' and self._state == "inactive":
                raise ValueError("Obiekt jest nieaktywny")
            return value

    return Wrapped


@state_manager
class User:
    def __init__(self, name):
        self.name = name

    def run_fast(self):
        print(f"{self.name} is runing very fast!")


user = User("Tomek")
print(user.get_state())

user.activate()
print(user.get_state())  # active

user.run_fast()  # Tomek is runing very fast!

# sprawdzenie stanu
try:
    user.deactivate()
    user.run_fast()
    print(user.get_state())
except ValueError as e:
    print(e)
# Obiekt jest nieaktywny
