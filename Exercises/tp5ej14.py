################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def es_capicua(numero):
    numero_referencia = ""

    for indice in range(len(numero), 0, -1):
            numero_referencia += numero[indice - 1]

    if numero_referencia == numero:
        return True
    
    return False


def prueba():
    valor = input("Ingrese un nímero para comprobar si es capicúa: ") 
    valor = es_capicua(valor)
    
    print(valor)



if __name__ == "__main__":
    prueba()