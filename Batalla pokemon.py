#Hagamos una batalla pokemon 

#Limpiar la pantalla
import os
os.system('cls')

#Obtener el randomzizador
import random

#Definir las variables
ataque_jugador = input("Ataque: ")
PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100
ataque = ["malicioso", "placaje", "ascuas"]


#Ciclo para ejecutar la batalla.
while PS_jugador > 0 and PS_oponente > 0:

    #Si el ataque del jugador es malicioso, la vida del oponente disminuirá en 10.
    if ataque_jugador == ataque[0]:
        PS_oponente -= 10

        if PS_oponente > 0 and PS_jugador > 0:
            print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
            print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")

            ataque_jugador = input("Siguiente ataque: ")
        else:
            continue

        #Si la defensa del oponente es menor o igual a 0, será igual a 1.
        if defensa_oponente <= 0:
            defensa_oponente = 1
        else:
            defensa_oponente = defensa_oponente

        #Si el ataque del jugador es placaje, la vida del oponente disminuirá en 35* (100/defensa_oponente)
    elif ataque_jugador == ataque[1]:
        PS_oponente -= 35* (100/defensa_oponente)
        
        if PS_oponente > 0 and PS_jugador > 0:
            print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
            print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")

            ataque_jugador = input("Siguiente ataque: ")
            
        else:
            continue

    #Si el ataque del jugador es ascuas, la vida del oponente disminuirá en 20.
    elif ataque_jugador == ataque[2]:
        PS_oponente -= 20

        if PS_oponente > 0 and PS_jugador > 0:
            print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
            print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")
            
            ataque_jugador = input("Siguiente ataque: ")
        else:
            continue

    #Si el ataque no se encuentra dentro de la lista, se indicará del error al usuario y se detendrá el ciclo.
    else:
        print ("Que estas haciendo?! Tus ataques son: malicioso, placaje, y ascuas! ")
        
        ataque_jugador = input("Siguiente ataque: ")


    #Turno del oponente

    #El ataque del oponente será igual a un número cualquiera entre el 1 y el 3.
    ataque_oponente= random.randrange(1,3+1)
    
    #Si el ataque del oponente es igual a látigo (1).
    if ataque_oponente == 1: 
        PS_jugador -= 10 

        #Y la defensa del oponente es menor o igual a 0, la defensa del jugador disminuirá en 10.
        if defensa_oponente >= 0:
            defensa_jugador -= 10

            #Si la defensa del jugador es menor o igual a 0, será igual a 1.
            if defensa_jugador <= 0:
                defensa_jugador = 1
            else:
                defensa_jugador = defensa_jugador

        #En caso de que el ataque del jugador sea placaje, su vida disminuirá en un 35* (100/defensa_jugador) 
    elif ataque_jugador == 2:
        PS_jugador -= 35* (100/defensa_jugador)


    elif ataque_oponente == 3: #Pistola de agua
        PS_jugador -= 40

    else:
        PS_jugador = PS_jugador


#Si las vida del jugador es mayor que 0 y la vida del oponente es mayor o igual a 0, el jugador habrá ganado.
if PS_oponente <= 0 and PS_jugador > 0:
    print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
    print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")

    print ("Felicidades, has ganado! ")

##Si las vida del oponente es mayor que 0 y la vida del oponente es menor o igual a 0, el oponente habrá ganado.

elif PS_jugador <= 0 and PS_oponente > 0:

    print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
    print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")

    print ("Lo siento, has perdido! ") 

#Si las vidas de los jugadores son menores o iguales a 0, se considerará un empate.
elif PS_jugador <= 0 and PS_oponente <= 0:
    print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
    print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")

    print ("Empate") 

else:

   
    print ("A tu oponente le quedan ", PS_oponente, "puntos de vida")
    print ("A tu pokemon le quedan ", PS_jugador, "puntos de vida")
    
    quit ()
 


    



