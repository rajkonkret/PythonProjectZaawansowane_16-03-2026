from dataclasses import dataclass


@dataclass
class Dane:
    nazwa: str
    licznik: int
    cena: float = 10.00

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self, me):
        self._licznik = me


p = Dane("Pudełko", 4, 11.67)
print(p)  # Dane(nazwa='Pudełko', licznik=4, cena=11.67)
print(p.licznik)  # 4
p.licznik = 56
print(p)  # Dane(nazwa='Pudełko', licznik=56, cena=11.67)
print(p.__dict__)  # {'nazwa': 'Pudełko', '_licznik': 56, 'cena': 11.67}

p.imie = "Tomek"
print(p)
# Dane(nazwa='Pudełko', licznik=56, cena=11.67)
print(p.imie)


# Tomek

# użycie __slots__ z dataclass

@dataclass(slots=True)
class People:
    name: str
    age: str


u = People("Tomek", 30)
print(u.name)
# u.imie = "Zenek" # AttributeError: 'People' object has no attribute 'imie' and no __dict__ for setting new attributes

u.age = 123
print(u.age)  # 123
