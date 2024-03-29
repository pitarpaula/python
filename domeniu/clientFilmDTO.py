from dataclasses import dataclass

@dataclass
class ClientFilmDTO:
    numeClient: str
    titluFilm: str

class ClientFilmDTOAssambler:
    @staticmethod
    def creaza(client, film):
        numeClient = client.getNume()
        titluFilm = film.getTitlu()
        return ClientFilmDTO(numeClient, titluFilm)
