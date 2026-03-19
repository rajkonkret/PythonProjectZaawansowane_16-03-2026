class Zwierze:
    def daj_odglos(self):
        raise NotImplementedError("subklasa musi mieć zaimplementowana metodę")


class Pies(Zwierze):
    def daj_odglos(self):
        return "hau hau"


class Kot(Zwierze):
    def daj_odglos(self):
        return "miau miau"


class Swinia(Zwierze):
    def hodowla(self, gdzie):
        return f"Zwierze hodowane w {gdzie}"


zw1 = Pies()
zw2 = Kot()
zw3 = Swinia()

print(zw1.daj_odglos())  # hau hau
print(zw2.daj_odglos())  # miau miau

print(zw3.hodowla("chlew"))  # Zwierze hodowane w chlew

# print(zw3.daj_odglos())  # NotImplementedError: subklasa musi mieć zaimplementowana metodę
