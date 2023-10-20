
import random

empates = 0
ganados_usuario = 0
ganados_compu = 0
partidos_totales = 0

while True:
    jugada_usuario = input("Ingresa tu jugada: piedra(I), papel(P), tijera(T) o salir(S):")
    jugada_usuario = jugada_usuario.upper()
    
    #si elige "S" termina el juego y muestro resultados
    if jugada_usuario == "S":
        break
    elif jugada_usuario == "I" or jugada_usuario == "T" or jugada_usuario == "P":
        #empieza el juego
        lista_jugadas_compu = ["I", "P", "T"]
        jugada_compu = random.choice(lista_jugadas_compu)
        
        #evalúo las posibilidades y asigno los resultados
        if jugada_usuario == "I" and jugada_compu == "I":
            #empate
            empates += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: Empate!")
            print()

        if jugada_usuario == "I" and jugada_compu == "P":
            #compu
            ganados_compu += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: ganó la compu!")
            print()

        if jugada_usuario == "I" and jugada_compu == "T":
            #usuario
            ganados_usuario += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: ganó el usuario!")
            print()

        if jugada_usuario == "P" and jugada_compu == "I":
            #usuario
            ganados_usuario += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: ganó el usuario!")
            print()

        if jugada_usuario == "P" and jugada_compu == "P":
            #empate
            empates += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: Empate!")
            print()

        if jugada_usuario == "P" and jugada_compu == "T":
            #compu
            ganados_compu += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: ganó la compu!")
            print()

        if jugada_usuario == "T" and jugada_compu == "I":
            #compu
            ganados_compu += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: ganó la compu!")
            print()

        if jugada_usuario == "T" and jugada_compu == "P":
            #usuario
            ganados_usuario += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: ganó el usuario!")
            print()

        if jugada_usuario == "T" and jugada_compu == "T":
            #empate
            empates += 1
            partidos_totales +=1
            print(f"La compu jugó : {jugada_compu}")
            print("Resultado: Empate!")
            print()
      
        continue

    else:
        #jugada no permitida
        print("Jugada no permitida, vuelve a intentar:")
        continue    


print("Fin del juego, estos son los resultados:")
print(f"Partidos totales: {partidos_totales}")
print(f"Empates: {empates}")
print(f"Partidos ganados por el usuario: {ganados_usuario}")
print(f"Partidos ganados por la compu: {ganados_compu}")

#si no se jugó ningún partido no se puede sacar el % de partidos ganados
if partidos_totales > 0:
    porcentaje_ganados_usuario = (ganados_usuario * 100) / partidos_totales
    print(f"Porcentaje de partidos ganados: {porcentaje_ganados_usuario}%")

    






