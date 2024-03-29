from domeniu.film import Film
from repository.repository import Repository


def testAdaugaFilmRepository():
    filmRepository = Repository()
    film = Film("1", "e", "e", "e")

    filmRepository.adauga(film)

    filme = filmRepository.getAll()
    assert len(filme) == 1
    assert filmRepository.getById("1") is not None
    assert filmRepository.getById("1").getTitlu() == "e"
    assert filmRepository.getById("1").getDescriere() == "e"
    assert filmRepository.getById("1").getGen() == "e"

    try:
        filmRepository.adauga(film)
        assert False
    except KeyError:
        ...

def testModificaFilmRepository():
    filmRepository = Repository()
    film = Film("1", "e", "e", "e")
    filmRepository.adauga(film)
    filmNou1 = Film("1", "r", "r", "r")
    filmNou2 = Film("1", "t", "t", "t")

    filmRepository.modifica(filmNou1)

    assert filmRepository.getById("1").getTitlu() == "r"
    assert filmRepository.getById("1").getDescriere() == "r"
    assert filmRepository.getById("1").getGen() == "r"

    try:
        filmRepository.modifica(filmNou2)
    except KeyError:
        ...

def testStergeFilmRepository():
    filmRepository = Repository()
    film = Film("1", "e", "e", "e")
    filmRepository.adauga(film)

    filmRepository.sterge("1")

    assert len(filmRepository.getAll()) == 0

    try:
        filmRepository.sterge("1")
        assert False
    except KeyError:
        ...