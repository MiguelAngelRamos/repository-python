mi_diccionario = {'nombre': 'Sofia', 'cuidad': 'Santiago', 'pais': 'Chile'}

# Recorrer las claves
for clave in mi_diccionario:
    print(clave)

for key in mi_diccionario.keys():
    print(key)

# Recorrer sus valores

for value in mi_diccionario.values():
    print(value)

# Recorrer clave y el valor

for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")