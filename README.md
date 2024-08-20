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

crear la lista con los dibujos del ahorcado

crear la lista con las palabras a adivinar

crear variable de numero de intentos

crear una lista que va a servir para indicar cuantas letras tiene la palabra 

crear lista donde se van a poner tus respuestas correctas

crear variable para saber que dibujo debe de imprimir

imprimir:bienvenido al juego y las instrucciones

generar un numero aleatorio para elegir la palabra de la lista

calcular las letras que tiene la palabra con la funcion len

usar un for para imprimir cuantos letras tiene la palabra en la lista indicada

while que inica el juego:
	imprimir el dibujo
 	imrpimir los intentos restantes
  	imprimir la lista con tu respuesta
   	preguntar una letra
    	For para comprobar si la letra esta en la lista
     		si esta imprimir: Si esta
       		poner la letra en la lista de respuesta
	 	comprobar si la lista de respuesta es la misma de la lista de palabra corecta
   			si esta:Imprimir:Ganaste
      		si no esta imprimir:No esta
		comprobar si aun tiene intentos restantes	
  			si ya no tiene imprimir:Se acabo el juego	
     			break
Salidas:

Dibujo del ahorcado

Cuantas letras lleva la palabra

Tu respuesta

Mensaje:Ganaste

Mensaje:Perdiste

Mensaje:Bienvenido al juego
	
	


