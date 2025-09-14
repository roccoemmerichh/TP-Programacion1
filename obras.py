import Main

# obras = [
#     [ID, Nombre, Precio]
# ]


obras = [
    {"ID": 1, "Nombre": "La Traviata", "Precio": 5000, "Usuarios": set()},
    {"ID": 2, "Nombre": "Hamlet", "Precio": 6500, "Usuarios": set()},
    {"ID": 3, "Nombre": "El Lago de los Cisnes", "Precio": 7000, "Usuarios": set()},
    {"ID": 4, "Nombre": "Don Quijote", "Precio": 5500, "Usuarios": set()},
]



def agregar_obras():
    id_obra = len(obras) + 1
    while True:
        nombre = input("Nombre de la obra que desea agregar: ")
        precio = Main.ingreso_entero("Precio de la obra: ")
        while precio < 0:
            print("Error el precio debe ser mayor que 0")
            precio = Main.ingreso_entero("Precio de la obra: ")
        obras.append({"ID": id_obra, "Nombre": nombre, "Precio": precio})
        break


def modificar_obra():
    id_modificar = Main.ingreso_entero("Ingrese el ID de la Obra a modificar: ")
    for i in obras:
        if i["ID"] == id_modificar:
            print(f'ID: {i["ID"]}, Nombre: "{i["Nombre"]}", Precio: ${i["Precio"]}')
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_precio = Main.ingreso_entero("Ingrese el nuevo precio: ")
            i["Nombre"] = nuevo_nombre
            i["Precio"] = nuevo_precio
            return None
    input("No se a encontrado el ID ingresado presione ENTER para continuar.")


def borrar_obra():
    lista_ids = []
    for d in obras:
        lista_ids.append(d["ID"])
    id_borrar = Main.ingreso_entero("Ingrese el ID de la Obra a borrar: ")
    if id_borrar in lista_ids:
        print(
            f'Esta seguro que quiere eliminar la obra: {obras[id_borrar -1]["Nombre"]}?'
        )
        opcion = Main.ingreso_entero("[1] Si\n[0] No\n")
        if opcion == 1:
            print("\nLa obra:\n")
            print(
                f'ID: {obras[id_borrar -1]["ID"]}, Nombre: "{obras[id_borrar -1]["Nombre"]}", Precio: ${obras[id_borrar -1]["Precio"]}'
            )
            print("\nHa sido eliminada\n")
            input("presione ENTER para continuar.")
            indice = lista_ids.index(id_borrar)
            obras.pop(indice)
            lista_ids.pop(indice)
            return None
        elif opcion == 0:
            print("\nNo se ha eliminado ninguna obra")
            input("presione ENTER para continuar.")
            return None
    print("No se a encontrado el ID ingresado presione ENTER para continuar.")
