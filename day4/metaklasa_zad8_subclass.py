class Base:

    # uruchamiane, gdy tworzymy klasę dziedziczącą po tej klasie
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Tworzę podklasę {cls.__name__}")


class Child(Base):
    pass  # Tworzę podklasę Child


class Animal:
    all_animals = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Animal.all_animals.append(cls)


class Dog(Animal):
    pass


class Cat(Animal):
    pass


print([c.__name__ for c in Animal.all_animals])
# ['Dog', 'Cat']
