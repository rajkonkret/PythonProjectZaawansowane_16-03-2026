class MojaMeta(type):
    def __new__(cls, clsname, superclass, attrs):
        print(f"--- {cls.__class__.__name__} ---")
        print(f'Nazwa kalsy: {clsname}')
        print(f"Klasy dziedziczone: {superclass}")
        print(f"Słownik atrybutów klasy: {attrs}")

        return type.__new__(cls, clsname, superclass, attrs)

    def jedynka(cls):
        return 1


class S:
    pass


class F:
    pass


class Specjalna(S, metaclass=MojaMeta):
    pass


# --- type ---
# Nazwa kalsy: Specjalna
# Klasy dziedziczone: (<class '__main__.S'>,)
# Słownik atrybutów klasy: {'__module__': '__main__', '__qualname__': 'Specjalna', '__firstlineno__': 22, '__static_attributes__': ()}

class B(Specjalna):
    pass


class C(F, B):

    @property
    def info(self):
        print("abc...")


# --- type ---
# Nazwa kalsy: C
# Klasy dziedziczone: (<class '__main__.F'>, <class '__main__.B'>)
# Słownik atrybutów klasy: {'__module__': '__main__', '__qualname__': 'C', '__firstlineno__': 35, 'info': <property object at 0x00000251D2A999E0>, '__static_attributes__': (), '__classdictcell__': <cell at 0x00000251D2A9E4A0: dict object at 0x00000251D2A36440>}

class D(F):
    pass


obiekt_c = C()
# print(obiekt_c.jedynka()) # AttributeError: 'C' object has no attribute 'jedynka'

klasa_c = C
print(type(obiekt_c))  # <class '__main__.C'>
print(type(klasa_c))  # <class '__main__.MojaMeta'>

print(klasa_c.jedynka())  # 1
