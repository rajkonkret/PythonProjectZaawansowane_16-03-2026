odp = input("Czy ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False


def odpowiedz(self):
    return "Tak! Ziemia jest płaska"


def nowa_odpowiedz(self):
    return "Nie! Ziemia jest elipsoidą"


def brak(self):
    return "brak odpowiedzi..."


class SednoOdpowiedzi(type):
    def __init__(cls, clsname, bases, attrs):
        if required:
            if attrs.get("n"):
                cls.odpowiedz = nowa_odpowiedz
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak


class Arystoteles(metaclass=SednoOdpowiedzi):
    pass


class Platon(metaclass=SednoOdpowiedzi):
    pass


class SwTomasz(metaclass=SednoOdpowiedzi):
    n = False


fil1 = Arystoteles()
print(f"Filozof {fil1.__class__.__name__} twierdzi: {fil1.odpowiedz()}")
# Czy ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n): t
# Filozof Arystoteles twierdzi: Tak! Ziemia jest płaska

fil2 = Platon()
print(f"Filozof {fil2.__class__.__name__} twierdzi: {fil2.odpowiedz()}")
# Filozof Arystoteles twierdzi: Tak! Ziemia jest płaska
# Filozof Platon twierdzi: Tak! Ziemia jest płaska

fil3 = SwTomasz()
print(f"Filozof {fil3.__class__.__name__} twierdzi: {fil3.odpowiedz()}")
# Filozof SwTomasz twierdzi: Tak! Ziemia jest płaska

# zadanie1:
# Klasa Kopernik
# ma odpowiadac: "Nie! Ziemia jest elipsoidą"
