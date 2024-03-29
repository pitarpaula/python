from unittest import TestCase

from domeniu.fimClient import FilmClient
from repository.repository import Repository
from service.filmService import FilmService


class TestFilmService(TestCase):
    def testAdauga(self):
        filmRepository = Repository()
        filmClientRepository = Repository()
        filmService = FilmService(filmRepository, filmClientRepository)
        filmService.adaugaFilm(1, "r", "r", "r")
        filme = filmService.getAllFilme()
        self.assertTrue( len(filme) == 1, 'lungimea listei de filme ar trebui sa fie 1')
        self.assertTrue( filme[0].getIdEntitate() == 1, 'id-ul filmului ar trebui sa fie 1')

    def testModifica(self):
        filmRepository = Repository()
        filmClientRepository = Repository()
        filmService = FilmService(filmRepository, filmClientRepository)
        filmService.adaugaFilm(1, "r", "r", "r")
        filmService.modificaFilm(1, "t", "t", "t")
        filme = filmService.getAllFilme()
        self.assertTrue( len(filme) == 1, 'lungimea listei de filme ar trebui sa fie 1')
        self.assertTrue( filme[0].getIdEntitate() == 1, 'id-ul filmului ar trebui sa fie 1')
        self.assertTrue( filme[0].getTitlu() == "t", 'titlul filmului ar trebui sa fie "t"')
        self.assertTrue( filme[0].getDescriere() == "t", 'descriere filmului ar trebui sa fie "t"')
        self.assertTrue( filme[0].getGen() == "t", 'genul filmului ar trebui sa fie "t"')


    def testSterge(self):
        filmRepository = Repository()
        filmClientRepository = Repository()
        filmService = FilmService(filmRepository, filmClientRepository)
        filmService.adaugaFilm(1, "r", "r", "r")
        filmClient = FilmClient(1, 1, 1)
        filmClientRepository.adauga(filmClient)
        filmService.stergeFilm(1)
        filme = filmService.getAllFilme()
        self.assertTrue( len(filme) == 0, 'lungimea listei de filme ar trebui sa fie 0' )
        self.assertTrue(len(filmClientRepository.getAll()) == 0, 'lungimea listei cu inscrieri ar trebui sa fie 0')