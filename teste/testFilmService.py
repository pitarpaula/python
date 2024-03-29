from repository.repository import Repository
from service.filmService import FilmService


def testAdaugaFilmService():
    filmRepository = Repository()
    filmService = FilmService(filmRepository)

    filmService.adaugaFilm("1", "e", "e", "e")
    filme = filmService.getAllFilme()
    assert len(filme) == 1
    assert filme[0].getIdFilm() == "1"
    assert filme[0].getTitlu() == "e"
    assert filme[0].getDescriere() == "e"
    assert filme[0].getGen() == "e"

    try:
        filmService.adaugaFilm("1", "e", "e", "e")
        assert False
    except KeyError:
        ...

def testModificaFilmService():
    filmRepository = Repository()
    filmClientRepository = Repository()
    filmService = FilmService(filmRepository, filmClientRepository)
    filmService.adaugaFilm("1", "e", "e", "e")

    filmService.modificaFilm("1", "r", "r", "r")

    filme = filmService.getAllFilme()
    assert filme[0].getTitlu() == "r"
    assert filme[0].getDescriere() == "r"
    assert filme[0].getGen() == "r"

    try:
        filmService.modificaFilm("2", "t", "t", "t")
        assert False
    except KeyError:
        ...

def testStergeFilmService():
    filmRepository = Repository()
    filmClientRepository = Repository()
    filmService = FilmService(filmRepository, filmClientRepository)
    filmService.adaugaFilm("1", "e", "e", "e")

    filmService.stergeFilm("1")
    filme =  filmService.getAllFilme()

    assert len(filme) == 0

    try:
        filmService.stergeFilm("1")
        assert False
    except KeyError:
        ...
