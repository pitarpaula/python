from domeniu.film import Film


def testFilmGet():
    film = Film("1", "e", "e", "e")

    assert film.getIdFilm() == "1"
    assert film.getTitlu() == "e"
    assert film.getDescriere() == "e"
    assert film.getGen() == "e"

def testFilmSet():
    film = Film("1", "e", "e", "e")

    film.setIdFilm("1")
    assert film.getIdFilm() == "1"

    film.setTitlu("e")
    assert film.getTitlu() == "e"

    film.setDescriere("e")
    assert film.getDescriere() == "e"

    film.setGen("e")
    assert film.getGen() == "e"
