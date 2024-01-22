# Programa para hacer una arepa
# Autor: Michelle Garcia
# Fecha: 09/01/2024


#Limpia la pantalla
import os
os.system('cls')


#Introducción al usuario
print ("Hola! Hoy vamos a hacer una arepa \n")

#Preguntar por los ingredientes al usuario
print ("Primero vamos a hacer la masa \n")

agua = float (input ("¿Cuántas tazas de agua vas a utilizar? "))
harina = float (input ("¿Cuántas tazas de harina? "))
sal = float (input ("¿Y las cucharaditas de sal? "))

#Convertir las cucharaditas de sal a su equivalente en taza
sal = sal/3/16

#Crear la mezcla de la arepa
masa = agua + harina + sal

#Imprimir la mezcla de la arepa.
print ("\n Ok, la mezcla está lista. El volumen de la masa es igual a ", masa ,"tazas") 

#Definir el valor del aceite.
aceite = float (input  ("\n Para cocinar la arepa ¿Cuántas cucharadas de aceite deberíamos utilizar? "))
aceite = aceite/16

#Cocinar la arepa
budare = masa + aceite

print ("\n La arepa está lista, ahora su volumen es igual a ", budare) 

#Finaliza el programa.
print ("Ya está lista para ser servida")



print ("\n La arepa está lista, ahora su volumen es igual a ", budare) 

#Finaliza el programa.
print ("Ya está lista para ser servida")

