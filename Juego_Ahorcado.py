# Esta función se encarga de imprimir cuantas letras tiene la palabra en forma de -
def Generador():
    Palabra: "Azul"
    NumPalabra = 4
    
    for i in range (1, NumPalabra+1):
        if i == NumPalabra:
            print("-")
        else:
            print("-", end = " ")

# Esta función se encarga de comprobar que tu letra ingresada este o no este en la palabra
def actualizar(letra,x1,x2,x3,x4,Vidas):
    Palabra: "Azul"
    NumPalabra = 4
    O = 0
    P = 4
    for i in range(1,NumPalabra + 1):
        if i == 1:
            if letra == "a" or x1 == 1 or letra == "A":
                print("A", end = " ")
                if x1 != 1:
                    O = O + 1
                x1 = 1
            else:
                print("-", end = " ")
        elif i == 2:
            if letra == "z" or x2 == 1:
                print("z", end = " ")
                if x2 != 1:
                    O = O + 1
                x2 = 1
            else:
                print("-", end = " ")
        elif i == 3:
            if letra == "u" or x3 == 1:
                print("u", end = " ")
                if x3 != 1:
                    O = O + 1
                x3 = 1
            else:
                print("-", end = " ")
        elif i == 4:
            if letra == "l" or x4 == 1:
                print("l")
                if x4 != 1:
                    O = O + 1
                x4 = 1
            else:
                print("-")
                
                
    if O == 0:
        Vidas = Vidas - 1
                
    return x1,x2,x3,x4,Vidas
                    
# Aqui es dpnde se lleva todo el juego, aqui se pregunta la letra y te dice si perdiste o ganaste 
def Main():
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    Vidas = 6
    Generador() 
    while True:
        print("numero de vidas", Vidas)
        letra = input("Ingresa: ")
        x1,x2,x3,x4,Vidas = actualizar(letra,x1,x2,x3,x4,Vidas)
        
        if Vidas == 0:
            print("Perdiste")
            break
        elif x1 == 1 and x2 == 1 and x3 == 1 and x4 == 1:
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
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    Vidas = 6
    Generador()
    
    R1 = "a"
    print("numero de vidas", Vidas)
    x1,x2,x3,x4,Vidas = actualizar(R1,x1,x2,x3,x4,Vidas)
    R1 = "l"
    print("numero de vidas", Vidas)
    x1,x2,x3,x4,Vidas = actualizar(R1,x1,x2,x3,x4,Vidas)
    R1 = "z"
    print("numero de vidas", Vidas)
    x1,x2,x3,x4,Vidas = actualizar(R1,x1,x2,x3,x4,Vidas)
    R1 = "q"
    print("numero de vidas", Vidas)
    x1,x2,x3,x4,Vidas = actualizar(R1,x1,x2,x3,x4,Vidas)
    R1 = "x"
    print("numero de vidas", Vidas)
    x1,x2,x3,x4,Vidas = actualizar(R1,x1,x2,x3,x4,Vidas)
    R1 = "u"
    print("numero de vidas", Vidas)
    x1,x2,x3,x4,Vidas = actualizar(R1,x1,x2,x3,x4,Vidas)
    if Vidas == 0:
            print("Perdiste")
    elif x1 == 1 and x2 == 1 and x3 == 1 and x4 == 1:
        print("Ganaste")
    
Main()