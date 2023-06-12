# Crear una función que reciba un diccionario con información de películas 
# y su duración y devuelva una lista ordenada por duración, de menor a mayor.

def procesar_lista(lista_peliculas, lista_nombres, lista_duracion):
    for llave, valor in lista_peliculas.items():
        lista_nombres.append(llave)
        lista_duracion.append(valor)
    return lista_nombres, lista_duracion

lista_nombres = []
lista_duracion = []
lista_ordenada = []

lista_peliculas = {
                    "El señor de los anillos" : 265, #Duración indicada en minutos
                    "Resplandor" : 120, 
                    "Ironman" : 75,
                    "Transformers" : 187,
}
 
procesar_lista(lista_peliculas, lista_nombres, lista_duracion)
lista_duracion.sort()
print(lista_duracion)

for i in range(len(lista_duracion)):
    for llave, valor in lista_peliculas.items():
        if lista_duracion[i] == valor:
            lista_ordenada.append(llave)
            
    
print(lista_ordenada)
    
