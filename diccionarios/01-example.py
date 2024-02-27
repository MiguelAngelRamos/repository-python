nuestro_diccionario = {
  'nombre': 'Sofia', 
  'edad': 27
  }

# Accediendo a sus valores por medio de clave (key)
print(nuestro_diccionario['nombre']) # Sofia
print(nuestro_diccionario['edad']) # 27

## Modificando Valores
nuestro_diccionario['edad'] = 28
print(nuestro_diccionario['edad'])
print(nuestro_diccionario)

## Agregando Pares Clave-Valor
nuestro_diccionario['profesion'] = 'Ingeniera de Software'
print(nuestro_diccionario)

diccionario_frutas = {
  1: 'Manzana',
  2: 'Naranja',
  3: 'Sandia',
  4: 'Melón'
}
# Accediendo a sus valores por medio de clave (key)
print(diccionario_frutas[1]) # Manzana
print(diccionario_frutas[2]) # Naranja
print(diccionario_frutas[3]) # Sandia
print(diccionario_frutas[4]) # Melón