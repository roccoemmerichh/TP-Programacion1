from obras import *
reservas = [
    [1, 1, 1, 2, "A1,A2",       12000, 24000],
    [2, 2, 2, 4, "B1,B2,B3,B4", 12000, 48000],
    [3, 3, 3, 3, "C1,C2,C3",    20000, 60000],
    [4, 4, 4, 1, "D1",          15000, 15000],
    [5, 5, 5, 2, "E1,E2",       15000, 30000],
]


butacas_visuales = [
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"],
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"],
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"],
    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"],
]
butacas_estado = [
#    1    2   3   4   5   6   7   8
    ["0","0","0","0","0","0","0","0"],  # Fila A
    ["0","0","0","0","0","0","0","0"],  # Fila B
    ["0","0","0","0","0","0","0","0"],  # Fila C
    ["0","0","0","0","0","0","0","0"],  # Fila D
    ["0","0","0","0","0","0","0","0"],  # Fila E
    ["0","0","0","0","0","0","0","0"],  # Fila F
    ["0","0","0","0","0","0","0","0"],  # Fila G
    ["0","0","0","0","0","0","0","0"],  # Fila H
]

def mostrar_butacas():
    print("\n======================== BUTACAS ============================")
    for i in range(len(butacas_visuales)):
        for j in range(len(butacas_visuales[i])):
            if butacas_estado[i][j] == "X":
                print("[X]", end="\t")  # ocupada
            else:
                print(butacas_visuales[i][j], end="\t")  # libre
        print()  # salto de línea por fila

def crear_reserva():
    usuario = int(input("Coloque el id de usuario:"))
    nr = len(reservas) + 1
    id_obra = int(input("Id de la obra:"))
    cant = int(input("Cuantas entradas deseas reservar"))
    mostrar_butacas(butacas_visuales)
    butacas_elgidas = []
    for i in range(cant):
        butaca = input("Butaca que desea:")
        butacas_elgidas.append(butaca)
    butacas_cadena = ",".join(butacas_elgidas) 
    precio = None
    encontrado = False 
    i = 0
    while i < len(obras):
        if obras[i][0] == id_obra:
            precio = obras[i][3]
            encontrado = True
        i += 1

    if not encontrado:
        print("No se encontró una obra con ese ID.")
        return
    print(f"El precio de cada entrada es de {precio}")
    total = precio * cant
    print(f"El total a abonar es de {total}")

    reserva = [usuario, nr, id_obra, cant, butacas_cadena, precio, total]
    reservas.append(reserva)

    print(f"Reserva realizada con existo! El numero de reserva es {nr}")


def mostrar_reservas(reservas):
    encabezados = ["Usuario", "NR", "ID Obra", "Cantidad", "Butacas", "Precio", "Total"]
    print("======================RESERVAS============================")
    for encabezado in encabezados:
        print(encabezado, end="\t")
    print()

    for reserva in reservas:
        fila = [
            (reserva[0]),
            (reserva[1]),
            (reserva[2]),
            (reserva[3]),
            str(reserva[4]),           
            (reserva[5]),
            (reserva[6]),
        ]
        for dato in fila:
            print(dato, end="\t")
        print()

if __name__ == "__main__":  # Para no ejecutar funciones al importar modulos
    mostrar_reservas(reservas)


def init_estado_desde_reservas():
    for reserva in reservas:
        campo = reserva[4]  # butacas, ahora como cadena "A1,A2"
        butacas_ocupadas = campo.split(",")  # lo paso a lista ["A1","A2"]

        for butaca in butacas_ocupadas:
            butaca = butaca.strip().upper()  # limpio espacios
            # Buscar la posición en la matriz visual
            for i in range(len(butacas_visuales)):
                for j in range(len(butacas_visuales[i])):
                    if butacas_visuales[i][j] == butaca:
                        butacas_estado[i][j] = "X"  # marcar ocupada
init_estado_desde_reservas()
mostrar_butacas()