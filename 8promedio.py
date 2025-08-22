notas = []

for i in range (1, 11):
    while True:
        try:
            n = float(input(f"Ingrese la nota número {i} (ej: 4.5): "))
            if n < 0:
                print("La nota no puede ser negativa")
                continue
            elif n > 5:
                print("La nota no puede ser mayor a 5.0")
                continue
            notas.append(n)
            break
        except ValueError:
            print("Debe ingresar números, no letras")

promedio = sum(notas) / len(notas)
print(f"El promedio es de {promedio}")