while True:
    try:
        minutos = int(input("Ingrese los minutos a convertir en segundos (eje: 5): "))
        if minutos < 1:
            print("Los minutos deben ser mayores a 0")
            continue
        break
    except ValueError:
        print("Debe ingresar números, no letras")

print(f"{minutos} minutos son {minutos * 60} segundos")