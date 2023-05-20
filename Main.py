from sympy import *
import pandas as pd
import numpy as np 



def menu():
    print("---------------------Metodo de Muller------------------")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

continuar = True

while continuar:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("1")
        

    elif opcion == "2":
        print("2")
        

    elif opcion == "3":
        print(" 3")
       

    elif opcion == "4":
        print("Saliendo del programa...")
        continuar = False
        

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

    respuesta = input("¿Deseas hacer algo más? (s/n): ")
    if respuesta.lower() != "s":
        continuar = False