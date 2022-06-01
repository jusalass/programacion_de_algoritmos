#Crear un arreglo unidimensional de tamaño 10, con elementos aleatorios de números enteros del 0 al 100,
# para ello deberá investigar la función que permita crear números aleatorios.


import random as rm
import numpy as np

arreglo = np.zeros(10, dtype=int)

for i in range(10):
    num = rm.randint(0, 100)
    arreglo[i] = num

print(arreglo)
