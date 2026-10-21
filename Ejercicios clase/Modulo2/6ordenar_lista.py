cadena = input("Introduce números separados por comas: ")

lista = cadena.split(',')
parse = []

for numero in lista:
    parse.append(int(numero)) 

parse.sort()

print(parse)