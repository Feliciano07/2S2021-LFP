
class Token():
    # PALABRA_RESERVADA = 1
    # CADENA  = 2
    # NUMERO = 3
    # VARIABLE = 4 
    # REPORTE = 5
    # DESCONOCIDO = 0
    lexemaValido = ''
    tipo = 0

    def __init__(self, lexema, tipo):
        self.lexemaValido = lexema
        self.tipo = tipo

    def getLexma(self):
        return self.lexemaValido
    
    def __repr__(self):
        return str(self.__dict__)