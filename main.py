from repository.fileClientRepository import FileClientRepository
from repository.fileFilmClientRepository import FileFilmClientRepository
from repository.fileFilmRepository import FileFilmRepository

from service.clientService import ClientService
from service.filmClientService import FilmClientService
from service.filmService import FilmService

from teste.testAll import testAll
from unit_test.test_all import TestAll
from ui.consola import Consola


def main():
    #testAll()
    TestAll()

    filmRepository = FileFilmRepository('filme.txt')
    clientRepository = FileClientRepository('clienti.txt')
    filmClientRepository = FileFilmClientRepository('filmeClienti.txt')

    filmService = FilmService(filmRepository, filmClientRepository)
    clientService = ClientService(clientRepository, filmClientRepository)
    filmClientService = FilmClientService(filmClientRepository, filmRepository, clientRepository)

    consola = Consola(filmService, clientService, filmClientService)
    consola.meniu()

main()