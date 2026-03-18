class SecureUser:
    def __init__(self):
        super().__setattr__("name", "Jan")
        super().__setattr__("age", 30)

    def __setattr__(self, name, value):
        if name not in self.__dict__ and name not in {"name", "age"}:
            raise AttributeError(f"Nie można dodać nowego atrybutu: {name}")
        super().__setattr__(name, value)


u = SecureUser()
u.name = "Adam"

print(u.name)  # Adam

try:
    u.city = "Warszawa"
except AttributeError as e:
    print("Bład:", e)
# Adam
# Bład: Nie można dodać nowego atrybutu: city
