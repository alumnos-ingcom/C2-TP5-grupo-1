################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factoriales_basicos():
    '''Funcion para calcular los factoriales basicos del 1 al 9'''

    diccionario_factoriales = {}

    for numero in range(0,10):

        factor = 1

        for n in range(1, numero + 1):

            factor *= n

        diccionario_factoriales[numero] = factor

    return diccionario_factoriales


def factoriones():
    """Funcion para calcular factoriones"""

    factoriones = []
    diccionario_factores = factoriales_basicos()


    for numero in range(1, 1499999):

        cadena = str(numero)
        suma_factores = 0

        for digito in cadena:

            suma_factores += diccionario_factores[int(digito)]
        
        if suma_factores == numero:

            factoriones.append(numero)
        
        
    return factoriones


def prueba():
    
    lista_factoriones = factoriones()

    print(lista_factoriones)

if __name__ == "__main__":
    prueba()

