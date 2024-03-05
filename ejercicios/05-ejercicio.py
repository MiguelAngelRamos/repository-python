# Iniciar el Stock de Libro
# Simular los prestamos
# Gestionar Devoluciones
# Notificar disponibilidad
# Limitación
# Reporte de Stock

# librerias de python a utilizar "time", "random"

import time
import random

# Inicializacion de los stocks de los libros
stock_mascara_roja = 2
stock_billy_summers = 2

# Contador de operaciones
contador_operaciones = 0

# Simulacion de prestamos
def simular_prestamo():
    global stock_mascara_roja, stock_billy_summers, contador_operaciones

    # Selección aleatoria de libro y cantidad de prestamo
    libro = random.choice([1, 2])
    cantidad = random.randint(1,3) # cantidad de prestamo

    # Procesamiento de préstamo
    if libro == 1 and stock_mascara_roja >= cantidad:
        stock_mascara_roja = stock_mascara_roja - cantidad
        # stock_mascara_roja -= cantidad
        print(f"Prestamo de {cantidad} unidad(es) del libro mascara roja realizado")
    elif libro == 2 and stock_billy_summers >= cantidad:
        stock_billy_summers = stock_billy_summers - cantidad
        print(f"Prestamo de {cantidad} unidad(es) del libro billy summers realizado")
    else:
        print("No hay stock suficiente para el préstamos solicitado")

    contador_operaciones = contador_operaciones + 1
    verificar_notificaciones()

def verificar_notificaciones():
    # Verificar disponibilidad para notificar a los usuarios
    if stock_mascara_roja > 0:
        print("Notificacion: el Libro mascara roja, si esta disponible para prestamo.")
    if stock_billy_summers > 0:
        print("Notificacion: el libro billy summers, si esta disponible para prestamo")

    # Reporte de stock cada 10 operaciones
    if contador_operaciones % 10 == 0:
        print(f"Reporte de stock - Libro Mascara Roja: {stock_mascara_roja}, Libro Billy Summers: {stock_billy_summers}")


# Simulacion de una bibioleteca
for _ in range(5):
    simular_prestamo()
    time.sleep(5)