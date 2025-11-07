import re
import os  # Importamos OS
from funciones import obtener_todas_las_funciones
from reservas import obtener_todas_las_reservas 
import Main

ARCHIVO_USUARIOS = "archivos/usuarios.txt"
patron_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
patron_telefono = re.compile(r'^\d{8,12}$')  

def obtener_todos_los_usuarios():
    #Lee todos los usuarios del archivo y los devuelve en una lista
    usuarios = []
    try:
        with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip() 
                if linea: 
                    try:
                        partes = linea.split(';')
                        usuario = [
                            int(partes[0]),   
                            partes[1],        
                            partes[2],        
                            partes[3],        
                            int(partes[4])    
                        ]
                        usuarios.append(usuario)
                    except (ValueError, IndexError):
                        print(f"Advertencia: Se omitió una línea mal formada en {ARCHIVO_USUARIOS}")
    except FileNotFoundError:
        print(f"Nota: No se encontró {ARCHIVO_USUARIOS}, se creará uno nuevo al guardar.")

    return usuarios

def obtener_ultimo_id_usuario(archivo):
    """
    Lee el archivo para encontrar el último ID de usuario.
    """
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

def crear_usuario():
    """
    Agrega un nuevo usuario al final del archivo (modo 'a').
    No carga todo el archivo en memoria.
    """
    ultimo_id = obtener_ultimo_id_usuario(ARCHIVO_USUARIOS)
    id_usuario = ultimo_id + 1 
        
    print(f"El ID del nuevo usuario será: {id_usuario}")
    nombre = input("Nombre del usuario: ")

    email = input("Email del usuario: ")
    while not patron_email.match(email):
        print("Email inválido. Ejemplo válido: usuario@dominio.com")
        email = input("Email del usuario: ")

    telefono = input("Teléfono del usuario (8 a 12 dígitos): ")
    while not patron_telefono.match(telefono):
        print("Teléfono inválido. Solo números (8-12 dígitos).")
        telefono = input("Teléfono del usuario: ")

    edad = Main.ingreso_entero("Edad del usuario: ")

    try:
        with open(ARCHIVO_USUARIOS, "a", encoding="UTF-8") as arch:
            nuevo_usuario = f'{id_usuario};{nombre};{email};{telefono};{edad}\n'
            arch.write(nuevo_usuario)
            print(f"Usuario {nombre} creado con éxito (ID: {id_usuario})")
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)

    input("Presione ENTER para continuar.")

def modificar_usuario():
    #Modifica un usuario usando el método de archivo temporal 
    id_modificar = str(Main.ingreso_entero("Ingrese el ID del usuario a modificar: "))
    temp_archivo = "archivos/usuarios.tmp"
    encontrado = False

    try:
        with open(ARCHIVO_USUARIOS, "rt", encoding="UTF-8") as arch, \
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
                    nombre_actual = datos[1]
                    email_actual = datos[2]
                    telefono_actual = datos[3]
                    edad_actual = datos[4] 
                    
                    print(f"Usuario encontrado: {nombre_actual}")
                    
                    nuevo_nombre = input("Nuevo nombre (enter para dejar igual): ").strip()
                    if nuevo_nombre == "":
                        nuevo_nombre = nombre_actual

                    nuevo_email = input("Nuevo email (enter para dejar igual): ").strip()
                    if nuevo_email == "":
                        nuevo_email = email_actual
                    else:
                        while not patron_email.match(nuevo_email):
                            print("Email inválido. Ejemplo válido: usuario@dominio.com")
                            nuevo_email = input("Nuevo email (enter para dejar igual): ")
                            if nuevo_email == "":
                                nuevo_email = email_actual
                                break

                    nuevo_telefono = input("Nuevo teléfono (enter para dejar igual): ").strip()
                    if nuevo_telefono == "":
                        nuevo_telefono = telefono_actual
                    else:
                        while not patron_telefono.match(nuevo_telefono):
                            print("Teléfono inválido. Solo números (8-12 dígitos).")
                            nuevo_telefono = input("Nuevo teléfono (enter para dejar igual): ")
                            if nuevo_telefono == "":
                                nuevo_telefono = telefono_actual
                                break
                    
                    nueva_linea = f"{codigo};{nuevo_nombre};{nuevo_email};{nuevo_telefono};{edad_actual}\n"
                    aux.write(nueva_linea)
                    print("Usuario modificado con éxito.")
                else:
                    aux.write(linea + '\n')
                    
    except FileNotFoundError:
        print(f"El archivo {ARCHIVO_USUARIOS} no existe.")
        return
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.remove(ARCHIVO_USUARIOS)
            os.rename(temp_archivo, ARCHIVO_USUARIOS)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp_archivo)
        print(f"No se encontró el usuario con ID {id_modificar}.")

    input("Presione ENTER para continuar.")

