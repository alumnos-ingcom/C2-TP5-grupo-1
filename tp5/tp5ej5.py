################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def inversion_textos(texto):
    """Funcion para invertir las mayusculas por minusculas y viceversa"""

    try:
        texto = str(texto)

    except ValueError:
        raise ValueError('Texto invalido')

    texto_nuevo = ''

    for caracter in texto:

        caracter_comprobador = caracter.upper()

        if caracter == caracter_comprobador:

            texto_nuevo += caracter.lower()
        
        else:
            
            texto_nuevo += caracter.upper()

    return texto_nuevo


def prueba():
    """Toda la interacción con el usuario va acá"""

    texto = input('Ingrese un texto a invertir: ')
    
    print(inversion_textos(texto))


if __name__ == "__main__":
    prueba()