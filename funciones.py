funciones = [
#<<<<<<< HEAD
    [1, 101, "2025-08-15"],
    [2, 102, "2025-08-20"],
    [3, 103, "2025-09-01"],
    [4, 104, "2025-09-10"],
    [5, 105, "2025-09-18"],

]

def crear_funcion():
    id_obra=int(input("ingrese el ID de la obra"))
    id_funcion= funciones[-1][0] + 1
    fecha= str(input("Ingrese la fecha"))
    funciones.append([id_funcion, id_obra, fecha])
 

def mostrar_funciones():
    encabezados_funciones = ["ID Función", "ID Obra", "Fecha"]

    for titulo in encabezados_funciones:
        print(titulo, end="\t")
    print() 

    for fila in funciones:
        for dato in fila:
            print(dato, end="\t")
        print()  


mostrar_funciones()
"""=======
    [1, 1, "2025-09-10", 120],
    [2, 1, "2025-09-12", 120],
    [3, 2, "2025-09-15", 200],
    [4, 3, "2025-09-18", 150],
    [5, 5, "2025-09-20", 100],
]
>>>>>>> 9a085fe6040a95aaaf59d3aa541e71424e67c902"""
