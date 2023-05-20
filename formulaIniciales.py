from sympy import *
import pandas as pd

class formulainciales:
   
    def pedirInformacion():
         
        x = symbols('x')
        dataX = []
        expresion = input('Ingrese el f(x) de la raiz a encontrar:\n')
        fx = sympify(expresion)
        for i in range(3):
            dataX.append(float(input('Ingrese el X'+str(i))))
        margenError = float(input('Ingrese el margen de error: \n'))
        
        #econtrando h1 y h0
        h0= dataX[1] - dataX[0]
        h1= dataX[2] - dataX[1]

        #econtrando Sigmas 0 y 1
        Sigma0=  float(fx.subs(x,dataX[1])) - float(fx.subs(x,dataX[0]))/h0
        Sigma1=  float(fx.subs(x,dataX[2]))- float(fx.subs(x,dataX[1]))/h1

        #encontrando constantes
        a= Sigma1-Sigma0 /h1-h0

        b= a*h1+Sigma1

        c= fx.subs(x,dataX[2])
        
       #encontrando x3
        if b >=0:
              x3= dataX[2] + -2*c / (b+sqrt(b**2-(4*a*c)))
        else:
              x3= dataX[2] + -2*c / (b-sqrt(b**2-(4*a*c)))

        print("sigma 1",Sigma0)
        pprint(x3)
    






            




    