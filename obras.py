import Main

# obras = [
#     [ID, Nombre, Precio]
# ]

# obras = [
#     [1, "La Traviata", 5000],
#     [2, "Hamlet", 6500],
#     [3, "El Lago de los Cisnes", 7000],
#     [4, "Don Quijote", 5500],
# ]


obras = [
    {"ID": 1, "Nombre": "La Traviata", "Precio": 5000},
    {"ID": 2, "Nombre": "Hamlet", "Precio": 6500},
    {"ID": 3, "Nombre": "El Lago de los Cisnes", "Precio": 7000},
    {"ID": 4, "Nombre": "Don Quijote", "Precio": 5500},
]


def agregar_obras():
    for i in range(Main.ingreso_entero("Obras que desea agregar: ")):
        id_obra = len(obras) + 1
        nombre = input("Nombre de la obra que desea agregar: ")
        precio = Main.ingreso_entero("Precio de la obra: ")
        while precio < 0:
            print("Error el precio debe ser mayor que 0")
            precio = Main.ingreso_entero("Precio de la obra: ")
        obras.append([id_obra, nombre, precio])
        print(f"La obra {nombre} fue agregada con exito")


def modificar_obra():
    id_modificar = Main.ingreso_entero("Ingrese el ID de la Obra a modificar: ")
    encontrada = 0
    for id_obra in obras:
        if id_obra[0] == id_modificar:
            print(f"Función encontrada: Obra {id_obra[1]}, Fecha {id_obra[2]}")
            nuevoNombre = input("Ingrese el Nombre a modificar: ")
            nuevoPrecio = input("Nuevo obra: ")
            if nuevoNombre != "":
                id_obra[1] = nuevoNombre
            if nuevoPrecio != "":
                id_obra[2] = int(nuevoPrecio)
            print("Obra modificada con exito.")
            encontrada = 1
    Main.mostrar_matriz(obras, ("ID", "Nombre", "Precio"))
