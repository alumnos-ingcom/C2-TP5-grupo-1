################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def fibonacci(numero):
    valoruno = 0
    valordos = 1

    for n in range(numero - 1):
        auxiliar = valordos
        valordos = valordos + valoruno
        valoruno = auxiliar
        
    return valordos


def prueba():
    numero = input('Ingrese el término límite de la sucesión de Fibonacci: ')
    numero = int(numero)
    numero = fibonacci(numero)
    print(numero)


if __name__ == "__main__":
    prueba()