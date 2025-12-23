class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_total(self, cantidad):
        return self.precio * cantidad

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, costo_envio):
        super().__init__(nombre, precio, stock)
        self.costo_envio = costo_envio

    def calcular_total(self, cantidad):
        
        return (self.precio * cantidad) + self.costo_envio

class ProductoDigital(Producto):
    def calcular_total(self, cantidad):
        
        return self.precio * cantidad

class Carrito:
    def __init__(self):
        self.productos = [] 

    def agregar(self, producto, cantidad):
        if producto.stock >= cantidad:
            
            producto.stock -= cantidad
            
            
            item = {
                "nombre": producto.nombre,
                "cantidad": cantidad,
                "total": producto.calcular_total(cantidad)
            }
            self.productos.append(item)
            print(f"Agregado: {producto.nombre}")
        else:
            print(f"No hay stock suficiente de {producto.nombre}")

    def mostrar_detalle(self):
        print("\n--- DETALLE DEL CARRITO ---")
        suma_total = 0
        for item in self.productos:
            print(f"Producto: {item['nombre']} | Cantidad: {item['cantidad']} | Costo: ${item['total']}")
            suma_total += item['total']
        
        print(f"\nTOTAL A PAGAR: ${suma_total}")