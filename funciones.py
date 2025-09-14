import Main
import re

funciones = [
    [1, 1, "2025-08-15"],
    [2, 2, "2025-08-20"],
    [3, 3, "2025-09-01"],
    [4, 4, "2025-09-10"],
    [5, 5, "2025-09-18"],
]

def crear_funcion():
    Main.mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

    id_obra = int(input("Ingrese el ID de la obra: "))
    id_funcion = funciones[-1][0] + 1 if len(funciones) > 0 else 1

    fecha_valida = False
    fecha = ""
    while fecha_valida == False:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
            fecha_valida = True
        else:
            print("❌ Formato inválido. Use YYYY-MM-DD (ejemplo: 2025-09-18).")

    funciones.append([id_funcion, id_obra, fecha])
    print("✅ Función creada con éxito.")

    Main.mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

def modificar_funcion():
    id_modificar = int(input("Ingrese el ID de la funcion a modificar: "))
    encontrada = 0
    for id_funcion in funciones:
        if id_funcion[0] == id_modificar:
            print(f"Función encontrada: Obra {id_funcion[1]}, Fecha {id_funcion[2]}")
            nuevaFecha = input("Ingrese la fecha nueva: ")
            nuevaObra = input("Ingrese nuevo ID: ")
            if nuevaFecha != "":
                id_funcion[2] = nuevaFecha
            if nuevaObra != "":
                id_funcion[1] = int(nuevaObra)
            print("Función modificada con exito.")
            encontrada = 1

    if encontrada == 0:
        print("Función no encontrada")
    Main.mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

def borrar_funcion():
    id_borrar = int(input("Ingrese el ID de la funcion a borrar: "))
    encontrado = False
    for id_funcion in funciones:
        if id_funcion[0] == id_borrar:
            funciones.remove(id_funcion)
            print(f"Usuario {id_funcion[1]} fue eliminado.")
            encontrado = True
    if not encontrado:
        print("Usuario no encontrado.")
