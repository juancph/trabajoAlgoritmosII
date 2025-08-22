while True:
    try:
        base = float(input("Ingrese la base de su triángulo (eje: 20): "))
        if base < 1:
            print("La base debe ser mayor a 0")
            continue
        altura = float(input("Ingrese la altura de su triángulo (eje: 12): "))
        if altura < 1:
            print("La altura debe ser mayores a 0")
            continue
        break
    except ValueError:
        print("Debe ingresar números, no letras")

print(f"El area de su triángulo es: {base * altura / 2}")