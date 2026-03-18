# uzycie tego samego deskryptora na dwóch różznych polach

class Descriptor:

    # mozemy używac dla róznych pól tego samego deskryptora
    def __set__name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Person:
    age = Descriptor()
    height = Descriptor()


p = Person()
p.age = 30
p.height = 100

print(p.age)
print(p.height)
