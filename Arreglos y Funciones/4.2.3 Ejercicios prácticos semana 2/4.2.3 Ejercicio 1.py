#Crear dos arreglos de dos dimensiones de tamaño 3 x 3, con elementos de tipo numérico entero, luego:
#Muestra la matriz 1.
#Muestra la matriz 2.
#Muestre la matriz resultante de la multiplicación de la matriz 1 y matriz 2.

import numpy as np
import random as ran

matriz1 = np.zeros((3, 3), dtype=int)
matriz2 = matriz1.copy()


for i in range(len(matriz1)):
    for n in range(len(matriz1)):
        matriz1[i, n] = ran.randint(0, 10)

for i in range(len(matriz2)):
    for n in range(len(matriz2)):
        matriz2[i, n] = ran.randint(0, 10)


print("Matriz 1:\n",matriz1)
print("Matriz 2:\n",matriz2)
print("Multiplicacion de matrices:\n", matriz1 * matriz2)