def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número.")


def calcular_media(valor1, valor2):
    return (valor1 + valor2) / 2


numero1 = leer_numero("Introduce el primer número: ")
numero2 = leer_numero("Introduce el segundo número: ")
media = calcular_media(numero1, numero2)

print(f"La media aritmética es: {media}")