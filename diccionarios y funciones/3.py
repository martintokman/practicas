# Crear una función que reciba un número entero y devuelva un diccionario con las n primeras potencias de 2.
# Consultar al usuario cual es el valor de n.

def devolver_potencias(n):
    for i in range(n):
        diccionario.update({f"2 ** {i+1}" : 2**(i+1)})
    return diccionario   
      
diccionario = {}
    
n = int(input("Ingresa la cantidad de n: "))
devolver_potencias(n)
print(diccionario)

