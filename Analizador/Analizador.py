from Token import Token
class Analizador:
    #Guardo lo que llevo reconociendo
    lexema = ''
    #Lista de tokens 
    tokens = []
    #estado, para saber donde ando
    estado = 0
    #metodo que se ejecuta al instanciar una clase, constructor. self referencia a mi objeto
    def __init__(self):
        print('Nuevo objeto')
    
    def analisis(self, entrada):
        #Para saber que llevo en ejecucion
        self.estado = 0

        self.lexema = ''
        self.tokens = []
        entrada = entrada +'#'
        actual = '$'
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            
            if self.estado == 0:
                if actual.isalpha():
                    self.estado = 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.lexema += actual
                    self.estado = 2
                    continue
                elif actual == '"':
                    self.lexema += actual
                    self.estado = 3
                    continue
                elif actual == '#':
                    print("Analisis Finalizado")
                    continue
                elif actual == '=' or actual == ";" or actual == "<" or actual == ">" or actual == "," or actual == "[" or actual == ']' or actual == '{' or actual == "}":
                    self.estado = 0
                    continue
                elif actual == ' ' or actual =="\n" or actual == "\r":
                    self.estado = 0
                    continue
                else:
                    print('Error', actual)
                    continue
            #Estado para manejar numeros y letras
            if self.estado == 1:
                if actual.isalnum():
                    self.estado = 1
                    self.lexema += actual
                else:
                    #Verificar si es palabra reservada, agregar token
                    if self.Palabras():
                        self.AgregarToken(1)
                    elif self.Reporte():
                        self.AgregarToken(5)
                    else:
                        self.AgregarToken(4)
                    i -= 1
            #Maneja digitos
            if self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.lexema += actual
                else:
                    self.AgregarToken(3)
                    i -= 1
            #Manejar cadenas
            if self.estado == 3:
                if actual != '"':
                    self.lexema += actual
                    self.estado = 3
                else:
                    self.lexema += actual
                    self.AgregarToken(2)
        return self.tokens

    def AgregarToken(self, tipo):
        self.tokens.append(Token(self.lexema,tipo))
        self.lexema = ''
        self.estado = 0
    def Palabras(self):
        if self.lexema == 'Nombre':
            return True
        elif self.lexema == 'Valores':
            return True
        elif self.lexema == 'Reportes':
            return True
        else:
            return False
    def Reporte(self):
        if self.lexema == 'ASC':
            return True
        if self.lexema == 'DESC':
            return True
        else:
            return False