import random
import string

longitud = 12
caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
print("Contraseña generada:", contraseña)
