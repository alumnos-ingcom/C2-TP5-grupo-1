################
# Tomas Grossi - @Ladrusca 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificador(texto, cant_rotacion):
    """Funcion para codificar por rotacion"""
    
    salida = ''
    cant_rotacion = int(cant_rotacion)

    for letra in texto:
        letra_unicode = ord(letra)
        salida += chr(letra_unicode * cant_rotacion)

    return salida

def decodificador(codigo, cant_rotacion):
    """Funcion para codificar por rotacion"""
    
    salida = ''
    cant_rotacion = int(cant_rotacion)

    for caracter in codigo:
        letra_unicode = ord(caracter)
        letra_unicode = letra_unicode / cant_rotacion
        salida += chr(int(letra_unicode))

    return salida

def prueba():
    """Toda la interacción con el usuario va acá"""

    bucle = True

    while bucle:

        opcion = input("1) Codificar 2) decodificar 3) salir ")

        if opcion == "1":
            texto = input("Ingrese un texto a codificar ")
            cant_rotacion = input("Ingrese cuantas veces debe rotar ")
            texto = codificador(texto, cant_rotacion)
            print(texto)

        if opcion == "2":          
            texto = input("Ingrese un texto a decodificar ")
            cant_rotacion = input("Ingrese la cantidad de rotacion ")
            texto = decodificador(texto, cant_rotacion)
            print(texto)

        if opcion == "3":
            bucle = False

if __name__ == "__main__":
    prueba()

