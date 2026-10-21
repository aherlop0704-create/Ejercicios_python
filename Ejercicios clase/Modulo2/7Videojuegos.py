videojuegos = ["Minecraft", "Fortnite", "Valorant", "FIFA", "GTA V"]

buscar = input("Introduce un videojuego: ")
juego = ""
esta = False

for juego in videojuegos:
    esta = juego.lower().strip() == buscar.lower().strip()
    if esta:
        break

if esta:
    print("si")
else:
    print("no")
    
