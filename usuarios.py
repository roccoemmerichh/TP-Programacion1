import re
from funciones import leer_funciones
from reservas import leer_reservas
import Main

ARCHIVO_USUARIOS = "archivos/usuarios.txt"
patron_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
patron_telefono = re.compile(r'^\d{8,12}$')  

def leer_usuarios():
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

def guardar_usuarios(usuarios):
    """
    Recibe la lista de listas y la guarda en usuarios.txt.
    """
    try:
        with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as f:
            for usuario in usuarios:
                linea_items = [str(item) for item in usuario]
                linea = ";".join(linea_items)
                f.write(linea + "\n")
    except OSError as e:
        print(f"Error fatal al guardar usuarios: {e}")


def crear_usuario():
    usuarios = leer_usuarios() 
    
    if usuarios:
        id_usuario = usuarios[-1][0] + 1 
    else:
        id_usuario = 1 
        
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

    usuario = [id_usuario, nombre, email, telefono, edad]
    usuarios.append(usuario)
    
    guardar_usuarios(usuarios) 
    
    print(f"Usuario {nombre} creado con éxito (ID: {id_usuario})")
    input("Presione ENTER para continuar.")

def modificar_usuario():
    usuarios = leer_usuarios()
    
    id_modificar = Main.ingreso_entero("Ingrese el ID del usuario a modificar: ")
    encontrado = False
    
    for usuario in usuarios:
        if usuario[0] == id_modificar:
            print(f"Usuario encontrado: {usuario[1]}")
            nuevo_nombre = input("Nuevo nombre (enter para dejar igual): ")
            nuevo_email = input("Nuevo email (enter para dejar igual): ")
            nuevo_telefono = input("Nuevo teléfono (enter para dejar igual): ")

            if nuevo_nombre != "":
                usuario[1] = nuevo_nombre
            if nuevo_email != "":
                usuario[2] = nuevo_email
            if nuevo_telefono != "":
                usuario[3] = nuevo_telefono
            
            guardar_usuarios(usuarios)
            print("Usuario modificado con éxito.")
            encontrado = True
            break 
            
    if not encontrado:
        print("Usuario no encontrado.")
        
    input("Presione ENTER para continuar.")

def borrar_usuario():
    usuarios = leer_usuarios()
    
    id_borrar = Main.ingreso_entero("Ingrese el ID del usuario a borrar: ")
    encontrado = False
    
    for i, usuario in enumerate(usuarios):
        if usuario[0] == id_borrar:
            confirmacion = input(f"¿Seguro que quiere borrar a '{usuario[1]}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                usuarios.pop(i) 
                guardar_usuarios(usuarios)
                print(f"Usuario {usuario[1]} fue eliminado.")
            else:
                print("Operación cancelada.")
            encontrado = True
            break
            
    if not encontrado:
        print("Usuario no encontrado.")
        
    input("Presione ENTER para continuar.")

def usuarios_con_mas_reservas():
    usuarios = leer_usuarios()
    conteo_reservas = {}

    lista_de_reservas = leer_reservas() 

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
    usuarios = leer_usuarios()
    lista_de_funciones = leer_funciones()
    
    lista_de_reservas = leer_reservas()

    if not usuarios:
        print("No hay usuarios registrados para calcular promedios.")
        input("Presione ENTER para continuar.")
        return
        
    print("\n--- Promedio de Edad por Función ---")
    for funcion in lista_de_funciones:
        id_funcion = funcion[0]     
        id_obra_funcion = funcion[1] 
        nombre_funcion = f"Función {id_funcion} (Obra ID: {id_obra_funcion}) - {funcion[2]}"

        edades = []
        
        for reserva in lista_de_reservas:
            id_obra_reserva = reserva[2] 
            
            if id_obra_reserva == id_obra_funcion:    
                id_usuario_reserva = reserva[0]
                
                for usuario in usuarios:
                    if usuario[0] == id_usuario_reserva:
                        edades.append(usuario[4]) 
                        break 
        try:
            prom = promedio(edades)
            print(f"{nombre_funcion}: promedio de edad = {prom:.2f} años (sobre {len(edades)} reservas)")
            
            primeras_edades = edades[:3] 
            print(f"   -> Primeras 3 edades en reservar: {primeras_edades}")

        except ZeroDivisionError:
            print(f"{nombre_funcion}: no hay reservas registradas para esta función.")
            
    input("Presione ENTER para continuar.")
