# importar las funciones de mifuncion.py
from mifuncion import validar_caracteres, load_sustantivo, archivo_tokens

def separador_de_caracteres(cadena):
    # Separar por palabras
    return cadena.split()

# Leer el contenido de un archivo .txt
def leer_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        return file.read()

# Especificar el archivo de entrada
archivo_de_entrada = 'cadena.txt'

# Leer la cadena desde el archivo
cadena_escrita = leer_archivo(archivo_de_entrada)
cadena = cadena_escrita.lower()

# Lista para almacenar los tokens
lista_tokens = []

# Mostrar los caracteres si la cadena es válida
if validar_caracteres(cadena):
    palabras_separadas = separador_de_caracteres(cadena)
    
    # Verificar cada palabra en el archivo
    for palabra in palabras_separadas:
        load_sustantivo(palabra, lista_tokens)
else:
    print("\n❌ La cadena ingresada contiene caracteres no válidos. ❌")

# definir archivo de salida para los tokens
salida_tokens = 'tokens.txt'

# Escribir los tokens en el archivo
archivo_tokens(lista_tokens, salida_tokens)
