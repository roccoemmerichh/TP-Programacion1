import obras
import re
import Main
import json
import os 

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


def obtener_todas_las_reservas():
    #Lee todas las reservas del archivo y las devuelve en una lista
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

def obtener_ultima_nr_reserva(archivo):
    #Lee el archivo para encontrar el último numero de reserva.
    ultimo_nr = 0
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if linea:
                    try:
                        datos = linea.split(";")
                        nr_actual = int(datos[1]) 
                        if nr_actual > ultimo_nr:
                            ultimo_nr = nr_actual
                    except (ValueError, IndexError):
                        pass 
    except FileNotFoundError:
        pass  
    return ultimo_nr

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
    print(f"{encabezados[0]:<10} {encabezados[1]:<5} {encabezados[2]:<10} {encabezados[3]:<10} {encabezados[4]:<20} {encabezados[5]:<10} {encabezados[6]:<10}")
    print("-" * 75)
    i = 0
    while i < len(reservas_):
        r = reservas_[i]
        print(f"{r[0]:<10} {r[1]:<5} {r[2]:<10} {r[3]:<10} {r[4]:<20} {r[5]:<10} {r[6]:<10}")
        i += 1
    print()
    input("Presione ENTER para continuar")

def init_estado_desde_reservas():
    #Lee de reservas.txt para llenar la matriz 'butacas_estado' al inicio del programa
    reservas = obtener_todas_las_reservas()
    
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
    print("Estado de butacas inicializado desde el archivo.")

def crear_reserva():
    """
    Agrega una nueva reserva al final del archivo (modo 'a').
    No carga todo el archivo en memoria (excepto para obtener el último ID).
    """
    
    usuario = Main.ingreso_entero("Coloque el id de usuario: ")
    
    ultimo_nr = obtener_ultima_nr_reserva(ARCHIVO_RESERVAS)
    nr = ultimo_nr + 1
        
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
        for b in butacas_elegidas:
            pos = buscar_pos(b)
            if pos:
                butacas_estado[pos[0]][pos[1]] = "0"
    else:
        total = precio * cant
        print(f"El precio de cada entrada es de ${precio}")
        print(f"El total a abonar es de ${total}")
        
        try:
            with open(ARCHIVO_RESERVAS, "a", encoding="UTF-8") as arch:
                nueva_reserva = f"{usuario};{nr};{id_obra_valido};{cant};{butacas_cadena};{precio};{total}\n"
                arch.write(nueva_reserva)
            print(f"¡Reserva realizada con éxito! El número de reserva es {nr}")
        except OSError as e:
            print(f"Error al guardar la reserva: {e}")
            for b in butacas_elegidas:
                pos = buscar_pos(b)
                if pos:
                    butacas_estado[pos[0]][pos[1]] = "0"
            print("Se revirtió la ocupación de butacas en memoria.")
            
    mostrar_butacas()
    input("Presione ENTER para continuar.")

