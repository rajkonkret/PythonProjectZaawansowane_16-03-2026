class Exam:
    def __init__(self):
        self._part_a = 0
        self._part_b = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError("Ocena musi być wartością z przeziału 0-100!")

    @property
    def part_a_grade(self):
        return self._part_a

    @part_a_grade.setter
    def part_a_grade(self, value):
        self._check_grade(value)
        self._part_a = value

    @property
    def part_b_grade(self):
        return self._part_b

    @part_b_grade.setter
    def part_b_grade(self, value):
        self._check_grade(value)
        self._part_b = value
