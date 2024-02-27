import math

def area_cuadrado(lado):
    return lado * lado

def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def execute():
    print("Calculadora de áreas")
    print("1. Cuadrado")
    print("2. Circulo")
    print("3. Rectangulo")

    opcion = input("Seleccione la figura para calcular el area (1/2/3): ")

    if opcion == '1':
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"El área del cuadrado es: {area_cuadrado(lado)}")
    elif opcion == '2':
        radio = float(input("Ingrese el radio del circulo"))
        print(f"El área del circulo es: {area_circulo(radio)}")
    elif opcion == '3':
        base = float(input("Ingrese la base del rectangulo"))
        altura = float(input("Ingrese la altura del rectangulo"))
        print(f"El area del rectangulo es: {area_rectangulo(base, altura)}")


if __name__ == "__main__":
    execute()


#* 1 + 2 = 3
#* '10' + '4' = '104' ? 14???? o no??

#! float("hola") -> no hay numero equivalente para "hola"
#* float("1") -> 1.0
#* float("424.3") -> 424.3









