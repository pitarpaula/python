from unittest import TestCase

from domeniu.clienti import Client
from domeniu.film import Film
from domeniu.fimClient import FilmClient
from repository.repository import Repository
from service.filmClientService import FilmClientService


class TestFilmClientService(TestCase):
    def testAdauga(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        filmRepository = Repository()
        client = Client(1, "ana", "1")
        clientRepository.adauga(client)
        client = Client(2, "ion", "1")
        clientRepository.adauga(client)
        film = Film(1, "t", "t", "t")
        filmRepository.adauga(film)
        film = Film(2, "a", "a", "a")
        filmClientService = FilmClientService(filmClientRepository, filmRepository, clientRepository)
        filmClientService.adaugaInscriere(1, 1, 1)
        inscrieri = filmClientService.getAllInscrieri()
        self.assertTrue(len(inscrieri) == 1, 'lungimea listei de clienti ar trebui sa fie 1')
        self.assertTrue(inscrieri[0].getIdEntitate() == 1, 'id-ul clientului ar trebui sa fie 1')

        id = 2
        idc = 3
        idf = 1
        self.assertRaises(KeyError, filmClientService.adaugaInscriere, id, idc, idf)
        id = 2
        idc = 1
        idf = 3
        self.assertRaises(KeyError, filmClientService.adaugaInscriere, id, idc, idf)
        id = 2
        idc = 1
        idf = 1
        self.assertRaises(KeyError, filmClientService.adaugaInscriere, id, idc, idf)

    def testSterge(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        filmRepository = Repository()
        client = Client(1, "ana", "1")
        clientRepository.adauga(client)
        client = Client(2, "ion", "1")
        clientRepository.adauga(client)
        film = Film(1, "t", "t", "t")
        filmRepository.adauga(film)
        film = Film(2, "a", "a", "a")
        filmClientService = FilmClientService(filmClientRepository, filmRepository, clientRepository)
        filmClientService.adaugaInscriere(1, 1, 1)
        filmClient = FilmClient(1, 1, 1)
        filmClientService.stergeInscriere(1, 1)
        inscrieri = filmClientService.getAllInscrieri()
        self.assertTrue(len(inscrieri) == 0, 'lungimea listei de clienti ar trebui sa fie 0')

    def testOrdoneazaDTO1(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        filmRepository = Repository()
        client = Client(1, "ana", "1")
        clientRepository.adauga(client)
        client = Client(2, "ion", "1")
        clientRepository.adauga(client)
        film = Film(1, "t", "t", "t")
        filmRepository.adauga(film)
        film = Film(2, "a", "a", "a")
        filmRepository.adauga(film)
        filmClientService = FilmClientService(filmClientRepository, filmRepository, clientRepository)
        filmClientService.adaugaInscriere(1, 1, 1)
        filmClientService.adaugaInscriere(2, 2, 2)

        inscrieri = filmClientService.ordoneazaDTO1()
        self.assertTrue(inscrieri[0].titluFilm == "a", 'titlul filmului ar trebui sa fie a')
        self.assertTrue(inscrieri[1].titluFilm == "t", 'titlul filmului urmator ar trebui sa fie t')
        self.assertTrue(inscrieri[0].numeClient == "ion", 'numarul inscrierilot ar trebui sa fie 1')
        self.assertTrue(inscrieri[1].numeClient == "ana", 'numarul inscrierilot ar trebui sa fie 1')

    def testOrdoneazaDTO2(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        filmRepository = Repository()
        client = Client(1, "ana", "1")
        clientRepository.adauga(client)
        client = Client(2, "ion", "1")
        clientRepository.adauga(client)
        film = Film(1, "t", "t", "t")
        filmRepository.adauga(film)
        film = Film(2, "a", "a", "a")
        filmRepository.adauga(film)
        filmClientService = FilmClientService(filmClientRepository, filmRepository, clientRepository)
        filmClientService.adaugaInscriere(1, 1, 1)
        filmClientService.adaugaInscriere(2, 2, 2)

        inscrieri = filmClientService.ordoneazaDTO2()
        self.assertTrue(inscrieri[0].titluFilm == "t", 'titlul filmului ar trebui sa fie t')
        self.assertTrue(inscrieri[1].titluFilm == "a", 'titlul filmului urmator ar trebui sa fie a')
        self.assertTrue(inscrieri[0].nrInchirieri == 1, 'numarul inscrierilot ar trebui sa fie 1')
        self.assertTrue(inscrieri[1].nrInchirieri == 1, 'numarul inscrierilot ar trebui sa fie 1')


    def testOrdoneazaDTO3(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        filmRepository = Repository()
        client = Client(1, "ana", "1")
        clientRepository.adauga(client)
        client = Client(2, "ion", "1")
        clientRepository.adauga(client)
        film = Film(1, "t", "t", "t")
        filmRepository.adauga(film)
        film = Film(2, "a", "a", "a")
        filmRepository.adauga(film)
        filmClientService = FilmClientService(filmClientRepository, filmRepository, clientRepository)
        filmClientService.adaugaInscriere(1, 1, 1)
        filmClientService.adaugaInscriere(2, 2, 2)

        inscrieri = filmClientService.ordoneazaDTO3()
        self.assertTrue(inscrieri[0].numeClient == "ana", 'titlul filmului ar trebui sa fie a')
        self.assertTrue(inscrieri[1].numeClient == "ion", 'titlul filmului urmator ar trebui sa fie t')
        self.assertTrue(inscrieri[0].nrInchirieri == 1, 'numarul inscrierilot ar trebui sa fie 1')
        self.assertTrue(inscrieri[1].nrInchirieri == 1, 'numarul inscrierilot ar trebui sa fie 1')
