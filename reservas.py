import obras
import re
import Main

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

def butaca_valida(b):
    return re.match(r"^[A-Ha-h][1-8]$", b.strip()) is not None

def buscar_pos(butaca):
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

def _construir_ids_obras():
    ids = []
    i = 0
    while i < len(obras.obras):
        o = obras.obras[i]
        val = o.get("ID")
        ya = False
        j = 0
        while j < len(ids):
            if ids[j] == val:
                ya = True
            j += 1
        if not ya:
            ids.append(val)
        i += 1
    return ids

def buscar_precio(id):
    i = 0
    while i < len(obras.obras):
        o = obras.obras[i]
        if o.get("ID") == id:
            return o.get("Precio")
        i += 1
    return None

def mostrar_butacas():
    print("\n======================== BUTACAS ============================")
    numeros = ""
    n = 1
    while n <= 8:
        numeros = numeros + f"{n:>4}"
        n += 1
    print("    " + numeros)
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
        partes = butacas_str.split(",")
        j = 0
        while j < len(partes):
            buscada = partes[j].strip().upper()
            pos = buscar_pos(buscada)
            if pos is not None:
                ff, cc = pos
                butacas_estado[ff][cc] = "X"
            j += 1
        i += 1

def crear_reserva():
    usuario = Main.ingreso_entero("Coloque el id de usuario: ")
    nr = len(reservas) + 1
    ids_obras = _construir_ids_obras()
    id_obra_valido = 0
    ok = False
    while ok == False:
        id_obra_valido = Main.ingreso_entero("Id de la obra: ")
        esta = False
        i = 0
        while i < len(ids_obras):
            if ids_obras[i] == id_obra_valido:
                esta = True
            i += 1
        if esta:
            ok = True
        else:
            print("ID de obra inexistente. Mostrá las obras y elegí un ID válido.")
    cant = 0
    listo = False
    while listo == False:
        cant = Main.ingreso_entero("Cuántas entradas deseas reservar: ")
        if cant > 0:
            listo = True
        else:
            print("La cantidad debe ser un entero positivo.")
    mostrar_butacas()
    butacas_elegidas = []
    i = 0
    while i < cant:
        valida = False
        while valida == False:
            butaca = input("Butaca que desea (" + str(i+1) + "/" + str(cant) + "): ").strip().upper()
            if not butaca_valida(butaca):
                print("Formato inválido. Usá A-H y 1-8 (ej: C5).")
            else:
                repetida = False
                r = 0
                while r < len(butacas_elegidas):
                    if butacas_elegidas[r] == butaca:
                        repetida = True
                    r += 1
                if repetida:
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
    precio = buscar_precio(id_obra_valido)
    if precio is None:
        print("No se encontró una obra con ese ID. No se guardará la reserva.")
    else:
        total = precio * cant
        print("El precio de cada entrada es de " + str(precio))
        print("El total a abonar es de " + str(total))
        reserva = [usuario, nr, id_obra_valido, cant, butacas_cadena, precio, total]
        reservas.append(reserva)
        print("¡Reserva realizada con éxito! El número de reserva es " + str(nr))
    mostrar_butacas()

def modificar_reserva():
    mostrar_reservas(reservas)
    nr = Main.ingreso_entero("Ingrese el número de reserva que desea modificar: ")
    indice = None
    i = 0
    while i < len(reservas) and indice is None:
        if reservas[i][1] == nr:
            indice = i
        i += 1

    if indice is None:
        print("No se encontró la reserva.")
        return

    reserva = reservas[indice]
    print("Reserva actual:")
    print("Usuario:", reserva[0], "NR:", reserva[1], "ID Obra:", reserva[2],
          "Cantidad:", reserva[3], "Butacas:", reserva[4],
          "Precio:", reserva[5], "Total:", reserva[6])

    nuevo_usuario = input("Nuevo usuario (ENTER para dejar igual): ").strip()
    if nuevo_usuario != "":
        if nuevo_usuario.isdigit():
            reserva[0] = int(nuevo_usuario)

    nuevo_id_obra = input("Nuevo ID de Obra (ENTER para dejar igual): ").strip()
    if nuevo_id_obra != "":
        if nuevo_id_obra.isdigit():
            id_obra_int = int(nuevo_id_obra)
            precio = buscar_precio(id_obra_int)
            if precio is not None:
                reserva[2] = id_obra_int
                reserva[5] = precio
                reserva[6] = precio * reserva[3]

    nueva_cant = input("Nueva cantidad (ENTER para dejar igual): ").strip()
    if nueva_cant != "":
        if nueva_cant.isdigit():
            cant_int = int(nueva_cant)
            if cant_int > 0:
                reserva[3] = cant_int
                reserva[6] = reserva[5] * cant_int

    nuevas_butacas = input("Nuevas butacas separadas por coma (ENTER para dejar igual): ").strip()
    if nuevas_butacas != "":
        reserva[4] = nuevas_butacas
        partes = nuevas_butacas.split(",")
        cantidad_real = 0
        j = 0
        while j < len(partes):
            if partes[j].strip() != "":
                cantidad_real += 1
            j += 1
        reserva[3] = cantidad_real
        reserva[6] = reserva[5] * cantidad_real

    print("✅ Reserva modificada con éxito:")
    print("Usuario:", reserva[0], "NR:", reserva[1], "ID Obra:", reserva[2],
          "Cantidad:", reserva[3], "Butacas:", reserva[4],
          "Precio:", reserva[5], "Total:", reserva[6])

def borrar_reserva():
    mostrar_reservas(reservas)
    nr = Main.ingreso_entero("Ingrese el número de reserva que desea borrar: ")
    indice = None
    i = 0
    while i < len(reservas) and indice is None:
        if reservas[i][1] == nr:
            indice = i
        i += 1
    if indice is None:
        print("No se encontró una reserva con ese número.")
    else:
        partes = reservas[indice][4].split(",")
        j = 0
        while j < len(partes):
            buscada = partes[j].strip().upper()
            pos = buscar_pos(buscada)
            if pos is not None:
                f, c = pos
                butacas_estado[f][c] = "0"
            j += 1
        reservas.pop(indice)
        print("Reserva " + str(nr) + " eliminada correctamente. Las butacas fueron liberadas.")
    mostrar_butacas()

if __name__ == "__main__":
    mostrar_reservas(reservas)
    init_estado_desde_reservas()
    mostrar_butacas()
