class Token():
    lexema_valido = ''
    tipo = 0
    fila = 0
    columna = 0

    #ENUM
    PALABRA_RESERVADA = 1
    CADENA = 2
    NUMERO = 3
    ID = 4
    IGUAL = 5
    LLAVE_I =6
    LLAVE_D = 7
    COMA = 8
    BOOLEANOS = 9
    DESCONOCIDO =10

    #Constructor de la clase
    def __init__(self,lexma,tipo,fila,columna):
        self.lexema_valido = lexma
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema_valido

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.PALABRA_RESERVADA:
            return 'PALABRA_RESERVADA'
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.ID:
            return 'ID'
        elif self.tipo == self.IGUAL:
            return 'IGUAL'
        elif self.tipo == self.LLAVE_I:
            return 'Llave Izquierda'
        elif self.tipo == self.LLAVE_D:
            return "Llave derecha"
        elif self.tipo == self.COMA:
            return "Coma"
        elif self.tipo == self.BOOLEANOS:
            return "Booleano"