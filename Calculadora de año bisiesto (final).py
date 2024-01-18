#Calcular el año bisiesto

#Limpia la terminal.
import os
os.system('cls')

count = 1

#Introducir el año a evaluar.
año = int (input ("Introduzca un año entre 1900 y 2199: "))


#Verificar que el año cumpla con los parámetros.
if año >= 1900 and año <= 2199:
    #Si es disivisible entre 4 pasa al próximo condicional.
    if año%4 == 0 :
        #Si es disivisible entre 100 pasa al próximo condicional.
        if año%100 == 0:
            #Si es disivisble entre 4, 100 y 400, es bisiesto.
            if año%400 == 0:
                n = 1
                print ("Es bisiesto.")
            #Si no es divisible entre 400 pero si es divisible entre 100, no es bisiesto.
            else: 
                n = 0
                print("Este año no es bisiesto.")
                quit ()
        #Si no es divisible entre 100 pero es divisible entre 4, es bisiesto.
        else: 
            n = 1
            print ("Es bisiesto.")
    #Si no es divisible entre 4 no es bisiesto.
    else: 
        n = 0 
        print("Este año no es bisiesto.")
        quit ()


#Decision para que solo se ejecute cuando el año sea bisiesto.
    if n == 1:
    #El contador empieza el 1 debido a que el año inicial es bisiesto.
        count = 1
    #Por cada año que sea bisiesto dentro del rango, se le añadirá 1 al contador.
    for año in range (1900, año):
       if año%4 == 0 :
        if año%100 == 0:
            if año%400 == 0:
                count += 1
                #Es bisiesto.
            else: 
                count += 0
                #No es bisiesto.
        else: 
            count += 1
            #Es bisiesto.
    else: 
        count += 0
        #No es bisiesto.


    #Si es bisiesto y el contador es mayor que 1, se imprimirá la cantidad de años bisiestos entre el rango.
    if n == 1 and count > 1 :
        print ("El número de años bisiestos entre 1900 y", año+1, "es: ", count)
    #Si el contador no es mayor que 1, el año no es bisiesto.
    else:
        print("Este año no es bisiesto.")

        
#No entra dentro de los parámetros.
else: 
    print("Este año no está dentro de los parámetros")
