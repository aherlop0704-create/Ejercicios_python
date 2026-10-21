try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
finally:
    print("Fin del programa")