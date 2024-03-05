# Método print()

# print('hola mundo') # hola mundo

# find() y replace()

text = 'Hola, espero que te encuentres muy bien y aprendas el mundo de la programación'
# buscar la posición de la substring "mundo"
position = text.find('mundo')
print(position)
# replace
replaced_text = text.replace('mundo', 'notebook')
print(replaced_text)


# Convert 
email = "Alejandro.Ramirez@correo.com" #alejandro.ramirez@correo.com
upper_case = email.upper()
print(upper_case)

lower_case = email.lower()
print(lower_case)

# Métodos join() y split()
words = ['Hola', 'mundo'] # Hola mundo
joined = ' '.join(words)
print(joined) # Hola mundo

# volver a lo de antes
split = joined.split(' ')
print(split)