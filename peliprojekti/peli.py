
from luokat import Pelaaja, Huone, Esine

name = input("Mikä on nimesi? ")

while True:
    try:
        age = int(input("Kuinka vanha olet? "))
        break
    except ValueError:
        print("Anna ikä numeroina.")

taskulamppu = Esine("Taskulamppu", 0.5)
rynkky = Esine("RK-62", 3.5)
avain = Esine("Avain", 99999.0)
glokki = Esine("Glokki", 1.2)

tehdashalli = Huone("Tehdashalli", taskulamppu)
toimisto = Huone("Toimisto", avain)
suihku = Huone("Suihku", None)
vessa = Huone("Vessa", glokki)
aula = Huone("Aula", None)
leikkihuone = Huone("Leikkihuone", rynkky)

pelaaja = Pelaaja(name, tehdashalli)

huoneet = [
    tehdashalli,
    toimisto,
    suihku,
    vessa,
    aula,
    leikkihuone
]

inventory = pelaaja.esineet

kuvaukset = {
    "Tehdashalli": "Olet MASSIIVISESSA hylätyssä tehtaassa. Ilmassa tuoksuu asbesti ja homehtuneet seinät.",
    "Toimisto": "Päädyit toimistoon. Täällä aikoinaan pelattiin PixelGun 3D:tä ja juotiin valkoista monsteria",
    "Suihku": "Olet vanhassa suihkutilassa. Hanoista tippuu tippoja alas ja lattialla on homehtunutta ruokaa.",
    "Vessa": "Stumblasit vessaan. Lattialla on 9mm luodin hylsyjä maassa ja seinällä punaisia täpliä.",
    "Aula": "Olet tehtaan aulassa. Täällä on MELKO siistiä, mutta katolta roikkuu 10 moottorisahaa.",
    "Leikkihuone": "Olet pienessä leikkihuoneessa, jossa ennen leikki työntekijöiden lapset. Lattialla on jonkun takia rynkyn hylsyjä."
}


def start_game():
    print("\nOlet aloittanut pelin!")
    print("Olet hylätyllä tehtaalla.")
    print("Tutki tehtaan huoneita ja kerää esineitä.")
    show_room()


def show_room():
    print(f"\n<><> {pelaaja.sijainti.nimi} <><>")
    print(kuvaukset[pelaaja.sijainti.nimi])

    if pelaaja.sijainti.esine is None:
        print("Huoneessa ei ole esineitä.")
    else:
        esine = pelaaja.sijainti.esine
        print(f"Huoneessa on esine: {esine.nimi}")


def show_inventory():
    print("\n<><> INVENTAARIO <><>")

    if len(inventory) == 0:
        print("Inventaario on tyhjä.")
    else:
        for esine in inventory:
            print(f"- {esine.nimi} (Paino: {esine.paino} kg)")


def collect_item():
    esine = pelaaja.sijainti.esine

    if esine is None:
        print("Huoneessa ei ole esineitä.")
    else:
        inventory.append(esine)
        pelaaja.sijainti.esine = None
        print(f"Keräsit esineen: {esine.nimi}")


def move_to_room():
    print("\n<><> HUONEET <><>")

    for i, huone in enumerate(huoneet):
        print(f"{i + 1}. {huone.nimi}")

    try:
        choice = int(input("Valitse huone (1-6): ")) - 1

        if 0 <= choice < len(huoneet):
            pelaaja.move(huoneet[choice])
            show_room()
        else:
            print("Error 404. Yritä uudelleen.")

    except ValueError:
        print("Anna huoneen numero.")


def show_instructions():
    print("\n<><> OHJEET <><>")
    print("Tervetuloa Vanhaan Hylättyyn Tehtaaseen!")
    print("1. Tutki eri huoneita valitsemalla haluamasi huone numerolla.")
    print("2. Kerää huoneissa olevia esineitä.(jos huoneessa on esineitä)")
    print("3. Tarkista inventaariosta keräämäsi esineet.")
    print("4. Pelin sisällä voit aina palata päävalikkoon.")
    print("Toivottavasti pidät pelistä! :)")


def play_game():
    while True:
        print("\n<><> PELIVALIKKO <><>")
        print("1. Tarkista inventaario")
        print("2. Kerää esine")
        print("3. Vaihda huonetta")
        print("4. Palaa päävalikkoon")

        action = input("Mitä haluat tehdä? ")

        if action == "1":
            show_inventory()
        elif action == "2":
            collect_item()
        elif action == "3":
            move_to_room()
        elif action == "4":
            print("Palaat päävalikkoon.")
            break
        else:
            print("Error 404. Yritä uudelleen. :<)")


def show_menu():
    print("\n<><> PÄÄVALIKKO <><>")
    print("1. Aloita peli")
    print("2. Ohjeet")
    print("3. Lopeta peli")


def main():
    if age < 12:
        print("Peli on sallittu vain 12 vuotta täyttäneille.")
        return

    print(f"\nTervetuloa peliin, {name}!")

    while True:
        show_menu()
        action = input("Valitse toiminto: ")

        if action == "1":
            start_game()
            play_game()

        elif action == "2":
            show_instructions()

        elif action == "3":
            print(f"Kiitos pelaamisesta, {name}!")
            break

        else:
            print("Error 404. Valitse 1, 2 tai 3. :)")


if __name__ == "__main__":
    main()
