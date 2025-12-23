class Trabajador:
    def __init__(self, nombre, rut, sueldo_base):
        self.nombre = nombre
        self.rut = rut
        self.sueldo_base = sueldo_base
        self.activo = True

    def calcular_sueldo_final(self):
        return self.sueldo_base


class Vendedor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, ventas, comision):
        super().__init__(nombre, rut, sueldo_base)
        self.ventas = ventas
        self.comision = comision 

    def calcular_sueldo_final(self):
        bono = self.ventas * (self.comision / 100)
        return self.sueldo_base + bono


class Gerente(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, bono_fijo):
        super().__init__(nombre, rut, sueldo_base)
        self.bono_fijo = bono_fijo

    def calcular_sueldo_final(self):
        return self.sueldo_base + self.bono_fijo


class Practicante(Trabajador):
    def __init__(self, nombre, rut, valor_hora, horas):
        super().__init__(nombre, rut, 0)
        self.valor_hora = valor_hora
        self.horas = horas

    def calcular_sueldo_final(self):
        return self.valor_hora * self.horas

class Empresa:
    def __init__(self):
        self.trabajadores = []

    def contratar(self, trabajador):
        self.trabajadores.append(trabajador)

    def total_sueldos(self):
        total = 0
        for t in self.trabajadores:
            if t.activo:
                total += t.calcular_sueldo_final()
        return total