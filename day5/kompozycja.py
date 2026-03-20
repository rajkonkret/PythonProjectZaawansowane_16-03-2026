class KontrolerSamochodu(type):
    def __new__(cls, name, bases, attrs):
        print(f"Tworzenei klasy samochodu: {name}")
        attrs['informacje'] = lambda self: f"Model: {self.model}, moc silnika: {self.silnik.moc}"
        return super().__new__(cls, name, bases, attrs)


class Silnik:
    def __init__(self, moc):
        self.moc = moc

    def uruchom(self):
        return f"Silnik o mocy {self.moc} KM został uruchomiony!"


class Samochod(metaclass=KontrolerSamochodu):
    def __init__(self, model, moc_silnik):
        self.model = model
        self.silnik = Silnik(moc_silnik)

    def uruchom_samochod(self):
        return f"Smochód {self.model}: {self.silnik.uruchom()}"


silnik1 = Silnik(150)
print(silnik1.uruchom())  # Silnik o mocy 150 KM został uruchomiony!

samochod1 = Samochod("Tesla Mosel S", 670)
print(samochod1.uruchom_samochod())  # Smochód Tesla Mosel S: Silnik o mocy 670 KM został uruchomiony!

print(samochod1.informacje())  # Model: Tesla Mosel S, moc silnika: 670
