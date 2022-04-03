from io import open

def Leer_Archivos():
    archivos_texto = open('archivoEntrada.pxla', 'r')
    texto = archivos_texto.read()
    return texto

def Menu():
    print("MENU ANALIZADOR")
    print("--- Seleccione una opcion ---")
    print('1. Ver tokens')
    print('2. Ver errores Lexicos')
    print('3. Analisis Sintactico')
    print('4. Ver Errores Sintactico')
    print('0. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida
