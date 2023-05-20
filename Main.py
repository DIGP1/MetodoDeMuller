from sympy import *
import pandas as pd
import numpy as np 
from formulaIniciales import *



def menu():
    print("---------------------Metodo de Muller------------------")
    print("1. Encontrar una raiz")
    print("2. Mostrar Grafica")
    print("3. Presentacion de la informacion")
    print("4. Salir")



continuar = True
tabla = []
while continuar:
    menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
       tabla = formulainciales.pedirInformacion()

    elif opcion == "2":
        print("2")
    
    elif opcion == "3":
        formulainciales.presentacionDeInformacion(tabla)

    elif opcion == "4":
        print("Saliendo del programa...")
        continuar = False
        
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
    
    if respuesta.lower() != "s":
        continuar = False
    
    respuesta = input("¿Deseas hacer algo más? (s/n): ")


    #Aasasasa