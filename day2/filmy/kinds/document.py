from day2.filmy.film import Film


class DocumentaryFilm(Film):
    def play(self):
        print(f"Odtwarzanie filmu dokumentalnego: {self.title}")

    def get_info(self):
        return f"{self.title}, reżyseria: {self.director}, produkcja: {self.year}"
