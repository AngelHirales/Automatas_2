# Función para validar caracteres con una gramática
def validar_caracteres(cadena):
    caracteres_validos = [
        'a', 'á', 'b', 'c', 'd', 'e', 'é',
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
            # hacer un split a partir de :
            data = line.strip().split(':')
            token = data[0]
            palabras = data[1]
            # hacer un split a partir de una ,
            for db_string in palabras.split(','):
                if palabra == db_string.strip().lower():
                    print(f"\n✅ Encontré '{palabra}' su token es -> {token}")
                    lista_tokens.append(token)
                    return token
    token = 666
    print(f"\n❌ A la palabra: '{palabra}' se asigno el token: '{token}' para palabras no encontradas")
    # agregar cada token a la lista
    lista_tokens.append(token)
    return token

# Escribir los tokens en un archivo
def archivo_tokens(lista_tokens, salida_tokens):
    with open(salida_tokens, 'w', encoding='utf-8') as file:
        for token in lista_tokens:
            file.write(f"{token},\n")
