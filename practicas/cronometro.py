import time

def cronometro(segundos):
    while segundos:
        print(f"⏳ {segundos} segundos restantes")
        time.sleep(1)
        segundos -= 1
    print("¡Tiempo terminado! 🔔")

cronometro(5)
