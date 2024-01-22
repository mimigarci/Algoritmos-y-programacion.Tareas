# Año bisiesto (Solo ciclos)
# Autor: Michelle Garcia
# Fecha: 21/01/2024

#Limpiar el programa
import os
os.system('cls')

#Crear un ciclo que revise cada año entre 1900 y 2199.
for año in range (1900, 2199):
    #Condicional que defina si cumple con los parámetros para ser bisiesto.
    #Si es disivisible entre 4 pasa al próximo condicional.
    if año%4 == 0:

        #Si es disivisible entre 100 pasa al próximo condicional.
        if año%100 == 0: 

            #Si es disivisible entre 400 pasa al próximo condicional.
            if año%400 == 0:
                print ("\n", año, "Es bisiesto.")

            #Si no es divisible entre 400 pero si es divisible entre 100, no es bisiesto.
            else:
                print ("\n", año, "No es bisiesto.")   

        #Si no es divisible entre 100 pero es divisible entre 4, es bisiesto.    
        else:
            print ("\n", año, "Es bisiesto.")
    
    #Si no es divisible entre 4 no es bisiesto.
    else:
        print ("\n", año, "No es bisiesto.")
    
