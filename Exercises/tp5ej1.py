################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

from tp4ej1 import IngresoIncorrecto


def comprobar_par_impar(numero):
    try:
        numero = float(numero) / 2
        
    except ValueError as err:
        raise IngresoIncorrecto("No es un número!") from err

    auxiliar = str(numero)
    auxiliar = auxiliar[-1]
    
    if auxiliar == "0":
        return True
    else:
        return False


def prueba():
    numero = input("Ingrese un número para saber si es par(True) o impar(False): ")
    numero = comprobar_par_impar(numero)
    print(numero)
    

if __name__ == "__main__":
    prueba()