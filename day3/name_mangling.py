# name_mangling - zaciemnie widoczności poprzez manipulację nazwą

class Car:

    def __init__(self, model, year):
        # self._model = model
        # self._year = year
        self.__model = model
        self.__year = year

    def wypisz_model(self):
        print(self.__model)


car = Car("Volvo", 2025)
# print(car._model)  # Volvo
# car._model = "Audi"
# print(car._model)  # Audi
# AttributeError: 'Car' object has no attribute '_model' dla __model
car.wypisz_model()  # Volvo
car.__model = "Renault"
car.wypisz_model()  # Volvo
print(car._Car__model)  # Volvo -> idea name mangling
print(car.__model)  # Renault
