#importaciones
from Analizador import Analizador
from Helpers import Menu, Leer_Archivos



def main():
    entrada = ""
    opcion = Menu()
    lexico = Analizador()
    while opcion != 0 :
        if opcion == 1:
           entrada = Leer_Archivos()
        elif opcion == 2:
            lexico.scanner(entrada)
        elif opcion ==3:
            print("Lista de tokens")
            lexico.Imprimir()
        elif opcion == 4:
            print('Lista de errores')
            lexico.ImprimirErrores()
        elif opcion == 0 :
            print('Terminando el programa...')
        opcion = Menu();

if __name__ == "__main__":
    main()