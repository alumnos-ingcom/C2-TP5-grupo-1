################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

class IngresoIncorrecto(Exception):
    """Excepción para el ingreso incorrecto"""
    pass


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


def ingresos():
    """Función que crea la lista que quiera generar el usuario"""
    
    lista = []
    bucle = True

    while bucle:

        ingreso = input("Ingrese un valor entero para la lista: ")
        lista.append(ingreso)

        limite = input("¿Desea ingresar otro valor? (si/no): ")
            
        if limite == "no":       
            return lista
        elif limite == "si":       
            pass
        else:
            raise IngresoIncorrecto("Debe responder 'si' o 'no'")
                
    
def prueba():
    lista_original = ingresos()
    cant_promedio = input("Ingrese un valor para promediar: ")

    lista_movil = promedio_movil(lista_original, cant_promedio)

    print('Lista original: ', lista_original)
    print(f'Lista Promediada({cant_promedio}): ', lista_movil)
            
if __name__ == "__main__":
    prueba()