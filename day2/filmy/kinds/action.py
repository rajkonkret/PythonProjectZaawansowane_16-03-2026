from day2.filmy.award import AwardWinning
from day2.filmy.film import Film


# mozna dziedziczyc po wielu klasach
class ActionFilm(Film, AwardWinning):
    def __init__(self, title: str, director: str, year: int, duration: float):
        # super().__init__(title, director, year, duration)
        Film.__init__(self, title, director, year, duration)
        AwardWinning.__init__(self)

    def play(self):
        print(f"Odtwarzanie filmu akcji: {self.title}")

    def get_info(self):
        info = f"{self.title}, reżyseria: {self.director}, produkcja: {self.year},  czas trwnia [h]: {self.duration}"
        if self.awards:
            info += f" | Nagrody: {','.join(self.awards)}"
        return info


if __name__ == '__main__':
    # kolejnośc rozwiązywania nazw
    print(ActionFilm.__mro__)
    # (<class '__main__.ActionFilm'>, <class 'day2.filmy.film.Film'>, <class 'abc.ABC'>,
    # <class 'day2.filmy.award.AwardWinning'>, <class 'object'>)
