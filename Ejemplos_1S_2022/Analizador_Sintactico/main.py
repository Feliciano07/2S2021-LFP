#importaciones
from Analizador import Analyzer
from Sintactico import Sintactico
from Helpers import Menu, Leer_Archivos

print("Mi analizador")


def main():
    entrada = ""
    opcion = Menu()
    entrada = Leer_Archivos()
    lexico = Analyzer(entrada)
    while opcion != 0 :
        if opcion == 1:
           lexico.printTokens()
        elif opcion == 2:
            lexico.printErrors()
        elif opcion ==3:
            sintactico = Sintactico(lexico.tokens)
            #print("analisis sintactico")
        elif opcion == 4:
            print('Ver Errores Sintactico')
        elif opcion == 0 :
            print('Terminando el programa...')
        opcion = Menu();

if __name__ == "__main__":
    main()