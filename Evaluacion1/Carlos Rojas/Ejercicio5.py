from os import system
system("cls")

class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio

    def mostrar_info(self):
        print(f"Título: {self.titulo} | Género: {self.genero} | Año: {self.anio}")

class Catalogo:
    def __init__(self):
        self.peliculas = []

    def registrar_pelicula(self, titulo, genero, anio):
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                print("Esa película ya está registrada.")
                return
        nueva_pelicula = Pelicula(titulo, genero, anio)
        self.peliculas.append(nueva_pelicula)
        print(f"Película '{titulo}' registrada correctamente.")

    def mostrar_catalogo(self):
        if not self.peliculas:
            print("No hay películas registradas en el catálogo.")
        else:
            print("Catálogo de películas:")
            for pelicula in self.peliculas:
                pelicula.mostrar_info()

    def buscar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                pelicula.mostrar_info()
                return
        print("Película no encontrada en el catálogo.")

    def filtrar_por_genero(self, genero):
        filtradas = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if not filtradas:
            print("No se encontraron películas de ese género.")
        else:
            print(f"Películas del género '{genero}':")
            for pelicula in filtradas:
                pelicula.mostrar_info()

def menu():
    catalogo = Catalogo()
    while True:
        system("cls")
        print("====== CATÁLOGO DE PELÍCULAS ======")
        print("1. Registrar nueva película")
        print("2. Mostrar catálogo completo")
        print("3. Buscar película por título")
        print("4. Filtrar películas por género")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            titulo = input("Ingrese el título de la película: ")
            genero = input("Ingrese el género: ")
            anio = input("Ingrese el año de lanzamiento: ")
            catalogo.registrar_pelicula(titulo, genero, anio)
        elif opcion == "2":
            catalogo.mostrar_catalogo()
        elif opcion == "3":
            titulo = input("Ingrese el título a buscar: ")
            catalogo.buscar_pelicula(titulo)
        elif opcion == "4":
            genero = input("Ingrese el género a filtrar: ")
            catalogo.filtrar_por_genero(genero)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu()
