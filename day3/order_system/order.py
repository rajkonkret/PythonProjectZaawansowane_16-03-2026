from dataclasses import dataclass, field
from customer import Customer
from orderitem import OrderItem
from typing import List
import datetime


@dataclass
class Order:
    customer: Customer
    items: List[OrderItem] = field(default_factory=list)
    order_date: datetime.datetime = field(default_factory=datetime.datetime.now)
    status: str = "Pending"

    def add_item(self, item: OrderItem):
        if item.product.is_available(item.quantity):
            item.product.stock -= item.quantity
            self.items.append(item)
        else:
            raise ValueError(f"Produkt {item.product.name} jest niedosstępny żądanej ilości")

    def total_order_value(self) -> float:
        return sum(item.total_price() for item in self.items)

    def summary(self) -> str:
        item_details = "\n".join(f"{item.product.name} x {item.quantity} - {item.total_price()} zł"
                                 for item in self.items)

        return (f"Zamówienie dla: {self.customer.full_name()}: \n"
                f"Data zamówienia: {self.order_date}\n"
                f"Status: {self.status} \n"
                f"Pozycje: \n {item_details}\n"
                f"Łączna kwota: {self.total_order_value()} zł")
