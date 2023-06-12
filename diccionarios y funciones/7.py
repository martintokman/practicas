# Crear una función que reciba dos listas y devuelva un diccionario con las 
# claves de la primera y los valores de la segunda.

def generar_salida(lista_uno, lista_dos, diccionario_de_salida):

    for i in range(len(lista_uno)):
        diccionario_de_salida.update({ lista_uno[i] : lista_dos[i] })

    return diccionario_de_salida


lista_uno = ['Nombre', 'Apellido', 'Edad', 'Estado civil']
lista_dos = ['Juan', 'Pereira', 38, 'Casado']
diccionario_de_salida = {}

print(generar_salida(lista_uno, lista_dos, diccionario_de_salida))

