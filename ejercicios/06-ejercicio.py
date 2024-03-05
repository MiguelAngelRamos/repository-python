# Ejercicio de lógica para entrevista laboral.

# Enunciado del Ejercicio

# Crea una función en python que tome dos listas de numeros enteros y retorne una nueva lista con los elementos que se encuentran en ambas listas, sin repetir los elementos en la lista resultante, la funcion debe ser eficiente en terminos de complejidad.

# lista_1 = [1,2,2,4,5,6]
# lista_2 = [6,6,2,3,5,1]
def interseccion_listas(lista_1, lista_2):
    conjunto_1 = set(lista_1)
    conjunto_2 = set(lista_2)

    # Realizamos la intersección de ambos conjuntos
    interseccion = conjunto_1.intersection(conjunto_2)

    lista_interseccion = list(interseccion)

    return lista_interseccion


# Vamos a invocar la función
lista_1 = [1,2,2,4,5,6]
lista_2 = [6,6,2,3,5,1]

resultado = interseccion_listas(lista_1, lista_2)
print(resultado)