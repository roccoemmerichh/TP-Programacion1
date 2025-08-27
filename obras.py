obras = [
    [1, "La Traviata", 150, 5000],
    [2, "Hamlet", 200, 6500],
    [3, "El Lago de los Cisnes", 180, 7000],
    [4, "Don Quijote", 220, 5500],
]


def agregar_obras():
    cant_obras = int(input("Obras que desesa agregar:"))
    for i in range(cant_obras):
        id_obra = len(obras) + 1
        nombre = input("Nombre de la obra que desea agregar:")
        capacidad = int(input("capacidad:"))
        while capacidad < 0:
            print("error la capacidad debe ser mayor que 0")
            capacidad = int(input("capacidad:"))
        precio = int(input("Precio de la obra:"))
        while precio < 0:
            print("Error el precio debe ser mayor que 0")
            precio = int(input("Precio de la obra:"))
        obra = [
            id_obra,
            nombre,
            capacidad,
            precio,
        ]
        obras.append(obra)
        print(f"La obra {nombre} fue agregada con exito")