name = input("Mikä on nimesi:")
age  = int(input("Kuinka vanha olet: "))
if age <= 12:
    print("Olet alaikäinen, niin et voi pelata peliä.")
else:
    print(f"Tervetuloa peliin, {name}!")

while True:
        print("....GAME MENU....")
        print("1. aloita peli")
        print("2. ohjeet")
        print("3. sulje peli")

        action = int(input("Mitä haluat tehdä? "))

        if action == 1:
            print("Peli alkaoi. Gl!")

        elif action == 2:
            print("ohjeita ei vielä ole.")

        elif action == 3:
            print("Peli suljetaan.")
            break

        else:
            print("Komentoa ei löydy.")
            break

print(name)
print(age)