def modificar_reserva():
    #Modifica una reserva usando el método de archivo temporal.
    nr_modificar = str(Main.ingreso_entero("Ingrese el número de reserva que desea modificar: "))
    temp_archivo = "archivos/reservas.tmp"
    encontrado = False
    reserva_modificada = ""

    try:
        with open(ARCHIVO_RESERVAS, "rt", encoding="UTF-8") as arch, \
             open(temp_archivo, "wt", encoding="UTF-8") as aux:

            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue
                
                try:
                    datos = linea.split(";")
                    codigo_nr = datos[1]
                except (ValueError, IndexError):
                    aux.write(linea + '\n')
                    continue

                if codigo_nr == nr_modificar:
                    encontrado = True
                    usuario_actual = datos[0]
                    id_obra_actual = datos[2]
                    cant_actual = datos[3]
                    butacas_actuales = datos[4]
                    precio_actual = datos[5]
                    
                    print(f"Reserva actual (NR {codigo_nr}): Usuario {usuario_actual}, Obra {id_obra_actual}")

                    nuevo_usuario = input("Nuevo ID de usuario (ENTER para dejar igual): ").strip()
                    if nuevo_usuario == "" or not nuevo_usuario.isdigit():
                        nuevo_usuario = usuario_actual
                    
                    nuevo_id_obra = input("Nuevo ID de Obra (ENTER para dejar igual): ").strip()
                    if nuevo_id_obra == "" or not nuevo_id_obra.isdigit():
                        nuevo_id_obra = id_obra_actual
                        nuevo_precio = precio_actual
                    else:
                        precio_buscado = buscar_precio(int(nuevo_id_obra))
                        if precio_buscado is not None:
                            nuevo_precio = precio_buscado
                        else:
                            print("ID de obra nuevo no encontrado. Se mantiene la obra original.")
                            nuevo_id_obra = id_obra_actual
                            nuevo_precio = precio_actual
                    
                    total_nuevo = int(nuevo_precio) * int(cant_actual)
                    
                    nueva_linea = f"{nuevo_usuario};{codigo_nr};{nuevo_id_obra};{cant_actual};{butacas_actuales};{nuevo_precio};{total_nuevo}\n"
                    aux.write(nueva_linea)
                    reserva_modificada = nueva_linea.strip()
                    print("Reserva modificada.")
                else:
                    aux.write(linea + '\n')
                    
    except FileNotFoundError:
        print(f"El archivo {ARCHIVO_RESERVAS} no existe.")
        return
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.remove(ARCHIVO_RESERVAS)
            os.rename(temp_archivo, ARCHIVO_RESERVAS)
            print(f"Reserva nueva: {reserva_modificada}")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp_archivo)
        print(f"No se encontró la reserva con NR {nr_modificar}.")

    input("Presione ENTER para continuar.")


def borrar_reserva():
    #Borra una reserva usando el metodo de archivo temporal.
    nr_borrar = str(Main.ingreso_entero("Ingrese el número de reserva que desea borrar: "))
    temp_archivo = "archivos/reservas.tmp"
    encontrado = False
    butacas_a_liberar = []

    try:
        with open(ARCHIVO_RESERVAS, "rt", encoding="UTF-8") as arch, \
             open(temp_archivo, "wt", encoding="UTF-8") as aux:

            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue
                
                try:
                    datos = linea.split(";")
                    codigo_nr = datos[1]
                except (ValueError, IndexError):
                    aux.write(linea + '\n')
                    continue

                if codigo_nr == nr_borrar:
                    encontrado = True
                    confirmacion = input(f"¿Seguro que quiere borrar la reserva {codigo_nr} (Usuario: {datos[0]})? (s/n): ").strip().lower()
                    if confirmacion == 's':
                        butacas_a_liberar = datos[4].split(",")
                        print(f"Reserva {codigo_nr} eliminada.")
                    else:
                        aux.write(linea + '\n')
                        print("Operación cancelada.")
                        encontrado = False 
                else:
                    aux.write(linea + '\n') 
    except FileNotFoundError:
        print(f"El archivo {ARCHIVO_RESERVAS} no existe.")
        return
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.remove(ARCHIVO_RESERVAS)
            os.rename(temp_archivo, ARCHIVO_RESERVAS)
            
            j = 0
            while j < len(butacas_a_liberar):
                buscada = butacas_a_liberar[j].strip().upper()
                pos = buscar_pos(buscada)
                if pos is not None:
                    f, c = pos
                    butacas_estado[f][c] = "0" 
                j += 1
            print("Las butacas fueron liberadas en el sistema.")

        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp_archivo)
        if not butacas_a_liberar: 
            print(f"Reserva no encontrada con NR {nr_borrar}.")
        
    mostrar_butacas()
    input("Presione ENTER para continuar.")

if __name__ == "__main__":
    init_estado_desde_reservas()
    reservas_leidas = obtener_todas_las_reservas()
    mostrar_reservas(reservas_leidas)
    mostrar_butacas()
