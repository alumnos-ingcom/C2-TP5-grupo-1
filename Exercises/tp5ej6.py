################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def balanceo_caracteres(delimitador_abierto, delimitador_cerrado, texto):
    """Funcion para comprobar si estan balanceados los caracteres
"""

    abiertos = 0
    salida = ''

    for caracter in texto:

        if caracter == delimitador_abierto:
            abiertos += 1
            
        
        if caracter == delimitador_cerrado and abiertos == 0:
            salida += 'NO '

        if caracter == delimitador_cerrado and abiertos >= 1:
            salida += 'OK '
            abiertos -= 1
    

    return salida


def prueba():
    
    delimitador_abierto = input('Ingrese un delimitador abierto: ')
    delimitador_cerrado = input('Ingrese un delimitador cerrado: ')
    texto = input("Ingrese un texto a analzar: ")

    respuesta = balanceo_caracteres(delimitador_abierto, delimitador_cerrado, texto)
    print(respuesta)


if __name__ == "__main__":
    prueba()