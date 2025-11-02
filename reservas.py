import obras
import re
import Main
import json

ARCHIVO_RESERVAS = "archivos/reservas.txt"

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


def leer_reservas():
    """
    Lee el archivo reservas.txt y devuelve una lista de listas.
    """
    reservas = []
    try:
        with open(ARCHIVO_RESERVAS, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    try:
                        partes = linea.split(';')

                        reserva = [
                            int(partes[0]),  
                            int(partes[1]),  
                            int(partes[2]),   
                            int(partes[3]),   
                            partes[4],       
                            int(partes[5]),   
                            int(partes[6])    
                        ]
                        reservas.append(reserva)
                    except (ValueError, IndexError):
                        print(f"Advertencia: Se omitió una línea mal formada en {ARCHIVO_RESERVAS}")
    except FileNotFoundError:
        print(f"Nota: No se encontró {ARCHIVO_RESERVAS}, se creará uno nuevo al guardar.")
    
    return reservas

def guardar_reservas(reservas):
    """
    Recibe la lista de listas y la guarda en reservas.txt.
    """
    try:
        with open(ARCHIVO_RESERVAS, 'w', encoding='utf-8') as f:
            for reserva in reservas:
                linea_items = [str(item) for item in reserva]
                linea = ";".join(linea_items)
                f.write(linea + "\n")
    except OSError as e:
        print(f"Error fatal al guardar reservas: {e}")

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
    try:
        with open("archivos/obras.json", "r", encoding="UTF-8") as f:
            lista_obras = json.load(f)
        
        ids = []
        for o in lista_obras:
            val = o.get("ID")
            if val not in ids:
                ids.append(val)
        return ids
    except:
        print("Error al leer obras.json para construir IDs")
        return []


def buscar_precio(id):
    try:
        with open("archivos/obras.json", "r", encoding="UTF-8") as f:
            lista_obras = json.load(f)
        for o in lista_obras:
            if o.get("ID") == id:
                return o.get("Precio")
        return None
    except:
        print("Error al leer obras.json para buscar precio")
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
    print()
    input("Presione ENTER para continuar")

def init_estado_desde_reservas():
    """
    Función CRÍTICA: Ahora lee de reservas.txt para llenar la matriz 'butacas_estado'.
    """
    reservas = leer_reservas()
    
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
    reservas = leer_reservas()
    
    usuario = Main.ingreso_entero("Coloque el id de usuario: ")
    
    if reservas:
        nr = reservas[-1][1] + 1 
    else:
        nr = 1
        
    ids_obras = _construir_ids_obras()
    if not ids_obras:
        print("Error: No se pudieron cargar las obras. No se puede reservar.")
        return

    id_obra_valido = 0
    ok = False
    while ok == False:
        id_obra_valido = Main.ingreso_entero("Id de la obra: ")
        if id_obra_valido in ids_obras:
            ok = True
        else:
            print("ID de obra inexistente. Mostrá las obras y elegí un ID válido.")
    
    cant = Main.ingreso_entero("Cuántas entradas deseas reservar (1 o más): ")
    while cant <= 0:
        cant = Main.ingreso_entero("La cantidad debe ser un entero positivo: ")
        
    mostrar_butacas()
    butacas_elegidas = []
    i = 0
    while i < cant:
        valida = False
        while valida == False:
            butaca = input(f"Butaca que desea ({i+1}/{cant}): ").strip().upper()
            if not butaca_valida(butaca):
                print("Formato inválido. Usá A-H y 1-8 (ej: C5).")
            else:
                if butaca in butacas_elegidas:
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
        print("Error crítico: No se encontró el precio de la obra. No se guardará la reserva.")
    else:
        total = precio * cant
        print(f"El precio de cada entrada es de ${precio}")
        print(f"El total a abonar es de ${total}")
        reserva = [usuario, nr, id_obra_valido, cant, butacas_cadena, precio, total]
        reservas.append(reserva)
        
        guardar_reservas(reservas)
        print(f"¡Reserva realizada con éxito! El número de reserva es {nr}")
        
    mostrar_butacas()
    input("Presione ENTER para continuar.")

def modificar_reserva():
    reservas = leer_reservas()
    
    if not reservas:
        print("No hay reservas para modificar.")
        input("Presione ENTER para continuar.")
        return

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
        input("Presione ENTER para continuar.")
        return

    reserva = reservas[indice]
    print(f"Reserva actual: {reserva}")

    nuevo_usuario = input("Nuevo usuario (ENTER para dejar igual): ").strip()
    if nuevo_usuario != "" and nuevo_usuario.isdigit():
        reserva[0] = int(nuevo_usuario)

    nuevo_id_obra = input("Nuevo ID de Obra (ENTER para dejar igual): ").strip()
    if nuevo_id_obra != "" and nuevo_id_obra.isdigit():
        id_obra_int = int(nuevo_id_obra)
        precio = buscar_precio(id_obra_int)
        if precio is not None:
            reserva[2] = id_obra_int
            reserva[5] = precio
            reserva[6] = precio * reserva[3] 

    guardar_reservas(reservas)
    print("Reserva modificada.")
    print(f"Reserva nueva: {reserva}")
    input("Presione ENTER para continuar.")

def borrar_reserva():
    reservas = leer_reservas()
    
    if not reservas:
        print("No hay reservas para borrar.")
        input("Presione ENTER para continuar.")
        return

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
        
        guardar_reservas(reservas)
        print(f"Reserva {nr} eliminada correctamente. Las butacas fueron liberadas.")
        
    mostrar_butacas()
    input("Presione ENTER para continuar.")

if __name__ == "__main__":
    init_estado_desde_reservas()
    reservas_leidas = leer_reservas()
    mostrar_reservas(reservas_leidas)
    mostrar_butacas()
