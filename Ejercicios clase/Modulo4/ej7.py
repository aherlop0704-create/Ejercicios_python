import json

with open("user.json", "r", encoding="utf-8") as f:
    usuario = json.load(f)

usuario["ciudad"] = "Granada"

print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Profesión:", usuario["profesión"])
print("Ciudad:", usuario["ciudad"])

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(usuario, f, indent=2)
