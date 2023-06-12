# Crear una función que reciba una lista de nombres y un diccionario con su edad y 
# devuelva una lista ordenada por edad, de mayor a menor.

lista_de_edades = []
lista_ordenda = []
lista_de_nombres = ['Martin', 'Juan', 'Pedro', 'Mariana', 'Claudia']
diccionario_de_edades = {
                        'Martin' : 47,
                        'Pedro' :38,
                        'Claudia': 21,
                        'Juan': 58,
                        'Mariana': 74
}


def generar_salida(lista_de_nombres, lista_de_edades, lista_ordenada):
    
    #genero lista ordenada de edades
    for llave, valor in diccionario_de_edades.items():
        lista_de_edades.append(valor)
    
    lista_de_edades.sort()
    

    # Recorro la lista ordenada y genero la salida
    for i in range(len(lista_de_edades)):
        
        for llave, valor in diccionario_de_edades.items():
            
            if valor == lista_de_edades[i]:
                lista_ordenda.append(llave)
    
    return lista_ordenda

print(generar_salida(lista_de_nombres, lista_de_edades, lista_ordenda))