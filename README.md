# Fantasy of Python
Contexto
Fantazy of Python es un juego de turnos en el que eres un aventurero en una tierra nueva en la que tendras que enfrentarte a
varios enemigos mientras vives tu aventura por esta tierra desconocida, el juego funciona por un sistema de turnos en el que
tienes diferentes acciones que puedes realizar: Atacar, Defender y Subir Defensa, tendras que usar estrategia para poder vencer a los diferentes enemigos que hay
por las tierras de Fantasy of Python.


# Algoritmo del proyecto

Entrada:

1.-Nombre del Jugador

2.-Elegir acción de Combate:Atacar o Defender o Subir Ataque

Proceso:

Crear el objeto del Jugador y darle sus características y sus valores :Vida, Nombre y Defensa.

Crear las funciones del jugador de ataque, defensa y Subir ataque del jugador.

Crear el objeto del enemigo y darle sus características:Vida, Nombre y Defensa.

Crear las funciones del enemigo de ataque, defensa y Subir ataque del jugador.

Crear IA del enemigo, Si tiene menos del 20% de vida defender, Si tiene más del 80% de la vida subir ataque y sino atacar

Crear función de creador de enemigo que le valores a las características dependiendo el tipo de enemigo

Pedir el nombre del jugador

Mientras la vida del jugador sea mayor a 0 :
	curar al jugador
	Función de crear enemigo
	imprimir: es hora de combatir
	Imprimir Valor de vida
	Preguntarle al jugador si quiere combatir, defender o subir ataque
	si elige combatir:
		funcion ataque
	si elige defensa:
		Función defensa
	si elige Subir ataque: 
		Función subir ataque
	imprimir: turno del enemigo
	Funcion IA del enemigo
	imprimir: Que hizo el enemigo

imprimir:has perdido

Salidas:

Preguntar Nombre del jugador
Mensaje: Vida del personaje
Mensaje: SI hay combate
Mensaje: Acción del enemigo
	
	


