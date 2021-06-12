################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def promedio_movil(lista_original, cant_promedio):
    """Funcion para calcular un promedio movil en base a un valor ajustable"""
    
    lista_promediada = []
    cant_promedio = int(cant_promedio)

    for indice in range(0, len(lista_original)):

        if indice < cant_promedio - 1:
            
            lista_promediada.append(lista_original[indice])
        else:

            valor_promediado = 0
            
            for valor in range(indice, (indice - cant_promedio), -1):

                valor_promediado += int(lista_original[valor])

            valor_promediado = valor_promediado / cant_promedio

            lista_promediada.append(valor_promediado)
        
    return lista_promediada


def ingreso_enteros():
    '''Funcion para crear una lista con los ingresos del usuario'''
    
    bucle = True
    lista = []

    while bucle:

        valor = input('Ingrese un valor entero para la lista: ')
        lista.append(valor)

        opcion = input('ingresar otro valor? s/n: ')
            
        if opcion == 'n':
                   
            return lista
    
def prueba():
    """Toda la interacción con el usuario va acá"""

    lista_original = ingreso_enteros()
    cant_promedio = input('Ingrese un valor para promediar: ')

    lista_movil = promedio_movil(lista_original, cant_promedio)

    print('Lista original: ', lista_original)
    print(f'Lista Promediada({cant_promedio}): ', lista_movil)
            
if __name__ == "__main__":
    prueba()

