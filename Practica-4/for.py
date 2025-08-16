lista = ['rafa', 'bris', 'rosa']

posicion = 1
for nombre in lista:
    print(f'{posicion}: {nombre}')
    posicion += 1

for nombres in lista:
    if nombres.startswith('r'):
        print(nombres)
    else:
        print(f'{nombres} no empieza con r')

numeros = [1,2,3,4]

total = 0
for num in numeros:
    total = num + total

print(total)


# Pedir texto al usuario
texto = input("Ingresa un texto: ").lower()

# Pedir 3 letras al usuario y asegurarnos que sean solo una letra cada una
letras = []
while len(letras) < 3:
    letra = input(f"Ingresa la letra {len(letras)+1}: ").lower()
    if len(letra) == 1 and letra.isalpha():
        letras.append(letra)
    else:
        print("Por favor ingresa solo una letra válida.")

# Contar cuántas veces aparece cada letra y guardar en un diccionario
conteos = {}
for letra in letras:
    count = texto.count(letra)
    if count == 0:
        mensaje = "ninguna vez"
    elif count == 1:
        mensaje = "1 vez"
    else:
        mensaje = f"{count} veces"
    conteos[letra] = mensaje


frutas = {
    "manzana": 3,
    "banana": 5,
    "naranja": 2
}

for fruta, cantidad in frutas.items():
    print(f"{fruta}: {cantidad}")
