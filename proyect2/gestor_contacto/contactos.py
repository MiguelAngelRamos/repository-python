from . import contactos

def add_contacto(nombre, telefono):
    contacto = {"nombre": nombre, "telefono": telefono}
    contactos.append(contacto)
    print("Contacto añadido correctamente.")

def mostrar_contactos():
    if contactos:
        print("** Contactos **")
        for contacto in contactos:
            print(f"{contacto['nombre']} - {contacto['telefono']}")
    else:
        print("No hay contactos en la agenda")


# [
#  {"nombre": 'sofia', "telefono": 209494}, 
#  {"nombre": "catalina", "telefono": 2929}
# ]