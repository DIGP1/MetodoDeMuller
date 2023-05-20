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
        #Se realiza la primera iteracion
        ite = 5
        dataX[0],dataX[1],dataX[2],mError = formulainciales.iterar(dataX,fx,x)
        print("Raiz = "+str(dataX[2]))
        print("margen de error = "+str(mError))
        print(dataX[2])


    def iterar(datosX, fx,X):
        #econtrando h1 y h0
        h0= datosX[1] - datosX[0]
        h1= datosX[2] - datosX[1]

        #econtrando Sigmas 0 y 1
        Sigma0=  float(fx.subs(X,datosX[1])) - float(fx.subs(X,datosX[0]))
        Sigma0 /=h0
        Sigma1=  float(fx.subs(X,datosX[2])) - float(fx.subs(X,datosX[1]))
        Sigma1 /=h1

        #encontrando constantes
        a= Sigma1-Sigma0
        a /= h1-h0 

        b= a*h1+Sigma1
        c= fx.subs(X,datosX[2])
        
       #encontrando x3
        if b >=0:
                raiz = b+sqrt(b**2-(4*a*c))
                x3= datosX[2] + -2*c / raiz
                print(raiz)

        else:
                raiz = b-sqrt(b**2-(4*a*c))
                x3= datosX[2] + -2*c / raiz
        #Calculo margen de error
        margenError = x3-datosX[2]
        margenError /= x3
        margenError = abs(margenError)*100
        return datosX[1], datosX[2],x3,margenError
        #print("h0: "+str(h0))
        #print("h1: "+str(h1))
        #print("Sigma0: "+str(Sigma0))
        #print("Sigma1: "+str(Sigma1))
        #print("a: "+str(a))
        #print("b: "+str(b))
        #print("c: "+str(c))
        #print("x3: "+str(x3))
        #print(dataX[2])
        #print(fx.subs(x,dataX[2]))
        #print(fx.subs(x,dataX[1]))
        #print(fx.subs(x,dataX[2]) - fx.subs(x,dataX[1]))

    






            




    