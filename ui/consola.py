from domeniu.exceptii.duplicateError import DuplicateError
from service.clientService import ClientService
from service.filmClientService import FilmClientService
from service.filmService import FilmService


class Consola:
    def __init__(self, filmService: FilmService, clientService: ClientService, filmClientService: FilmClientService):
        self.__filmService = filmService
        self.__clientService = clientService
        self.__filmClientService = filmClientService

    def adaugaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            descriere = input("Dati descriererea filmului: ")
            gen = input("Dati genul filmului: ")
            self.__filmService.adaugaFilm(idFilm, titlu, descriere, gen)
        except KeyError as e:
            print(e)

    def modificaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de modificat: ")
            titluNou = input("Dati titlul nou al filmului: ")
            descriereNou = input("Dati descriere noua a filmului: ")
            genNou = input("Dati genul nou al filmului: ")
            self.__filmService.modificaFilm(idFilm, titluNou, descriereNou, genNou)
        except KeyError as e:
            print(e)

    def stergeFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de sters: ")
            self.__filmService.stergeFilm(idFilm)
        except KeyError as e:
            print(e)

    def adaugaClient(self):
        try:
            idClient = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            self.__clientService.adaugaClient(idClient, nume, CNP)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaClient(self):
        try:
            idClient = input("Dati id-ul clientului de modificat: ")
            numeNou = input("Dati noul nume al clientului: ")
            CNPNou = input("Dati CNP-ul nou clientului: ")
            self.__clientService.modificaClient(idClient, numeNou, CNPNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def stergeClient(self):
        try:
            idClient = input("Dati id-ul clientmului de sters: ")
            self.__clientService.stergeClient(idClient)
        except KeyError as e:
            print(e)

    def inscrieFilmLaClient(self):
        try:
            idFilmClient = input("Dati id-ul inscrierii: ")
            idFilm = input("Dati id-ul filmului: ")
            idClient = input("Dati id-ul clientului: ")
            self.__filmClientService.adaugaInscriere(idFilmClient, idFilm, idClient)
        except DuplicateError as e:
            print(e)
        except KeyError as e:
            print(e)

    def stergeInscriere(self):
        idFilm = input("Dati id-ul filmului: ")
        idClient = input("Dati id-ul clientului:")
        self.__filmClientService.stergeInscriere(idFilm, idClient)

    def ordoneazaClientiDupaFilme(self):
        rezultat = self.__clientService.ordoneazaClientiDupaNrFilmeInchiriate()
        self.afiseaza(rezultat)

    def celeMaiInchiriateFilme(self):
        rezultat = self.__filmService.FilmeInchiriate()
        self.afiseaza(rezultat)

    def clienti30(self):
        try:
            rezultat = self.__filmClientService.clienti3Filme()
            self.afiseaza(rezultat)
        except KeyError as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def afiseazaDTO1(self):
        l = self.__filmClientService.ordoneazaDTO1()
        for i in l:
            print(f'Nume client: {i.numeClient}, Nume Film: {i.titluFilm}')

    def afiseazaDTO2(self):
        l = self.__filmClientService.ordoneazaDTO2()
        for i in l:
            print(f'Nume film: {i.titluFilm}, Numar inchirieri: {i.nrInchirieri}')

    def afiseazaDTO3(self):
        l = self.__filmClientService.ordoneazaDTO3()


        for i in range(len(l)):
            print(f'Nume client: {l[i].numeClient}, Numar inscrieri: {l[i].nrInchirieri}')

        print('\n')

        for i in range(k):
            print(f'Nume client: {l[i].numeClient}, Numar inscrieri: {l[i].nrInchirieri}')

    def printMenu(self):
        print("1. Adauga film")
        print("2. Modifica film")
        print("3. Sterge film")
        print("4. Adauga client")
        print("5. Modifica client")
        print("6. Sterge client")
        print("7. Inscrie film la client")
        print("8. Sterge inscriere")
        print("9. Ordoneaza clienti dupa filme")
        print("10. Cele mai inchiriate filme")
        print("11. Primi 30% clienti cu cele mai multe filme")
        print("a. Afiseaza toate filmele")
        print("t. Afiseaza toti clientii")
        print("i. Afiseaza toate inscrierile")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMenu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaFilm()
            elif optiune == "2":
                self.modificaFilm()
            elif optiune == "3":
                self.stergeFilm()
            elif optiune == "4":
                self.adaugaClient()
            elif optiune == "5":
                self.modificaClient()
            elif optiune == "6":
                self.stergeClient()
            elif optiune == "7":
                self.inscrieFilmLaClient()
            elif optiune == "8":
                self.stergeInscriere()
            elif optiune == "9":
                self.afiseazaDTO1()
            elif optiune == "10":
                self.afiseazaDTO2()
            elif optiune == "11":
                self.afiseazaDTO3()
            elif optiune == "a":
                self.afiseaza(self.__filmService.getAllFilme())
            elif optiune == "t":
                self.afiseaza(self.__clientService.getAllClienti())
            elif optiune == "i":
                self.afiseaza(self.__filmClientService.getAllInscrieri())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita!")