#Es palíndromo

def dar_vuelta(entrada_usuario):  
    
    return entrada_usuario[::-1]
        

lista_entradas = []
otra_lista = []
lista_palindromos = []
total_palindromos = 0

print("Ingresa 5 palabras y te digo cuáles son palíndromos.")

#Creo una lista con las palabras del usuario y otra con los reversos
for i in range (5):
    entrada_usuario = input(f"Ingresa la palabra {i+1}: ")
    lista_entradas.append(entrada_usuario)
    otra_lista.append(dar_vuelta(entrada_usuario))
    
#Itero las dos listas y comparo resultados, creo nueva lista con los palíndromos
for i in range(len(lista_entradas)):
    if lista_entradas[i] == otra_lista[i]:
        lista_palindromos.append(lista_entradas[i])
        total_palindromos += 1

#Imprimo resultados
if total_palindromos > 0:
    print(f"Hay {total_palindromos} en total.")
    print("Estos son los palíndromos: ", end="")
    for valor in lista_palindromos:
        print(valor, end=" ") 
else:
    print("Lo siento. Ningún palíndromo en la lista")      
