from domeniu.clienti import Client
from repository.repository import Repository


def testAdaugaClientRepository():
    clientRepository = Repository()
    client = Client("1", "ion", "1")

    clientRepository.adauga(client)

    clienti = clientRepository.getAll()
    assert len(clienti) == 1
    assert clientRepository.getById("1") is not None
    assert clientRepository.getById("1").getNume() == "ion"
    assert clientRepository.getById("1").getCNP() == "1"

    try:
        clientRepository.adauga(client)
        assert False
    except KeyError:
        ...

def testModificaClientRepository():
    clientRepository = Repository()
    client = Client("1", "ion", "1")
    clientRepository.adauga(client)
    clientNou1 = Client("1", "paul", "2")
    clientNou2 = Client("2", "ana", "3")

    clientRepository.modifica(clientNou1)

    assert clientRepository.getById("1").getNume() == "paul"
    assert clientRepository.getById("1").getCNP() == "2"

    try:
        clientRepository.modifica(clientNou2)
    except KeyError:
        ...

def testStergeClientRepository():
    clientRepository = Repository()
    client = Client("1", "ion", "1")
    clientRepository.adauga(client)

    clientRepository.sterge("1")

    assert len(clientRepository.getAll()) == 0

    try:
        clientRepository.sterge("1")
        assert False
    except KeyError:
        ...