class Osoba:
    def __init__(self, imie, nazwisko, wiek, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost

    def get_waga(self):
        return self.waga

    def set_waga(self, nowa_waga):
        self.waga = nowa_waga

    @property  # odpowiednik gettera
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        self._wiek = nowy_wiek

    @property
    def bmi(self):
        return self.waga / (self.wzrost / 100) ** 2


os = Osoba("Jan", "Kos", 30, 89, 176)
print(os)
print(os.get_waga())
os.set_waga(98)
print(os.get_waga())
# 89
# 98

print(os.wiek)  # uruchamiamy @property, 30

os.wiek = 38
print(os.wiek)  # 38

print(os.waga)

print(f"{os.bmi}")  # 31.63739669421488

os.set_waga(87)
os.wzrost = 190
print(os.bmi)  # 24.099722991689752
