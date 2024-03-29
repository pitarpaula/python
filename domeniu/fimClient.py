from domeniu.entitate import Entitate

class FilmClient(Entitate):
    def __init__(self, idFilmClient, idFilm, idClient):
        super().__init__(idFilmClient)
        self.__idFilm = idFilm
        self.__idClient = idClient

    def getIdFilm(self):
        return self.__idFilm

    def getIdClient(self):
        return self.__idClient

    def setIdFilm(self, idFilm):
        self.__idFilm = idFilm

    def setIdClient(self, idClient):
        self.__idClient = idClient

    def __str__(self):
        return f'id: {self.getIdEntitate()}, id film: {self.__idFilm},' \
               f' id client: {self.__idClient}'