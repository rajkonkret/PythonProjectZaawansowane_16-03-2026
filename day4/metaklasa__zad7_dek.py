def class_decorator(cls):
    cls.extra = 123
    return cls


@class_decorator
class A:
    pass


print(A.extra)  # 123


class Meta(type):
    def __new__(cls, name, bases, namespace):
        namespace['extra'] = 123
        return super().__new__(cls, name, bases, namespace)


class B(metaclass=Meta):
    pass


print(B.extra)  # 123
