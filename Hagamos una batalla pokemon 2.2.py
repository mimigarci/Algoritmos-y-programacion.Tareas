#28/01/24
#Hagamos una batalla pokemon utilizando diccionarios
#Autor: Michelle García

#Limpiar la pantalla
import os
os.system('cls')

#Obtener el randomzizador
import random



#Definir las variables principales.

#Puntos de los jugadores. Vida, defensa.
jugador = (100, 100)
oponente = (100, 100)


#Lista con los ataques del jugador.
ataque = ["malicioso", "placaje", "ascuas"]


#Registro de los ataques del jugador.
r_jugador = {"malicioso" : 0, 
            "placaje": 0,
            "ascuas": 0}


#Registro de los ataques del oponente.
r_oponente = {"latigo" : 0, 
            "placaje": 0,
            "pistola de agua": 0}


#Diccionario con los efectos de los ataques.
ataques = {"malicioso": (10, 0),
           "placaje1": (35* (100/oponente[1]), 0),
           "ascuas": (20, 0),
           "latigo" : (10, 10),
           "placaje2": (35* (100/jugador[1]), 0),
           "pistola de agua": (40,0)} 



#Definir los ataques.

def malicioso (vida_o):

    vida_o = vida_o - ataques["malicioso"][0]
    r_jugador["malicioso"] += 1

    return (vida_o, oponente[1])


def placaje1 (vida_o):

    vida_o = vida_o - ataques["placaje1"][0]
    r_jugador["placaje"] += 1

    return (vida_o, oponente[1])


def ascuas (vida_o):

    vida_o = vida_o - ataques["ascuas"][0]
    r_jugador["ascuas"] += 1

    return (vida_o, oponente[1])


def placaje2 (vida_j):

    vida_j = vida_j - ataques["placaje2"][0]
    r_oponente["placaje"] += 1

    return (vida_j, jugador[1])


def latigo (vida_j, def_j):

    vida_j = vida_j - ataques["latigo"][0]
    def_j = def_j - ataques["latigo"][1]
    r_oponente["latigo"] += 1

    return (vida_j, def_j)


def PDA (vida_j):

    vida_j = vida_j - ataques["pistola de agua"][0]
    r_oponente["pistola de agua"] += 1

    return (vida_j, jugador[1])




#Introducción a la batalla.
print ("¿Estás listo para tu primera batalla pokemon? ")

#Primer ataque de la partida.
ataque_jugador = input("\n¿Cuál va a ser tu ataque? ")

#Ciclo para ejecutar la batalla.
while jugador[0] > 0 and oponente[0] > 0:

    #Si el ataque del jugador es malicioso, la vida del oponente disminuirá en 10 y se añadirá 1 a malicioso dentro del registro.
    if ataque_jugador == ataque[0]:
        oponente = malicioso(oponente[0])
        
        print ("A tu oponente le quedan ", oponente, "puntos de vida y defensa")
        print ("A tu pokemon le quedan ", jugador, "puntos de vida y defensa")
    
        #Mientras los puntos de vida del jugador y el oponente sean mayores que 0, continua la batalla.
        if oponente[0] > 0 and jugador[0] > 0:
            ataque_jugador = input("\nSiguiente ataque: ")
        else:
            continue


    #Si el ataque del jugador es placaje, la vida del oponente disminuirá en 35* (100/defensa_oponente) y se añadirá 1 a placaje dentro dal registro.
    elif ataque_jugador == ataque[1]:
        oponente = placaje1(oponente[0])

        print ("A tu oponente le quedan ", oponente, "puntos de vida y defensa")
        print ("A tu pokemon le quedan ", jugador, "puntos de vida y defensa")
        
        #Mientras los puntos de vida del jugador y el oponente sean mayores que 0, continua la batalla.
        if oponente[0] > 0 and jugador[0] > 0:
            ataque_jugador = input("\nSiguiente ataque: ")
        else:
            continue

    #Si el ataque del jugador es ascuas, la vida del oponente disminuirá en 20 y se añadirá 1 a ascuas dentro del registro.
    elif ataque_jugador == ataque[2]:
        oponente = ascuas(oponente[0])

        print ("A tu oponente le quedan ", oponente, "puntos de vida y defensa")
        print ("A tu pokemon le quedan ", jugador, "puntos de vida y defensa")

        #Mientras los puntos de vida del jugador y el oponente sean mayores que 0, continua la batalla.
        if oponente[0] > 0 and jugador[0] > 0:
            ataque_jugador = input("\nSiguiente ataque: ")
        else:
            continue

    #Si el ataque no se encuentra dentro de la lista, se indicará del error al usuario.
    else:
        print ("¡¿Que estas haciendo?! Tus ataques son: malicioso, placaje, y ascuas! \n")

        oponente = oponente
        jugador = jugador

        ataque_jugador = input("Siguiente ataque: ")


    #Turno del oponente

    #El ataque del oponente será igual a un número cualquiera entre el 1 y el 3.
    ataque_oponente= random.randrange(1,3+1)

    #El oponente solo ha de atacar si el ataque introducido por el usuario es válido.
    if ataque_jugador == ataque[0] or ataque_jugador == ataque[1] or ataque_jugador == ataque[2] :
        #Si el ataque del oponente es igual a látigo (1).
        if ataque_oponente == 1: 
            jugador = latigo(jugador[0],jugador[1])

            if jugador[1] <= 0:
                jugador[1] = 1
            else:
                jugador = jugador

        #En caso de que el ataque del jugador sea placaje, su vida disminuirá en un 35* (100/defensa_jugador) 
        elif ataque_jugador == ataque[1]:
            jugador = placaje2(jugador[0])
            
        #Si el ataque del oponente es pistola de agua, el jugador perderá 40 puntos de vida.
        elif ataque_oponente == 3: 
            jugador = PDA(jugador[0])

        #De no ser ninguno de los ataques previos, la vida del jugador no se verá afectada.
        else:
            jugador = jugador


#Si las vida del jugador es mayor que 0 y la vida del oponente es mayor o igual a 0, el jugador habrá ganado y se ha de imprimir el registro de la batalla.
if oponente[0] <= 0 and jugador[0] > 0:

    print ("\nFelicidades, has ganado! \n")

    print ("Tus movimientos fueron: ", r_jugador)
    print ("Los movimientos de tu oponente fueron: ", r_oponente, "\n")

##Si las vida del oponente es mayor que 0 y la vida del oponente es menor o igual a 0, el oponente habrá ganado y se ha de imprimir el registro de la batalla.

elif jugador[0] <= 0 and oponente[0] > 0:

    print ("\nLo siento, has perdido! \n")

    print ("Tus movimientos fueron: ", r_jugador)
    print ("Los movimientos de tu oponente fueron: ", r_oponente, "\n")

#Si las vidas de los jugadores son menores o iguales a 0, se considerará un empate y se ha de imprimir el registro de la batalla.
elif jugador[0] <= 0 and oponente[0] <= 0:

    print ("\nEs un empate! \n") 

    print ("Tus movimientos fueron: ", r_jugador)
    print ("Los movimientos de tu oponente fueron: ", r_oponente, "\n")

#Si las vidas de los participantes no cumplen con las condiciones establecidas, se ha de imprimir su vida y se acabará el juego.
else:
    print ("A tu oponente le quedan ", oponente, "puntos de vida y defensa")
    print ("A tu pokemon le quedan ", jugador, "puntos de vida y defensa")

    quit ()
 