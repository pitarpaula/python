from teste.testClientRepository import testAdaugaClientRepository, testModificaClientRepository, \
    testStergeClientRepository
from teste.testFilmRepository import testAdaugaFilmRepository, testModificaFilmRepository, testStergeFilmRepository
from teste.testFilmService import testStergeFilmService, testModificaFilmService


def testAll():

    testAdaugaFilmRepository()
    testModificaFilmRepository()
    testStergeFilmRepository()

    testModificaFilmService()
    testStergeFilmService()

    testAdaugaClientRepository()
    testModificaClientRepository()
    testStergeClientRepository()