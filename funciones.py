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
    

def mostrar_funciones():
    encabezados = ["ID FUNCION", "ID OBRA", "FECHA"]
    print("\n======================USUARIOS============================")
    for titulo in encabezados:
        print(titulo, end="\t\t\t")
    print()
    for fila in funciones:
        for dato in fila:
            print(dato, end="\t\t\t")
        print()

def updetearFuncion():
    id_modificar = int(input("Ingrese el ID de la funcion a modificar: "))
    encontrada = 0  
    for id_funcion in funciones:
        if id_funcion[0] == id_modificar: 
            print(f"Función encontrada: Obra {id_funcion[1]}, Fecha {id_funcion[2]}")
            nuevaFecha = input("Ingrese la fecha nueva:")
            nuevaObra = input("Nuevo obra: ")
            if nuevaFecha != "":
                id_funcion[2] = nuevaFecha
            if nuevaObra != "":
                id_funcion[1] = int(nuevaObra)
            print("Función modificada con exito.")
            encontrada = 1
    
    if encontrada == 0:
        print("Función no encontrada")
    mostrar_funciones()

def borrarFuncion():
    id_borrar = int(input("Ingrese el ID de la obra a borrar: "))
    encontrado = False 
    for id_funcion in funciones:
        if id_funcion[0] == id_borrar:
            funciones.remove(id_funcion)
            print(f"Funcion {id_funcion[1]} fue eliminada.")
            encontrado = True
    if not encontrado:
        print("Funcion no encontrada.")

mostrar_funciones()
updetearFuncion()
