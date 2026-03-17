from film_collection import FilmCollection
from kinds.action import ActionFilm
from kinds.comedy import ComedyFilm
from kinds.document import DocumentaryFilm

collections = FilmCollection()

film1 = ActionFilm("Mad Max", "George Orwell", 2025, 2)
film2 = ComedyFilm("Naga Broń", "Andrzej Wajda", 2005, 1.75,
                   "Uniwersum Naga Broń", 1)
film3 = DocumentaryFilm("The Social Dilema", "Jeff Orlowsky", 2002, 1.7)
# Utworzono nowy obiekt oparty na klasie ActionFilm
# Utworzono nowy obiekt oparty na klasie ComedyFilm
# Utworzono nowy obiekt oparty na klasie DocumentaryFilm

film1.add_award("Oscar za najlepszy montaż")
film1.add_award("Oscar za najlepszy dźwięk")

collections.add_film(film1)
collections.add_film(film2)
collections.add_film(film3)

collections.display_all_films()
# Mad Max, reżyseria: George Orwell, produkcja: 2025,  czas trwnia [h]: 2 | Nagrody: Oscar za najlepszy montaż,Oscar za najlepszy dźwięk
# Naga Broń, reżyseria: Andrzej Wajda, produkcja: 2005,  czas trwnia [h]: 1.75 | Seial: Uniwersum Naga Broń, część: 1
# The Social Dilema, reżyseria: Jeff Orlowsky, produkcja: 2002

film1.play()
# Odtwarzanie filmu akcji: Mad Max

film2.play()
# Odtwarzanie komedii: Naga Broń
