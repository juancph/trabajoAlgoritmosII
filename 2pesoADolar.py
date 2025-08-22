while True:
   try:
      pesos = int(input("Ingrese los pesos a convertir a dólares (ej: 20000): "))
      if pesos < 1:
         print("El número tiene que ser mayor a 0")
         continue
      break
   except ValueError:
      print("Debe ingresar números, no letras")

print(f"{pesos} COP en dólares son: {pesos//4000} USD")