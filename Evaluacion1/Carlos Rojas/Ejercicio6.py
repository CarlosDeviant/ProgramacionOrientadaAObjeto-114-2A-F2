from os import system
system("cls")

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario.lower() == nombre_usuario.lower():
                print("El nombre de usuario ya existe.")
                return
        nuevo_usuario = Usuario(nombre_usuario, contrasena)
        self.usuarios.append(nuevo_usuario)
        print("Usuario registrado correctamente.")

    def iniciar_sesion(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario.lower() == nombre_usuario.lower():
                if usuario.contrasena == contrasena:
                    print("Acceso concedido. Bienvenido.")
                else:
                    print("Contraseña incorrecta.")
                return
        print("El usuario no existe.")

    def consultar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario.lower() == nombre_usuario.lower():
                print("El usuario está registrado en el sistema.")
                return
        print("El usuario no está registrado.")

def menu():
    sistema = SistemaAutenticacion()
    while True:
        system("cls")
        print("====== SISTEMA DE AUTENTICACIÓN DE USUARIOS ======")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Consultar usuario")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            sistema.registrar_usuario(nombre_usuario, contrasena)
        elif opcion == "2":
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            sistema.iniciar_sesion(nombre_usuario, contrasena)
        elif opcion == "3":
            nombre_usuario = input("Ingrese el nombre de usuario a consultar: ")
            sistema.consultar_usuario(nombre_usuario)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu()
