# Crear una función que reciba una lista de diccionarios con información de empleados 
# y devuelva una lista ordenada de los apellidos.

lista = [{"Nombre" : "Martin", "Apellido" : "Tokman"}, 
         {"Nombre" : "Nuria", "Apellido" : "Calmo"},
         {"Nombre" : "Jorge", "Apellido" : "Zafiro"},
         {"Nombre" : "Miguel", "Apellido" : "Pepe"},
         {"Nombre" : "Carla", "Apellido" : "Calderon"},
         {"Nombre" : "Claudia", "Apellido" : "Mini"},
         {"Nombre" : "Antonio", "Apellido" : "Gonzalez"}
         ]

lista_apellidos = []

for i in range(len(lista)):
    lista_apellidos.append(lista[i].get("Apellido"))
    
lista_apellidos.sort()
print(lista_apellidos)

