# Separar y validar los caracteres de una cadena de texto
import re

def separador_de_caracteres(cadena):
    return[caracter for caracter in cadena]

def validar_caracteres(cadena):
    caracteres_validos = re.compile(
        r"^[ a-zñA-ZÑáéíóúüÁÉÍÓÚ0-9.,;:!*\-¿?@#\$%\^&=+\-\'\"()\t]+$"
    )
    return bool(caracteres_validos.match(cadena))

cadena_escrita = input("Escriba una cadena de texto: ")

if validar_caracteres(cadena_escrita):
    caracteres_separados = separador_de_caracteres(cadena_escrita)
    print("✅ La cadena escrita es la siguiente: ", caracteres_separados)
else:
    print("❌ Error. La cadena ingresada contiene caracteres no validos.")
