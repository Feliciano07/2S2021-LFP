from Token import Token
from TypeToken import TypeToken


class LexicoInstrucciones():
    
    tipo = TypeToken.DESCONOCIDO

    def __init__(self,entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens= []
        entrada = entrada + "#"
        actual = ''
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]

            if self.estado == 0:

                if actual.isalpha():
                    self.estado = 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 2
                    self.lexema += actual
                    continue
                elif actual == '{':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.LLAVE_ABRE.name)
                    continue
                elif actual == '}':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.LLAVE_CIERRA.name)
                    continue
                elif actual == ',':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.COMA.name)
                    continue
                elif actual == ':':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.DOS_PUNTOS.name)
                    continue
                elif actual =='#':
                    print( '********* ANALISIS INTRUCCIONES FINALIZADOS ***********')
                    continue
                elif actual == ' ' or actual =="\n" or actual == "\r" or actual =='\t':
                    self.estado = 0
                    continue
                else:
                    print("@@@@ ERROR: ", actual)
                    self.lexema = ''
                    continue
            # Estado para manejar letras
            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.lexema += actual
                    continue
                else:
                    # Verificar si esta dentro de las palabras que solicitan
                    if self.Reservada():
                        self.AgregarToken(self.tipo.name)
                    else:
                        self.AgregarToken(TypeToken.LETRAS.name)
                        i -= 1
            #Estado para manejar cadenas
            if self.estado == 2:
                if actual != '"':
                    self.estado = 2
                    self.lexema += actual
                    continue
                else:
                    self.estado = 3
                    self.lexema += actual
                    self.AgregarToken(TypeToken.CADENA.name)


    def AgregarToken(self, tipo):
        self.tokens.append(Token(self.lexema, tipo))
        self.lexema =''
        self.estado = 0
        self.tipo = TypeToken.DESCONOCIDO

    def Reservada(self):
        palabra = self.lexema.upper();
        #lista_palabras = ['NOMBRE', 'GRAFICA']
        if palabra =='NOMBRE':
            self.tipo = TypeToken.NOMBRE  #Mejor control
            return True
        if palabra == 'GRAFICA':
            self.tipo = TypeToken.GRAFICA #Mejor control
            return True
        return False

    def printTokens(self):
        for token in self.tokens:
            print(token.lexema + " -> Tipo: " + str(token.type))