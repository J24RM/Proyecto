import random
# Esta función se encarga de imprimir cuantas letras tiene la palabra en forma de -
def Generador():
  Nivel1 = ["dinosaurio","tec","iphone","caña","edificio","parangaricutirimícuaro","llaves","elefante","Jesus","programacion","azul"]

  Respuesta = []
  CorrectoComparar = []

  Pelejida = random.randint(0,len(Nivel1)-1)
  for i in range (len(Nivel1[Pelejida])):
    Respuesta.append("-")
  for j in range (len(Nivel1[Pelejida])):
    CorrectoComparar.append(Nivel1[Pelejida][j])

  return Nivel1[Pelejida],Respuesta,CorrectoComparar

# Esta función se encarga de guardar un nuevo usuario en el archivo
def agregar_usuario(nombre,contrasena):
  file = open("usuarios.txt","a+")
  file.seek(0)
  lineas = file.readlines()
  ultimoNumero = lineas[-4]
  ultimoNumero = ultimoNumero.replace("\n","")
  ultimoNumero = int(ultimoNumero)
  ultimoNumero += 1
  ultimoNumero = str(ultimoNumero)
  file.writelines("\n"+ultimoNumero+"\n")
  file.writelines(nombre+"\n")
  file.writelines(contrasena+"\n")
  file.writelines("0")
  file.close()
  print("Tu Id es:", ultimoNumero)

#Esta función comprueba que el nombre ingresado para crear un usuario nuevo no este repetido
def buscar_nombre(nombre):
  file = open("usuarios.txt","r")
  tamano = file.readlines()
  dbuscar = len(tamano) / 4
  dbuscar = int(dbuscar)
  file.seek(0)
  o = 0
  x= 0
  for i in range(0,dbuscar):
    com = str(tamano[i+o+1])
    com = com.replace("\n","")
    if nombre == com:
      x = 1
      file.close()
      return x
    else:
      o = o + 3
  file.close()
  return x

#Esta función busca que un usuario por su id para poder iniciar sesión
def buscar_usario(id):
  file = open("usuarios.txt","r")
  tamano = file.readlines()
  idbuscar = len(tamano) / 4
  idbuscar = int(idbuscar)
  file.seek(0)
  o = 0
  size = len(tamano)
  for i in range(0,idbuscar):
    com = str(tamano[i+o])
    com = com.replace("\n","")
    if id == com:
      nombre = tamano[i+o+1]
      nombre = nombre.replace("\n","")
      print("Bienvenido " + nombre)
      contrasena = tamano[i+o+2]
      contrasena = contrasena.replace("\n","")
      puntuacion = tamano[i+o+3]
      puntuacion = puntuacion.replace("\n","")
      print("Su puntuación es: " + puntuacion)
      file.close()
      return nombre, contrasena, puntuacion,size
    else:
      o = o + 3
  file.close()

#Esta función cambia la puntuación del usuario que inicio sesión
def cambiar_puntuacion(id,puntuacion):
  file = open("usuarios.txt","r+")
  file.seek(0)
  tamano = file.readlines()
  file.close()
  id = int(id)
  lugar = id * 4
  id = str(id)
  tamano[lugar-1] = puntuacion
  file = open("usuarios.txt","w+")
  file.seek(0)
  file.writelines(tamano)
  file.close()

# Esta función cambia la contraseña del usuario que inicio sesión
def cambiar_contrasena(id,contrasena):
  file = open("usuarios.txt","r+")
  file.seek(0)
  tamano = file.readlines()
  file.close()
  id = int(id)
  lugar = id * 4
  id = str(id)
  lugar = lugar - 1
  tamano[lugar-1] = contrasena
  file = open("usuarios.txt","w+")
  file.seek(0)
  file.writelines(tamano)
  file.close()

# Esta función imprime el id, nombre y puntuación de cada usuario
def imprimir_puntuaciones():
  print("#ID_____Nombre_____Puntación")
  file = open("usuarios.txt","r")
  file.seek(0)
  tamano = file.readlines()
  file.close()
  tamL = len(tamano)/4
  tamL = int(tamL)
  lugarr = 0
  while tamL > 0:
    tamL = tamL - 1
    print("#ID:",tamano[lugarr] + "Nombre:",tamano[lugarr+1] + "Puntuación:",tamano[lugarr+3])
    lugarr = lugarr + 4
# Esta función se encarga de comprobar que tu letra ingresada este o no este en la palabra
def actualizar(letra,Vidas,VidasD,Respuesta,Correcto):
  QuitarVida = 0
  for i in range (len(Correcto)):
    if letra == Correcto[i]:
      Respuesta[i] = letra
      QuitarVida = 1
  if QuitarVida == 0:
    Vidas = Vidas - 1
    VidasD = VidasD + 1
  return Vidas,VidasD,Respuesta

# Esta función se encarga de imprimir el ahorcado
def Dibujo(VidaD):
  Dibuj=["""
   +---+
   |   |

       |

       |

       |

       |

========= """ , """

   +---+

   |   |

   O   |

       |

       |

       |

========= """ , """
   +---+

   |   |

   O   |

   |   |

       |

       |

========= """ , """
   +---+

   |   |

   O   |

  /|   |

       |

       |

========= """ , """
   +---+

   |   |

   O   |

  /|\  |

       |

       |

========= """ , """
   +---+

   |   |

   O   |

  /|\  |

  /    |

       |
========= """ , """
   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

========= """]

  print(Dibuj[VidaD])
