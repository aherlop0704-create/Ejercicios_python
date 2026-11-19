compras_trimestre ={
    "enero": 1000,
    "febrero": 2000,
    "marzo": 3000
}
media = 0
for compra in compras_trimestre.values():
    media += compra
media /= len(compras_trimestre)

print(f"Media: {media}")