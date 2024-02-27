# Creación de una lista
# Los indices de una lista comienzan desde 0
# Array, Arreglos o Vectores -> listas
mi_lista = [1, 2, 3, 4, 5]
#  indices  0, 1, 2, 3, 4
print("Lista: ", mi_lista)

# Recuerda en Python, el indice comienza en 0
print("Primer Elemento: ", mi_lista[0]) # 1
print("Tercer Elemento: ", mi_lista[2]) # 3

# Modificación de elementos
mi_lista[1] = 60
print("Lista después de modificar el segundo elemento:", mi_lista)

# Añadir elementos
mi_lista.append(6)
print("Lista después de añadir un elemento: ", mi_lista)

# Longitud de la lista
print("Longitud de la lista:", len(mi_lista))

# Elimina el último elemento y lo devuelve
elemento_eliminado = mi_lista.pop()
print("Elemento eliminado con pop():", elemento_eliminado)
print("Lista despues de pop(): ", mi_lista)

# Recorrer una lista

empresas = ["microsoft", "google", "amazon", "openia", "facebook", "netflix", "disneyplus"]

# Para -> for
for empresa in empresas:
    print(empresa)