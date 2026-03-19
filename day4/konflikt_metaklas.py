class MetaA(type):
    pass


class MetaB(type):
    pass


class A(metaclass=MetaA):
    pass


class B(metaclass=MetaB):
    pass


# class C(A, B):
#     pass
# TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

# obejście problemu
class MetaAB(MetaA, MetaB):
    pass


class C(A, B, metaclass=MetaAB):
    pass
