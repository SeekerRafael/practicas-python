
palabra = 'Rafael'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# mejor ejemplo
lista2 = [letra for letra in 'rafael']
print(lista2)

lista3 = [n for n in range(0, 21, 2)]
print(lista3)


lista4 = [num if num * 2 > 10 else 'no' for num in range(0,21,2)]
print(lista4)

lista5 = ['menor' if num <= 18 else 'mayor' for num in range(0, 21)]
print(lista5)
