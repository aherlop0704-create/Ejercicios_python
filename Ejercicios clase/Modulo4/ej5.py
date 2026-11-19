'''
def apliar(pila,num):
    pila.append(num)

def desapilar(pila,num):
    return pila.pop()
'''

pila = []

pila.append(420)
pila.append(69)
pila.append(67)

print(f"Pila original: {pila}")
for numero in pila:
    print (f"{numero}")

pila.pop()

print(f"Pila final: {pila}")
for numero in pila:
    print (f"{numero}")