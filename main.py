# Separar y validar los caracteres de una cadena de texto

def separador_de_caracteres(cadena):
    # Separar por palabras
    return cadena.split()

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

# buscar las palabras ingresadas en los recursos
def load_sustantivo(palabra):
    with open('folder/recursos.txt', 'r', encoding='utf-8') as fid:
        for line in fid:
            data = line.strip().split(':')
            if len(data) == 2:
                categoria, palabras = data
                for db_string in palabras.split(','):
                    if palabra in db_string.strip():
                        print(f"\n✅ Encontré '{palabra}' en: {categoria} \nEntre las palabras: {palabras}")
                        return categoria
    print(f"\n❌ No se encontró la palabra: '{palabra}'")
    return None

# Pedir al usuario una cadena de texto
cadena_escrita = input("\nEscriba una cadena de texto: ")

# Mostrar los caracteres si la cadena es válida
if validar_caracteres(cadena_escrita):
    palabras_separadas = separador_de_caracteres(cadena_escrita)
    print("\n✅ Cadena válida ✅\n La cadena escrita es la siguiente: ", palabras_separadas)
    
    # Verificar cada palabra en el archivo
    for palabra in palabras_separadas:
        load_sustantivo(palabra)
else:
    print("\n❌ La cadena ingresada contiene caracteres no válidos. ❌")
