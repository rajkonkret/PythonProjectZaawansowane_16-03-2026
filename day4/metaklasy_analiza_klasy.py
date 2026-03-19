class Field:
    def __init__(self):
        self.name = None


class ModelMeta(type):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        cls._fields = {}

        for attr_name, attr_value in namespace.items():
            if isinstance(attr_value, Field):
                attr_value.name = attr_name
                cls._fields[attr_name] = attr_value
        return cls


class Model(metaclass=ModelMeta):
    pass


class User(Model):
    name = Field()
    age = Field()


print(User._fields)
# {'name': <__main__.Field object at 0x0000028B89C28AD0>, 'age': <__main__.Field object at 0x0000028B89C18A50>}
print(User.name.name)  # name
