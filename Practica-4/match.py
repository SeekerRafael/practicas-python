valor = 2

match valor:
    case 1:
        print("Es uno")
    case 2:
        print("Es dos")
    case 3:
        print("Es tres")
    case _:
        print("No es ninguno de los anteriores")


edades = [15, 20, 18, 25, 12, 30]

for edad in edades:
    match edad:
        case edad if edad <= 18:
            print(f"{edad} años → menor")
        case edad if edad > 18:
            print(f"{edad} años → mayor")
