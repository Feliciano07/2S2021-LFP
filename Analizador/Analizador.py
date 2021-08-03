class Analizador:
    #Guardo lo que llevo reconociendo
    lexema = ''
    #Guardo en que posicion del archivo estoy
    estado = 0
    #metodo que se ejecuta al instanciar una clase, constructor. self referencia a mi objeto
    def __init__(self):
        print('Nuevo objeto')
    
    def analisis(self, entrada):
        self.estado = 0
        self.lexema = ''
        entrada = entrada +'#'
        actual = '$'
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            print(actual)
