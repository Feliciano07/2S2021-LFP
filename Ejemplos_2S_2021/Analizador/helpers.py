from io import open

def Leer_Archivos():
    archivos_texto = open('Entrada.lfp', 'r')
    texto = archivos_texto.read()
    return texto

def Menu():
    print("MENU ANALIZADOR")
    print("--- Seleccione una opcion ---")
    print('1. Leer Archivo')
    print('2. Obtener reportes')
    print('3. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida
