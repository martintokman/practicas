# Crear una función que reciba un diccionario con nombres y edades y 
# devuelva un nuevo diccionario con los nombres de las personas mayores de edad.

diccionario_de_entrada = {
                            'Martin' : 47,
                            'Laura' : 28,
                            'Emilio' : 14,
                            'Juana' : 61,
                            'Miguel' : 59,
                            'Carla': 8,
                            'Julio': 82
}

diccionario_de_salida = {}
lista_de_edades = []

# Recorro el diccionario, si la edad es > 18 lo agrego al diccionario de salida
for nombre, edad in diccionario_de_entrada.items():
    if edad > 18:
        diccionario_de_salida.update({ nombre : edad })

# Muestro el resultado
print("Lista de nombres mayores de edad:")
print("--------------------------------")
for nombre in diccionario_de_salida.keys():
    print(nombre)
    

    

