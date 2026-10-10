name = input("Mikä on nimesi: ")
age = int(input("Kuinka vanha olet: "))

if age < 12:
    print("Peli on sallittu vain 12 vuotta täyttäneille.")

else:
    print(f"Tervetuloa peliin, {name}!")

    while True:
        print("\n.... GAME MENU ....")
        print("1. Aloita peli")
        print("2. Ohjeet")
        print("3. Sulje peli")

        action = input("Mitä haluat tehdä? ")

        if action == "1":
            print("Peli alkaa. Good luck!")

        elif action == "2":
            print("Ohjeita ei vielä ole.")

        elif action == "3":
            print("Peli suljetaan.")
            break

        else:
            print("Komentoa ei löydy. Yritä uudelleen.")

    print(f"Kiitos pelaamisesta, {name}!")