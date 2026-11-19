l_nums = list(range(1,6))

while(True):
    try:
        print(f"Lista: {l_nums}")
        num = int(input("Introduce un Numero a eliminar de la lista >> "))
        if (num in l_nums):
            l_nums.remove(num)
            print(f"Numero eliminado con exito. Lista final: {l_nums}")
            break
        else:
            print("ERROR: El numero no está en la lsita")
            continue
    except ValueError:
        print("No has introducido un numero entero")
        continue