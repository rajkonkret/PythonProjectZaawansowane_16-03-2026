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
