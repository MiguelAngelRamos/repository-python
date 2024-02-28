# Bucle while, se ejecuta mientras se cumpla una condición
# numero = float(input("Por favor, ingresa un número positivo (si ingresas un numero negativo terminas el bucle): "))

while numero >= 0:
    print(f"Has ingresado el numero:  {numero}")
    numero = float(input("Ingresa otro número positivo para continuar o para terminar la ejecución ingrese un numero negativo: "))

# while True:
#     print("Soy un ciclo infinito no me detengo jamas!!")

print("Has ingresado un numero negativo, por lo tanto el programa a finalizado.")