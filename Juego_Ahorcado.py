import random
# Esta función se encarga de imprimir cuantas letras tiene la palabra en forma de -
def Generador():
  Nivel1 = ["Azul","Rojo","Verde"]
  Nivel2 = []
  Nivel3 = []

  Respuesta = []
  CorrectoComparar = []

  Pelejida = random.randint(0,len(Nivel1)-1)
  for i in range (len(Nivel1[Pelejida])):
    Respuesta.append("-")
  for j in range (len(Nivel1[Pelejida])):
    CorrectoComparar.append(Nivel1[Pelejida][j])

  return Nivel1[Pelejida],Respuesta,CorrectoComparar

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
    Vidas = 6
    VidasD = 0
    Correcto,Respuesta,CorrectoComparar = Generador()
    while True:
        Dibujo(VidasD)
        print(Respuesta)
        print("numero de vidas", Vidas)
        letra = input("Ingresa: ")
        Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto)

        if Vidas == 0:
            print("Perdiste")
            break
        elif CorrectoComparar == Respuesta:
            print("Ganaste")
            break


"""
Input 1: a
Respuesta: a---
Vidas:6

Input 2: l
Respuesta: a--l
Vidas:6

Input 3: z
Respuesta: az-l
Vidas:6

Input 4: q
Respuesta: az-l
Vidas:5

Input 5: x
Respuesta: az-l
Vidas:4

Input 6: u
Respuesta: azul
Vidas:4
Ganaste
"""
def Prueba():

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

    letra = "u"
    Vidas,VidasD,Respuesta = actualizar(letra,Vidas,VidasD,Respuesta,Correcto) 
    Dibujo(VidasD)
    print(Respuesta)
    print("numero de vidas", Vidas)

    if Vidas == 0:
      print("Perdiste")
    elif CorrectoComparar == Respuesta:
      print("Ganaste")

Main()
