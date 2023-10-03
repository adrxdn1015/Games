import random


def adivina_el_numero(x):

    print("============")
    print("Bienvenido(a) al juego :)")
    print("============")

    print("Tu meta es adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1,x) #numero aleatorio

    prediccion = 0

    while prediccion != numero_aleatorio:
        #El usuario ingresa un número
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez, este número es muy pequeño.")

        elif prediccion > numero_aleatorio:
            print("Intenta otra vez, este número es muy grande.")

    print(f"!Felicidades! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(20)