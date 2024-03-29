from dataclasses import dataclass

@dataclass
class FilmInchirieriDTO:
    titluFilm: str
    nrInchirieri: int

class FilmInchirieriDTOAssambler:
    @staticmethod
    def creaza(film, inchirieri):
        titluFilm = film.getTitlu()
        nrInchiriere = len(inchirieri)
        return FilmInchirieriDTO(titluFilm, nrInchiriere)