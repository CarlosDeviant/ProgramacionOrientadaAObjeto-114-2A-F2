from clases.tienda import Carrito, ProductoFisico, ProductoDigital

def main():
    
    zapatillas = ProductoFisico("Nike", 50000, 10, 3000) 
    curso_python = ProductoDigital("Curso Udemy", 10000, 100)

    carrito = Carrito()

   
    carrito.agregar(zapatillas, 2) 
    carrito.agregar(curso_python, 1) 

    
    carrito.mostrar_detalle()

if __name__ == "__main__":
    main()