################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia_numerica(n1, n2):
    """Funcion calcular distancia entre dos numeros"""
    try:
        n1 = float(n1)
        n2 = float(n2)

    except ValueError:
        raise ValueError("Esos no son numeros!")


    if n1 < 0:
        n1 = n1 * -1
    
    if n2 < 0:
        n2 = n2 * -1
    
    return n1 + n2



def prueba():
    """Toda la interacción con el usuario va acá"""

    numero_1 = input('Ingrese el primer numero: ')
    numero_2 = input('Ingrese el segundo numero: ')
    
    distancia = distancia_numerica(numero_1, numero_2)
    
    print(distancia)


if __name__ == "__main__":
    prueba()

