from io import open

def Leer_Data():
    archivos_texto = open('Entrada.data', 'r')
    texto = archivos_texto.read()
    return texto

def Leer_Intrucciones():
    archivos_texto = open('Reporte.lfp', 'r')
    texto = archivos_texto.read()
    return texto

def Menu():
    print("MENU ANALIZADOR")
    print("--- Seleccione una opcion ---")
    print('1. Cargar Data')
    print('2. Cargar Intrucciones')
    print('3. Obtener Grafica')
    print('4. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida