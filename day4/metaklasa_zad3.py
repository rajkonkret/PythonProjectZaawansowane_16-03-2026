class RequireRunMeta(type):
    def __new__(cls, name, bases, namespace):
        cls = super().__new__(cls, name, bases, namespace)
        if name != "BaseTask" and "run" not in namespace:
            raise TypeError(f"Klasa {name} musi definiować metodę run()")
        return cls


class BaseTask(metaclass=RequireRunMeta):
    pass


class GoodTask(BaseTask):
    def run(self):
        print("OK")


class BadTask(BaseTask):
    pass
#     raise TypeError(f"Klasa {name} musi definiować metodę run()")
# TypeError: Klasa BadTask musi definiować metodę run()