
#Crear un arreglo unidimensional con nombre arregloA y de tamaño 100, con elementos aleatorios de números enteros del 0 al 500, luego:
#Mostrar por pantalla sólo los valores que se encuentren en los índices pares del arreglo.
#Mostrar el elemento mayor del arreglo.
#Mostrar el índice (posición) del elemento mayor.
#Mostrar el elemento menor del arreglo.
#Generar la copia de arreglo A y multiplicar por 3 cada elemento. Mostrar resultado.
#Mostrar la suma de los elementos del segundo arreglo.
#Calcular el promedio de los elementos del segundo arreglo.


import numpy as np
import random as ran
a = 0

arregloA = np.zeros(100, dtype= int)

for i in range(len(arregloA)): #Ingresa numeros aleatorios al arreglo
    arregloA[i] = ran.randint(0,500)

impares = np.zeros(50, dtype=int) #Indices impares, crear otro array con la mitad de elementos, impares = 2n+1
for n in range(50):
    impares[n] = arregloA[2 * a +1]
    a += 1

copia = arregloA.copy() #Copia de arregloA
copia *= 3 #Multiplica cada elemento por 3


print("ArregloA:\n",arregloA)
print("\nIndices impares:\n",impares)
print("\nMayor numero del arreglo:\t",arregloA.max())
print("Indice numero mayor:\t\t",np.where(arregloA == arregloA.max())[0][0])
print("Menor numero del arreglo:\t",arregloA.min())
print("\nArreglo multiplicado por tres:\n",copia)
print("\nSuma numeros de copia:\t\t",copia.sum())
print("Promedio numeros de copia\t",copia.mean())

