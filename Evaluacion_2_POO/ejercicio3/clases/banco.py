class Cuenta:
    def __init__(self, numero, titular, saldo_inicial):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.historial = [] 

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.historial.append(f"Deposito: +{monto}")
            print(f"Depositados {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("El monto debe ser positivo.")

    
    def retirar(self, monto):
        pass 

class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo, linea_credito):
        super().__init__(numero, titular, saldo)
        self.linea_credito = linea_credito

    def retirar(self, monto):
        
        if (self.saldo + self.linea_credito) >= monto:
            self.saldo -= monto
            self.historial.append(f"Retiro: -{monto}")
            print(f"Retiro OK. Saldo actual: {self.saldo}")
        else:
            print("No tienes fondos suficientes.")

class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo, tasa_interes):
        super().__init__(numero, titular, saldo)
        self.tasa_interes = tasa_interes 

    def retirar(self, monto):
        
        if self.saldo >= monto:
            self.saldo -= monto
            self.historial.append(f"Retiro: -{monto}")
            print(f"Retiro OK. Saldo actual: {self.saldo}")
        else:
            print("Falta saldo en cuenta de ahorro.")

    def aplicar_interes(self):
        ganancia = self.saldo * self.tasa_interes
        self.saldo += ganancia
        self.historial.append(f"Interés ganado: +{ganancia}")
        print(f"Interés aplicado. Nuevo saldo: {self.saldo}")