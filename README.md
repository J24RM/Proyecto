# Ahorcado Python
Contexto
El ahorcado es un juego en el que el jugador tiene que adivinar una palabra puesta por el dueño del juego y el jugador tiene una 
cierta cantidad de intentos para poder adivinar antes que la persona ahorcada se dibuje por completo, el jugador puede escribir una letra
para haci ir poco a poco descubriendo la palabra a adivinar o adivinarla toda de una, pero si la palabra o letra introducida es incorrecta
se va a dibujar una persona colgada en un poste poco a poco hasta que se dibujo por completo y pierdas el juego.


# Algoritmo del proyecto

Entrada:

Respuesta del Jugador

Proceso:

1.-crear la lista con los dibujos del ahorcado

2.-crear la lista con las palabras a adivinar

3.-crear variable de numero de intentos

4.-crear una lista que va a servir para indicar cuantas letras tiene la palabra 

5.-crear lista donde se van a poner tus respuestas correctas

6.-crear variable para saber que dibujo debe de imprimir

7.-imprimir:bienvenido al juego y las instrucciones

8.-generar un numero aleatorio para elegir la palabra de la lista

9.-calcular las letras que tiene la palabra con la funcion len

10.-usar un for para imprimir cuantos letras tiene la palabra en la lista indicada

11.-while que inica el juego:
	12.-imprimir el dibujo
 	13.-imrpimir los intentos restantes
  	14.-imprimir la lista con tu respuesta
   	15.-preguntar una letra
    	16.-For para comprobar si la letra esta en la lista
     		17.-si esta imprimir: Si esta
       		18.-poner la letra en la lista de respuesta
	 	19.-comprobar si la lista de respuesta es la misma de la lista de palabra corecta
   			20.-si esta:Imprimir:Ganaste
      		21.-si no esta imprimir:No esta
		22.-comprobar si aun tiene intentos restantes	
  			23.-si ya no tiene imprimir:Se acabo el juego	
     			break
Salidas:

Dibujo del ahorcado

Cuantas letras lleva la palabra

Tu respuesta

Mensaje:Ganaste

Mensaje:Perdiste

Mensaje:Bienvenido al juego
	
	


