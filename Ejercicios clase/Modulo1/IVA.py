from sys import exit
from Modulo1 import calcular_IVA

p_bruto = float()
porcentaje = float()
p_neto = calcular_IVA(p_bruto, porcentaje)

try:
    p_bruto = float(input("Introduce el precio bruto: "))
except ValueError:
    print("ERROR: Valor no válido")
    exit(1)
    
try: 
    porcentaje = float(input("Escribe el porcentaje del IVA [1-100]: "))
    
    p_neto = 0.0
    
    if 0 <= porcentaje <= 100:
        p_neto = calcular_IVA(p_bruto, porcentaje)
        print(f"Precio sin IVA: {p_bruto:.2f}")
        print(f"Precio con IVA: {p_neto:.2f} ({porcentaje}%)")
    else:
        print("Valor de porcentaje fuera de rango [1-100]")
        
        
except ValueError:
    print("ERROR: Porcentaje no válido")
    exit(1)
    
