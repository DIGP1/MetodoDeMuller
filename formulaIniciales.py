from sympy import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class formulainciales:
   
   #se define una funcion para pedir la informacion al usuario
    def pedirInformacion():
         
        x = symbols('x') #se define la variable que vamos a evaluar
        
        dataX = [] #creamos un arreglo que almacenara los puntos x0 x1 x2
        expresion = input('Ingrese el f(x) de la raiz a encontrar:\n')
        fx = sympify(expresion) #pedimos datos de la funcion y usamos la funcion sympify

        for i in range(3):  #definimos un for donde vamos ir agregando al arreglo esos daatos por medio del usuaario
            dataX.append(float(input('Ingrese el X-'+str(i))))
        margenError = float(input('Ingrese el margen de error: \n'))#pedimos el error

        #Se declaran las variables para su posterior uso
        mError = 100
        iteracion = 1
        datosTabla = []
        raiz = 0.0
        valor=0
        #Se empieza a iterar
        while mError> margenError: 
            try:
                 dataX[0],dataX[1],dataX[2],mError,fx = formulainciales.iterar(dataX,fx,x)
                 print("=========================================")
                 print("Raiz en la iteracion "+str(iteracion)+" es: "+str(dataX[2]))
                 print("margen de error = "+str(mError))
                 #print("Con cuantos digitos desea redondear"+str(valor))
                 fila = [iteracion,dataX[1], dataX[2],mError]
                 datosTabla.append(fila)#Se guardan los datos para ser mostrados en la tabla
                 iteracion +=1
                 raiz = dataX[2]
            except:
                 
                mError = margenError-1
                print("El ejercicio no cumple con las condiciones")
        return datosTabla,expresion,raiz
        


        

    def iterar(datosX, fx,X):
        #econtrando h1 y h0
        h0= datosX[1] - datosX[0]
        h1= datosX[2] - datosX[1]
        

     #validar cambio de signo

        
             #econtrando Sigmas 0 y 1
        if(h0!=0 and h1!=0):
                  Sigma0=  fx.subs(X,datosX[1]) - fx.subs(X,datosX[0])
                  Sigma0 /=h0
                  Sigma1=  fx.subs(X,datosX[2]) - fx.subs(X,datosX[1])
                  Sigma1 /=h1
        else:
                 print(ZeroDivisionError)


       
        
        #encontrando constantes
        a= Sigma1-Sigma0
        a /= h1-h0 

        b= a*h1+Sigma1
        c= fx.subs(X,datosX[2])
        
       #encontrando x3
        if b >=0:
             
            
               raiz = b+ math.sqrt(b**2-(4*a*c))
               divi = -2*c / raiz
               x3= round(datosX[2] + divi, 5 )
               

        else:
        
            raiz = b-math.sqrt(b**2+(4*a*c))
            divi = -2*c / raiz
            x3= round(datosX[2] + divi, 5 )


        #Calculo margen de error
        margenError = x3-datosX[2]
        margenError /= x3
        margenError = round(abs(margenError)*100,5)
        return datosX[1], datosX[2],x3,margenError,fx
    
        print("h0: "+str(h0))
        print("h1: "+str(h1))
        print("Sigma0: "+str(Sigma0))
        print("Sigma1: "+str(Sigma1))
        print("a: "+str(a))
        print("b: "+str(b))
        print("c: "+str(c))
        print("x3: "+str(x3))
        print(dataX[2])
        print(fx.subs(x,dataX[2]))
        print(fx.subs(x,dataX[1]))
        print(fx.subs(x,dataX[2]) - fx.subs(x,dataX[1]))

    def presentacionDeInformacion(tabla):
         encabezados =['Iteracion','Raiz anterior','Raiz resultante', 'Margen de error %']

         df = pd.DataFrame(tabla, columns=encabezados)#Se mandan los datos al dataFrame
         print(df)

    def mostrarGrafico(x, fx,raiz):
         #Se definen los valores de x
         
         rango_x = np.linspace(-5,5,100)
         plt.plot([valor for valor in rango_x],[fx.subs(x,valorY) for valorY in rango_x])#Se guardan los datos de x y se evalua la funcion para encontrar "y" y guardarla para graficarla
         plt.plot(raiz, fx.subs(x,raiz), 'ro', label='Raíz encontrada')#Se guarda la posicion de la raiz para ser mostrada en la grafica
         plt.axhline(0, color="Black")
         plt.axvline(0, color="Black")
         plt.xlabel('x')
         plt.ylabel('f(x)')
         plt.title("RAIZ")


         plt.xlim(-20,20)#Se limita los datos que se mostraran en x y "y"
         plt.ylim(-20,20)


         plt.legend()
         plt.grid(True)
         plt.show()#Se muestra la grafica










            




    