from Token import Token

class Analizador:
    #Guarda lo que llevo actualmente
    lexema = ''
    #lista de tokens
    tokens= []
    #Estado en que me encuentro
    estado = 1
    #Fila en la que me encuentro
    fila = 1
    #Columna en que me cuentro
    columna = 1
    #booleano para saber si tengo errores
    generar = False

    #Esto es solo para manejar los tipos
    tipos = Token("lexema", -1, -1, -1)

    def scanner(self,entrada):
        self.estado = 1
        self.lexema = ''
        self.tokens = []
        self.fila = 1
        self.columna = 1
        self.generar = True

        entrada = entrada + '#'
        actual = ''
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            
            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                elif actual == '"':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                elif actual == '=':
                    self.columna +=1
                    self.AgregarToken(tipos.IGUAL)
                elif actual == '{':
                    self.columna +=1
                    self.AgregarToken(tipos.LLAVE_D)
                elif actual == '}':
                    self.columna += 1
                    self.AgregarToken(tipos.LLAVE_I)
                elif actual == ',':
                    self.columna +=1
                    self.AgregarToken(tipos.COMA)
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 1
                    self.columna = 1
                elif actual =='\r':
                    self.estado = 1
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 1
                elif actual == '#' and i ==longitud - 1:
                    print('Analisis terminado')
                else:
                    self.lexema += actual
                    self.AgregarToken(tipos.DESCONOCIDO)
                    self.columna += 1
                    self.generar = False
                
            
            elif self.estado == 2:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                else:
                    if self.es_palabra_reserva(self.lexema):
                        self.AgregarToken(tipos.PALABRA_RESERVADA)
                    elif self.es_true_false(self.lexema):
                        self.AgregarToken(tipos.BOOLEANOS)
                    else:
                        self.AgregarToken(tipos.ID)

            elif self.estado == 3:
                if actual.isalpha():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                else:
                    self.AgregarToken(tipos.ID)

            elif self.estado == 4:
                if actual.isdigit():
                    self.estado = 4    
                    self.columna += 1
                    self.lexema += actual
                else:
                    self.lexema = actual
                    self.columna += 1
                    self.AgregarToken(tipos.DESCONOCIDO) 

            elif self.estado == 5:
                if actual != '"':
                    self.estado = 5
                    self.columna +=1
                    self.lexema += actual
                elif actual == '"':
                    self.lexema +=actual 
                    self.AgregarToken(tipos.CADENA)

    
    def AgregarToken(self,tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 1


    def es_palabra_reserva(self,entrada = ''):
        entrada = entrada.lower() #convertir todo a minuscula
        valor = False
        reservadas = ["variables","valores"];
        
        if entrada in reservadas:
            valor = True
        
        return valor

    def es_true_false(self,entrada = ''):
        entrada = entrada.lower()
        valor = False
        valores = ["true", 'false']
        if entrada in valores:
            valor = True
        
        return valor

    def Imprimir(self):
        for x in self.tokens:
            if x.tipo != tipos.DESCONOCIDO:
                print(x.getLexema()," --> ",x.getTipo(),' --> ',x.getFila(), ' --> ',x.getColumna())
    

    def ImprimirErrores(self):
        for x in self.tokens:
            if x.tipo == tipos.DESCONOCIDO:
                print(x.getLexema()," --> ",x.getFila(), ' --> ',x.getColumna(),'--> Error Lexico')
    
    

    