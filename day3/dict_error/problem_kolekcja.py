class Book:
    lista = []

    def __init__(self, title):
        self.title = title
        Book.lista.append(self)


book = Book("Pan Tadeusz")
print(book.lista)

book2 = Book("Lalka")
print(Book.lista)


# [<__main__.Book object at 0x00000270C2288AD0>, <__main__.Book object at 0x00000270C2278A50>]

class Book2:
    title = None


book3 = Book2()
book3.title = "Radek"

book4 = Book2()
book4.title = "Tomek"

print(book3.title)
print(book4.title)
# Radek
# Tomek
print(Book2.title)  # None

book4.isbn = "7890987890"
print(book4.isbn)  # 7890987890
