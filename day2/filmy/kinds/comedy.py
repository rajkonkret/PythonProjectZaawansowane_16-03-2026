# film, series
from day2.filmy.film import Film
from day2.filmy.series import SeriesPart


class ComedyFilm(Film, SeriesPart):
    def __init__(self, title: str, director: str, year: int, duration: float, series_name: str, part_number: int):
        Film.__init__(self, title, director, year, duration)
        SeriesPart.__init__(self, series_name, part_number)

    def play(self):
        print(f"Odtwarzanie komedii: {self.title}")

    def get_inf(self):
        info = f"{self.title}, reżyseria: {self.director}, produkcja: {self.year},  czas trwnia [h]: {self.duration}"
        series_info = self.get_series_info()
        info += f' | {series_info}'
        return info
