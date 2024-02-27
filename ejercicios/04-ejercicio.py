# Iniciamos con diccionario vacio para almacenar la información de los clientes

#clientes = {
#    'sofia': 2828991
#}

clientes = {}

def agregar_cliente(nombre, telefono):
    clientes[nombre] = telefono
    print(f"El cliente: {nombre} se agrego con exito!.")


def actualizar_telefono(nombre, nuevo_telefono):
    # Verificar si el cliente existe
    if nombre in clientes:
        clientes[nombre] = nuevo_telefono
        print(f"Teléfono de: {nombre}, se actualizo con éxito.")
    else:
        print("Cliente no encontrado")


def eliminar_cliente(nombre):
    if nombre in clientes:
        del clientes[nombre]
        print(f"Cliente {nombre}, eliminado con éxito.")
    else:
        print("Cliente no encontrado.")

def listar_clientes():
    if clientes:
        print("Listado de clientes:")
        for nombre, telefono in clientes.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("No hay clientes registrados")

# Utilizar funciones

agregar_cliente("Sofia", 2828991)
agregar_cliente("Richard", 4646461)
actualizar_telefono("Sofia", 7777991)
eliminar_cliente("Richard")
listar_clientes()

# CRUD  CREATE READ UPDATE DELETE