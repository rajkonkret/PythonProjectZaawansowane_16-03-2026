class RegistryMeta(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "BasePlugin":
            mcls.registry[name] = cls
        return cls


class BasePlugin(metaclass=RegistryMeta):
    pass


class CsvPlugin(BasePlugin):
    pass


class JsonPlugin(BasePlugin):
    pass


print(RegistryMeta.registry)
# {'CsvPlugin': <class '__main__.CsvPlugin'>, 'JsonPlugin': <class '__main__.JsonPlugin'>}
