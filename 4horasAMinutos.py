while True:
    try:
        horas = int(input("Ingrese las horas a convertir en minutos (eje: 5): "))
        if horas < 1:
            print("Las horas deben ser mayores a 0")
            continue
        break
    except ValueError:
        print("Debe ingresar números, no letras")

print(f"{horas} horas son {horas * 60} minutos")