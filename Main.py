import time, os

from obras import *
from funciones import *
from reservas import *
from usuarios import *


# TODO Mejorar para que se ajuste automaticamente cada columna
def mostrar_matriz(matriz, encabezados="-" * 20):
    print()
    for titulo in encabezados:  # Encabezados
        print(f"{titulo:<25}", end="")
    print()
    for fila in matriz:  # Contenido
        for dato in fila:
            print(f"{dato:<25}", end="")
        print()
    print()
    input("Presione ENTER para continuar")


def mostrar_lista_diccionarios(lista):
    print()
    for clave in lista[0].keys():  # Encabezados
        print(f"{clave:<25}", end="")
    print()
    for diccionario in lista:  # Contenido
        for dato in diccionario:
            print(f"{diccionario[dato]:<25}", end="")
        print()
    print()
    input("Presione ENTER para continuar")


def limpiar_terminal():
    if os.name == "nt":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Mac/Linux


def ingreso_entero(mensaje="Ingrese un número entero: "):
    """Solamente permite ingresar enteros positivos o 0. Devuelve un int."""
    while True:
        valor = input(mensaje)
        if valor.isnumeric():
            return int(valor)
        else:
            print("ERROR: Ingreso inválido, solamente ingresar numeros enteros")


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
            print("[1] Gestión de Obras")
            print("[2] Gestión de Funciones")
            print("[3] Gestión de Reservas")
            print("[4] Gestión de Usuarios")
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
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ OBRAS")
                    print("---------------------------")
                    print("[1] Mostrar obras")
                    print("[2] Agregar obra")
                    print("[3] Modificar obra")
                    print("[4] Eliminar obra")
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
                    mostrar_lista_diccionarios(obras)

                elif opcion == "2":  # Opción 2
                    mostrar_lista_diccionarios(obras)
                    agregar_obras()
                    mostrar_lista_diccionarios(obras)

                elif opcion == "3":  # Opción 3
                    mostrar_lista_diccionarios(obras)
                    modificar_obra()
                    mostrar_lista_diccionarios(obras)

                elif opcion == "4":  # Opción 4
                    mostrar_lista_diccionarios(obras)
                    borrar_obra()

        elif opcion == "2":  # MENÚ FUNCIONES
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ FUNCIONES")
                    print("---------------------------")
                    print("[1] Mostrar funciones")
                    print("[2] Agregar función")
                    print("[3] Modificar función")
                    print("[4] Borrar función")
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
                    mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

                elif opcion == "2":
                    crear_funcion()

                elif opcion == "3":
                    modificar_funcion()

                elif opcion == "4":
                    borrar_funcion()

        elif opcion == "3":  # MENÚ RESERVAS
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ RESERVAS")
                    print("---------------------------")
                    print("[1] Mostrar reservas")
                    print("[2] Agregar reserva")
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
                    mostrar_matriz(
                        reservas,
                        (
                            "Usuario",
                            "NR",
                            "ID Obra",
                            "Cantidad",
                            "Butacas",
                            "Precio",
                            "Total",
                        ),
                    )

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
                    print("[1] Mostrar Usuarios")
                    print("[2] Crear Usuario")
                    print("[3] Modificar Usuario")
                    print("[4] Borrar Usuario")
                    print("[5] Mostrar promedio de edad de Usuarios en la funcion")
                    print("[6] Usuarios con mas Reservas")
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
                    mostrar_matriz(
                        usuarios, ("ID Usuario", "Nombre", "Email", "Teléfono","Edad")
                    )

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

