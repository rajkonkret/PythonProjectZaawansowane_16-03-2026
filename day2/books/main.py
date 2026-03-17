from book import Book
from book_collections import BookCollections
from books_.novel import Novel
from books_.textbook import TextBook

# TypeError: Can't instantiate abstract class Book without an implementation for abstract methods 'get_info', 'read'
# book1 = Book("Pan Tadeusz", "Adam", 1856, 345)
# print(book1) # <book.Book object at 0x000001F791A30AD0>
# # repr -> Obiekt klasy Book (Pan Tadeusz -> Adam)
# book1.get_info()

collection = BookCollections()

novel = Novel("1984", "George Orwell", 1949, 328)
textbook = TextBook("Python programming", "Jhon Brown", 2021, 467)

collection.add_book(novel)
collection.add_book(textbook)

collection.dispaly_all_books()
# 1984, George Orwell, 328 stron
# Python programming, Jhon Brown, 467 stron

novel.read()
textbook.read()
# Przeczytano powiesć 1984
# Przeczytano podręcznik Python programming. Zawieera dodatkowe materiały

# pokaż obiekty
print(novel)
print(textbook)
# Obiekt klasy Novel (1984 -> George Orwell)
# Obiekt klasy TextBook (Python programming -> Jhon Brown)

# wykorzystanie obiektu jako funkcja
# __call__
print(novel(45))
print(novel(60))
print(textbook(60))
# Ilość stron z dodatkami: 333, cena: 45
# Ilość stron z dodatkami: 333, cena: 60
# Ilość stron z dodatkami: 472, cena: 60
