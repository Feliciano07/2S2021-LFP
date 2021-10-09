from tokenFile import Token
from typeToken import TypeToken
import re


class Sintactico:
    preanalisis = TypeToken.DESCONOCIDO
    posicion = 0
    lista = []
    errorSintactico = False

    def __init__(self, lista):
        self.errorSintactico = False
        self.lista = lista
        self.lista.append(Token("#", TypeToken.ULTIMO.name, 0, 0))
        self.posicion = 0
        self.preanalisis = self.lista[self.posicion].type
        self.Inicio()
    

    def Match(self,tipo):
        if self.preanalisis != tipo:
            print(self.lista[self.posicion].valid_lexeme, "-- Sintactico", " -- Se esperaba "+str(tipo))
            self.errorSintactico = True
        
        if self.preanalisis != TypeToken.ULTIMO.name:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].type
        
        if self.preanalisis == TypeToken.ULTIMO.name:
            print('Se finalizado el analisis sintactico')


    def Inicio(self):
        print('Inicio del analisis')
        if TypeToken.TITULO.name == self.preanalisis:
            self.Titulo()
            self.Repetir()
        elif TypeToken.ANCHO.name == self.preanalisis:
            self.Ancho()
            self.Repetir()
        elif TypeToken.CELDAS.name == self.preanalisis:
            self.Celdas()


    def Titulo(self):
        self.Match(TypeToken.TITULO.name)
        self.Match(TypeToken.IGUAL.name)
        self.Match(TypeToken.CADENA.name)
        self.Match(TypeToken.PUNTO_Y_COMA.name)

    def Ancho(self):
        self.Match(TypeToken.ANCHO.name)
        self.Match(TypeToken.IGUAL.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.PUNTO_Y_COMA.name)
    
    def Celdas(self):
        self.Match(TypeToken.CELDAS.name)
        self.Match(TypeToken.IGUAL.name)
        self.Match(TypeToken.LLAVE_IZQUIERDA.name)
        self.Bloque_Celdas()
        # self.Match(TypeToken.LLAVE_DERECHA.name)
        # self.Match(TypeToken.PUNTO_Y_COMA.name)


    def Bloque_Celdas(self):
        if TypeToken.CORCHETE_IZQUIERDA.name == self.preanalisis:
            print('entro a bloque celdas')
            self.Cuerpo_Celda()
    
    def Cuerpo_Celda(self):
        self.Match(TypeToken.CORCHETE_IZQUIERDA.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.COMA.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.COMA.name)
        self.Boleano()
        self.Match(TypeToken.COMA.name)
        self.Match(TypeToken.COLOR.name)
        self.Match(TypeToken.CORCHETE_IZQUIERDA.name)

    def Boleano(self):
        self.Match(TypeToken.BOOLEANO.name)

    def Repetir(self):
        if TypeToken.TITULO.name == self.preanalisis:
            self.Titulo()
            self.Repetir()
        elif TypeToken.ANCHO.name == self.preanalisis:
            self.Ancho()
            self.Repetir()
