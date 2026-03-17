from day2.books.book import Book


class TextBook(Book):
    def get_info(self):
        return f"{self.title}, {self.author}, {self.pages}"

    def read(self):
        print(f"Przeczytano podręcznik {self.title}. Zawieera dodatkowe materiały")
