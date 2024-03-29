from domeniu.clienti import Client
from repository.repository import Repository


class ClientService:
    def __init__(self, clientRepository: Repository, filmClientRepository: Repository):
        self.__clientRepository = clientRepository
        self.__filmClientRepository = filmClientRepository

    def getAllClienti(self):
        '''
        returneaza lista de clienti
        :return: o lista de obiecte de tipul client
        '''
        return self.__clientRepository.getAll()

    def adaugaClient(self, idClient, nume, CNP):
        '''
        adauga un client
        :param idClient: string
        :param nume: string
        :param CNP: string
        :return:
        '''
        client = Client(idClient, nume, CNP)
        self.__clientRepository.adauga(client)

    def modificaClient(self, idClient, numeNou, CNPNou):
        '''
        modifica un client dupa id-ul dat
        :param idClient: string
        :param numeNou: string
        :param CNPNou: string
        :return:
        '''
        client = Client(idClient, numeNou, CNPNou)
        self.__clientRepository.modifica(client)

    def stergeClient(self, idClient):
        '''
        strege un client dupa id
        :param idClient: string
        :return:
        '''
        inscrieri = self.__filmClientRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdClient() == idClient:
                self.__filmClientRepository.sterge(inscriere.getIdEntitate())
        self.__clientRepository.sterge(idClient)