# Aqui es dpnde se lleva todo el juego, aqui se pregunta la letra y te dice si perdiste o ganaste
def Main():
    print("Bienvenido a Hangman")
    while True:
      file = open("usuarios.txt","r")
      ta = file.readlines()
      file.close()
      tam = len(ta) 
      tam = tam / 4
      Ini = int(input("1.-Iniciar Sesión 2.-Agregar Usuario 3.-Puntuaciones 4.-Función Prueba"))
      if Ini == 1:
        id = input("Ingrese su ID: ")
        id = int(id)
        if id > tam:
          print("ID no registrado")
        else:
          id = str(id)
          nombre,contrasena,puntuacion,size = buscar_usario(id)
          size = int(size)
          size = size / 4
          size = int(size)
          size = size
          contra = str(input("Ingrese su contraseña: "))
          nombre = str(nombre)
          puntuacion = int(puntuacion)
          if contra == contrasena:
            print("Bienvenido")
            break
          else:
            print("Contraseña incorrecta")
      if Ini == 2:
        nombre = str(input("Ingrese su nombre: "))
        x = buscar_nombre(nombre)
        if x == 1:
          print("Nombre ya registrado")
        else:
          contrasena = str(input("Ingrese su contraseña: "))
          agregar_usuario(nombre,contrasena)
          print("Usuario agregado")
      if Ini == 3:
        imprimir_puntuaciones()
      if Ini == 4:
        Prueba()
    while True:
      Ina = int(input("1.-Iniciar Juego 2.-Cambiar Contraseña 3.-Salir"))
      if Ina == 1:
        print("Iniciando el Juego")
        perdiste = 0
        vidas = 0
        while perdiste == 0:
          Vidas = 6
          VidasD = 0
          Correcto,Respuesta,CorrectoComparar = Generador()
          while True:
              Dibujo(VidasD)
              print(Respuesta)
              print("numero de vidas", Vidas)
              letra = input("Ingresa: ")
              letra = letra.lower()
              Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
              if Vidas == 0:
                  Dibujo(VidasD)
                  print("Perdiste")
                  perdiste = 1
                  break
              elif CorrectoComparar == Respuesta:
                  print(Respuesta)
                  puntuacion = int(puntuacion)
                  puntuacion = puntuacion + 500
                  puntuacion = str(puntuacion)
                  print("Ganaste")
                  break
        puntuacion = str(puntuacion)
        id = int(id)
        if size == id:
          id = str(id)
          cambiar_puntuacion(id,puntuacion)
          print("Su nueva puntuación es:", puntuacion)
        else:
          cambiar_puntuacion(id,puntuacion+"\n")
          print("Su nueva puntuación es:", puntuacion)
      if Ina == 2:
        contra = str(input("Ingrese su contraseña: "))
        if contra == contrasena:
          contrasena = str(input("Ingrese su nueva contraseña: "))
          cambiar_contrasena(id,contrasena+"\n")
          print("Contraseña cambiada")
        else:
          print("Contraseña incorrecta")
      if Ina == 3:
        print("Saliendo")
        break


"""
Input 1: 1
Respuesta: Ingresa el Id
Input 2: 1
Respuesta: Bienvenido Jesús
Respuesta: Ingrese su contraseña
Input 3:2006
Respuesta: Contraseña correcta
Respuesta: 1.-Inicar Juego 2.-Cambiar Contraseña 3.-Salir
Input 4: 1
Respuesta: Iniciando el Juego
Respuesta: ----
numero de vidas 6

Input 5: a
Respuesta: a---
Vidas:6

Input 6: l
Respuesta: a--l
Vidas:6

Input 7: z
Respuesta: az-l
Vidas:6

Input 8: q
Respuesta: az-l
Vidas:5

Input 9: x
Respuesta: az-l
Vidas:4

Input 10: o
Respuesta: az-l
Vidas:3

Input 11: p
Respuesta: az-l
Vidas:2

Input 12: y
Respuesta: az-l
Vidas:1


Perdiste
Puntuación 1000
"""
def Prueba():
    print("1.-Iniciar Sesión 2.-Agregar Usuario 3.-Puntuaciones 4.-Función Prueba")
    id = 1
    id = str(id)
    nombre,contrasena,puntuacion,size = buscar_usario(id)
    size = int(size)
    size = size / 4
    size = int(size)
    size = size
    contra = 2006
    nombre = str(nombre)
    puntuacion = int(puntuacion)
    if contra == 2006:
        print("Bienvenido")
    print("1.-Inicar Juego 2.-Cambiar Contraseña 3.-Salir")
    Ini = 1
    Vidas = 6
    VidasD = 0

    Correcto = "azul"
    CorrectoComparar = ["a","z","u","l"]
    Respuesta = ["-","-","-","-"]

    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "a"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "l"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "z"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "q"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "x"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "z"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "q"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "z"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "o"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "p"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    letra = "y"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)



    if Vidas == 0:
      print("Perdiste")
      puntuacion = puntuacion + 0
      puntuacion = str(puntuacion)
      print("Su nueva puntuación es:", puntuacion)
    elif CorrectoComparar == Respuesta:
      print("Ganaste")

Main()
