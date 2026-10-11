
class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine


class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def move(self, kohde):
        self.sijainti = kohde
        print(f"Siirryit huoneeseen: {kohde.nimi}")

    def collect_item(self):
        if self.sijainti.esine is None:
            print("Tässä huoneessa ei ole esineitä.")
        else:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"Sait esineen: {esine.nimi}")
