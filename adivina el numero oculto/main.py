#Adivina el número oculto
import random, sys


intentos = 0

def validar_entrada_usuario(entrada_usuario):
    try:
        if  int(entrada_usuario) <= 50 :
            return entrada_usuario
    
        else:
            entrada_usuario = 200 #Entrada fuera de rango
            return entrada_usuario
    
    except ValueError:
        entrada_usuario = 400 #Entrada no permitida
        return entrada_usuario
       

compu = random.randint(1,10)
print("Acabo de elegir un número entre 1 y 50, ingresa un número y te digo si adivinaste.")

while True:
    entrada_usuario = input("Ingresa un número (0 para salir): ")
    resultado = validar_entrada_usuario(entrada_usuario)
    intentos += 1
    
    if int(resultado) == 0:
        print(f"La compu había elegido el {compu}")
        print(f"Salis del juego antes de adivinar. Hiciste {intentos} intentos.")
        print("Gracias por jugar conmigo :)")
        sys.exit()
    
        
    if int(resultado) == compu:
        print(f"Ganaste!. La compu eligió: {compu}.")
        print(f"Adivinaste en {intentos} intentos.")
        sys.exit()
    
    elif resultado == 200:
        print("Entrada no permitida. Intenta nuevamente con un número entre 1 y 50")
        continue
    
    elif resultado == 400:
        print("Entrada no permitida. No se admiten letras o símbolos")
        continue
    
    
    