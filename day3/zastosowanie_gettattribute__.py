class SecureData:
    def __init__(self, public, secret):
        self.public = public
        self._secret = secret

    @property
    def info(self):
        return f"PUBLIC={self.public}"

    def __getattribute__(self, name):
        print(f"[LOG] Próba dostępu do atrybutu: {name}")

        if name == "_secret":
            raise AttributeError("Brak dostępu do _secret")

        return super().__getattribute__(name)


print("--- Tworzenie obiektu ---")
obj = SecureData("widoczne dane", "tajne dane")

print("--- Normalny atrybut ---")
print(obj.public)

print("--- Odczyt propery ---")
print(obj.info)
# --- Normalny atrybut ---
# [LOG] Próba dostępu do atrybutu: public
# widoczne dane
# --- Odczyt propery ---
# [LOG] Próba dostępu do atrybutu: info
# [LOG] Próba dostępu do atrybutu: public
# PUBLIC=widoczne dane

print("--- Zablokowany element ---")
try:
    print(obj._secret)
except AttributeError as e:
    print("Bład:", e)
# [LOG] Próba dostępu do atrybutu: _secret
# Bład: Brak dostępu do _secret
