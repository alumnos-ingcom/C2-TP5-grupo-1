################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibonacci(numero):
    """Sucesion fibonacci hasta el limite indicado"""

    try:
        numero = int(numero)

    except ValueError:
        raise ValueError('Valor invalido')

    valor_1 = 0
    valor_2 = 1

    for n in range(numero-1):
        valor_temp = valor_2
        valor_2 += valor_1
        valor_1 = valor_temp
        
    return valor_2

def prueba():
    """Toda la interacción con el usuario va acá"""

    numero = input('Ingrese el termino limite de la sucesion Fibonacci: ')
    
    print(fibonacci(numero))


if __name__ == "__main__":
    prueba()