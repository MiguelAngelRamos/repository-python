# Nuestras funciones
#!def seleccionarTipoDeCafe()

#* snake_case
def seleccionar_tipo_de_cafe():
    print("¿Qué tipo de café te gustaría?")
    print("1: Expresso")
    print("2: Americano")
    print("3: Cappucino")
    # int es a integer es que valor entero sin punto decimal
    opcion = int(input("Seleccione una opción (1-3): "))
    return opcion

def seleccionar_taza():
    print("¿Qué que tamaño de taza prefieres?")
    print("1: Pequeña")
    print("2: Mediana")
    print("3: Grande")
    opcion = int(input("Seleccione una opcion (1-3): "))
    return opcion

# taza es el tamaño de la misma
def preparar_cafe(tipo_de_cafe, taza):
    print("Preparando tu café......")

    if tipo_de_cafe == 1:
        print("Preparando un expresso...")
    elif tipo_de_cafe == 2:
        print("Preparando un americano...")
    elif tipo_de_cafe == 3:
        print("Prerando un capuchino...")
    # control + d 
    if taza == 1:
        print("en una taza pequeña...")
    elif taza == 2:
        print("en una taza mediana...")
    elif taza == 3:
        print("en una taza grande...")
    
    print("Tu Café esta listo!. Enjoy!")

tipo_de_cafe = seleccionar_tipo_de_cafe()
taza = seleccionar_taza()

preparar_cafe(tipo_de_cafe, taza)