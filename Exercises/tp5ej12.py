################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

class IngresoIncorrecto(Exception):
    """Excepción para el ingreso incorrecto"""
    pass


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
    """Función que crea la lista que quiera generar el usuario"""
    
    lista = []
    bucle = True

    while bucle:

        ingreso = input(f"Ingrese un valor entero para la lista {n_lista}: ")
        lista.append(ingreso)

        limite = input("¿Desea ingresar otro valor? (si/no): ")
            
        if limite == "no":       
            return lista
        elif limite == "si":       
            pass
        else:
            raise IngresoIncorrecto("Debe responder 'si' o 'no'")


def prueba():
    primer_lista = ingreso_valor('1')
    segunda_lista = ingreso_valor('2')
    
    resultado = comparador_listas(primer_lista, segunda_lista)
    print(resultado)
       
       
if __name__ == "__main__":
    prueba()