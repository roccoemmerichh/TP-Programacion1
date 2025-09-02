funciones = [
    [1, 101, "2025-08-15"],
    [2, 102, "2025-08-20"],
    [3, 103, "2025-09-01"],
    [4, 104, "2025-09-10"],
    [5, 105, "2025-09-18"],
]


def crear_funcion():
    id_obra = int(input("ingrese el ID de la obra: "))
    id_funcion = funciones[-1][0] + 1
    fecha = str(input("Ingrese la fecha: "))
    funciones.append([id_funcion, id_obra, fecha])
