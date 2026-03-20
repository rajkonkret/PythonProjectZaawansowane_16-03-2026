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
            # if attrs.get("n"): # nie pokazuje dziedziczonych
            if getattr(cls, "n", False):
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

class Kopernik(metaclass=SednoOdpowiedzi):
    n = True


fil4 = Kopernik()
print(f"Filozof {fil4.__class__.__name__} twierdzi: {fil4.odpowiedz()}")


# Filozof Kopernik twierdzi: Nie! Ziemia jest elipsoidą

# zad2
# przebudować rozwiązanie tak, żeby można było dodać dowolnych filozofów nowożytnych
#  Nie! Ziemia jest elipsoidą

class FilozofNowozytny(metaclass=SednoOdpowiedzi):
    n = True


fil5 = FilozofNowozytny()
print(f"Filozof {fil5.__class__.__name__} twierdzi: {fil5.odpowiedz()}")


# Filozof FilozofNowozytny twierdzi: Nie! Ziemia jest elipsoidą

class Koeprnik2(FilozofNowozytny):
    pass


fil6 = Koeprnik2()
print(f"Filozof {fil6.__class__.__name__} twierdzi: {fil6.odpowiedz()}")


# Czy ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n): t
# Filozof Arystoteles twierdzi: Tak! Ziemia jest płaska
# Filozof Platon twierdzi: Tak! Ziemia jest płaska
# Filozof SwTomasz twierdzi: Tak! Ziemia jest płaska
# Filozof Kopernik twierdzi: Nie! Ziemia jest elipsoidą
# Filozof FilozofNowozytny twierdzi: Nie! Ziemia jest elipsoidą
# Filozof Koeprnik2 twierdzi: Nie! Ziemia jest elipsoidą

class Einstein(FilozofNowozytny):
    pass


fil7 = Einstein()
print(f"Filozof {fil7.__class__.__name__} twierdzi: {fil7.odpowiedz()}")


# Filozof Einstein twierdzi: Nie! Ziemia jest elipsoidą

class Galileusz(FilozofNowozytny):
    pass


fil8 = Galileusz()
print(f"Filozof {fil8.__class__.__name__} twierdzi: {fil8.odpowiedz()}")
# Filozof Galileusz twierdzi: Nie! Ziemia jest elipsoidą
