#Crear un programa que le pregunte al usuario un número entre el 1 y 1000, además, el programa lanzará un número al azar dentro de ese rango
#y si ambos números son los mismos, el usuario ganará el Sorteo, de lo contrario, perderá.
import random


print("¡----Si desea detener el programa, presione 0.----!")
print("")

#Creamos un ciclo While para que el usuario pueda intentar todas las veces que desee.
while True:
    n = int(input("Ingrese un número entre el 1 y el 1000: ")) #Creamos una variable de tipo integer en la cual almacenamos un número que el usuario ingrese.
    winner = random.choice(range(1,1000)) #Creamos otra variable en la que el programa eligirá un número random entre el 1 y 1000, el cual será el ganador.

    if(n==winner):print(f"El número ganador es {winner} ¡Felicidades!") #Establecemos una condición en la que si n es igual al número ganador, el usuario será felicitado.
    elif(n==0): exit()  #Dejamos esta opción para que el usuario pueda parar el programa.
    else: print(f"El número ganador es {winner} ¡Suerte la próxima!")