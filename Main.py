import time, os

from obras import *
from funciones import *
from reservas import *
from usuarios import *

# obras = [[id_obra][nombre]]
# funciones=[[id_funcion][id_obra][fechas][capacidad]]
# reservas = [[nr][id_funcion][nombre][mail][cant][total]]


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


# ----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
# ----------------------------------------------------------------------------------------------
def main():
    # -------------------------------------------------
    # Inicialización de variables
    # ----------------------------------------------------------------------------------------------

    # -------------------------------------------------
    # Bloque de menú
    # ----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 9
            print()
            print("-" * 20)
            print("MENÚ PRINCIPAL")
            print("-" * 20)
            print("1-Mostrar obras")
            print("2-Agregar obras")
            print("3-Mostrar reservas")
            print("4-Agregar reservas")
            print("5-Mostrar Usuarios")
            print("6-Agregar Usuario")
            print("7-Modificar Usuarios")
            print("8-Eliminar Usuarios")
            print("-" * 20)
            print("[0] Salir del programa")
            print("-" * 20)
            print()

            opcion = input("Seleccione una opción: ")
            if opcion in [
                str(i) for i in range(0, opciones + 1)
            ]:  # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":  # Opción salir del programa
            print("Gracias por usar el sistema")
            time.sleep(2)
            limpiar_terminal()
            exit()  # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        # elif opcion == "1":   # Opción 1
        # while True:
        #     while True:
        #         opciones = 4
        #         print()
        #         print("---------------------------")
        #         print("MENÚ PRINCIPAL > MENÚ DE CLIENTES")
        #         print("---------------------------")
        #         print("[1] Ingresar clientes")
        #         print("[2] Opción 2")
        #         print("[3] Opción 3")
        #         print("[4] Opción 4")
        #         print("---------------------------")
        #         print("[0] Volver al menú anterior")
        #         print("---------------------------")
        #         print()

        #         opcion = input("Seleccione una opción: ")
        #         if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
        #             break
        #         else:
        #             input("Opción inválida. Presione ENTER para volver a seleccionar.")
        #     print()

        #     if opcion == "0": # Opción salir del submenú
        #         break # No salimos del programa, volvemos al menú anterior
        #     elif opcion == "1":   # Opción 1
        #         clientes = altaCliente(clientes)
        #         print("Dando de alta al cliente...")

        #     elif opcion == "2":   # Opción 2
        #         ...
        #     elif opcion == "3":   # Opción 3
        #         ...
        #     elif opcion == "4":   # Opción 4
        #         ...

        elif opcion == "1":  # Opción 1
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

        elif opcion == "2":  # Opción 2
            agregar_obras()

        elif opcion == "3":  # Opción 3
            encabezados_reservas = [
                "N reserva",
                "Id obra",
                "Nombre",
                "Mail",
                "total",
                "Cantidad",
            ]
            mostrar_matriz(reservas, encabezados_reservas)

        elif opcion == "4":  # Opción 4
            agregar_reservas()

        elif opcion == "5":  # Opción 5
            mostrar_usuarios()

        elif opcion == "6":  # Opción 6
            crear_usuario()

        elif opcion == "7":  # Opción 7
            modificar_usuario()

        elif opcion == "8":  # Opción 8
            borrar_usuario()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


if __name__ == "__main__":  # Para no ejecutar funciones al importar modulos
    main()
