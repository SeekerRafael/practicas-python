import random

while True:
    input("Presiona Enter para lanzar los dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Dado 1: {dado1}, Dado 2: {dado2}")

    if input("¿Lanzar otra vez? (s/n): ").lower() != "s":
        break
