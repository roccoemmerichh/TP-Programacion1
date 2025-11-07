import Main
import re
import os  
from functools import reduce
from datetime import datetime

ARCHIVO_FUNCIONES = "archivos/funciones.txt"

def obtener_todas_las_funciones():
    #Lee todas las funciones del archivo y las devuelve en una lista.
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

def obtener_ultimo_id_funcion(archivo):
    #Lee el archivo para encontrar el último ID de función.
    ultimo_id = 0
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if linea:
                    try:
                        datos = linea.split(";")
                        ultimo_id = int(datos[0])
                    except (ValueError, IndexError):
                        pass 
    except FileNotFoundError:
        pass  
    return ultimo_id

def crear_funcion():
    #Agrega una nueva función al final del archivo modo "a".
    ultimo_id = obtener_ultimo_id_funcion(ARCHIVO_FUNCIONES)
    nuevo_id = ultimo_id + 1
    
    print(f"El ID de la nueva función será: {nuevo_id}")
    id_obra = Main.ingreso_entero("Ingrese el ID de la obra: ")

    fecha_valida = False
    fecha = ""
    while fecha_valida == False:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
            fecha_valida = True
        else:
            print("Formato inválido. Use YYYY-MM-DD (ejemplo: 2025-09-18).")

    try:
        with open(ARCHIVO_FUNCIONES, "a", encoding="UTF-8") as arch:
            nueva_funcion = f'{nuevo_id};{id_obra};{fecha}\n'
            arch.write(nueva_funcion)
            print("Función creada con éxito.")
            print(f'{nuevo_id}: Obra {id_obra} - Fecha {fecha}')
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)

    input("Presione ENTER para continuar.")

def modificar_funcion():
    #Modifica una función usando el método de archivo temporal
    id_modificar = str(Main.ingreso_entero("Ingrese el ID de la funcion a modificar: "))
    temp_archivo = "archivos/funciones.tmp"
    encontrado = False

    try:
        with open(ARCHIVO_FUNCIONES, "rt", encoding="UTF-8") as arch, \
             open(temp_archivo, "wt", encoding="UTF-8") as aux:

            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue 
                try:
                    datos = linea.split(";")
                    codigo = datos[0]
                except (ValueError, IndexError):
                    aux.write(linea + '\n') 
                    continue

                if codigo == id_modificar:
                    encontrado = True
                    id_obra_actual = datos[1]
                    fecha_actual = datos[2]

                    print(f"Función encontrada: Obra {id_obra_actual}, Fecha {fecha_actual}")
                    
                    nueva_fecha = input("Ingrese la fecha nueva (enter para dejar igual): ").strip()
                    if nueva_fecha == "":
                        nueva_fecha = fecha_actual
                    
                    nuevo_id_obra = input("Ingrese nuevo ID de obra (enter para dejar igual): ").strip()
                    if nuevo_id_obra == "":
                        nuevo_id_obra = id_obra_actual
                    else:
                        try:
                            int(nuevo_id_obra) 
                        except ValueError:
                            print("ID de obra inválido, se mantendrá el original.")
                            nuevo_id_obra = id_obra_actual

                    nueva_linea = f"{codigo};{nuevo_id_obra};{nueva_fecha}\n"
                    aux.write(nueva_linea)
                    print(f"Función {codigo} modificada.")
                else:
                    aux.write(linea + '\n')
                    
    except FileNotFoundError:
        print(f"El archivo {ARCHIVO_FUNCIONES} no existe.")
        return
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.remove(ARCHIVO_FUNCIONES)
            os.rename(temp_archivo, ARCHIVO_FUNCIONES)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp_archivo) 
        print(f"No se encontró la función con ID {id_modificar}.")

    input("Presione ENTER para continuar.")


def borrar_funcion():
    #Borra una función usando el método de archivo temporal
    id_borrar = str(Main.ingreso_entero("Ingrese el ID de la funcion a borrar: "))
    temp_archivo = "archivos/funciones.tmp"
    encontrado = False

    try:
        with open(ARCHIVO_FUNCIONES, "rt", encoding="UTF-8") as arch, \
             open(temp_archivo, "wt", encoding="UTF-8") as aux:

            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue 
                
                try:
                    datos = linea.split(";")
                    codigo = datos[0]
                except (ValueError, IndexError):
                    aux.write(linea + '\n') 
                    continue

                if codigo == id_borrar:
                    encontrado = True
                    confirmacion = input(f"¿Seguro que quiere borrar la función {codigo} (Obra: {datos[1]})? (s/n): ").strip().lower()
                    if confirmacion == 's':
                        print(f"La funcion {codigo} fue eliminada.")
                    else:
                        aux.write(linea + '\n') 
                        print("Operación cancelada.")
                else:
                    aux.write(linea + '\n')

    except FileNotFoundError:
        print(f"El archivo {ARCHIVO_FUNCIONES} no existe.")
        return
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.remove(ARCHIVO_FUNCIONES)
            os.rename(temp_archivo, ARCHIVO_FUNCIONES)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp_archivo)
        print(f"Funcion no encontrada con ID {id_borrar}.")
    
    input("Presione ENTER para continuar.")

def encontrar_funciones_por_obra(id_obra_buscada, funciones):
    #Usamos filter para encontrar todas las funciones de una obra específica

    funciones_filtradas = list(filter(lambda f: f[1] == id_obra_buscada, funciones))
    
    print(f"\n--- Funciones encontradas para la Obra ID {id_obra_buscada} (usando FILTER) ---")
    if not funciones_filtradas:
        print("No se encontraron funciones para esa obra.")
    else:
        Main.mostrar_matriz(funciones_filtradas, ("ID Función", "ID Obra", "Fecha"))
    
    return funciones_filtradas

def obtener_fechas_como_objetos(lista_funciones):
    #Usa map para convertir todas las fechas en objetos datetime
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
    #Usamos reduce para encontrar la función con la fecha más lejana
    if not funciones:
        print("\nNo hay funciones para comparar.")
        return

    try:
        ultima = reduce(lambda f1, f2: f1 if f1[2] > f2[2] else f2, funciones)
        print(f"\n--- Última función programada (usando REDUCE) ---")
        print(f"ID Función: {ultima[0]}, Obra: {ultima[1]}, Fecha: {ultima[2]}")
    except Exception as e:
        print(f"Error al reducir funciones: {e}")


def reportes_con_lambdas():
    #función principal que se llama desde el menú.
    funciones = obtener_todas_las_funciones()

    if not funciones:
        print("No hay funciones cargadas para generar reportes.")
        input("Presione ENTER para continuar.")
        return

    print("=============================================")
    print(" EJECUTANDO REPORTES CON FUNCIONES LAMBDA ")
    print("=============================================")
    
    id_obra = Main.ingreso_entero("Ingrese ID de obra para FILTRAR (ej: 1): ")
    funciones_filtradas = encontrar_funciones_por_obra(id_obra, funciones)
  
    obtener_fechas_como_objetos(funciones_filtradas)

    encontrar_ultima_funcion(funciones)
    
    input("\nPresione ENTER para continuar.")
