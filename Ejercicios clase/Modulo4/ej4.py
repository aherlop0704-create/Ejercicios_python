usuarios = [
    {"nombre": "Jose", "edad": 24},
    {"nombre": "Antonio", "edad": 26},
    {"nombre": "Isma", "edad": 25},
]
nombre = input("Escribe un nombre: ")
while(True):
    try:    
        edad = int(input("Escribe una edad: "))
        break
    except ValueError:
        print("ERROR: la edad tiene que ser un número")

usuarios.append({"nombre":nombre, "edad":edad})

print(f"Lista final: ")

archivo = open("usuario.txt", "w", encoding="utf-8")

for datos in usuarios:
    print(f"Nombre: {datos["nombre"]} - Edad: {datos["edad"]}\n")
    archivo.write(f"Nombre: {datos["nombre"]} - Edad: {datos["edad"]}\n")


archivo.close()
print("Archivo guardado")