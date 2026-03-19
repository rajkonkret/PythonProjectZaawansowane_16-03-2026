# można tworzyc klasy za pomocą type()

B = type("B", (), {"x": 20})
print(B.x)  # 20
print(B.__dict__)
# {'x': 20, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None}

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass
# class ABC(metaclass=ABCMeta):
#     """Helper class that provides a standard way to create an ABC using
#     inheritance.
#     """
#     __slots__ = ()
