import Main

obras = [
    {"ID": 1, "Nombre": "La Traviata", "Precio": 5000},
    {"ID": 2, "Nombre": "Hamlet", "Precio": 6500},
    {"ID": 3, "Nombre": "El Lago de los Cisnes", "Precio": 7000},
    {"ID": 4, "Nombre": "Don Quijote", "Precio": 5500},
]

def agregar_obras():
    id_obra = 1
    bandera = 1
    while bandera == 1:
        bandera = 0
        for obra in obras:
            if obra["ID"] == id_obra:
                id_obra += 1
                bandera = 1

    nombre = input("Nombre de la obra que desea agregar: ")
    while nombre == "":
        nombre = input("No puede quedar vacío, ingrese un nombre: ")

    precio = Main.ingreso_entero("Precio de la obra: ")
    while precio == "" or precio <= 0:
        print("Error el precio debe ser mayor que 0")
        precio = Main.ingreso_entero("Precio de la obra: ")

    obras.append({"ID": id_obra, "Nombre": nombre, "Precio": precio})

def modificar_obra():
    id_modificar = Main.ingreso_entero("Ingrese el ID de la Obra a modificar: ")
    encontrada = 0
    for i in obras:
        if i["ID"] == id_modificar:
            print(f'ID: {i["ID"]}, Nombre: "{i["Nombre"]}", Precio: ${i["Precio"]}')
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            if nuevo_nombre == "":
                nuevo_nombre = i["Nombre"]
            nuevo_precio = Main.ingreso_entero("Ingrese el nuevo precio: ")
            if nuevo_precio == "":
                nuevo_precio = i["Precio"]
            i["Nombre"] = nuevo_nombre
            i["Precio"] = nuevo_precio
            encontrada = 1
    if encontrada == 0:
        input("No se encontró el ID ingresado. Presione ENTER para continuar.")

def borrar_obra():
    id_borrar = Main.ingreso_entero("Ingrese el ID de la Obra a borrar: ")
    encontrada = 0
    i = 0
    while i < len(obras):
        if obras[i]["ID"] == id_borrar:
            print(f'¿Está seguro que quiere eliminar la obra: {obras[i]["Nombre"]}?')
            opcion = Main.ingreso_entero("[1] Sí\n[0] No\n")
            if opcion == 1:
                print("\nLa obra:\n")
                print(f'ID: {obras[i]["ID"]}, Nombre: "{obras[i]["Nombre"]}", Precio: ${obras[i]["Precio"]}')
                print("\nHa sido eliminada\n")
                input("Presione ENTER para continuar.")
                obras.pop(i)
            else:
                print("\nNo se ha eliminado ninguna obra")
                input("Presione ENTER para continuar.")
            encontrada = 1
        i += 1
    if encontrada == 0:
        input("No se encontró el ID ingresado. Presione ENTER para continuar.")
