edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Mu chico")
elif 18 <= edad <= 64:
    print("Adulto")
else:
    print("Mu viejo")