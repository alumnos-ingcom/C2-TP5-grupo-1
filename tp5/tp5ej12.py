################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comparador_listas(primer_lista, segunda_lista):
    """Funcion para comparar la igualdad de elementos en distintas listas"""
    
    temp_primer_lista = primer_lista.copy()
    temp_segunda_lista = segunda_lista.copy()

    for elemento in primer_lista:

        for s_elemento in segunda_lista:

            if s_elemento == elemento:

                temp_primer_lista.remove(elemento)
                temp_segunda_lista.remove(elemento)
                pass

        
    if len(temp_primer_lista) == 0 and len(temp_segunda_lista) == 0:

        return True

    else:

        return False

def ingreso_valor(n_lista):
    '''Funcion para crear una lista con los ingresos del usuario'''
    
    lista = []

    for indice in range(0, 2):

        bucle = True

        while bucle:

            valor = input(f'Ingrese un valor a la lista {n_lista}: ')
            
            lista.append(valor)

            opcion = input('ingresar otro valor? s/n: ')
                
            if opcion == 'n':
                
                return lista

def prueba():
    """Toda la interacción con el usuario va acá"""

    primer_lista = ingreso_valor('1')
    segunda_lista = ingreso_valor('2')
    
    print(comparador_listas(primer_lista, segunda_lista))
            
if __name__ == "__main__":
    prueba()

