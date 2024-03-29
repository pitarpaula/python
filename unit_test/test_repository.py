from unittest import TestCase
from domeniu.entitate import Entitate
from domeniu.clienti import Client
from repository.repository import Repository

class TestRepository(TestCase):
    def testAdauga(self):
        repository = Repository()
        entitate = Entitate(1)
        repository.adauga(entitate)
        entitati = repository.getAll()
        self.assertTrue(len(entitati) == 1, 'lungimea listei ar trebui sa fie 1')
        self.assertTrue(entitati[0].getIdEntitate() == 1, 'id-ul entitatii ar trebui sa fie 1')
        self.assertRaises(KeyError, repository.adauga, entitate)

    def testModifica(self):
        repository = Repository()
        client = Client(1, "ana", "1")
        clientN = Client(1, "ion", "2")
        clientE = Client(2, "mara", "3")
        repository.adauga(client)
        repository.modifica(clientN)
        entitati = repository.getAll()
        self.assertTrue(len(entitati) == 1, 'lungimea listei ar trebui sa fie 1')
        self.assertTrue(entitati[0].getIdEntitate() == 1, 'id-ul clientului ar trebui sa fie 1')
        self.assertTrue(entitati[0].getNume() , 'numele clientului ar trebui sa fie "ion"')
        self.assertRaises(KeyError, repository.modifica , clientE)

    def testSterge(self):
        repository = Repository()
        entitate = Entitate(1)
        repository.adauga(entitate)
        repository.sterge(1)
        entitati = repository.getAll()
        self.assertTrue(len(entitati) == 0, 'lungimea listei ar trebui sa fie 0')
        self.assertRaises(KeyError, repository.sterge, entitate)