obras = []
reservas = []


def agregar_obras():
    cant_obras = int(input("Obras que desesa agregar:"))
    for i in range(cant_obras):
        id_obra = len(obras) + 1
        nombre = input("Nombre de la obra que desea agregar:")
        fecha = input("Fecha de la obra:")
        horario = input("Horario:")
        capacidad = int(input("capacidad:"))
        while capacidad < 0:
            print("error la capacidad debe ser mayor que 0")
            capacidad = int(input("capacidad:"))
        precio = int(input("Precio de la obra:"))
        while precio < 0:
            print("Error el precio debe ser mayor que 0")
            precio = int(input("Precio de la obra:"))
        ocupada = int(input("Cuantos lugares ya estan ocupados:"))
        obra = [id_obra, nombre, fecha, horario, capacidad, precio, ocupada]
        obras.append(obra)
        print(f"La obra {nombre} fue agregada con exito")


def agregar_reservas():
    cant_reservas = int(input("¿Cuántas reservas desea agregar?: "))
    for i in range(cant_reservas):
        nreserva = len(reservas) + 1
        id_obra = int(input("Ingrese el ID de la obra: "))
        nombre = input("Nombre del cliente: ")
        mail = input("Mail del cliente: ")
        cant = int(input("Cantidad de entradas: "))
        while cant <= 0:
            print("Error: la cantidad debe ser mayor que 0.")
            cant = int(input("Cantidad de entradas: "))
        total = int(input("Total a pagar: "))

        reserva = [nreserva, id_obra, nombre, mail, cant, total]
        reservas.append(reserva)
        print(f"La reserva {nreserva} fue agregada con éxito")


def mostrar_obras(obras):
    encabezados_obras = [
        "id obra",
        "Nombre",
        "Fecha",
        "Horario",
        "Capacidad",
        "Precio",
        "Ocupadas",
    ]
    for titulo in encabezados_obras:
        print(titulo, end="\t")
    print()
    for fila in obras:
        for dato in fila:
            print(dato, end="\t")
        print()


def mostrar_reservas(reservas):
    encabezados_reservas = [
        "N reserva",
        "Id obra",
        "Nombre",
        "Mail",
        "total",
        "Cantidad",
    ]
    for titulo in encabezados_reservas:
        print(titulo, end="\t")
    print()
    for fila in reservas:
        for dato in fila:
            print(dato, end="\t")
        print()


def menu():
    while True:
        print("===Menu===")
        print("1-Mostrar obras")
        print("2-Agregar obras")
        print("3-Mostrar reservas")
        print("4-Agregar reservas")
        print("5-Salir")

        opcion = int(input("Escoja una opcion:"))
        if opcion == 1:
            mostrar_obras(obras)
        elif opcion == 2:
            agregar_obras()
        elif opcion == 3:
            mostrar_reservas(reservas)
        elif opcion == 4:
            agregar_reservas()
        elif opcion == 5:
            print("Gracias por usar el sistema")
            exit()
        else:
            print("Error opcion invalida")


menu()
