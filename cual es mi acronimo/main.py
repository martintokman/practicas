#¿Cuál es mi acrónimo?

def procesar_texto(entrada):
    lista = entrada.split()
    salida = ""
    for valores in lista:
        salida += valores[0]
    return salida.upper()


entrada = input("Ingrese el nombre completo de una organización y te digo el acrónimo: ")
print(procesar_texto(entrada))