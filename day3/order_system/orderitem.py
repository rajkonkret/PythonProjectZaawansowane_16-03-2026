from dataclasses import dataclass
from product import Product


@dataclass
class OrderItem:
    product: Product
    quantity: int

    def total_price(self) -> float:
        if not self.product.is_available(self.quantity):
            raise ValueError(f"Produkt {self.product.name} jest niedosstępny żądanej ilości")
        return self.quantity * self.product.price
