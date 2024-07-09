# Función para validar caracteres con una gramática
def validar_caracteres(cadena):

    caracteres_validos = [
        'A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 
        'K', 'L', 'M', 'N', 'Ñ', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'Ú', 'V', 'W', 'X', 'Y', 'Z', 'a', 'á', 'b', 'c', 'd', 'e', 'é',
        'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó',
        'p', 'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z', ' ',
        '.', ',', ';', ':', '¿', '?', '!', '-', '(', ')', '\"', '\'', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n', '\t'
    ]

    caracteres_no_validos = []

    # Capturar y mostrar caracteres no válidos
    for caracter in cadena:
        if caracter not in caracteres_validos:
            caracteres_no_validos.append(caracter)
    
    if caracteres_no_validos:
        print(f"\n❗Error❗\n Se encontraron caracteres no válidos: {caracteres_no_validos}")
        return False
    return True

# Buscar las palabras ingresadas en el archivo db.txt
def load_sustantivo(palabra, lista_tokens):
    with open('folder/db.txt', 'r', encoding='utf-8') as fid:
        for line in fid:
            data = line.strip().split(':')
            if len(data) == 2:
                token, palabras = data
                for db_string in palabras.split(','):
                    if palabra.lower() == db_string.strip().lower():
                        print(f"\n✅ Encontré '{palabra}' su token es -> {token}")
                        lista_tokens.append(token)
                        return token
    token = 666
    print(f"\n❌ No encontré la palabra: '{palabra}' se asigno el token: '{token}' para palabras no encontradas")
    lista_tokens.append(str(token))
    return token
