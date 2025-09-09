obras = [
    [1, "La Traviata", 5000],
    [2, "Hamlet", 6500],
    [3, "El Lago de los Cisnes", 7000],
    [4, "Don Quijote", 5500],
]


def agregar_obras():
    cant_obras = int(input("Obras que desesa agregar:"))
    for i in range(cant_obras):
        id_obra = len(obras) + 1
        nombre = input("Nombre de la obra que desea agregar:")
        precio = int(input("Precio de la obra:"))
        while precio < 0:
            print("Error el precio debe ser mayor que 0")
            precio = int(input("Precio de la obra:"))
        obra = [
            id_obra,
            nombre,
            precio,
        ]
        obras.append(obra)
        print(f"La obra {nombre} fue agregada con exito")


def modificar_obra():
    id_modificar = int(input("Ingrese el ID de la Obra a modificar: "))
    encontrada = 0
    for id_obra in obras:
        if id_obra[0] == id_modificar:
            print(f"Función encontrada: Obra {id_obra[1]}, Fecha {id_obra[2]}")
            nuevoNombre = input("Ingrese el Nombre a actualizar:")
            nuevoPrecio = input("Nuevo obra: ")
            if nuevoNombre != "":
                id_obra[1] = nuevoNombre
            if nuevoPrecio != "":
                id_obra[2] = int(nuevoPrecio)
            print("Obra modificada con exito.")
            encontrada = 1
    mostrarObras()


def mostrar_obras():
    encabezados = [
        "ID",
        "Nombre",
        "Precio",
    ]
    print("\n======================OBRAS============================================")
    for titulo in encabezados:
        print(titulo, end="\t\t\t\t")
    print()
    for id_obra in obras:
        for dato in id_obra:
            print(dato, end="\t\t\t\t")
        print()
