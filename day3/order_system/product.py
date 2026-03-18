from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int
    stock: int

    def is_available(self, quantity: int) -> bool:
        return self.stock >= quantity
