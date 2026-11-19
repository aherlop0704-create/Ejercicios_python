def calcular_media(*valores):
    if len(valores) < 2:
        raise ValueError("Debes introducir al menos dos valores.")
    if not all(isinstance(valor, (int, float)) for valor in valores):
        raise TypeError("Todos los valores deben ser numéricos.")

    return sum(valores) / len(valores)


while True:
    entrada = input(
        "Introduce dos o más números separados por espacios: "
    )
    try:
        numeros = [float(valor) for valor in entrada.split()]
        media = calcular_media(*numeros)
        break
    except ValueError as error:
        print(f"Entrada no válida: {error}")

print(f"La media aritmética es: {media}")
