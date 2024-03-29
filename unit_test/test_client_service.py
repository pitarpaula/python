from unittest import TestCase

from domeniu.fimClient import FilmClient
from repository.repository import Repository
from service.clientService import ClientService


class TestClientService(TestCase):
    def testAdauga(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        clientService = ClientService(clientRepository, filmClientRepository)
        clientService.adaugaClient(1, "ana", "1")
        clienti = clientService.getAllClienti()
        self.assertTrue( len(clienti) == 1, 'lungimea listei de clienti ar trebui sa fie 1')
        self.assertTrue( clienti[0].getIdEntitate() == 1, 'id-ul clientului ar trebui sa fie 1')

    def testModifica(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        clientService = ClientService(clientRepository, filmClientRepository)
        clientService.adaugaClient(1, "ana", "1")
        clientService.modificaClient(1, "ion", "2")
        clienti = clientService.getAllClienti()
        self.assertTrue( len(clienti) == 1, 'lungimea listei de clienti ar trebui sa fie 1')
        self.assertTrue( clienti[0].getIdEntitate() == 1, 'id-ul clientului ar trebui sa fie 1')
        self.assertTrue( clienti[0].getNume() == "ion", 'numele cientului ar trebui sa fie "ion"')
        self.assertTrue( clienti[0].getCNP() == "2", 'CNP-ul clientului ar trebui sa fie "2"')

    def testSterge(self):
        clientRepository = Repository()
        filmClientRepository = Repository()
        clientService = ClientService(clientRepository, filmClientRepository)
        clientService.adaugaClient(1, "ana", "1")
        filmClient = FilmClient(1, 1, 1)
        filmClientRepository.adauga(filmClient)
        clientService.stergeClient(1)
        clienti = clientService.getAllClienti()
        self.assertTrue( len(clienti) == 0, 'lungimea listei de clienti ar trebui sa fie 0' )
        self.assertTrue(len(filmClientRepository.getAll()) == 0, 'lungimea listei cu inscrieri ar trebui sa fie 0')