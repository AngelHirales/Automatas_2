# Separar y validar los caracteres de una cadena de texto

def separador_de_caracteres(cadena):
    return[caracter for caracter in cadena]

def validar_caracteres(cadena):
    caracteres_extra = " .,;:!*-¿?@#$%^&=+-'/\"()\\t"
    
    for caracter in cadena:
        return bool(caracter.isalnum() or caracter in caracteres_extra)

cadena_escrita = input("Escriba una cadena de texto: ")

if validar_caracteres(cadena_escrita):
    caracteres_separados = separador_de_caracteres(cadena_escrita)
    print("✅ La cadena escrita es la siguiente: ", caracteres_separados)
else:
    print("❌ Error. La cadena ingresada contiene caracteres no validos.")
