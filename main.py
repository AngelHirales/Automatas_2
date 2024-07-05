# Separar y validar los caracteres de una cadena de texto

# importar las funciones de mifuncion.py
from mifuncion import validar_caracteres, load_sustantivo

def separador_de_caracteres(cadena):
    # Separar por palabras
    return cadena.split()

# Leer el contenido de un archivo .txt
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()

# Especificar el archivo de entrada
archivo_de_entrada = 'cadena.txt'

# Leer la cadena desde el archivo
cadena_escrita = leer_archivo(archivo_de_entrada)

# Mostrar los caracteres si la cadena es válida
if validar_caracteres(cadena_escrita):
    palabras_separadas = separador_de_caracteres(cadena_escrita)
    print("\n✅ Cadena válida ✅\n La cadena escrita es la siguiente: ", palabras_separadas)
    
    # Verificar cada palabra en el archivo
    for palabra in palabras_separadas:
        load_sustantivo(palabra)
else:
    print("\n❌ La cadena ingresada contiene caracteres no válidos. ❌")
