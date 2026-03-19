class RenameMeta(type):
    def __new__(cls, name, bases, namespace):
        new_namespace = {}

        for attr_name, attr_value in namespace.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                new_namespace[f"meta_{attr_name}"] = attr_value
            else:
                new_namespace[attr_name] = attr_value

        return super().__new__(cls, name, bases, new_namespace)


class Demo(metaclass=RenameMeta):
    def hello(self):
        return "Hello"


d = Demo()
print(d.meta_hello())

print(d.hello())  # AttributeError: 'Demo' object has no attribute 'hello'
