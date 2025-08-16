import random

num = random.randint(1, 100)
numero = 0
print(num)
vidas = int(input('Cuntas vidas quieres tener? '))

while numero != num:
    numero = int(input('Intenta adivinar que numero es entre el 1 y 100: '))

    if numero < 1 or numero > 100:
        print('Ingresa un numero entre el 1 y 100')
        continue

    if numero > num:
        print('el numero que ingresaste es grande')
    elif numero < num:
        print('el numero que ingresaste es pequeno')
    else:
        print(f'le atinaste al numero, te sobraron {vidas} vidas')
        break

    vidas -= 1
    if vidas == 0:
        print(f'Te quedaste sin vidas, el numero era {num}')
        break
    else:
        print(f'te quedan {vidas} vidas')

