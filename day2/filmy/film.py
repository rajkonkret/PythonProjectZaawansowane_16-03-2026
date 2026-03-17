from abc import ABC, abstractmethod


class Film(ABC):
    def __init__(self, title: str, director: str, year: int, duration: float):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration
        self.create_film()
