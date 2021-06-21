################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

class IngresoIncorrecto(Exception):
    """Excepción para el ingreso incorrecto"""
    pass


def buscador_palabra(texto, palabra):
    """Función para buscar la posicion de una palabra en un texto"""
   
    lista_texto = []
    nueva_palabra = ""
    for c in texto:

        if c != " ":
            nueva_palabra += c  
        else:
            lista_texto.append(nueva_palabra)
            nueva_palabra = ""
        
    try:
        for p in range(0, len(lista_texto)):

            if lista_texto[p] == palabra:
                return p + 1
            
    except ValueError as err:
        raise IngresoIncorrecto("La palabra no existe dentro del texto")


def prueba():
    texto = input("Ingrese un texto: ")
    palabra_a_buscar = input("Ingrese una palabra para buscar dentro del texto: ")
    
    resultado = buscador_palabra(texto, palabra_a_buscar)

    print("Posición ", resultado)



if __name__ == "__main__":
    prueba()