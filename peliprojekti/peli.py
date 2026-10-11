#tuodaan peliin luokat "luokat.py" tiedostosta
from luokat import Pelaaja, Huone, Esine
#tuodaan peliin funktiot "funktiot.py" tiedostosta
from funktiot import (
    show_room,
    show_inventory,
    collect_item,
    move_to_room,
    show_instructions,
    choose_escape_route,
    tee_ymparistoteko
)


def main():
    #käynnistää pelin ja luo päävalikon.
    name = input("Mikä on nimesi? ")

    while not name:
        print("HEI! Et kirjoittanut nimeäsi! Laitappas nimi tänne.")
        name = input("Mikä on nimesi? ")

    #kysytään pelaajan ikää ja katsotaan että hän on ainakin 12v vanha.
    while True:
        try:
            age = int(input("Kuinka vanha olet? "))

            if age <= 0:
                print("Anna oikea ikä!")
                continue

            break

        except ValueError:
            print("Anna ikä numeroina!(Monnin moka)")

    if age < 12:
        print("Peli on tarkoitettu vähintään 12-vuotiaille. Ette keuli! >:(")
        return

    #luodaan esineet ja niiden paino.
    taskulamppu = Esine("Taskulamppu", 12345.67)
    rynkky = Esine("RK-62", 2000000.67)
    avain = Esine("Avain", 99999.0)
    glokki = Esine("Glokki", 1000.5)

    #luodaan huoneet ja laitetaan esineet niihin.
    tehdashalli = Huone("Tehdashalli", taskulamppu)
    toimisto = Huone("Toimisto", avain)
    suihku = Huone("Suihku")
    vessa = Huone("Vessa", glokki)
    aula = Huone("Aula")
    leikkihuone = Huone("Leikkihuone", rynkky)

    huoneet = [
        tehdashalli,
        toimisto,
        suihku,
        vessa,
        aula,
        leikkihuone
    ]

    #luodaan pelaaja ja laitetaan se aloitushuoneeseen.
    pelaaja = Pelaaja(name, tehdashalli)

    print(f"\nTervetuloa peliin, {name}!")
    print("Heräsit vanhalla hylätylä tehtaalla.")
    print("Tutki huoneita, kerää esineitä, tee ympäristöystävällisiä tekoja ja etsi tie ulos. Onnea matkaan soturi!")

    # päävalikko, joka toistuu kunnes peli päättyy
    while True:
        print("\n<><> PÄÄVALIKKO <><>")
        print("1. Aloita peli")
        print("2. Ohjeet")
        print("3. Lopeta peli")

        action = input("Valitse toiminto: ")

        if action == "1":
            print("\nAloitit pelin!")
            show_room(pelaaja)

            # pelivalikko, joka toistuu kunnes pelaaja päättää palata takaisin päävalikkoon
            while True:
                print("\n<><> PELIVALIKKO <><>")
                print("1. Tarkista kamat")
                print("2. Kerää esine")
                print("3. Vaihda huonetta")
                print("4. Back to the päävalikko")
                print("5. Yritä paeta")
                print("6. Tee ympäristöteko(pls)")

                game_action = input("Mitä haluat tehdä? ")

                if game_action == "1":
                    show_inventory(pelaaja)

                elif game_action == "2":
                    collect_item(pelaaja)

                elif game_action == "3":
                    move_to_room(pelaaja, huoneet)

                elif game_action == "4":
                    print("Palaat päävalikkoon.")
                    break

                elif game_action == "5":
                    if choose_escape_route(pelaaja):
                        print(f"\nKiitos pelaamisesta, {name}!")
                        return

                elif game_action == "6":
                    tee_ymparistoteko(pelaaja)

                else:
                    print("Error 404. Yritä uudelleen.")

        elif action == "2":
            # näytetään ohjeet pelaajalle
            show_instructions()

        elif action == "3":
            # lopetetaan peli
            print(f"Kiitos pelaamisesta, {name}!")
            break

        else:
            print("Error 404. Valitse 1, 2 tai 3.")

if __name__ == "__main__":
    main()
