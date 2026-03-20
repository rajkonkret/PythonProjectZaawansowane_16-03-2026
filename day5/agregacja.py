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
    def __init__(self, model, silnik: Silnik):
        self.model = model
        self.silnik = silnik

    def uruchom_samochod(self):
        return f"Samochod {self.model}: {self.silnik.uruchom()}"


silnik1 = Silnik(150)  # Tworzenei klasy samochodu: Samochod
samochod1 = Samochod("VW Scirocco", silnik1)
print(samochod1.uruchom_samochod())
# Samochod VW Scirocco: Silnik o mocy 150 KM został uruchomiony!
print(samochod1.informacje())
# Model: VW Scirocco, moc silnika: 150
