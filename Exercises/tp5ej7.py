################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertidor_float(numero):
    """Funcion para convertir a float y o lanzar una excepcion
"""

    try:
            return float(numero)

    except ValueError:
        raise ValueError("Esos no son numeros!")

def distancia_numerica(n1, n2):
    """Funcion calcular distancia entre dos numeros
"""
    
    if n1 < 0:
        n1 = n1 * -1
    
    if n2 < 0:
        n2 = n2 * -1
    
    return n1 + n2

def prueba():
   
    numero_1 = input('Ingrese el primer numero: ')
    numero_2 = input('Ingrese el segundo numero: ')
    
    numero_1 = convertidor_float(numero_1)
    numero_2 = convertidor_float(numero_2)

    distancia = distancia_numerica(numero_1, numero_2)
    
    print(distancia)


if __name__ == "__main__":
    prueba()

