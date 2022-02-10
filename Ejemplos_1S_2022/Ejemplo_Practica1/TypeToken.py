from enum import Enum

class TypeToken(Enum):
    CADENA = 2
    NUMERO = 3
    LLAVE_ABRE = 4
    LLAVE_CIERRA =5
    CORCHETE_ABRE = 6
    CORCHETE_CIERRE = 7
    PUNTO_COMA = 8
    COMA = 9
    DOS_PUNTOS =10
    DESCONOCIDO = 11
    NOMBRE = 12
    GRAFICA = 13
    LETRAS = 14