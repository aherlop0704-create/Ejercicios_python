
while True:
    nombre = input("Escriba su nombre [5-10]: ")

    if len(nombre) in range(5,11) and nombre.isalpha():
        print("Usuario correcto")
        break
    else:
        print("Formato del nombre incorrecto")

while True:
    contraseña = input("Escriba su contraseña (8 caracteres mínimo): ")

    if len(contraseña) > 8 and contraseña.isalnum():
        print("Contraseña correcta")
        print("\nUsuario y contraseña establecidos correctamente")
        break
    else:
        print("Longitud o formato de contraseña incorrectos")
        break