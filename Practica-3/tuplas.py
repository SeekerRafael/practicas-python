mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
 
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
 
mi_lista = list(mi_tupla)

mi_tupla = (1, 2, 3, 4)
 
a, b, c, d = mi_tupla

print(mi_tupla)

# Crear un set
mi_set = {1, 2, 3, 3, 4}

print(mi_set)  # {1, 2, 3, 4}  -> elimina el duplicado

# Agregar elementos
mi_set.add(5)
print(mi_set)  # {1, 2, 3, 4, 5}

# Operaciones entre sets
a = {1, 2, 3, 8}
b = {3, 4, 9, 4}

print(a | b)  # Unión -> {1, 2, 3, 4, 5}
print(a & b)  # Intersección -> {3}
print(a - b)  # Diferencia -> {1, 2}

