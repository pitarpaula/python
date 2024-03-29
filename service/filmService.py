from domeniu.film import Film
from repository.repository import Repository


class FilmService:
    def __init__(self, filmRepository: Repository, filmClientRepository: Repository):
        self.__filmRepository = filmRepository
        self.__filmClientRepository = filmClientRepository

    def getAllFilme(self):
        '''
        returneaza lista de filme
        :return: o lista de obiecte de tipul Film
        '''
        return self.__filmRepository.getAll()

    def adaugaFilm(self, idFilm, titlu, descriere, gen):
        '''
        adauga un film
        :param idFilm: string
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return:
        '''
        film = Film(idFilm, titlu, descriere, gen)
        self.__filmRepository.adauga(film)

    def modificaFilm(self, idFilm, titluNou, descriereNou, genNou):
        '''
        modifica un film dupa id-ul dat
        :param idFilm: string
        :param titluNou: string
        :param descriereNou: string
        :param genNou: string
        :return:
        '''
        filmNou = Film(idFilm, titluNou, descriereNou,genNou)
        self.__filmRepository.modifica(filmNou)

    def stergeFilm(self, idFilm):
        '''
        strege un film dupa id
        :param idFilm: string
        :return:
        '''
        inscrieri = self.__filmClientRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdFilm() == idFilm:
                self.__filmClientRepository.sterge(inscriere.getIdEntitate())
        self.__filmRepository.sterge(idFilm)

    '''def FilmeInchiriate(self):
        filmeInchiriate = {}
        inscrieri = self.__filmClientRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdFilm() in filmeInchiriate:
                filmeInchiriate[inscriere.getIdFilm()] += 1
            else:
                filmeInchiriate[inscriere.getIdFilm()] = 1

        idFilmeOrdonati = sorted(filmeInchiriate, key=lambda idFilme: filmeInchiriate[idFilme], reverse=True)
        filmeOrdonati = []
        for idFilm in idFilmeOrdonati:
            filmeOrdonati.append((idFilm, filmeInchiriate[idFilm]))
        return filmeOrdonati'''
