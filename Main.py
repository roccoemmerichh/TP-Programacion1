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
    print()
    input("Presione ENTER para continuar")


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
            print("1-Gestión de Obras")
            print("2-Gestión de Reservas")
            print("3-Gestión Usuarios")
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

        elif opcion == "1":  # MENÚ OBRAS
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ OBRAS")
                    print("---------------------------")
                    print("1-Mostrar obras")
                    print("2-Agregar obras")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [
                        str(i) for i in range(0, opciones + 1)
                    ]:  # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":  # Opción salir del submenú
                    break  # Volver al menú anterior

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

        elif opcion == "2":  # MENÚ RESERVAS
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ RESERVAS")
                    print("---------------------------")
                    print("1-Mostrar reservas")
                    print("2-Agregar reservas")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [
                        str(i) for i in range(0, opciones + 1)
                    ]:  # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":  # Opción salir del submenú
                    break  # Volver al menú anterior

                elif opcion == "1":  # Opción 1
                    encabezados_reservas = [
                        "N reserva",
                        "Id obra",
                        "Nombre",
                        "Mail",
                        "total",
                        "Cantidad",
                    ]
                    mostrar_matriz(reservas, encabezados_reservas)

                elif opcion == "2":  # Opción 2
                    agregar_reservas()

        elif opcion == "3":  # MENÚ USUARIOS
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ USUARIOS")
                    print("---------------------------")
                    print("1-Mostrar Usuarios")
                    print("2-Crear Usuario")
                    print("3-Modificar Usuario")
                    print("4-Borrar Usuario")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [
                        str(i) for i in range(0, opciones + 1)
                    ]:  # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":  # Opción salir del submenú
                    break  # Volver al menú anterior

                elif opcion == "1":  # Opción 1
                    mostrar_usuarios()

                elif opcion == "2":  # Opción 2
                    crear_usuario()

                elif opcion == "3":  # Opción 3
                    modificar_usuario()

                elif opcion == "4":  # Opción 4
                    borrar_usuario()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


if __name__ == "__main__":  # Para no ejecutar funciones al importar modulos
    main()
