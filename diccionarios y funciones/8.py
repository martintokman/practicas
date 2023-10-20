# Crear una función que reciba una cadena de texto y devuelva un diccionario 
# con la cantidad de palabras de cada longitud (por ejemplo, cuántas palabras de 2 letras hay, cuántas de 3, etc).

def procesar_texto(texto):

    lista_de_palabras = texto.split(" ")
    for palabra in lista_de_palabras:
        nueva_palabra = ""
        for i in range(len(palabra)):
            es_letra = palabra[i]
            if es_letra.isalpha() == True:
                nueva_palabra = nueva_palabra + es_letra
            else:
                continue
        lista.append(nueva_palabra)
    
    # Elimino cualquier item vacío de la lista
    lista.remove("")  
    
    #genero una lista con cada palabra y la cantidad de letras que tiene
    palabras_contadas = []
    
    for palabra in lista:
        
        contador = len(palabra)
        palabras_contadas.append((contador))
    
    # Genero el indice del diccionario
    indice_diccionario = set(palabras_contadas)
    
    # Itero el índice, cuento cuantos hay de cada uno y armo el diccionario de salida
    for indice in indice_diccionario:
        diccionario_de_salida.update({ indice : palabras_contadas.count(indice) })
    
    
    return diccionario_de_salida
        
    
texto = "Ju!an tiene cua%tro pe.lotas de col!or rojo y 2 de color blanco."
lista = []
diccionario_de_salida = {}

diccionario_de_salida = procesar_texto(texto)

# Muestro resultados
for clave, valor in diccionario_de_salida.items():
    print(f"Hay {valor} palabras con {clave} caracter/es")






