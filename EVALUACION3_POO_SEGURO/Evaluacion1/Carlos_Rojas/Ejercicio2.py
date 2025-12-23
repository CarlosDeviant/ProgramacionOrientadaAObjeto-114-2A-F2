from os import system
system("cls")

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Alumno: {self.nombre}")

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir_alumno(self, nombre):
        for alumno in self.alumnos:
            if alumno.nombre.lower() == nombre.lower():
                print("El alumno ya está inscrito en el curso.")
                return
        nuevo_alumno = Alumno(nombre)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno '{nombre}' inscrito correctamente.")

    def remover_alumno(self, nombre):
        for alumno in self.alumnos:
            if alumno.nombre.lower() == nombre.lower():
                self.alumnos.remove(alumno)
                print(f"Alumno '{nombre}' ha sido removido del curso.")
                return
        print("El alumno no está inscrito en el curso.")

    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos inscritos en el curso.")
        else:
            print(f"Listado de alumnos inscritos en '{self.nombre}':")
            for alumno in self.alumnos:
                alumno.mostrar_info()

    def mostrar_estado(self):
        print(f"Curso: {self.nombre}")
        print("Alumnos inscritos:")
        if not self.alumnos:
            print("Ninguno")
        else:
            for alumno in self.alumnos:
                print(f"- {alumno.nombre}")

def menu():
    system("cls")
    nombre_curso = input("Ingrese el nombre del curso: ")
    curso = Curso(nombre_curso)

    while True:
        system("cls")
        print(f"====== SISTEMA DE INSCRIPCIÓN - CURSO: {curso.nombre} ======")
        print("1. Inscribir alumno")
        print("2. Remover alumno")
        print("3. Listar alumnos inscritos")
        print("4. Mostrar estado del curso")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno a inscribir: ")
            curso.inscribir_alumno(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del alumno a remover: ")
            curso.remover_alumno(nombre)
        elif opcion == "3":
            curso.listar_alumnos()
        elif opcion == "4":
            curso.mostrar_estado()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu()
