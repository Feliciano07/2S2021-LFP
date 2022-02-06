from tokenFile import Token
from typeToken import TypeToken
import re

class Analyzer():

    tipo = TypeToken.DESCONOCIDO

    def __init__(self, inputFile):
        self.state = 0
        self.lexeme = ''
        self.tokens = []
        self.row = 1
        self.column = 1
        self.generate = True

        inputFile = inputFile + '&'
        actual = ''
        length = len(inputFile)

        for i in range(length):
            actual = inputFile[i]
            if self.state == 0:
                #simplificación estado 1 y 5
                if re.search(r"[a-zA-Z]", actual):
                    self.lexeme += actual
                    self.column += 1
                    self.state = 1
                elif re.search(r"[0-9]", actual):
                    self.lexeme += actual
                    self.column += 1
                    self.state = 2
                elif self.IsSymbol(actual):
                    self.lexeme += actual
                    self.column += 1                    
                    if actual == '=':
                        self.AddToken(TypeToken.IGUAL.name)
                    elif actual == '[':
                        self.AddToken(TypeToken.CORCHETE_IZQUIERDA.name)
                    elif actual == ']':
                        self.AddToken(TypeToken.CORCHETE_DERECHA.name)
                    elif actual == '{':
                        self.AddToken(TypeToken.LLAVE_IZQUIERDA.name)
                    elif actual == '}':
                        self.AddToken(TypeToken.LLAVE_DERECHA.name)
                    elif actual == ',':
                        self.AddToken(TypeToken.COMA.name)
                    elif actual == ';':
                        self.AddToken(TypeToken.PUNTO_Y_COMA.name)

                elif actual == '#':
                    self.lexeme += actual
                    self.column += 1
                    self.state = 4                    
                elif actual == '@':
                    self.lexeme += actual
                    self.column += 1
                    self.state = 6
                elif actual == '"':
                    self.lexeme += actual
                    self.column += 1
                    self.state = 7
                elif re.search(r"[\n]", actual):
                    self.row += 1
                    self.column = 0
                    self.state = 0
                elif re.search(r"[ \t]", actual):
                    self.column += 1
                    self.state = 0
                elif actual == ' ' or actual == '':
                    self.column += 1
                    self.state = 0
                elif actual == '&' and i == (length-1):
                    print("Fin del Analisis")
                else:
                    self.lexeme += actual
                    self.column += 1   
                    self.AddToken(TypeToken.DESCONOCIDO.name)
            elif self.state == 1:
                if re.search(r"[a-zA-Z]", actual):
                    self.lexeme += actual
                    self.column += 1
                    self.state = 1
                elif re.search(r"[0-9]", actual):                    
                    self.lexeme += actual
                    self.column += 1
                    self.state = 1
                else:
                    #i -= 1
                    if self.IsReservedWord(self.lexeme):
                        self.AddToken(self.tipo.name)
                    elif self.IsBool(self.lexeme):
                        self.AddToken(TypeToken.BOOLEANO.name)
                    else:
                        self.AddToken(TypeToken.ID.name)
                    #validar luego si el siguiente es un simbolo que nos interese
                    if self.IsSymbol(actual):
                        self.lexeme += actual
                        self.column += 1                    
                        if actual == '=':
                            self.AddToken(TypeToken.IGUAL.name)
                        elif actual == '[':
                            self.AddToken(TypeToken.CORCHETE_IZQUIERDA.name)
                        elif actual == ']':
                            self.AddToken(TypeToken.CORCHETE_DERECHA.name)
                        elif actual == '{':
                            self.AddToken(TypeToken.LLAVE_IZQUIERDA.name)
                        elif actual == '}':
                            self.AddToken(TypeToken.LLAVE_DERECHA.name)
                        elif actual == ',':
                            self.AddToken(TypeToken.COMA.name)
                        elif actual == ';':
                            self.AddToken(TypeToken.PUNTO_Y_COMA.name)    
                    else:
                        if actual != ' ':
                            self.lexeme += actual
                            self.column += 1   
                            self.AddToken(TypeToken.DESCONOCIDO.name)
                        
            elif self.state == 2:
                if re.search(r"[0-9]", actual):
                    self.lexeme += actual
                    self.column += 1
                    self.state = 2
                else:
                    #i -= 1
                    if self.lexeme.isdigit():
                        self.AddToken(TypeToken.NUMERO.name)
                    else:
                        self.AddToken(TypeToken.DESCONOCIDO.name)
                    #validar luego si el siguiente es un simbolo que nos interese
                    if self.IsSymbol(actual):
                        self.lexeme += actual
                        self.column += 1                    
                        if actual == '=':
                            self.AddToken(TypeToken.IGUAL.name)
                        elif actual == '[':
                            self.AddToken(TypeToken.CORCHETE_IZQUIERDA.name)
                        elif actual == ']':
                            self.AddToken(TypeToken.CORCHETE_DERECHA.name)
                        elif actual == '{':
                            self.AddToken(TypeToken.LLAVE_IZQUIERDA.name)
                        elif actual == '}':
                            self.AddToken(TypeToken.LLAVE_DERECHA.name)
                        elif actual == ',':
                            self.AddToken(TypeToken.COMA.name)
                        elif actual == ';':
                            self.AddToken(TypeToken.PUNTO_Y_COMA.name) 
                    else:
                        self.lexeme += actual
                        self.column += 1   
                        self.AddToken(TypeToken.DESCONOCIDO.name)
                    
            elif self.state == 4:
                if re.search(r"[a-fA-F0-9]", actual):
                    self.lexeme += actual
                    self.column += 1
                    self.state = 4
                else:
                    if self.IsColor(self.lexeme):
                        self.AddToken(TypeToken.COLOR.name)
                    else:
                        self.AddToken(TypeToken.DESCONOCIDO.name)
                    if self.IsSymbol(actual):
                        self.lexeme += actual
                        self.column += 1                    
                        if actual == '=':
                            self.AddToken(TypeToken.IGUAL.name)
                        elif actual == '[':
                            self.AddToken(TypeToken.CORCHETE_IZQUIERDA.name)
                        elif actual == ']':
                            self.AddToken(TypeToken.CORCHETE_DERECHA.name)
                        elif actual == '{':
                            self.AddToken(TypeToken.LLAVE_IZQUIERDA.name)
                        elif actual == '}':
                            self.AddToken(TypeToken.LLAVE_DERECHA.name)
                        elif actual == ',':
                            self.AddToken(TypeToken.COMA.name)
                        elif actual == ';':
                            self.AddToken(TypeToken.PUNTO_Y_COMA.name) 

            elif self.state == 6:
                if actual == '@':
                    self.lexeme += actual
                    self.column += 1
                    self.state = 6
                else:
                    #i -= 1
                    if self.IsSeparator(self.lexeme):
                        self.AddToken(TypeToken.SEPARADOR.name)
                    else:
                        self.AddToken(TypeToken.DESCONOCIDO.name)
            elif self.state == 7:
                if actual != '"':                    
                    self.lexeme += actual
                    self.column += 1
                    self.state = 7
                elif actual == '"':
                    self.lexeme += actual
                    self.AddToken(TypeToken.CADENA.name)


    
    def AddToken(self, type):
        self.tokens.append(Token(self.lexeme, type, self.row, self.column))
        self.lexeme = ''
        self.state = 0

    def IsReservedWord(self, word):
        word = word.upper()
        wordsReserved = ['TITULO', 'ANCHO', 'ALTO', 'FILAS', 'COLUMNAS', 'CELDAS', 'FILTROS', 'MIRRORX', 'MIRRORY', 'DOUBLEMIRROR']

        if word == 'TITULO':
            self.tipo = TypeToken.TITULO
            return True
        elif word =='ANCHO':
            self.tipo = TypeToken.ANCHO
            return True
        elif word == 'ALTO':
            self.tipo = TypeToken.ALTO
            return True
        elif word =='FILAS':
            self.tipo = TypeToken.FILA
            return True
        elif word == 'COLUMNAS':
            self.tipo = TypeToken.COLUMNA
            return True
        elif word == 'CELDAS':
            self.tipo = TypeToken.CELDAS
            return True
        elif word == 'FILTROS':
            self.tipo = TypeToken.FILTROS
            return True
        elif word == 'MIRRORX':
            self.tipo = TypeToken.MIRRORX
            return True
        elif word == 'MIRRORY':
            self.tipo = TypeToken.MIRRORY
            return True
        elif word == 'DOUBLEMIRROR':
            self.tipo = TypeToken.DOUBLEMIRROR
            return True
        
        return False

    def IsBool(self, key):
        key = key.upper()
        keys = ['TRUE', 'FALSE']

        if key in keys:
            return True
        
        return False
    
    def IsSeparator(self, key):
        keys = ['@@@@']

        if key in keys:
            return True
        
        return False

    def IsSymbol(self, key):
        keys = ['=','[',']','{','}',',',';']

        if key in keys:
            return True
        
        return False
        
    def IsColor(self, key):

        if len(key) >= 4 and len(key) <= 5 or len(key) == 7:
            return True
        
        return False

    def printTokens(self):
        for token in self.tokens:
            if token.type != TypeToken.DESCONOCIDO.name:
                print(token.valid_lexeme + " -> Tipo: " + str(token.type) + " Fila: " + str(token.row) + " Columna: " + str(token.column))

    def printErrors(self):
        for token in self.tokens:
            if token.type == TypeToken.DESCONOCIDO.name:
                print(token.valid_lexeme + " -> Tipo: " + str(token.type) + " Fila: " + str(token.row) + " Columna: " + str(token.column))

    def getTokens(self):
        return self.tokens
    
    def fileWithError(self):
        for token in self.tokens:
            if token.type == TypeToken.DESCONOCIDO.name:
                return True