def borrar_usuario():
    #Borra un usuario usando el método de archivo temporal  
    id_borrar = str(Main.ingreso_entero("Ingrese el ID del usuario a borrar: "))
    temp_archivo = "archivos/usuarios.tmp"
    encontrado = False

    try:
        with open(ARCHIVO_USUARIOS, "rt", encoding="UTF-8") as arch, \
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
                    confirmacion = input(f"¿Seguro que quiere borrar a '{datos[1]}'? (s/n): ").strip().lower()
                    if confirmacion == 's':
                        print(f"Usuario {datos[1]} fue eliminado.")
                    else:
                        aux.write(linea + '\n') 
                        print("Operación cancelada.")
                else:
                    aux.write(linea + '\n') 

    except FileNotFoundError:
        print(f"El archivo {ARCHIVO_USUARIOS} no existe.")
        return
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.remove(ARCHIVO_USUARIOS)
            os.rename(temp_archivo, ARCHIVO_USUARIOS)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp_archivo)
        print(f"Usuario no encontrado con ID {id_borrar}.")
        
    input("Presione ENTER para continuar.")

def usuarios_con_mas_reservas():
    usuarios = obtener_todos_los_usuarios()
    lista_de_reservas = obtener_todas_las_reservas() 

    conteo_reservas = {}

    for reserva in lista_de_reservas:
        id_usuario = reserva[0]
        conteo_reservas[id_usuario] = conteo_reservas.get(id_usuario, 0) + 1

    if not conteo_reservas:
        print("No hay reservas registradas.")
        input("Presione ENTER para continuar.")
        return

    max_reservas = max(conteo_reservas.values())
    usuarios_max = set()

    print(f"\nUsuarios con más reservas ({max_reservas} reserva/s):")
    for usuario in usuarios:
        if conteo_reservas.get(usuario[0], 0) == max_reservas:
            usuarios_max.add(usuario[1])

    if not usuarios_max:
        print("No se encontraron usuarios coincidentes.")
    else:
        for nombre in usuarios_max:
            print(f"- {nombre}")
            
    input("Presione ENTER para continuar.")

promedio = lambda lista: sum(lista) / len(lista)

def promedio_edad_por_funcion():
    usuarios = obtener_todos_los_usuarios()
    lista_de_funciones = obtener_todas_las_funciones()
    lista_de_reservas = obtener_todas_las_reservas()

    if not usuarios:
        print("No hay usuarios registrados para calcular promedios.")
        input("Presione ENTER para continuar.")
        return
        
    print("\n--- Promedio de Edad por Función ---")
    for funcion in lista_de_funciones:
        id_funcion_actual = funcion[0]     
        
        edades = []
        reservas_encontradas = 0
        
        for reserva in lista_de_reservas:
            id_obra_reserva = reserva[2] 
            id_obra_funcion = funcion[1]
            
            if id_obra_reserva == id_obra_funcion:    
                id_usuario_reserva = reserva[0]
                reservas_encontradas += 1
                
                for usuario in usuarios:
                    if usuario[0] == id_usuario_reserva:
                        edades.append(usuario[4]) 
                        break 
        
        nombre_funcion = f"Función {funcion[0]} (Obra ID: {funcion[1]}) - {funcion[2]}"

        try:
            prom = promedio(edades)
            print(f"{nombre_funcion}: promedio de edad = {prom:.2f} años (sobre {reservas_encontradas} reservas)")
            
            primeras_edades = edades[:3] 
            print(f"   -> Primeras 3 edades en reservar: {primeras_edades}")

        except ZeroDivisionError:
            print(f"{nombre_funcion}: no hay reservas registradas para esta función.")
            
    input("Presione ENTER para continuar.")
