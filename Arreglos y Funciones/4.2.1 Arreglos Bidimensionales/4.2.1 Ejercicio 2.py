#Utilice las siguientes funciones en el arreglo creado en el punto 1
#Promedio de los elementos.
#Suma de los elementos.
#Mostrar el elemento mayor.
#Mostrar el elemento menor.
#Mostrar sólo los elementos de la diagonal principal.

import numpy as np
import random as ran

arreglo = np.zeros((3, 3), dtype=int)

for i in range(len(arreglo)):
    for n in range(len(arreglo)):
        arreglo[i, n] = ran.randint(0, 100)

print("Arreglo:\n",arreglo)
print("Promedio de los elementos:\t\t", round(arreglo.mean(), 2))
print("Suma de los elementos:\t\t\t", arreglo.sum())
print("Elemento mayor:\t\t\t\t\t",arreglo.max())
print("Elemento menor:\t\t\t\t\t",arreglo.min())
print("Elementos diagonal principal:\t",arreglo.diagonal())