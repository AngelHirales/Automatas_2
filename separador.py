# Separar y validar los caracteres de una cadena de texto

def separador_de_caracteres(cadena):
    # Separar los caracteres
    return[caracter for caracter in cadena]

def validar_caracteres(cadena):

    caracteres_validos = [
        'A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 
        'K', 'L', 'M', 'N', 'Ñ', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'Ú', 'V', 'W', 'X', 'Y', 'Z', 'a', 'á', 'b', 'c', 'd', 'e', 'é',
        'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó',
        'p', 'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z', ' ',
        '.', ',', ':', ';', '¿', '?', '!', '-', '(', ')', '\"', '\'', '0',
        '1','2', '3', '4', '5', '6', '7', '8', '9'
    ]

    caracteres_no_validos = []

    # Capturar y mostrar caracteres no validos
    for caracter in cadena:
        if caracter not in caracteres_validos:
            caracteres_no_validos.append(caracter)
    
    if caracteres_no_validos:
        print(f"\n❗Error❗\n Se encontraron caracteres no válidos: {caracteres_no_validos}")
        return False
    return True

# Pedir al usuario una cadena de texto
cadena_escrita = input("\nEscriba una cadena de texto: ")

# Mostrar los caracteres si la cadena es valida
if validar_caracteres(cadena_escrita):
    caracteres_separados = separador_de_caracteres(cadena_escrita)
    print("\n✅Cadena valida✅\n La cadena escrita es la siguiente: ", caracteres_separados)
