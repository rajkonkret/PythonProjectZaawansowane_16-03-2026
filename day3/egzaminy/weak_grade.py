from weakref import WeakKeyDictionary


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Ocena musi być wartością zprzedziału 0-100!")
        self._values[instance] = value


class ExamH:
    math_grade = Grade()
    alg_grade = Grade()
    prog_grade = Grade()
