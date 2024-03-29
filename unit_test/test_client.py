from unittest import TestCase
from domeniu.clienti import Client


class TestClient(TestCase):
    def testIdClient(self):
        client = Client(1, "ana", "1")
        self.assertTrue(client.getIdEntitate() == 1, 'id-ul clientului ar trebui sa fie 1')
        client.setIdEntitate(2)
        self.assertTrue(client.getIdEntitate() == 2, 'id-ul clientului dupa set ar trebui sa fie 2')

    def testNume(self):
        client = Client(1, "ana", "1")
        self.assertTrue(client.getNume(), 'numele clientului ar trebui sa fie "ana"')
        client.setNume("ion")
        self.assertTrue(client.getNume() , 'numele clientului dupa set ar trebui sa fie "ion"')

    def testCNP(self):
        client = Client(1, "ana", "1")
        self.assertTrue(client.getCNP(), 'CNP-ul clientului ar trebui sa fie "1"')
        client.setCNP("2")
        self.assertTrue(client.getCNP(), 'CNP-ul clientului dupa set ar trebui sa fie "2"')
