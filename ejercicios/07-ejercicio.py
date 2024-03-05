# Enunciado:

# Escribe un programa en Python que reciba un texto y retorne un diccionario con las palabras que contiene el texto como claves y el número de veces que aparece cada palabra en el texto como valores. Considera lo siguiente:

# 1. Una palabra se define como una secuencia de caracteres alfabéticos (a-z, A-Z), y las palabras son insensibles a las mayúsculas y minúsculas (es decir, "Hola" y "hola" se consideran la misma palabra).
# 2. Ignora cualquier carácter que no sea alfabético, considerándolos como separadores de palabras.
# 3. Asume que el texto no contiene caracteres especiales de otros idiomas (acentos, eñes, etc.), pero tu solución debe ser fácilmente adaptable para incluirlos.

def counter_word(text):
    text = text.lower()

    clean_text = ""

    for caracter in text:#hola 2024
        if caracter.isalpha():
            #* "" = "" + "h"
            #* "h"
            #* h = h + o
            #* ho
            # clean_text += caracter
            clean_text = clean_text + caracter
        else:
            clean_text = clean_text + " "

    
    words = clean_text.split()
    print(words)

    
text = "Hola, ¿cómo estás? !Yo estoy genial, apriendo ejercicios de lógica en python 3."
counter_word(text)
    
          