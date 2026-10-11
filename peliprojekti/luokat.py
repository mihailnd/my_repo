
class Esine:
    #luokka kamoille, joilla on nimi ja paino.
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Huone:
    #luokka huoneille, joilla on nimi ja ehkä joku esine.
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine


class Pelaaja:
    #luokka pelaajalle, jolla on nimi, sijainti ja inventaario.
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti
        self.kestavyys_pisteet = 0

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

    def has_item(self, nimi):
        for esine in self.esineet:
            if esine.nimi == nimi:
                return True

        return False
