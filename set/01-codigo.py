mi_set = set()
print(type(mi_set))

# Añadir elementos
mi_set.add(4)
mi_set.add(10)
mi_set.add(10)
mi_set.add(20)
mi_set.add(44)
mi_set.add(2)
print(mi_set)


# Eliminando elementos de un set

mi_set.remove(44)
# mi_set.remove(77)
mi_set.discard(77)
print(mi_set)

#* Operaciones de Conjunto.

#* Intersección

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b) # Obtener la intersección de conjuntos. {3, 4}

#* Unión
print(a | b)

#* Diferencia de conjuntos
print(a - b) # {1, 2}, elementos en "a" pero no en "b"

#* Diferencia simétrica de conjuntos
print(a^b) # {1,2,5,6} elementos en "a" o "b", pero no ambos