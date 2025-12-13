from clases.personal import Empresa, Vendedor, Gerente, Practicante

def main():
    empresa = Empresa()

    
    v1 = Vendedor("Juan", "1-9", 400000, 1000000, 5) 
    g1 = Gerente("Ana", "2-8", 1500000, 200000)      
    p1 = Practicante("Pedro", "3-7", 5000, 100)      

    empresa.contratar(v1)
    empresa.contratar(g1)
    empresa.contratar(p1)

    print("\n--- REPORTE DE SUELDOS ---")
    print(f"Vendedor gana: ${v1.calcular_sueldo_final()}")
    print(f"Gerente gana:  ${g1.calcular_sueldo_final()}")
    print(f"Practicante:   ${p1.calcular_sueldo_final()}")

    print(f"\nGASTO TOTAL EMPRESA: ${empresa.total_sueldos()}")

if __name__ == "__main__":
    main()