numero = int(input("Escribe un número entero: "))

print(f"Tabla del multiplicar del {numero}:")
for multiplica in range(1, 11):
    resultado = numero * multiplica
    print(f"{numero} x {multiplica} = {resultado}")