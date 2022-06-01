#Crear una copia del arreglo y muestre:
#Elemento mayor
#Elemento menor
#Suma de los elementos
#Promedio de los elementos
#Mostrar todos los elementos
import numpy as np
import random as rm

arreglo = np.zeros(10, dtype=int)

for i in range(10):
    num = rm.randint(0, 100)
    arreglo[i] = num
copia = arreglo[:].copy()

print("Elemento mayor:\t\t",copia.max())
print("Elemento menor:\t\t",copia.min())
print("Suma:\t\t\t\t",copia.sum())
print("Promedio:\t\t\t",copia.mean())

print(copia)
