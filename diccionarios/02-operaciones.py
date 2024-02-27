products_inventory = {
  'notebook': 10,
  'teclado': 3,
  'monitor': 10
}

# Aplicando items
# [('notebook', 10), ('teclado', 3), ('monitor', 10)]
# [(elemento1), (elemento2), (elemento3)]

# Si queremos imprimir cada producto con cantidad, lo podemos hacer de la siguiente manera

for producto, cantidad in products_inventory.items():
  print(f"El {producto}, tiene una cantidad de: {cantidad}")

# Otro ejemplo
  
productos = { 'productoA': 10, 'productoB': 20 }

# cuando productos le aplico el método items productos.items(), lo que voy a obtener es lo siguiente

# dict_items([('productoA',10), ('productoB', 20)])

