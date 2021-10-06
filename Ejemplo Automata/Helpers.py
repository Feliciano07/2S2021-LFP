from io import open

def Leer_Archivos():
    archivos_texto = open('Entrada.txt', 'r')
    texto = archivos_texto.read()
    return texto

def Menu():
    print("MENU ANALIZADOR")
    print("--- Seleccione una opcion ---")
    print('1. Leer Archivo')
    print('2. Analizar')
    print('3. Obtener lista de tokens')
    print('4. Obtener errores')
    print('0. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida