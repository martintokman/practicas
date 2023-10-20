Juego de piedra, papel o tijera:

Vamos a jugar contra la computadora. Primero se pide al usuario que indique si va a jugar piedra(I), papel(P) o tijera(T).
Una vez que el usuario hizo su jugada la aplicación elige la suya al azar y se muestra el resultado. 

El juego termina cuando el usuario indica (S) para salir. 

Al finalizar el juego se Se muestran los números de ganados y perdidos por cada jugador junto con el % de juegos ganados
y un mensaje de felicitaciones.

Posibilidades: 

	
	| USUARIO | COMPU |  RESULTADO  |
	|---------|-------|-------------|
	|    I	  |   I   |    EMPATE   |	
	|    I    |   P   |    COMPU    |
	|    I    |   T   |   USUARIO   | 
	|    P	  |   I   |   USUARIO   |
	|    P    |   P   |    EMPATE   |
	|    P    |   T   |    COMPU    |
	|    T	  |   I   |    COMPU    |
	|    T    |   P   |   USUARIO   |
	|    T    |   T   |   EMPATE    |




*******************************************************************************************************************
                                                  PSEUDOCÓDIGO
*******************************************************************************************************************

abro bucle infinito (inicio_juego)
    pido al usuario que ingrese su jugada
    convierto la jugada a mayúscula
    el usuario jugó "S"?
        salgo del bucle infinito (inicio_juego)
    el usuario jugó "I", "P" o "T"?
        #empieza el juego
        juega la compu: genero un random de "I", "P" o "T"

        la jugada del usuario = "I" y la jugada de la compu = "I"?
            se declara empate
            agrego 1 a partidos totales
            muestro la jugada de la compu
            muestro el resultado

        la jugada del usuario = "I" y la jugada de la compu = "P"?
            se declara ganador a la compu
            agrego 1 a partidos totales
            muestro la jugada de la compu
            muestro el resultado

        agrego el resto de las condiciones y resultados que faltan a partir de la siguiente tabla
		
		---------------------------------
        | USUARIO | COMPU |  RESULTADO  |
        |---------|-------|-------------|
        |    I    |   I   |    EMPATE   |   
        |    I    |   P   |    COMPU    |
        |    I    |   T   |   USUARIO   | 
        |    P    |   I   |   USUARIO   |
        |    P    |   P   |    EMPATE   |
        |    P    |   T   |    COMPU    |
        |    T    |   I   |    COMPU    |
        |    T    |   P   |   USUARIO   |
        |    T    |   T   |   EMPATE    |
        ---------------------------------
		
		...

        vuelve al inicio del bucle infinito (inicio_juego) para un nuevo juego

    else:
        muestro "Jugada no permitida"
        vuelve al inicio del bucle infinito (inicio_juego) para un nuevo juego

muestro mensaje "Fin del juego"
muestro el total de partidos jugados
muestro la cantidad de empates
muestro la cantidad de partidos ganados por el usuario
muestro la cantidad de partidos ganados por la compu

se jugó por lo menos 1 partido?
    genero el % de partidos ganados por el usuario
    muestro el valor de % partidos ganados por el usuario

