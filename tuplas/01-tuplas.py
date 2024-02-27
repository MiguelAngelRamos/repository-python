# Tuplas son una estructura de dato, similares a las listas, pero con diferencia que las tuplas son inmutables, no puedes cambiar, añadir, ni eliminar elementos de la tupla.

# Caso de uso: En situaciones donde quieres asegurar que los datos permanezcan constantes.

# Crear un tupla

my_tupla = 1,2,3
mi_tupla = (1,2,3) # Forma recomendada.

# Crear una tupla vacia

# {} para los diccionarios
# [] para las listas
# () para las tuplas
tupla_vacia = ()

# Crear una tupla con un elemento
tupla_un_elemento = (1,)

# Acceder a los elementos de una tupla

productos_electronicos = ('monitor', 'notebook', 'teclado', 'mouse')
print(productos_electronicos[2])

# Inmutabilidad
videos_juegos = ('lol', 'age of empires', 'cs', 'mario kars')
# videos_juegos[0] = 'fortnite'

# Desempaquetado de tuplas
vg1, vg2, vg3, vg4 = videos_juegos

print(vg1)
print(vg2)
print(vg3)
print(vg4)

# Métodos de tuplas
new_tupla = ('python', 'java', 'c', 'c#', 'php','cobol', 'java', 'python', 'python')
print(new_tupla.count('python')) # count contamos cuantas veces aparece un elemento en la tupla
print(new_tupla.index('java'))