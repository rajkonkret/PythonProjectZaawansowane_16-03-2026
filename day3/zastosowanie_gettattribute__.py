class SecureData:
    def __init__(self, public, secret):
        self.public = public
        self._secet = secret

    @property
    def info(self):
        return f"PUBLIC={self.public}"

    def __getattribute__(self, name):
        print(f"[LOG] Próba dostępu do atrybutu: {name}")

        if name == "_secret":
            raise AttributeError("Brak dostępu do _secret")

        return super().__getattribute__(name)
