from clases.banco import CuentaCorriente, CuentaAhorro

def main():
    
    cta_cte = CuentaCorriente("C1", "Roberto", 100000, 50000)
    
    
    cta_ahorro = CuentaAhorro("A1", "Maria", 200000, 0.10)

    print("--- OPERACIONES ---")
    cta_cte.retirar(120000) 
    cta_ahorro.aplicar_interes() 

    print("\n--- HISTORIAL CUENTA CTE ---")
    for mov in cta_cte.historial:
        print(mov)

    print("\n--- HISTORIAL CUENTA AHORRO ---")
    for mov in cta_ahorro.historial:
        print(mov)

if __name__ == "__main__":
    main()