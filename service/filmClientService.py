from domeniu.clientFilmDTO import ClientFilmDTOAssambler
from domeniu.clientInchirieriDTO import ClientInchirieriDTOAssambler
from domeniu.filmInchirieriDTO import FilmInchirieriDTOAssambler
from domeniu.fimClient import FilmClient
from repository.repository import Repository



class FilmClientService:
    def __init__(self, filmClientRepository: Repository,
                 filmReository: Repository,
                 clientRepository: Repository):
        self.__filmClientRepository = filmClientRepository
        self.__filmRepository = filmReository
        self.__clientRepository = clientRepository

    def adaugaInscriere(self, idFilmClient, idFilm, idClient):
        if self.__filmRepository.getById(idFilm) is None:
            raise KeyError("Nu exista un film cu id-ul dat")
        if self.__clientRepository.getById(idClient) is None:
            raise KeyError("Nu exista un client cu id-ul dat")

        inscrieri = self.__filmClientRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdFilm() == idFilm and inscriere.getIdClient() == idClient:
                raise KeyError("Filmul este deja inscris la clientul dat")

        inscriere = FilmClient(idFilmClient, idFilm, idClient)
        self.__filmClientRepository.adauga(inscriere)

    def getAllInscrieri(self):
        return self.__filmClientRepository.getAll()

    def stergeInscriere(self, idFilm, idClient):
        inscrieri = self.__filmClientRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdFilm() == idFilm and inscriere.getIdClient() == idClient:
                self.__filmClientRepository.sterge(inscriere.getIdEntitate())

    '''def clienti3Filme(self):
        clientiNrFilme = {}
        inscrieri = self.__filmClientRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdFilm() in clientiNrFilme:
                clientiNrFilme[inscriere.getIdFilm()] += 1
            else:
                clientiNrFilme[inscriere.getIdFilm()] = 1

        idClientiOrdonati = sorted(clientiNrFilme, key=lambda idClient: clientiNrFilme[idClient], reverse=True)
        clientiOrdonati = []
        for idClienti in idClientiOrdonati:
            clientiOrdonati.append((idClienti, clientiNrFilme[idClienti]))

        l = []
        nr = 50 * len(clientiOrdonati) // 100
        for i in range(nr):
            l.append(clientiOrdonati[i])
        return l'''

    def creazaDTO1(self):
        inscrieri = self.getAllInscrieri()
        l = []
        for inscriere in inscrieri:
            client = self.__clientRepository.getById(inscriere.getIdClient())
            film = self.__filmRepository.getById(inscriere.getIdFilm())
            filmClientDTO = ClientFilmDTOAssambler.creaza(client, film)
            l.append(filmClientDTO)
        return l

    def ordoneazaDTO1(self):
        l = self.creazaDTO1()
        l.sort(key=lambda obiect: obiect.titluFilm)
        return l

    def creazaDTO2(self):
        inscrieri = self.getAllInscrieri()
        l = {}
        for inscriere in inscrieri:
            if inscriere.getIdFilm() in l:
                l[inscriere.getIdFilm()].append(inscriere.getIdClient())
            else:
                l[inscriere.getIdFilm()] = []
                l[inscriere.getIdFilm()].append(inscriere.getIdClient())

        dto = []
        for i in l:
            film = self.__filmRepository.getById(i)
            fid = FilmInchirieriDTOAssambler.creaza(film, l[i])
            dto.append(fid)
        return dto

    def ordoneazaDTO2(self):
        l = self.creazaDTO2()
        l.sort(key=lambda i: i.nrInchirieri, reverse=True)
        lmax = []
        lmax.append(l[0])
        for i in range(1, len(l)):
            if l[i].nrInchirieri == lmax[0].nrInchirieri:
                lmax.append(l[i])
        return lmax

    def creazaDTO3(self):
        inscrieri = self.getAllInscrieri()
        l = {}
        for inscriere in inscrieri:
            if inscriere.getIdClient() in l:
                l[inscriere.getIdClient()].append(inscriere.getIdFilm())
            else:
                l[inscriere.getIdClient()] = []
                l[inscriere.getIdClient()].append(inscriere.getIdFilm())

        dto = []
        for i in l:
            client = self.__clientRepository.getById(i)
            cid = ClientInchirieriDTOAssambler.creaza(client, l[i])
            dto.append(cid)
        return dto

    def ordoneazaDTO3(self):
        l = self.creazaDTO3()
        l.sort(key=lambda i: i.nrInchirieri, reverse=True)
        k = len(l) * 3 // 10
        if k == 0:
            k = 1
        return l




