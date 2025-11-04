import json
from Main import *


def agregar_obras(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            obras = json.load(datos)

            if len(obras) == 0:
                nuevo_id = 1
            else:
                nuevo_id = max(obra["ID"] for obra in obras) + 1

            nombre = ingreso_texto(  # Ingreso Nombre
                "Nombre de la obra: ",
                "Ingreso Inválido: El nombre no puede estar vacío. Presione ENTER para reintentar.",
            ).capitalize()

            precio = ingreso_entero("Precio de la obra: ")  # Ingreso Precio

            categoria = ingreso_texto(  # Ingreso Categoría
                "Categoría de la obra: ",
                "Ingreso Inválido: La Categoría no puede estar vacío. Presione ENTER para reintentar.",
            ).capitalize()

            duracion = ingreso_entero(
                "Ingrese la Duración de la obra (minutos): "
            )  # Ingreso Duración

            nueva_obra = {
                "ID": nuevo_id,
                "Nombre": nombre,
                "Precio": precio,
                "Categoría": categoria,
                "Duración": duracion,
            }
            obras.append(nueva_obra)

            with open(archivo, "w", encoding="UTF-8") as datos:
                json.dump(obras, datos, ensure_ascii=False)
            print(
                f"Obra agregada: | ID: {nuevo_id} | Nombre: {nombre} | Precio: ${precio} | Categoría: {categoria} | Duración: {duracion} min |"
            )
            input("Presione ENTER para continuar.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")


def modificar_obra(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            obras = json.load(datos)

        if len(obras) == 0:
            print("No hay obras para modificar.")
            input("Presione ENTER para continuar.")
            return
        print("\nObras actuales:")
        for o in obras:
            print(f'{o["ID"]} - {o["Nombre"]} - ${o["Precio"]}')
        id_mod = input("Ingrese el ID de la obra a modificar: ").strip()
        while not id_mod.isnumeric():
            id_mod = input("ID inválido. Ingrese un número: ").strip()
        id_mod = int(id_mod)
        obra = None
        for o in obras:
            if o["ID"] == id_mod:
                obra = o
                break
        if obra is None:
            print("No se encontró una obra con ese ID.")
            input("Presione ENTER para continuar.")
            return
        nuevo_nombre = input(
            f"Nuevo nombre (ENTER para dejar '{obra['Nombre']}'): "
        ).strip()
        if nuevo_nombre != "":
            obra["Nombre"] = nuevo_nombre
        while True:
            entrada = input(
                f"Desea modificar el precio? (ENTER para dejar ${obra['Precio']}): "
            ).strip()
            if entrada == "":
                print("Se mantiene el precio actual.")
                break
            try:
                nuevo_precio = int(entrada)
                if nuevo_precio > 0:
                    obra["Precio"] = nuevo_precio
                    break
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Precio inválido. Ingrese un número entero mayor a 0.")

        with open(archivo, "w", encoding="UTF-8") as datos:
            json.dump(obras, datos, ensure_ascii=False, indent=4)
        print(f"Obra modificada: {obra}")
        input("Presione ENTER para continuar.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")


def borrar_obra(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            obras = json.load(datos)

        if len(obras) == 0:
            print("No hay obras para borrar.")
            input("Presione ENTER para continuar.")
            return

        print("\nObras actuales:")
        for o in obras:
            print(f'{o["ID"]} - {o["Nombre"]} - ${o["Precio"]}')

        id_borrar = input("Ingrese el ID de la obra a borrar: ").strip()
        while not id_borrar.isnumeric():
            id_borrar = input("ID inválido. Ingrese un número: ").strip()
        id_borrar = int(id_borrar)

        for i, o in enumerate(obras):
            if o["ID"] == id_borrar:
                confirmacion = (
                    input(f'¿Seguro que quiere borrar "{o["Nombre"]}"? (s/n): ')
                    .strip()
                    .lower()
                )
                if confirmacion == "s":
                    obras.pop(i)
                    print("Obra eliminada.")
                else:
                    print("No se eliminó ninguna obra.")
                input("Presione ENTER para continuar.")
                with open(archivo, "w", encoding="UTF-8") as datos:
                    json.dump(obras, datos, ensure_ascii=False, indent=4)
                return

        print("No se encontró una obra con ese ID.")
        input("Presione ENTER para continuar.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
