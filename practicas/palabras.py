import string

texto = input("Escribe un texto: ")
texto = texto.lower()
for simbolo in string.punctuation:
    texto = texto.replace(simbolo, "")
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
for palabra, veces in frecuencia.items():
    print(f"{palabra}: {veces}")
