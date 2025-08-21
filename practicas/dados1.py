import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

d1, d2 = lanzar_dados()
print(f"Lanzaste {d1} y {d2} (total = {d1 + d2})")
