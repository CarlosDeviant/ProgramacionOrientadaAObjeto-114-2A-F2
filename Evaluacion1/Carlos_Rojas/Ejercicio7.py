from os import system
system("cls")

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Correo: {self.correo}")

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, correo):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("El contacto ya existe en la agenda.")
                return
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Listado de contactos:")
            for contacto in self.contactos:
                contacto.mostrar_info()

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                contacto.mostrar_info()
                return
        print("No se encontró un contacto con ese nombre.")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"Contacto '{nombre}' eliminado correctamente.")
                return
        print("No se encontró un contacto con ese nombre.")

def menu():
    agenda = Agenda()
    while True:
        system("cls")
        print("====== AGENDA DE CONTACTOS ======")
        print("1. Agregar nuevo contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto por nombre")
        print("4. Eliminar contacto")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            correo = input("Ingrese el correo electrónico: ")
            agenda.agregar_contacto(nombre, telefono, correo)
        elif opcion == "2":
            agenda.mostrar_contactos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu()
