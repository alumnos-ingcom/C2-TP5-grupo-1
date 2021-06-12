################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comprobador_capicua(numero):
    """Funcion para analizar si un numero entero es capicua"""

    numero_referencia = ''

    for indice in range(len(numero), 0, -1):
            numero_referencia += numero[indice - 1]

    if numero_referencia == numero:
        return True
        
    return False


def prueba():
    """Toda la interacción con el usuario va acá"""

    valor = input('Ingrese un numero para comprobar si es capicua: ') 
    valor = comprobador_capicua(valor)
    
    print(valor)



if __name__ == "__main__":
    prueba()

