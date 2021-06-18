################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def es_perfecto(numero):
    divisores = []
    suma = 0

    for n in range(1, numero):        
        if numero % n == 0:
            divisores.append(n)
            suma += n

    if numero == suma:
        return True 
    else:
        return False


def prueba():
    numero = input("Ingrese un número para comprobar si es perfecto: ")
    numero = int(numero)
    numero = es_perfecto(numero)
    print(numero)


if __name__ == "__main__":
    prueba()