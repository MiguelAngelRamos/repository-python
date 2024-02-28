from gestor_contacto.contactos import add_contacto, mostrar_contactos
from gestor_contacto.utilidades import leer_entrada

def menu():
    while True:
        print("\nGestor de Contactos")
        print("1. Añadir Contacto")
        print("2. Mostrar contactos")
        print("3. Salir")
        opcion = leer_entrada("Seleccione una opción: ")

        if opcion == "1":
            nombre = leer_entrada("\nNombre del contacto: ")
            telefono = leer_entrada("Teléfono del contacto: ")
            add_contacto(nombre, telefono)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no válida. Intente de nuevo")

if __name__ == "__main__":
    menu()