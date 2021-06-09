################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def tribonacci(numero):
    """Sucesion tribonacci hasta el limite indicado"""

    try:
        numero = int(numero)

    except ValueError:
        raise ValueError('Valor invalido')

    valor_1 = 1
    valor_2 = 1
    valor_3 = 1

    for n in range(numero-1):
        valor_temp = valor_1 + valor_2 + valor_3

        valor_1 = valor_2
        valor_2 = valor_3
        valor_3 = valor_temp

    return valor_3

def prueba():
    """Toda la interacción con el usuario va acá"""

    numero = input('Ingrese el termino limite de la sucesion Tribonacci: ')
    
    print(tribonacci(numero))


if __name__ == "__main__":
    prueba()