# Crear una función que reciba una lista de diccionarios con información de productos y su precio y 
# devuelva una lista con los nombres de los productos ordenados por precio, de mayor a menor.

lista_completa = [{'Agua' : 250}, 
         {'Soda' : 180}, 
         {'Gaseosa' : 270}, 
         {'Vino en caja' : 210}, 
         {'Vino en botella' : 545}, 
         {'Jugo de naranja' : 371}, 
         {'Jugo de limón' : 290},
         {'Agua saborizada': 270}
         ]

lista_de_precios = []
lista_de_salida = []

def procesar_lista(lista_completa):
    # Genero una lista de precios ordenada de mayor a menor
    for item in lista_completa:
        for clave, valor in item.items():
            lista_de_precios.append(valor)

    lista_ordenada = set(lista_de_precios)

    # Elimino los elementos duplicados
    lista_ordenada = list(lista_ordenada)
    lista_ordenada.sort(reverse=True)

    # Recorro la lista completa y genero la lista de productos 
    for precio_lista_ordenada in lista_ordenada:
        
        # Para cada valor de la lista ordenada busco el precio 
        for precio_lista_completa in lista_completa:
            
            # Para cada valor de la lista completa busco el precio en el diccionario
            for clave, valor in precio_lista_completa.items():
                
                # Si los dos precios son iguales agrego el producto a la lista de salida
                if valor == precio_lista_ordenada:
                    lista_de_salida.append(clave)
    
    return lista_de_salida    

# Proceso la lista completa
lista_de_salida = procesar_lista(lista_completa)

# Muestro los resultados
print("Productos ordenados de mayor a menor:")
for producto in lista_de_salida:
    print(producto)
            
                

            






    


        
