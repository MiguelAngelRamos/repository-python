# Crear un string Unicode en python
# U+1F30E el globo terraqueo

cadena_unicode = 'Hola, mundo! 👋🌍'

# Codificar el string Unicode en una secuencia de bytes usando UTF-8
cadena_codificada_utf8 = cadena_unicode.encode('utf-8')

# Mostrar la secuencia de bytes codificada
print(cadena_codificada_utf8)

# Decodificar la sencuencia de bytes
cadena_codificada_utf8 = cadena_codificada_utf8.decode('utf-8')

print(cadena_codificada_utf8)