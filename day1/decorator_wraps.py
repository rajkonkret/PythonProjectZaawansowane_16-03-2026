from functools import wraps
import inspect


def decor_no_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decor_with_wraps(func):
    @wraps(func)  # dostaniemy dodatkowe informacje o funkcji dekorowanej
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decor_no_wraps
def add(a: int, b: int) -> int:
    """Dodawanie dwie liczby"""
    return a + b


@decor_with_wraps
def mul(a: int, b: int) -> int:
    """Mnoży dwie liczby"""
    return a * b


print("=== Bezz @wraps ===")
print("name:", add.__name__)
print("qualname:", add.__qualname__)
print("doc:", add.__doc__)
print("annotations:", add.__annotations__)
print("has __wrapped__:", hasattr(add, "__wrapped__"))
# === Bezz @wraps ===
# name: wrapper
# qualname: decor_no_wraps.<locals>.wrapper
# doc: None
# annotations: {}
# has __wraped__: False


print("=== Bezz @wraps ===")
print("name:", mul.__name__)
print("qualname:", mul.__qualname__)
print("doc:", mul.__doc__)
print("annotations:", mul.__annotations__)
print("has __wrapped__:", hasattr(mul, "__wrapped__"))
# === Bezz @wraps ===
# name: mul
# qualname: mul
# doc: Mnoży dwie liczby
# annotations: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
# has __wrapped__: True
