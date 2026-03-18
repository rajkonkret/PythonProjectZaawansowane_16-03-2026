from customer import Customer
from orderitem import OrderItem
from product import Product
from order import Order

if __name__ == '__main__':
    product1 = Product(name="Laptop", price=4500, stock=10)
    product2 = Product(name="smartphone", price=2700, stock=15)

    # tworzenie klienta
    customer = Customer(first_name="Jan", last_name="Kowalski", email="jan.kowalski1@gmail.com")

    # tworzenie zamóienai
    order = Order(customer=customer)

    # dodawanie pozycji do zamóienia
    try:
        order.add_item(OrderItem(product=product1, quantity=2))
        order.add_item(OrderItem(product=product2, quantity=1))
    except ValueError as e:
        print(f"Błąd: {e}")

print(order.summary())
# Zamówienie dla: Jan Kowalski:
# Data zamówienia: 2026-03-18 14:40:32.741709
# Status: Pending
# Pozycje:
#  Laptop x 2 - 9000 zł
# smartphone x 1 - 2700 zł
# Łączna kwota: 11700 zł