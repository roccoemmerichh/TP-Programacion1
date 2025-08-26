usuarios = [
    [1, "Juan Pérez", "juanperez@gmail.com", "12345678"],
    [2, "Ana Gómez", "anagomez@gmail.com", "87654321"],
    [3, "Carlos López", "carloslopez@gmail.com", "11223344"],
    [4, "María Díaz", "mariadiaz@gmail.com", "44332211"],
    [5, "Luis Fernández", "luisfernandez@gmail.com", "99887766"],
]


def crear_usuario():
    id_usuario = len(usuarios) + 1
    nombre = input("Nombre del usuario: ")
    email = input("Email del usuario: ")
    telefono = input("Teléfono del usuario: ")

    usuario = [id_usuario, nombre, email, telefono]
    usuarios.append(usuario)
    print(f" Usuario {nombre} creado con éxito (ID: {id_usuario})")


def mostrar_usuarios():
    encabezados = ["ID Usuario", "Nombre", "Email", "Teléfono"]
    print("\n======================USUARIOS============================")
    for titulo in encabezados:
        print(titulo, end="\t")
    print()
    for usuario in usuarios:
        for dato in usuario:
            print(dato, end="\t")
        print()
