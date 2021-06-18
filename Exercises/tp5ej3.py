################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def tribonacci(numero):
    valoruno = 1
    valordos = 1
    valortres = 1

    for n in range(numero - 1):
        auxiliar = valoruno + valordos+ valortres
        
        valoruno = valordos
        valordos = valortres
        valortres = auxiliar
        
    return valortres


def prueba():
    numero = input("Ingrese el término límite de la sucesión Tribonacci: ")
    numero = int(numero)
    numero = tribonacci(numero)
    print(numero)


if __name__ == "__main__":
    prueba()