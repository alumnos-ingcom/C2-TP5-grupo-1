################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertidor_binario(cadena):
    """Funcion para convertir a binario
"""

    cadena = int(cadena)
    salida = []

    while cadena > 1:

        resultado = str(cadena / 2)
        posicion_flotante = resultado.find('.')

        resto = int(resultado[posicion_flotante+1:])
        resultado = int(resultado[0: posicion_flotante])
        
        cadena = resultado
        
        if resto > 0:

            salida.append(1)
        else:

            salida.append(0)

    
    salida.append(1)

    s_invertida = ''

    for indice in range(len(salida)-1, -1, -1):

        s_invertida += str(salida[indice])
    
    return s_invertida


def convertidor_decimal(binario):
    """Funcion para convertir a decimal
"""

    largo_binario = len(binario)- 1
    numero = 0

    for digito in binario:

        digito = int(digito)
        numero += digito * 2**largo_binario

        largo_binario -= 1



    return numero


def prueba():
   
    bucle = True

    while bucle:

        opcion = input("1) Convertir a binario 2) Convertir a decimal 3) salir ")

        if opcion == "1":
            numero = input("Ingrese un numero a convertir ")
            numero = convertidor_binario(numero)
            print(numero)

        if opcion == "2":          
            binario = input("Ingrese un binario a convertir ")
            binario = convertidor_decimal(binario)
            print(binario)

        if opcion == "3":
            bucle = False
    numero = input("Ingrese numero a convertir: ")

if __name__ == "__main__":
    prueba()

