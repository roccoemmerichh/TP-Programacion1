from obras import *
import re

reservas = [
    [1, 1, 1, 2, "A1,A2",       12000, 24000],
    [2, 2, 2, 4, "B1,B2,B3,B4", 12000, 48000],
    [3, 3, 3, 3, "C1,C2,C3",    20000, 60000],
    [4, 4, 4, 1, "D1",          15000, 15000],
    [5, 5, 5, 2, "E1,E2",       15000, 30000],
]

butacas_visuales = [
    [("A1","A2","A3","A4","A5","A6","A7","A8")],
    [("B1","B2","B3","B4","B5","B6","B7","B8")],
    [("C1","C2","C3","C4","C5","C6","C7","C8")],
    [("D1","D2","D3","D4","D5","D6","D7","D8")],
    [("E1","E2","E3","E4","E5","E6","E7","E8")],
    [("F1","F2","F3","F4","F5","F6","F7","F8")],
    [("G1","G2","G3","G4","G5","G6","G7","G8")],
    [("H1","H2","H3","H4","H5","H6","H7","H8")],
]

butacas_estado = [
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
]

def butaca_valida(b: str) -> bool:
    return re.fullmatch(r"[A-Ha-h][1-8]", b.strip()) is not None

def buscar_pos(butaca: str):
    pos = None
    f = 0
    while f < len(butacas_visuales) and pos is None:
        fila_tupla = butacas_visuales[f][0]
        c = 0
        while c < len(fila_tupla) and pos is None:
            if fila_tupla[c] == butaca:
                pos = (f, c)
            c += 1
        f += 1
    return pos

def mostrar_butacas():
    print("\n======================== BUTACAS ============================")
    print("    " + " ".join([f"{n:>4}" for n in range(1, 9)]))
    f = 0
    while f < len(butacas_visuales):
        fila_letra = chr(ord('A') + f)
        fila_tupla = butacas_visuales[f][0]
        celdas = []
        c = 0
        while c < len(fila_tupla):
            if butacas_estado[f][c] == "X":
                celdas.append(f"{'[X]':>4}")
            else:
                celdas.append(f"{fila_tupla[c]:>4}")
            c += 1
        print(f"{fila_letra} | " + " ".join(celdas))
        f += 1

def mostrar_reservas(reservas_):
    encabezados = ["Usuario", "NR", "ID Obra", "Cantidad", "Butacas", "Precio", "Total"]
    print("\n====================== RESERVAS ============================")
    print("\t".join(encabezados))
    i = 0
    while i < len(reservas_):
        r = reservas_[i]
        fila = [str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6])]
        print("\t".join(fila))
        i += 1

def init_estado_desde_reservas():
    f = 0
    while f < len(butacas_estado):
        c = 0
        while c < len(butacas_estado[f]):
            butacas_estado[f][c] = "0"
            c += 1
        f += 1
    i = 0
    while i < len(reservas):
        butacas_str = reservas[i][4]
        for b in butacas_str.split(","):
            buscada = b.strip().upper()
            pos = buscar_pos(buscada)
            if pos is not None:
                ff, cc = pos
                butacas_estado[ff][cc] = "X"
        i += 1

def crear_reserva():
    try:
        usuario = int(input("Coloque el id de usuario: "))
    except ValueError:
        print("ID de usuario inválido.")
        usuario = -1
    nr = len(reservas) + 1
    try:
        id_obra = int(input("Id de la obra: "))
    except ValueError:
        print("ID de obra inválido.")
        id_obra = -1
    try:
        cant = int(input("Cuántas entradas deseas reservar: "))
    except ValueError:
        print("Cantidad inválida.")
        cant = 0
    mostrar_butacas()
    butacas_elegidas = []
    i = 0
    while i < cant:
        valida = False
        while not valida:
            butaca = input(f"Butaca que desea ({i+1}/{cant}): ").strip().upper()
            if not butaca_valida(butaca):
                print("Formato inválido. Usá A-H y 1-8 (ej: C5).")
            elif butaca in butacas_elegidas:
                print("Ya elegiste esa butaca en esta reserva. Probá otra.")
            else:
                pos = buscar_pos(butaca)
                if pos is None:
                    print("Esa butaca no existe. Probá de nuevo.")
                else:
                    f, c = pos
                    if butacas_estado[f][c] == "X":
                        print("Esa butaca ya está ocupada. Elegí otra.")
                    else:
                        butacas_estado[f][c] = "X"
                        butacas_elegidas.append(butaca)
                        valida = True
        i += 1
    butacas_cadena = ",".join(butacas_elegidas)

    #Buscar el precio de la obra
    precio = next((obra["Precio"] for obra in obras if obra["ID"] == id_obra), None)

    if precio is None:
        print("No se encontró una obra con ese ID. No se guardará la reserva.")
    else:
        total = precio * cant
        print(f"El precio de cada entrada es de {precio}")
        print(f"El total a abonar es de {total}")
        reserva = [usuario, nr, id_obra, cant, butacas_cadena, precio, total]
        reservas.append(reserva)

        #registrar usuario en el conjunto de la obra
        for obra in obras:
            if obra["ID"] == id_obra:
                obra["Usuarios"].add(usuario)

        print(f"¡Reserva realizada con éxito! El número de reserva es {nr}")
    mostrar_butacas()

def borrar_reserva():
    mostrar_reservas(reservas)
    try:
        nr = int(input("Ingrese el número de reserva que desea borrar: "))
    except ValueError:
        print("Número inválido.")
        nr = -1
    indice = None
    i = 0
    while i < len(reservas) and indice is None:
        if reservas[i][1] == nr:
            indice = i
        i += 1
    if indice is None:
        print("No se encontró una reserva con ese número.")
    else:
        for b in reservas[indice][4].split(","):
            buscada = b.strip().upper()
            pos = buscar_pos(buscada)
            if pos is not None:
                f, c = pos
                butacas_estado[f][c] = "0"
        reservas.pop(indice)
        print(f"Reserva {nr} eliminada correctamente. Las butacas fueron liberadas.")
    mostrar_butacas()

if __name__ == "__main__":
    mostrar_reservas(reservas)
    init_estado_desde_reservas()
    mostrar_butacas()
