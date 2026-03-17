#  pydoc -b wywołanie serwera projektu
# pydoc -w .\books\book.py
from abc import ABC, abstractmethod

# klasa abstrakcyjna
# nie można utworzyc obiektów tej klasy
# należy dziedziczyć po niej
# klasa dziedzicząca musi nadpisać metody abstrakcyjne
class Book(ABC):
    """
    Klasa Book
    """

    def __init__(self, title, author, year, page):
        """
        Metoda inicjalizująca
        :param title:
        :param author:
        :param year:
        :param page:
        """
        self.title = title
        self.author = author
        self.year = year
        self.page = page

    def __repr__(self):
        return f"Obiekt klasy {self.__class__.__name__} ({self.title} -> {self.author})"

    # __str__ działą tylko dla print() i str()

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def read(self):
        pass
