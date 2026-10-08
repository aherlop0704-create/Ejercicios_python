
try:
    dividendo = float(input("Introduce el dividendo: "))
    divisor = float(input("Introduce el divisor: "))

    resultado = dividendo / divisor

    print(f"{resultado:.2f}")

except ZeroDivisionError:
    print("ERROR: El dividendo no puede ser cero")

except ValueError:
    print("ERROR: Debes introducir un numero")
