#Piedra, papel o tijera
import sys
import random

#Declaro las variables globales
lista_jugadas = ["I", "P", "T"]
jugada_usuario = ""
jugada_compu = ""
empates = 0
ganadas_usuario = 0
ganadas_compu = 0
partidos_totales = 0


def validar_jugada(jugada_usuario):
    
    if jugada_usuario in lista_jugadas:
        validar_jugada_resultado = random.choice(lista_jugadas)
        return validar_jugada_resultado
        
    elif jugada_usuario not in lista_jugadas and jugada_usuario == "S":
        validar_jugada_resultado = "S"
        return validar_jugada_resultado
    
    else:
        validar_jugada_resultado = "JNP" #Jugada No Permitida
        return validar_jugada_resultado
    
   
def obtener_ganador(jugada_usuario, jugada_compu):
    jugada_compu = jugada_compu
    jugada_usuario = jugada_usuario
    
    #Evalúo el ganador
    if jugada_usuario == "I" and jugada_compu == "I":
        ganador = "Empate"
        return ganador
        
    elif jugada_usuario == "I" and jugada_compu == "P":
        ganador = "La compu"
        return ganador
        
    elif jugada_usuario == "I" and jugada_compu == "T":
        ganador = "El usuario"
        return ganador
        
    elif jugada_usuario == "P" and jugada_compu == "I":
        ganador = "El usuario"
        return ganador
        
    elif jugada_usuario == "P" and jugada_compu == "P":
        ganador = "Empate"
        return ganador
        
    elif jugada_usuario == "P" and jugada_compu == "T":
        ganador = "La compu"
        return ganador
         
    elif jugada_usuario == "T" and jugada_compu == "I":
        ganador = "La compu"
        return ganador
        
    elif jugada_usuario == "T" and jugada_compu == "P":
        ganador = "El usuario"
        return ganador
        
    elif jugada_usuario == "T" and jugada_compu == "T":
        ganador = "Empate"
        return ganador
        



while True:
    jugada_usuario = input("Indique su jugada:\n Piedra(I), papel(P) o tijera(T): ")
    jugada_usuario = jugada_usuario.upper()
    validar_jugada_resultado = validar_jugada(jugada_usuario) #3 opciones: (I/P/T, S, JNP)
    if validar_jugada_resultado == "S":
        break
    elif validar_jugada_resultado == "JNP":
        print("Jugada no permitida. Intenta con: piedra(I), papel(P) o tijera(T)")
        continue
    else:
        jugada_compu = validar_jugada_resultado
        ganador = obtener_ganador(jugada_usuario , jugada_compu)
        if ganador == "La compu":
            print(f"La compu juega: {jugada_compu}")
            print(f"El ganador es: {ganador}!")
            print("-----------------------------------------------")
            ganadas_compu += 1
            partidos_totales +=1
        elif ganador == "El usuario":
            print(f"La compu juega: {jugada_compu}")
            print(f"El ganador es: {ganador}!")
            print("-----------------------------------------------")
            ganadas_usuario +=1
            partidos_totales +=1
        else:
            print(f"La compu juega: {jugada_compu}")
            print(f"El ganador es: {ganador}!")
            print("-----------------------------------------------")
            empates += 1
            partidos_totales +=1
   
#Terminó el juego. Muestro los resultados
print("Resultados del juego:")
print(f"Ganadas compu: {ganadas_compu}")
print(f"Ganadas usuario: {ganadas_usuario}")
print(f"Empates: {empates}")
print(f"Partidos totales {partidos_totales}")
print(f"% de partidos ganados {int((ganadas_usuario / partidos_totales)*100)}%")