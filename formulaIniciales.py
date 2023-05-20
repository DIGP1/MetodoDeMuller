from sympy import *
import pandas as pd

class formulainciales:
    def pedirInformacion():
        x = symbols('x')
        dataX = []
        fx = input('Ingrese el f(x) de la raiz a encontrar:\n')
        expresion = sympify(fx)
        for i in range(3):
            dataX.append(float(input('Ingrese el X'+str(i))))
        margenError = float(input('Ingrese el margen de error: \n'))
        return dataX,expresion, margenError 
    