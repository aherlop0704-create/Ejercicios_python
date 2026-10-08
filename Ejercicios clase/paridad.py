
from Modulo1 import es_par
x = int(input("Escribe un número: \n"))

if(x%2 ==0):
    print(f"El numero {x} es par")

else:
    print (f"El numero {x} es impar")

print(f"{es_par(x)}")