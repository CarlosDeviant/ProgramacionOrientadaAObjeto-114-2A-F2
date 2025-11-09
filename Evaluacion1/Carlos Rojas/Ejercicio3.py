from os import system
system("cls")

class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def mostrar_info(self):
        print(f"Ítem: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Subtotal: ${self.calcular_subtotal():.2f}")

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, precio, cantidad):
        nuevo_item = Item(nombre, precio, cantidad)
        self.items.append(nuevo_item)
        print(f"Ítem '{nombre}' agregado al pedido.")

    def mostrar_items(self):
        if not self.items:
            print("No hay ítems en el pedido.")
        else:
            print("Detalle del pedido:")
            for item in self.items:
                item.mostrar_info()

    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self.items)
        return total

    def mostrar_total(self):
        if not self.items:
            print("El pedido está vacío.")
        else:
            self.mostrar_items()
            print(f"\nTotal a pagar: ${self.calcular_total():.2f}")

def menu():
    pedido = Pedido()
    while True:
        system("cls")
        print("====== SISTEMA DE PEDIDOS DE COMPRA ======")
        print("1. Agregar nuevo ítem")
        print("2. Mostrar ítems del pedido")
        print("3. Mostrar total del pedido")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            nombre = input("Ingrese el nombre del ítem: ")
            try:
                precio = float(input("Ingrese el precio del ítem: "))
                cantidad = int(input("Ingrese la cantidad: "))
                pedido.agregar_item(nombre, precio, cantidad)
            except ValueError:
                print("Debe ingresar valores numéricos válidos para precio y cantidad.")
        elif opcion == "2":
            pedido.mostrar_items()
        elif opcion == "3":
            pedido.mostrar_total()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu()
