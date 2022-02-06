
class Token():
    # PALABRA_RESERVADA = 1
    # CADENA  = 2
    # NUMERO = 3
    # VARIABLE = 4 
    # REPORTE = 5
    # DESCONOCIDO = 0
    lexemaValido = ''
    tipo = 0
    tipo_txt = ''

    def __init__(self, lexema, tipo):
        self.lexemaValido = lexema
        self.tipo = tipo
        if self.tipo == 1:
            self.tipo_txt = 'PALABRA_RESERVADA'
        elif self.tipo == 2:
            self.tipo_txt = 'CADENA'
        elif self.tipo == 3:
            self.tipo_txt = 'NUMERO'
        elif self.tipo == 4:
            self.tipo_txt = 'VARIABLE'
        elif self.tipo == 5:
            self.tipo_txt = 'REPORTE'
        elif self.tipo == 6:
            self.tipo_txt == 'DESCONOCIDO'

    def getLexma(self):
        return self.lexemaValido
    
    def __repr__(self):
        return str(self.__dict__)