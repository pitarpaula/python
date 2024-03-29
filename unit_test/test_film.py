from unittest import TestCase
from domeniu.film import Film


class TestFilm(TestCase):

    def testIdFilm(self):
        film = Film(1, "r", "r", "r")
        self.assertTrue(film.getIdEntitate() == 1, 'id-ul filmului ar trebui sa fie 1')
        film.setIdEntitate(2)
        self.assertTrue(film.getIdEntitate() == 2, 'id-ul filmului dupa set ar trebui sa fie 2')

    def testTitlu(self):
        film = Film(1, "r", "r", "r")
        self.assertTrue(film.getTitlu(), 'titlul filmului ar trebui sa fie "r"')
        film.setTitlu("v")
        self.assertTrue(film.getTitlu(), 'titlul filmului dupa set ar trebui sa fie "v"')

    def testDescriere(self):
        film = Film(1, "r", "r", "r")
        self.assertTrue(film.getDescriere(), 'descrierea filmului ar trebui sa fie "r"')
        film.setDescriere("d")
        self.assertTrue(film.getDescriere(), 'descrierea filmului dupa set ar trebui sa fie "d"')

    def testGen(self):
        film = Film(1, "r", "r", "r")
        self.assertTrue(film.getGen(), 'genul filmului ar trebui sa fie "r"')
        film.setGen("g")
        self.assertTrue(film.getGen(), 'genul filmului dupa set ar trebui sa fie "g"')

