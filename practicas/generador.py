import random
import string

def generar_password(longitud=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

print("Contraseña generada:", generar_password())
