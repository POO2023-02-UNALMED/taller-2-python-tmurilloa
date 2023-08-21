class Motor:

    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def CambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if self.tipo == "electrico" or self.tipo == "gasolina":
            self.tipo = tipo

class Asiento:

    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,color):
        if self.color == "rojo" or self.color == "verde" or self.color == "amarillo" or self.color == "negro" or self.color == "blanco":
            self.color = color 

class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        numAsientos = 0
        for i in self.asientos:
            if (type(i) == Asiento):
                numAsientos += 1

        return numAsientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in self.asientos:
                if (type(i) == Asiento):
                    if (i.registro) != self.registro:
                        return "Las piezas no son originales"
                    
            return "Auto original"
        else:
    
            return "Las piezas no son originales"


