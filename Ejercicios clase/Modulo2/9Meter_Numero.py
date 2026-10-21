try:
    numero = int(input("Introduce un numero: "))
except ValueError:
    print("No es un numero")
else:
    print(numero)
