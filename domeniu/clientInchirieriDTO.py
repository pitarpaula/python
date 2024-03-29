from dataclasses import dataclass

@dataclass
class ClientInchirieriDTO:
    numeClient: str
    nrInchirieri: int

class ClientInchirieriDTOAssambler:
    @staticmethod
    def creaza(client, inchirieri):
        numeClient = client.getNume()
        nrInchirieri = len(inchirieri)
        return ClientInchirieriDTO(numeClient, nrInchirieri)