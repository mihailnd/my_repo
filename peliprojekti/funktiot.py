def show_room(pelaaja):
    #Kuvailee pelaajalla minkälainen huoneessa on ja onko siellä esineitä.
    kuvaukset = {
        "Tehdashalli": (
            "Olet MASSIIVISESSA hylätyssä tehtaassa. "
            "Ilmassa tuoksuu asbesti ja seinät ovat homeessa."
        ),
        "Toimisto": (
            "Päädyit toimistoon. Täällä aikoinaan pelattiin "
            "PixelGun 3D:tä ja juotiin valkoista Monsteria."
        ),
        "Suihku": (
            "Olet vanhassa suihkutilassa. Hanoista tippuu vettä "
            "ja lattialla on homehtunutta ruokaa."
        ),
        "Vessa": (
            "Stumblasit vessaan. Lattialla on tyhjiä hylsyjä "
            "ja seinällä outoja punaisia täpliä."
        ),
        "Aula": (
            "Olet tehtaan aulassa. Täällä on melko siistiä, "
            "mutta katolta roikkuu vanhoja työkaluja."
        ),
        "Leikkihuone": (
            "Olet pienessä leikkihuoneessa, jossa työntekijöiden "
            "lapset leikkivät aikoinaan."
        )
    }

    huone = pelaaja.sijainti

    print(f"\n<><> {huone.nimi} <><>")
    print(kuvaukset.get(huone.nimi, "Huoneesta ei ole kuvausta."))

    if huone.esine is None:
        print("Huoneessa ei ole esineitä.")
    else:
        print(f"Huoneessa on esine: {huone.esine.nimi}")


def show_inventory(pelaaja):
    #Näyttää pelaajan inventaarion ja kertoo kamojen painot.
    print("\n<><> KAMAT <><>")

    if not pelaaja.esineet:
        print("Bludilla ei ole kamaa.")
    else:
        for esine in pelaaja.esineet:
            print(f"- {esine.nimi} (Paino: {esine.paino} kg)")


def collect_item(pelaaja):
    #Pelaaja kerää esineen huoneesta, jos huoneessa on joku esine.
    pelaaja.collect_item()


def move_to_room(pelaaja, huoneet):
    #Huoneita vaihetaan tämän funktion avulla.
    print("\n<><> HUONEET <><>")

    for i, huone in enumerate(huoneet):
        print(f"{i + 1}. {huone.nimi}")

    try:
        choice = int(input("Valitse huone (1-6): ")) - 1

        if 0 <= choice < len(huoneet):
            pelaaja.move(huoneet[choice])
            show_room(pelaaja)
        else:
            print("Virheellinen valinta.")

    except ValueError:
        print("Minnes haluat mennä. Anna huoneen numero)")


def show_instructions():
    #funktio näyttää ohjeet pelaajalle.
    print("\n<><> OHJEET <><>")
    try:
        with open("ohjeet.txt", "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())
    except FileNotFoundError:
        print("Hupsista. Ohjetiedostoa ei löytynyt. VARMISTA ETTÄ KÄYNNISTÄT PELIN OIKEASTA SIJAINNISTA.")


def check_escape_route(pelaaja, reitti):
    #Katsoo onko pelaajalla oikea esine pakoreittejä varten.
    vaatimukset = {
        "Pääovi": "Avain",
        "Huoltokäytävä": "Taskulamppu",
        "Hätäuloskäynti": "RK-62"
    }

    if reitti not in vaatimukset:
        print("Tuntematon reitti.")
        return False

    tarvittava_esine = vaatimukset[reitti]

    if pelaaja.has_item(tarvittava_esine):
        print(f"\nLöysit reitin: {reitti}!")
        print(f"Käytit esinettä: {tarvittava_esine}.")
        print("Pääsit ulos hylätystä tehtaasta!")
        print("Onnittelut siulle. Vedit läpi parhaan pelin vuodelta 2026!")
        return True

    print(f"\nEt voi käyttää reittiä {reitti}.")
    print(f"Tarvitset esineen: {tarvittava_esine}.")
    return False


def choose_escape_route(pelaaja):
    #Valitse tie ulos.
    print("\n<><> ULOSPÄÄSYREITIT <><>")
    print("1. Pääovi (tarvitset avaimen)")
    print("2. Huoltokäytävä (tarvitset taskulampun)")
    print("3. Hätäuloskäynti (tarvitset RK-62:n)")
    print("4. Peruuta")

    valinta = input("Valitse pakoreitti: ")

    reitit = {
        "1": "Pääovi",
        "2": "Huoltokäytävä",
        "3": "Hätäuloskäynti"
    }

    if valinta == "4":
        print("Palaat takaisin tutkimaan tehdasta.")
        return False

    if valinta not in reitit:
        print("Virheellinen valinta.")
        return False

    return check_escape_route(pelaaja, reitit[valinta])

def tee_ymparistoteko(pelaaja):
    #Tee ympäristöystävällinen teko ja saa kestävyyspisteitä.
    print("\n<><> YMPÄRISTÖTEKO <><>")
    print("1. Kierrätä metalliromu")
    print("2. Sulje vuotava vesihana")
    print("3. Soita tiimi, joka poistaa vaaralliset materiaalit")
    print("4. Palaa takaisin")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        pelaaja.kestavyys_pisteet += 1
        print("Kierrätit metalliromun! +1 kestävyyspiste.")

    elif valinta == "2":
        pelaaja.kestavyys_pisteet += 1
        print("Säästit vettä sulkemalla hanan! +1 kestävyyspiste.")

    elif valinta == "3":
        pelaaja.kestavyys_pisteet += 1
        print("Teollasi ehkäisit maailmanlopun!1!! +1 kestävyyspiste.")

    elif valinta == "4":
        print("Palaat takaisin.")

    else:
        print("Teeppäs ympäristöystävällinen teko.")
