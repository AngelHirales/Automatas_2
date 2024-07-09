# importar las funciones de mifuncion.py
from mifuncion import validar_caracteres, load_sustantivo, archivo_tokens

def separador_de_caracteres(cadena):
    # Separar por palabras
    return cadena.split()

# Leer el contenido de un archivo .txt
def leer_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        return file.read()

archivo_de_entrada = 'cadena.txt'

# Leer la cadena desde el archivo
cadena_escrita = leer_archivo(archivo_de_entrada)

lista_tokens = []

# Mostrar los caracteres si la cadena es válida
if validar_caracteres(cadena_escrita):
    palabras_separadas = separador_de_caracteres(cadena_escrita)
    print("\n✅ Cadena válida ✅\n La cadena escrita es la siguiente: ", palabras_separadas)
    
    # Verificar cada palabra en el archivo
    for palabra in palabras_separadas:
        load_sustantivo(palabra, lista_tokens)
else:
    print("\n❌ La cadena ingresada contiene caracteres no válidos. ❌")

# Imprimir la lista de tokens
#print(f"\nLista de tokens: {lista_tokens}")

# Especificar el archivo de salida para los tokens
salida_tokens = 'tokens.txt'

# Escribir los tokens en el archivo
archivo_tokens(lista_tokens, salida_tokens)
