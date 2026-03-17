#    A
#   / \
# B    C
#  \  /
#   D

class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__ start")
        A.__init__(self)
        print("B.__init__ end")


class C(A):
    def __init__(self):
        print("C.__init__ start")
        A.__init__(self)
        print("C.__init__ end")


class D(B, C):
    def __init__(self):
        print("D.__init__ start")
        B.__init__(self)
        C.__init__(self)
        print("D.__init__ end")
