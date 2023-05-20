from sympy import *
import pandas as pd
import numpy as np 



def menu():
    print("---------------------Metodo de Muller------------------")
    print("1. Encontrar una raiz")
    print("2. Mostrar Grafica")
    print("3. Salir")

def pedirInformacion():
    x = symbols('x')
    dataX = []
    fx = input('Ingrese el f(x) de la raiz a encontrar:\n')
    expresion = sympify(fx)
    for i in range(3):
        dataX.append(float(input('Ingrese el X'+str(i))))
    margenError = float(input('Ingrese el margen de error: \n'))
    return dataX,expresion, margenError

continuar = True

while continuar:
    menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        pedirInformacion()

    elif opcion == "2":
        print("2")
        
    elif opcion == "3":
        print("Saliendo del programa...")
        continuar = False
        
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

    respuesta = input("¿Deseas hacer algo más? (s/n): ")
    if respuesta.lower() != "s":
        continuar = False