import random

opciones = ["piedra", "papel", "tijeras"]

jugador = input("Elige piedra, papel o tijeras: ").lower()
cpu = random.choice(opciones)

print(f"CPU eligió: {cpu}")

if jugador == cpu:
    print("¡Empate!")
elif (jugador == "piedra" and cpu == "tijeras") or \
     (jugador == "papel" and cpu == "piedra") or \
     (jugador == "tijeras" and cpu == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste.")
