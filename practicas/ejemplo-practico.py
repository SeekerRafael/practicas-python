usuarios = []

def registrar_usuario():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))
    usuarios.append({
        "nombre": nombre,
        "correo": correo,
        "edad": edad
    })

def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados")
        return
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nombre']} | {u['correo']} | {u['edad']} años")

while True:
    print("\n1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        break
    else:
        print("Opción inválida")
