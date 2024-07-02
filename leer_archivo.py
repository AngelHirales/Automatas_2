# Separar y validar los caracteres de una cadena de texto

def separador_de_palabras(cadena):
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
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
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

# Ruta del archivo a leer
ruta_archivo = 'folder/recursos.txt'

def leer_archivo_y_separar_palabras(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"\n❗Error❗\n El archivo en: {ruta_archivo} no existe o la ruta no es correcta")
        return None

# Leer el contenido del archivo
contenido_archivo = leer_archivo_y_separar_palabras(ruta_archivo)

# Validar y separar las palabras si el archivo se leyó correctamente
if contenido_archivo and validar_caracteres(contenido_archivo):
    palabras_separadas = separador_de_palabras(contenido_archivo)
    print("\n✅Archivo válido✅\nEl contenido del archivo es el siguiente: ", palabras_separadas)
else:
    print("\n❌Contenido del archivo inválido.❌")
