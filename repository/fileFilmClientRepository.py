from repository.repository import Repository
from domeniu.fimClient import FilmClient


class FileFilmClientRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, filmClient):
        super().adauga(filmClient)
        self.__writeFile()

    def modifica(self, filmClientNou):
        super().modifica(filmClientNou)
        self.__writeFile()

    def sterge(self, idFilmClient):
        super().sterge(idFilmClient)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                id = line.split()[0]
                idFilm = line.split()[1]
                idClient = line.split()[2]
                filmClient = FilmClient(id, idFilm, idClient)
                self._entitati[id] = filmClient

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for filmClient in self.getAll():
                f.write(f'{filmClient.getIdEntitate()} {filmClient.getIdFilm()} {filmClient.getIdClient()}\n')