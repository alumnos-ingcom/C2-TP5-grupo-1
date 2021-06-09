################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def comprobacion_pares(numero):
    """Comprobacion de par e impar"""
    
    try:
        numero = float(numero) / 2

    except ValueError:
        raise ValueError('Valor invalido')


    if str(numero).endswith('0') == True:
        return True

    else:
        return False



def prueba():
    """Toda la interacción con el usuario va acá"""

    numero = input('Ingrese un numero a comprobar: ')
    numero = comprobacion_pares(numero)

    print(numero)


if __name__ == "__main__":
    prueba()