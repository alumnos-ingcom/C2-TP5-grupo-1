################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def buscador_palabla(texto, palabra):
    """Funcion para buscar la posicion de una palabra en un texto"""

    lista_texto = []
    nueva_palabra = ''

    for c in texto:

        if c != ' ':
            nueva_palabra += c
        
        else:
            lista_texto.append(nueva_palabra)
            nueva_palabra = ''

    for p in range(0, len(lista_texto)):

        if lista_texto[p] == palabra:
            return p + 1

    raise ValueError('La palabra no existe dentro del texto!')

def prueba():
    """Toda la interacción con el usuario va acá"""

    texto = input('Ingrese un texto a analizar: ')
    palabra_a_buscar = input('Ingrese una palabra a buscar: ')
    
    resultado = buscador_palabla(texto, palabra_a_buscar)

    print('Posicion ', resultado)



if __name__ == "__main__":
    prueba()

