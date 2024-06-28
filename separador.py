# Separador de caracteres
def separador_de_caracteres(cadena):

    caracteres = []
    for caracter in cadena:
        caracteres.append(caracter)
    return caracteres

cadena_escrita = input("Escriba una cadena de texto: ")

separar_caracteres = separador_de_caracteres(cadena_escrita)
print("La cadena escrita es la siguiente: ", separar_caracteres)
