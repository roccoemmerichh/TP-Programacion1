import Main
import re
from functools import reduce
from datetime import datetime

ARCHIVO_FUNCIONES = "archivos/funciones.txt"

def leer_funciones():

    funciones = []
    try:
        with open(ARCHIVO_FUNCIONES, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip() 
                if linea: 
                    try:
                        partes = linea.split(';')

                        funcion = [
                            int(partes[0]), 
                            int(partes[1]), 
                            partes[2]       
                        ]
                        funciones.append(funcion)
                    except (ValueError, IndexError):
                        print(f"Advertencia: Se omitió una línea mal formada en {ARCHIVO_FUNCIONES}")
    except FileNotFoundError:
        print(f"Nota: No se encontró {ARCHIVO_FUNCIONES}, se creará uno nuevo al guardar.")
    
    return funciones

def guardar_funciones(funciones):
    """
    Recibe la lista de listas y la guarda en funciones.txt.
    """
    try:
        with open(ARCHIVO_FUNCIONES, 'w', encoding='utf-8') as f:
            for funcion in funciones:
                linea_items = [str(item) for item in funcion]
                linea = ";".join(linea_items)
                f.write(linea + "\n")
    except OSError as e:
        print(f"Error fatal al guardar funciones: {e}")


def crear_funcion():
    funciones = leer_funciones()
    
    Main.mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

    id_obra = Main.ingreso_entero("Ingrese el ID de la obra: ")
    
    if funciones:
        id_funcion = funciones[-1][0] + 1 if len(funciones) > 0 else 1
    else:
        id_funcion = 1

    fecha_valida = False
    fecha = ""
    while fecha_valida == False:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
            fecha_valida = True
        else:
            print("Formato inválido. Use YYYY-MM-DD (ejemplo: 2025-09-18).")

    funciones.append([id_funcion, id_obra, fecha])
    
    guardar_funciones(funciones)
    print("Función creada con éxito.")

    Main.mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

def modificar_funcion():
    funciones = leer_funciones()
    
    id_modificar = Main.ingreso_entero("Ingrese el ID de la funcion a modificar: ")
    encontrada = 0
    for id_funcion in funciones:
        if id_funcion[0] == id_modificar:
            print(f"Función encontrada: Obra {id_funcion[1]}, Fecha {id_funcion[2]}")
            nuevaFecha = input("Ingrese la fecha nueva (enter para dejar igual): ")
            nuevaObra = input("Ingrese nuevo ID de obra (enter para dejar igual): ")
            
            if nuevaFecha != "":
                id_funcion[2] = nuevaFecha
            if nuevaObra != "":
                try:
                    id_funcion[1] = int(nuevaObra)
                except ValueError:
                    print("ID de obra inválido, no se modificó.")
            
            guardar_funciones(funciones)
            print("Función modificada con exito.")
            encontrada = 1
            break 

    if encontrada == 0:
        print("Función no encontrada")
    
    Main.mostrar_matriz(funciones, ("ID Función", "ID Obra", "Fecha"))

def borrar_funcion():
    funciones = leer_funciones()
    
    id_borrar = Main.ingreso_entero("Ingrese el ID de la funcion a borrar: ")
    encontrado = False
    for i, id_funcion in enumerate(funciones):
        if id_funcion[0] == id_borrar:
            confirmacion = input(f"¿Seguro que quiere borrar la función {id_funcion[0]} (Obra: {id_funcion[1]})? (s/n): ").strip().lower()
            if confirmacion == 's':
                funciones.pop(i)
                guardar_funciones(funciones)
                print(f"La funcion {id_funcion[0]} fue eliminada.")
            else:
                print("Operación cancelada.")
            encontrado = True
            break
            
    if not encontrado:
        print("Funcion no encontrada.")


def encontrar_funciones_por_obra(id_obra_buscada, funciones):
    """
    Usa FILTER para encontrar todas las funciones de una obra específica.
    (Ahora recibe 'funciones' como parámetro)
    """
    funciones_filtradas = list(filter(lambda f: f[1] == id_obra_buscada, funciones))
    
    print(f"\n--- Funciones encontradas para la Obra ID {id_obra_buscada} (usando FILTER) ---")
    if not funciones_filtradas:
        print("No se encontraron funciones para esa obra.")
    else:
        Main.mostrar_matriz(funciones_filtradas, ("ID Función", "ID Obra", "Fecha"))
    
    return funciones_filtradas

def obtener_fechas_como_objetos(lista_funciones):
    """
    Usa MAP para convertir todas las fechas (string) en objetos datetime.
    (Sin cambios, ya que recibía la lista como parámetro)
    """
    print(f"\n--- Fechas convertidas a objetos datetime (usando MAP) ---")
    if not lista_funciones:
        print("No hay fechas para convertir.")
        return

    try:
        fechas_objetos = list(map(lambda f: datetime.strptime(f[2], '%Y-%m-%d'), lista_funciones))
        for fecha in fechas_objetos:
            print(f"Día: {fecha.day}, Mes: {fecha.month}, Año: {fecha.year}")
    except ValueError as e:
        print(f"Error al convertir fechas: {e}. Asegúrese que el formato sea YYYY-MM-DD.")

def encontrar_ultima_funcion(funciones):
    """
    Usa REDUCE para encontrar la función con la fecha más lejana.
    (Ahora recibe 'funciones' como parámetro)
    """
    if not funciones:
        print("\nNo hay funciones para comparar.")
        return

    ultima = reduce(lambda f1, f2: f1 if f1[2] > f2[2] else f2, funciones)
    
    print(f"\n--- Última función programada (usando REDUCE) ---")
    print(f"ID Función: {ultima[0]}, Obra: {ultima[1]}, Fecha: {ultima[2]}")

def reportes_con_lambdas():
    """
    Esta es la función principal que se llama desde el menú.
    Ahora lee los datos primero.
    """
    funciones = leer_funciones()

    print("=============================================")
    print(" EJECUTANDO REPORTES CON FUNCIONES LAMBDA ")
    print("=============================================")
    
    id_obra = Main.ingreso_entero("Ingrese ID de obra para FILTRAR (ej: 1): ")
    funciones_filtradas = encontrar_funciones_por_obra(id_obra, funciones)
  
    obtener_fechas_como_objetos(funciones_filtradas)

    encontrar_ultima_funcion(funciones)
    
    input("\nPresione ENTER para continuar.")
