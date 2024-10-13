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
1.-Primer menu: 1.-Iniciar Sesión 2.-Agregar Usuario 3.-Imprimir Puntuaciones 4.-Función Prueba

2.-Si Agrega usuario pedir Nombre y comprobar si ese nombre no ha sido usado y luego pedir contreña para agregar al usuario

3.-Si Imprimir Puntuaciones: Imprimir el nombre, id y puntuaciones de cada usuario

4.-Si iniciar sesión

5.-Segundo menu: 1.-Jugar 2.-Cambiar Contraseña 3.-Salir
 6.-Si elejio cambiar contraseña, preguntar por la contraseña actual y si esta correcta preguntar por la contraseña nueva y cambiar contraseña

 7.-Si Elejio Salir
 Break

 8-Si elejio Jugar:
9.-crear la lista con los dibujos del ahorcado

10.-crear la lista con las palabras a adivinar

11.-crear variable de numero de intentos

12.-crear una lista que va a servir para indicar cuantas letras tiene la palabra 

13.-crear lista donde se van a poner tus respuestas correctas

14.-crear variable para saber que dibujo debe de imprimir

15.-imprimir:bienvenido al juego y las instrucciones

16.-generar un numero aleatorio para elegir la palabra de la lista

17.-calcular las letras que tiene la palabra con la funcion len

18.-usar un for para imprimir cuantos letras tiene la palabra en la lista indicada

19.-while que inica el juego:
	20.-imprimir el dibujo
 	21.-imrpimir los intentos restantes
  	22.-imprimir la lista con tu respuesta
   	23.-preguntar una letra
    	24.-For para comprobar si la letra esta en la lista
     		25.-si esta imprimir: Si esta
       		26.-poner la letra en la lista de respuesta
	 	27.-comprobar si la lista de respuesta es la misma de la lista de palabra corecta
   			27.-si esta:Imprimir:Ganaste
      		28.-si no esta imprimir:No esta
		29.-comprobar si aun tiene intentos restantes	
  			30.-si ya no tiene imprimir:Se acabo el juego	
     			break
Salidas:

Dibujo del ahorcado

Cuantas letras lleva la palabra

Tu respuesta

Mensaje: Bienvenido al juego

Mensaje:Puntuación

Mensaje:Ganaste

Mensaje:Perdiste

Mensaje:Bienvenido al juego
	
	


