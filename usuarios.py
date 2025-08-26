import re
from funciones import *
from reservas import *



usuarios = [
    [1, "Juan Pérez", "juanperez@gmail.com", "12345678"],
    [2, "Ana Gómez", "anagomez@gmail.com", "87654321"],
    [3, "Carlos López", "carloslopez@gmail.com", "11223344"],
    [4, "María Díaz", "mariadiaz@gmail.com", "44332211"],
    [5, "Luis Fernández", "luisfernandez@gmail.com", "99887766"],
]

patron_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
patron_telefono = re.compile(r'^\d{8,12}$')  

def crear_usuario():
    id_usuario = len(usuarios) + 1
    nombre = input("Nombre del usuario: ")

    
    email = input("Email del usuario: ")
    while not patron_email.match(email):
        print("❌ Email inválido. Ejemplo válido: usuario@dominio.com")
        email = input("Email del usuario: ")


    telefono = input("Teléfono del usuario (8 a 12 dígitos): ")
    while not patron_telefono.match(telefono):
        print("❌ Teléfono inválido. Solo números (8-12 dígitos).")
        telefono = input("Teléfono del usuario: ")

    edad = int(input("Edad del usuario: "))

    usuario = [id_usuario, nombre, email, telefono, edad]
    usuarios.append(usuario)
    print(f"✅ Usuario {nombre} creado con éxito (ID: {id_usuario})")



def modificar_usuario():
    id_modificar = int(input("Ingrese el ID del usuario a modificar: "))
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

            print("Usuario modificado con éxito.")
            return
    print("Usuario no encontrado o inactivo.")


def borrar_usuario():
    id_borrar = int(input("Ingrese el ID del usuario a borrar: "))
    encontrado = False

    for usuario in usuarios:
        if usuario[0] == id_borrar:
            usuarios.remove(usuario)
            print(f"Usuario {usuario[1]} fue eliminado.")
            encontrado = True
    if not encontrado:
        print("Usuario no encontrado.")


def usuarios_con_mas_reservas():
    conteo_reservas = [0] * len(usuarios)

    for reserva in reservas:
        id_usuario = reserva[0]
        conteo_reservas[id_usuario - 1] += 1

    if sum(conteo_reservas) == 0:
        print("No hay reservas registradas.")
        return

    max_reservas = max(conteo_reservas)

    print("\nUsuarios con más reservas:")
    for i, usuario in enumerate(usuarios):
        if conteo_reservas[i] == max_reservas:
            print(f"- {usuario[1]} ({max_reservas} reservas)")


promedio = lambda lista: sum(lista) / len(lista) if lista else 0


def promedio_edad_por_funcion():
    for funcion in funciones:
        id_funcion = funcion[1]
        nombre_funcion = f"Función {id_funcion} - {funcion[2]}"

        edades = []
        for reserva in reservas:
            if reserva[1] == id_funcion:
                for usuario in usuarios:
                    if usuario[0] == reserva[0]:
                        edades.append(usuario[4])

        if edades:
            print(f"{nombre_funcion}: promedio de edad = {promedio(edades):.2f} años")
        else:
            print(f"{nombre_funcion}: sin reservas registradas")
