import time, os

from obras import *
from funciones import *
from reservas import *
from usuarios import *

# obras = [[id_obra][nombre]]
# funciones=[[id_funcion][id_obra][fechas][capacidad]]
# reservas = [[nr][id_funcion][nombre][mail][cant][total]]


def agregar_obras():  # TODO Mover a obras.py
    cant_obras = int(input("Obras que desesa agregar:"))
    for i in range(cant_obras):
        id_obra = len(obras) + 1
        nombre = input("Nombre de la obra que desea agregar:")
        capacidad = int(input("capacidad:"))
        while capacidad < 0:
            print("error la capacidad debe ser mayor que 0")
            capacidad = int(input("capacidad:"))
        precio = int(input("Precio de la obra:"))
        while precio < 0:
            print("Error el precio debe ser mayor que 0")
            precio = int(input("Precio de la obra:"))
        obra = [
            id_obra,
            nombre,
            capacidad,
            precio,
        ]
        obras.append(obra)
        print(f"La obra {nombre} fue agregada con exito")


def agregar_reservas():  # TODO Mover a reservas.py
    cant_reservas = int(input("¿Cuántas reservas desea agregar?: "))
    for i in range(cant_reservas):
        nreserva = len(reservas) + 1
        id_obra = int(input("Ingrese el ID de la obra: "))
        nombre = input("Nombre del usuario: ")
        mail = input("Mail del cliente: ")
        cant = int(input("Cantidad de entradas: "))
        while cant <= 0:
            print("Error: la cantidad debe ser mayor que 0.")
            cant = int(input("Cantidad de entradas: "))
        total = int(input("Total a pagar: "))

        reserva = [nreserva, id_obra, nombre, mail, cant, total]
        reservas.append(reserva)
        print(f"La reserva {nreserva} fue agregada con éxito")


def mostrar_matriz(matriz, encabezados):
    print()
    for titulo in encabezados:
        print(titulo, end="\t")
    print()
    for fila in matriz:
        for dato in fila:
            print(dato, end="\t")
        print()


def limpiar_terminal():
    if os.name == "nt":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Mac/Linux
    return


def menu():  # TODO Mejorar el menú para que cuando se ingrese una tecla inválida no se cierre el programa
    while True:
        print()
        print("===Menu===")
        print("1-Mostrar obras")
        print("2-Agregar obras")
        print("3-Mostrar reservas")
        print("4-Agregar reservas")
        print("5-Agregar Usuario")
        print("6-Mostrar Usuarios")
        print("-" * 20)
        print("0-Salir")

        print()
        opcion = int(input("Escoja una opcion: "))
        if opcion == 0:  # Salir
            print("Gracias por usar el sistema")
            time.sleep(2)
            limpiar_terminal()
            break

        elif opcion == 1:
            encabezados_obras = [
                "id obra",
                "Nombre",
                "Fecha",
                "Horario",
                "Capacidad",
                "Precio",
                "Ocupadas",
            ]
            mostrar_matriz(obras, encabezados_obras)

        elif opcion == 2:
            agregar_obras()

        elif opcion == 3:
            encabezados_reservas = [
                "N reserva",
                "Id obra",
                "Nombre",
                "Mail",
                "total",
                "Cantidad",
            ]
            mostrar_matriz(reservas, encabezados_reservas)

        elif opcion == 4:
            agregar_reservas()

        elif opcion == 5:
            crear_usuario()

        elif opcion == 6:
            mostrar_usuarios()

        else:
            input("ERROR: opcion invalida, presione cualquier tecla para continuar")


if __name__ == "__main__":  # Para no ejecutar funciones al importar modulos
    menu()
