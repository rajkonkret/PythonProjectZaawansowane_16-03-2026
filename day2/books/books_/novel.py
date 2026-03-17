from day2.books.book import Book


class Novel(Book):

    def get_info(self):
        return f"{self.title}, {self.author}, {self.page} stron"

    def read(self):
        print(f"Przeczytano powiesć {self.title}")
