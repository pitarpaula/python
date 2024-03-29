from unit_test.test_client import TestClient
from unit_test.test_film import TestFilm
from unit_test.test_film_client_service import TestFilmClientService
from unit_test.test_repository import TestRepository
from unit_test.test_film_service import TestFilmService
from unit_test.test_client_service import TestClientService

def TestAll():
    testClient = TestClient()
    testFilm = TestFilm()
    testRepository = TestRepository()
    testFilmService = TestFilmService()
    testClientService = TestClientService()
    testFilmClient = TestFilmClientService()

    testFilm.testIdFilm()
    testFilm.testTitlu()
    testFilm.testDescriere()
    testFilm.testGen()

    testClient.testIdClient()
    testClient.testNume()
    testClient.testCNP()

    testRepository.testAdauga()
    testRepository.testModifica()
    testRepository.testSterge()

    testClientService.testAdauga()
    testClientService.testModifica()
    testClientService.testSterge()

    testFilmService.testAdauga()
    testFilmService.testModifica()
    testFilmService.testSterge()

    testFilmClient.testAdauga()
    testFilmClient.testSterge()
    testFilmClient.testOrdoneazaDTO1()
    testFilmClient.testOrdoneazaDTO2()
    testFilmClient.testOrdoneazaDTO3()



