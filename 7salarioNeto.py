aumento = 0

while True:
    try:
        salario = int(input("Ingrese su salario (eje: 1000000): "))
        if salario < 1:
            print("El salario debe ser mayor a 0")
            continue
        horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
        if horas_trabajadas < 1:
            print("Las horas trabajadas deben ser mayores a 1")
            continue
        break
    except ValueError:
        print("Debe ingresar números no letras")

if horas_trabajadas >= 38:
    aumento = salario * 0.5
    salario += aumento

print(f"Su salario final es de {salario} pesos, con un aumento de {aumento} pesos")