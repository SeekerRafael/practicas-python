textoUsuario = input('Ingresa un texto: ').lower()

letras1 = 1
while letras1 > 0:
    letra1 = input('Ingresa una letra: ').lower()
    letras1 = len(letra1) -1

letras2 = 1
while letras2 > 0:
    letra2 = input('Ingresa una letra: ').lower()
    letras2 = len(letra2) -1

letras3 = 1
while letras3 > 0:
    letra3 = input('Ingresa una letra: ').lower()
    letras3 = len(letra3) -1

conteo = textoUsuario.count(letra3)
print(textoUsuario)
print(f"La letra '{letra1}' aparece {textoUsuario.count(letra1)} veces")
print(f"La letra '{letra2}' aparece {textoUsuario.count(letra2)} veces")
print(f"La letra '{letra3}' aparece " +
      ("ninguna vez" if conteo == 0 else "1 vez" if conteo == 1 else f"{conteo} veces"))

total = textoUsuario.split()  
print(len(total))
print(textoUsuario[0])
print(textoUsuario[-1])
print(textoUsuario[::-1])
print(textoUsuario.count('python'))
palabraTexto = 'python' in textoUsuario
print(palabraTexto)
