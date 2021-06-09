################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def comprobacion_pares(numero):
    """Comprobacion de par e impar"""
    
    try:
        numero = float(numero) / 2

    except:
        return 'Valor invalido'


    if str(numero).endswith('0') == True:
        return True

    else:
        return False



def prueba():
    """Toda la interacción con el usuario va acá"""

    numero = input('Ingrese un numero a comprobar: ')
    
    print(comprobacion_pares(numero))


if __name__ == "__main__":
    prueba()