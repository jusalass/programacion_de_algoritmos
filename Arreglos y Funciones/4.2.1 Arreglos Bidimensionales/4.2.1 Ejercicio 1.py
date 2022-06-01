#Crear un arreglo de dos dimensiones de tamaño 3 x 3, con elementos aleatorios de números enteros del 0 al 100.

import numpy as np
import random as ran

arreglo = np.zeros((3, 3), dtype=int)

for i in range(len(arreglo)):
    for n in range(len(arreglo)):
        arreglo[i, n] = ran.randint(0, 100)

print(np.shape(arreglo))
