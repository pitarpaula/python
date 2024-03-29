from domeniu.clienti import Client


def testClientGet():
    client = Client("1", "ion", "1", "4")

    assert client.getIdClient() == "1"
    assert client.getNume() == "ion"
    assert client.getCNP() == "1"
    assert client.getIdFilm() == "4"

def testClientSet():
    client = Client("1", "ion", "1", "4")

    client.setIdClient("1")
    assert client.getIdClient() == "1"

    client.setNume("ion")
    assert client.getNume() == "ion"

    client.setCNP("1")
    assert client.getCNP() == "1"

    client.setIdFilm("4")
    assert client.getIdFilm() == "4"