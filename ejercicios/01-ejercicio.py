# Escribe un programa que pida al usuario que ingrese una temperatura en grados celsius y la convierta en grados Fahrenheit.

# ¿Cual es la formula?
# °F = °C×(9/5)+32

# pedir los datos al usuario
#Variables, celsius, fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# (), [], division, multiplicacion, suma o resta 
# 2+(3+2)*3 
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")