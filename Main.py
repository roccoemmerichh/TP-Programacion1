import time, os
from obras import *
from funciones import *
from reservas import *
from usuarios import *


# TODO Mejorar para que se ajuste automaticamente cada columna
def mostrar_matriz(matriz, encabezados="-" * 20):
    print()
    for titulo in encabezados: # Encabezados
        print(f"{titulo:<25}", end="")
    print()
    for fila in matriz: # Contenido
        for dato in fila:
            print(f"{dato:<25}", end="")
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
            opciones = 5
            print()
            print("-" * 20)
            print("MENÚ PRINCIPAL")
            print("-" * 20)
            print("1-Gestión de Obras")
            print("2-Gestión de Funciones")
            print("3-Gestión de Reservas")
            print("4-Gestión Usuarios")
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
                    print("3-Modificar obras")
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
                    encabezados_obras = (
                        "id obra",
                        "Nombre",
                        "Fecha",
                        "Horario",
                        "Capacidad",
                        "Precio",
                        "Ocupadas",
                    )
                    mostrar_matriz(obras, encabezados_obras)

                elif opcion == "2":  # Opción 2
                    agregar_obras()
                elif opcion == "3":  # Opción 3
                    updetearObra()

        elif opcion == "2":  # MENÚ FUNCIONES
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ FUNCIONES")
                    print("---------------------------")
                    print("1-Mostrar funciones")
                    print("2-Agregar funcion")
                    print("3-Modificar funcion")
                    print("4-Borrar funcion")
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

                elif opcion == "1":  # Mostrar Funciones
                    encabezados_funciones = ("ID Función", "ID Obra", "Fecha")
                    mostrar_matriz(funciones, encabezados_funciones)

                elif opcion == "2":
                    crear_funcion()
                    
                elif opcion == "3":
                    modificar_funcion()

                elif opcion == "4":
                    borrarfuncion()

        elif opcion == "3":  # MENÚ RESERVAS
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
                    encabezados_reservas = (
                        "Usuario",
                        "NR",
                        "ID Obra",
                        "Cantidad",
                        "Butacas",
                        "Precio",
                        "Total",
                    )
                    mostrar_matriz(reservas, encabezados_reservas)

                elif opcion == "2":  # Opción 2
                    crear_reserva()

        elif opcion == "4":  # MENÚ USUARIOS
            while True:
                while True:
                    opciones = 6
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ USUARIOS")
                    print("---------------------------")
                    print("1-Mostrar Usuarios")
                    print("2-Crear Usuario")
                    print("3-Modificar Usuario")
                    print("4-Borrar Usuario")
                    print("5-Mostrar promedio de edad de Usuarios en la funcion")
                    print("6-Usuarios con mas Reservas")
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
                    encabezados_usuarios = ("ID Usuario", "Nombre", "Email", "Teléfono")
                    mostrar_matriz(usuarios, encabezados_usuarios)

                elif opcion == "2":  # Opción 2
                    crear_usuario()

                elif opcion == "3":  # Opción 3
                    modificar_usuario()

                elif opcion == "4":  # Opción 4
                    borrar_usuario()

                elif opcion == "5":  # Opción 5
                    promedio_edad_por_funcion()

                elif opcion == "6":  # Opción 6
                    usuarios_con_mas_reservas()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


if __name__ == "__main__":  # Para no ejecutar funciones al importar modulos
    main()
