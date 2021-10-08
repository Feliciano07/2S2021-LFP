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
            print(self.lista[self.posicion].valid_lexeme, "-- Sintactico", " -- Se esperaba"+str(self.lista[self.posicion].type))
            self.errorSintactico = True
        
        if self.preanalisis != TypeToken.ULTIMO:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].type
        
        if self.preanalisis == TypeToken.ULTIMO:
            print('Se finalizado el analisis sintactico')

    def Inicio(self):
        print('Inicio del analisis', self.preanalisis)
        self.Match(TypeToken.TITULO.name)
