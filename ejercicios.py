import numpy as np


lista=[1,2,3,4,5]
arreglo= np.array(lista)
print(arreglo)

#ndim = indica cuantas dimensiones tien el arreglo

print(f"El arreglo es de {arreglo.ndim} dimension")

#Len = Indica el largo del arreglo

print(f"El arrgelo es ed largo {len(arreglo)}")

#slice
#Start:Stop:Step = Indica cuanto quiero mostrar del arreglo
#Star = Indica desde donde vamos a consultar
#Stop = Indica hasta donde vamos a consultar
#Step = Indica de cuanto en cuanto vamos a consultar

print(arreglo[1:5:2])

#Rellenar arreglo
#For
lista2 =[i for i in range(1,11)]
print( lista2)

arreglo2=np.array(lista2)
print(arreglo2)

#arantge(Start,Stop,Step) =Rellena el arreglo con valores segun la indicacion

arreglo3= np.arange(1,11)
print(arreglo3)

#Operaciones 
#Sumar
arreglo3+=5
print(arreglo3)

#Multiplicar

arreglo3*=10
print(arreglo3)

#Comparaciones o operadores relacionales

print(arreglo3>arreglo2)

#Sum() Entrega la suma de los valores del arreglo
print(arreglo3.sum())

#Mean() Entrega el promdeio de los valores del arrgelo

print(arreglo3.mean())

#Min = Muestra el valor mas bajo del arreglo
#Max = Muestra el valor mas alto del arreglo

print(f"Numero mas alto {arreglo3.max()}")
print(f"Numero mas bajo {arreglo3.min()}")