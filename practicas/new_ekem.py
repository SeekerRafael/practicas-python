personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 20}
]

ordenado = sorted(personas, key=lambda p: p["edad"])
print(ordenado)
