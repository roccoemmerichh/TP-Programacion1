import time, os, json
from obras import *
from funciones import (
    crear_funcion, modificar_funcion, borrar_funcion, 
    reportes_con_lambdas, obtener_todas_las_funciones
)
from reservas import (
    crear_reserva, modificar_reserva, borrar_reserva, 
    obtener_todas_las_reservas, init_estado_desde_reservas,
    mostrar_reservas
)
from usuarios import (
    crear_usuario, modificar_usuario, borrar_usuario,
    promedio_edad_por_funcion, usuarios_con_mas_reservas,
    obtener_todos_los_usuarios
)

def mostrar_matriz(matriz, encabezados="-" * 20):
    print()
    if isinstance(encabezados, (list, tuple)):
        for titulo in encabezados:
            print(f"{titulo:<25}", end="")
    else:
        print(encabezados)
    print()
    
    if not matriz:
        print("No hay datos para mostrar.")
        print()
        input("Presione ENTER para continuar")
        return

    for fila in matriz:
        for dato in fila:
            print(f"{dato:<25}", end="")
        print()
    print()
    input("Presione ENTER para continuar")


def mostrar_lista_diccionarios(archivo):
    try:
        with open(archivo, encoding="UTF-8") as datos:
            lista = json.load(datos)
            
            if not lista:
                print("\nNo hay obras para mostrar.")
                print()
                input("Presione ENTER para continuar")
                return

            print()
            for clave in lista[0].keys():
                print(f"{clave:<25}", end="")
            print()
            print("-" * (25 * len(lista[0].keys()))) 
            
            for diccionario in lista:
                for dato in diccionario:
                    print(f"{diccionario[dato]:<25}", end="")
                print()
            print()
            input("Presione ENTER para continuar")
    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
    except json.JSONDecodeError:
        print(f"Error: El archivo {archivo} está vacío o mal formado.")
        input("Presione ENTER para continuar")
    except IndexError:
         print("\nNo hay obras para mostrar (archivo vacío).")
         print()
         input("Presione ENTER para continuar")


def limpiar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def ingreso_entero(mensaje="Ingrese un número entero: "):
    """Solamente permite ingresar enteros positivos o 0. Devuelve un int."""
    while True:
        try:
            valor_ingresado = float(input(mensaje).strip())
            valor_entero = int(valor_ingresado)
            if valor_entero != valor_ingresado or valor_entero < 0:
                raise ValueError
            break
        except ValueError:
            print(
                "Error: Ingreso inválido, solamente ingresar numeros enteros positivos"
            )
        except KeyboardInterrupt:
            exit()
        except:
            print("Error inesperado")
    return valor_entero


def ingreso_texto(
    mensaje="Ingrese un texto: ",
    error="Ingreso inválido: No puede quedar vacío. Presione ENTER para reintentar",
):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            input(error)
        else:
            break
    return texto


# ----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
# ----------------------------------------------------------------------------------------------
def main():
    # -------------------------------------------------
    # Inicialización de variables
    # ----------------------------------------------------------------------------------------------
    init_estado_desde_reservas() # Carga el estado de las butacas desde el TXT al inicio
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
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":
            print("Gracias por usar el sistema")
            time.sleep(2)
            limpiar_terminal()
            exit()

        elif opcion == "1":  # MENÚ OBRAS
            while True:
                while True:
                    opciones = 5
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ OBRAS")
                    print("---------------------------")
                    print("[1] Mostrar obras")
                    print("[2] Agregar obra")
                    print("[3] Modificar obra")
                    print("[4] Eliminar obra")
                    print("[5] Estadistica precios")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [
                        str(i) for i in range(0, opciones + 1)
                    ]:  
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":  
                    break  

                elif opcion == "1":  
                    mostrar_lista_diccionarios("archivos/obras.json")

                elif opcion == "2": 
                    agregar_obras("archivos/obras.json")

                elif opcion == "3":  
                    modificar_obra("archivos/obras.json")

                elif opcion == "4": 
                    borrar_obra("archivos/obras.json")

                elif opcion == "5":  
                    estadisticas_precios_obras("archivos/obras.json")


        elif opcion == "2":  # MENÚ FUNCIONES
            while True:
                while True:
                    opciones = 5
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ FUNCIONES")
                    print("---------------------------")
                    print("[1] Mostrar funciones")
                    print("[2] Agregar función")
                    print("[3] Modificar función")
                    print("[4] Borrar función")
                    print("[5] Reportes con Lambdas (map, filter, reduce)")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":
                    break

                elif opcion == "1":  
                    lista_de_funciones = obtener_todas_las_funciones() 
                    mostrar_matriz(
                        lista_de_funciones, ("ID Función", "ID Obra", "Fecha")
                    )

                elif opcion == "2":
                    crear_funcion() 

                elif opcion == "3":
                    modificar_funcion() 
                elif opcion == "4":
                    borrar_funcion() 

                elif opcion == "5":
                    reportes_con_lambdas()

        elif opcion == "3":  # MENÚ RESERVAS
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ RESERVAS")
                    print("---------------------------")
                    print("[1] Mostrar reservas")
                    print("[2] Agregar reserva")
                    print("[3] Modificar reserva")
                    print("[4] Borrar reserva")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [
                        str(i) for i in range(0, opciones + 1)
                    ]:  
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":
                    break

                elif opcion == "1":  
                    lista_de_reservas = obtener_todas_las_reservas()
                    mostrar_reservas(lista_de_reservas)

                elif opcion == "2":  
                    crear_reserva() 

                elif opcion == "3":  
                    modificar_reserva() 

                elif opcion == "4":  
                    borrar_reserva() 

        elif opcion == "4":  # MENÚ USUARIOS
            while True:
                while True:
                    opciones = 6
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ USUARIOS")
                    print("---------------------------")
                    print("[1] Mostrar Usuarios")
                    print("[2] Agregar Usuario")
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
                    ]:  
                        break
                    else:
                        input(
                            "Opción inválida. Presione ENTER para volver a seleccionar."
                        )
                print()

                if opcion == "0":  
                    break 

                elif opcion == "1":  
                    lista_de_usuarios = obtener_todos_los_usuarios()
                    mostrar_matriz(
                        lista_de_usuarios,
                        ("ID Usuario", "Nombre", "Email", "Teléfono", "Edad"),
                    )

                elif opcion == "2":  
                    crear_usuario() 

                elif opcion == "3":  
                    modificar_usuario() 

                elif opcion == "4":  
                    borrar_usuario() 

                elif opcion == "5":  
                    promedio_edad_por_funcion()

                elif opcion == "6":  
                    usuarios_con_mas_reservas()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")

if __name__ == "__main__":
    main()
