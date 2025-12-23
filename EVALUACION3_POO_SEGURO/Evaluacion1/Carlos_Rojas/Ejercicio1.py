from os import system
system("cls")

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0:
            self.copias -= 1
            print(f"Se ha prestado '{self.titulo}'. Copias restantes: {self.copias}")
        else:
            print(f"No hay copias disponibles de '{self.titulo}'.")

    def devolver(self):
        self.copias += 1
        print(f"Se ha devuelto '{self.titulo}'. Copias disponibles: {self.copias}")

    def mostrar_info(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | Copias disponibles: {self.copias}")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, titulo, autor, copias):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print("Ese libro ya está registrado.")
                return
        nuevo_libro = Libro(titulo, autor, copias)
        self.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' registrado correctamente.")

    def mostrar_catalogo(self):
        if not self.libros:
            print("No hay libros registrados en la biblioteca.")
        else:
            print("Catálogo de libros:")
            for libro in self.libros:
                libro.mostrar_info()

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.prestar()
        else:
            print("El libro no existe en la biblioteca.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.devolver()
        else:
            print("El libro no existe en la biblioteca.")


def menu():
    biblioteca = Biblioteca()
    while True:
        system("cls")
        print("====== SISTEMA DE BIBLIOTECA ======")
        print("1. Registrar nuevo libro")
        print("2. Mostrar catálogo completo")
        print("3. Buscar libro por título")
        print("4. Registrar préstamo de libro")
        print("5. Registrar devolución de libro")
        print("6. Mostrar estado de un libro específico")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            try:
                copias = int(input("Ingrese el número de copias disponibles: "))
                biblioteca.registrar_libro(titulo, autor, copias)
            except ValueError:
                print("Debe ingresar un número válido de copias.")
        elif opcion == "2":
            biblioteca.mostrar_catalogo()
        elif opcion == "3":
            titulo = input("Ingrese el título a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                libro.mostrar_info()
            else:
                print("Libro no encontrado.")
        elif opcion == "4":
            titulo = input("Ingrese el título del libro a prestar: ")
            biblioteca.prestar_libro(titulo)
        elif opcion == "5":
            titulo = input("Ingrese el título del libro a devolver: ")
            biblioteca.devolver_libro(titulo)
        elif opcion == "6":
            titulo = input("Ingrese el título del libro a consultar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                libro.mostrar_info()
            else:
                print("Libro no encontrado.")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    menu()
