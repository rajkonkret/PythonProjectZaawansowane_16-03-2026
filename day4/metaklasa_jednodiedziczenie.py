def logger(self, m, n):
    return f"{m}: {n}"


class MultiBases(type):
    def __new__(cls, name, bases, attr):
        print(len(bases))
        if len(bases) > 1:
            raise TypeError("Możliwe jest tylko jednodziedziczenie!")
        return super().__new__(cls, name, bases, attr)

    def __init__(self, name, bases, attr):
        self.logger = logger


class Base(metaclass=MultiBases):
    pass


class A(Base):
    pass


class B(A):
    pass


class Extra:
    pass


# TypeError: Możliwe jest tylko jednodziedziczenie!
# class Test(Extra, B):
#     pass

b = B()

print(f"{b.logger(23, 'info A')}")


# 23: info A

def policz(self, x, y):
    return x - 2 * y


B.logger = policz
c = B()
print(c.logger(13, 5))  # 3


class C(B):
    pass


ob = C()
print(ob.logger(2, 1))
# 2: 1
