class Grade:
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        print("GET deskryptor id:", id(self))
        print("Instance id:", id(instance))
        return self._value

    def __set__(self, instance, value):
        print("SET deskryptor id:", id(self))
        print("Instance id:", id(instance))
        if not (0 <= value <= 100):
            raise ValueError("Ocena musi być wartością z przedziało 0-100!!!")
        self._value = value


class ExamG:
    math_grade = Grade()
    alg_grade = Grade()
    prog_grade = Grade()
