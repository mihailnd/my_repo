name = input("Mikä on nimesi? ")
age = int(input("Kuinka vanha olet? "))

if age < 12:
    print("Peli on sallittu vain 12 vuotta täyttäneille.")

else:
    print(f"Tervetuloa peliin, {name}!")

    inventory = []

    def start_game():
        print("\nOlet aloittanut pelin!")
        print("Olet hylätyllä tehtaalla.")
        print("Tutki tehtaan ympäristöä ja kerää esineitä.")

    def show_inventory():
        print("\n--- inventaario ---")

        if len(inventory) == 0:
            print("inventaario on tyhjä.")
        else:
            for esine in inventory:
                print(f"- {esine}")

    def collect_item():
        esine = input("Minkä esineen haluat kerätä? ")

        if esine.strip() == "":
            print("Et kirjoittanut esineen nimeä.")
        else:
            inventory.append(esine)
            print(f"Keräsit esineen: {esine}")

    while True:
        print("\n.... GAME MENU ....")
        print("1. Aloita peli")
        print("2. Tarkista inventaario")
        print("3. Kerää esine")
        print("4. Sulje peli")

        action = input("Mitä haluat tehdä? ")

        if action == "1":
            start_game()

        elif action == "2":
            show_inventory()

        elif action == "3":
            collect_item()

        elif action == "4":
            print(f"Kiitos pelaamisesta, {name}!")
            break

        else:
            print("Komentoa ei löydy. Yritä uudelleen.")
