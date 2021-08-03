#importaciones
from Analizador import Analizador
from helpers import Menu, Leer_Archivos

print("Mi analizador")


def main():
    entrada = ""
    opcion = Menu()
    while opcion != 3 :
        if opcion == 1:
           entrada = Leer_Archivos()
        elif opcion == 2:
            lexico = Analizador()
            lexico.analisis(entrada)
        elif opcion ==3:
            print("Terminando el programa...")
        opcion = Menu();

if __name__ == "__main__":
    main()