################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_perfecto(numero):
    """verificacion de numero perfecto"""

    try:
        numero = int(numero)

    except ValueError:
        raise ValueError('Valor invalido')

    divisores = []
    suma = 0

    for n in range(1,numero):
        
        if numero % n == 0:
            
            divisores.append(n)
            suma += n

    if numero == suma:
        return True
    
    else:
        return False

def prueba():
    """Toda la interacción con el usuario va acá"""

    numero = input('Ingrese un numero para comprobar su perfeccion!: ')
    
    print(numero_perfecto(numero))


if __name__ == "__main__":
    prueba()