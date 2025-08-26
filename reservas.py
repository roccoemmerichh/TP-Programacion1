reservas = [
    [1, 1, 1, 2, ["A1", "A2"], 12000, 24000],
    [2, 2, 2, 4, ["B1", "B2", "B3", "B4"], 12000, 48000],
    [3, 3, 3, 3, ["C1", "C2", "C3"], 20000, 60000],
    [4, 4, 4, 1, ["D1"], 15000, 15000],
    [5, 5, 5, 2, ["E1", "E2"], 15000, 30000],
]

butacas = [
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"],
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"],
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"],
    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"],
]


def mostrar_butacas(butacas):
    filas = len(butacas)
    columnas = len(butacas[0])
    print("========================BUTACAS============================")
    for fila in range(filas):
        for columna in range(columnas):
            print(butacas[fila][columna], end="\t")
        print()


def crear_reserva():
    usuario = int(input("Coloque el id de usuario:"))
    nr = len(reservas) + 1
    id_obra = int(input("Id de la obra:"))
    cant = int(input("Cuantas entradas deseas reservar"))
    mostrar_butacas(butacas)
    butacas_elgidas = []
    for i in range(cant):
        butaca = input("Butaca que desea:")
        butacas_elgidas.append(butaca)
    precio = int(input("Precio por entrada"))
    total = precio * cant
    print(f"El total a abonar es de {total}")

    reserva = [usuario, nr, id_obra, cant, butacas_elgidas, precio, total]
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
            str(reserva[0]),
            str(reserva[1]),
            str(reserva[2]),
            str(reserva[3]),
            ", ".join(reserva[4]),
            str(reserva[5]),
            str(reserva[6]),
        ]
        for dato in fila:
            print(dato, end="\t")
        print()


if __name__ == "__main__":  # Para no ejecutar funciones al importar modulos
    mostrar_reservas(reservas)
