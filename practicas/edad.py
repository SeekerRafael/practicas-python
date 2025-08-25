from datetime import date

def calcular_edad(año, mes, dia):
    hoy = date.today()
    nacimiento = date(año, mes, dia)
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

print("Tienes", calcular_edad(2000, 8, 15), "años")
