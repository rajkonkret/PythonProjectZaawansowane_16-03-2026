class MyMeta(type):
    def __new__(mcls, name, base, namespace):
        print(f"Tworzę klasę: {name}")
        return super().__new__(mcls, name, base, namespace)


class User(metaclass=MyMeta):
    pass


u = User()  # Tworzę klasę: User
print(u.__dict__)


class User(metaclass=MyMeta):
    x = 10


u = User()
print(u)  # <__main__.User object at 0x00000255EB3D8C20>

namespace = {"x": 10}
User = MyMeta("User", (), namespace)  # Tworzę klasę: User
print(type(User))  # <class '__main__.MyMeta'>
