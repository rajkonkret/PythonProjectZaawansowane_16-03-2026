class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_cose = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyValidator:

    @staticmethod
    def is_int(value, name):
        if not isinstance(value, int):
            raise MyTypeError(f"{name} must be integer")

    @staticmethod
    def not_zero(value, name):
        if value == 0:
            raise MyValueError(f"{name} cannot be zero")


def my_function(x: int, y: int) -> float:
    MyValidator.is_int(x, "x")
    MyValidator.is_int(y, "y")
    MyValidator.not_zero(y, "y")


try:
    my_function(1, 2)
    my_function(1, "2")
except MyTypeError as e:
    print("Błąd:", e)
# Błąd: y must be integer
