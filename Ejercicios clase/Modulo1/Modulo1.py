def suma(a,b):
    return a+b

def resta(a,b):
    return a-b
    
def multiplicacion (a,b):
    return a*b
    
def division (a,b):
    return a/b
    
def elevar (a,b):
    return a**b

def diventera (a,b):
    return a//b
    
def modulo (a,b):
    return a%b

def es_par(n: int):
    if n % 3 == 0:
        return f"{n} es par"
    else:
        return f"{n} es impar"

def calcular_IVA(precio_bruto:float, porcentaje:float):
    return precio_bruto * ((porcentaje/100)+1)