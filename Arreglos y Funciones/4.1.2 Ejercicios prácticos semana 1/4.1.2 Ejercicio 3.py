
#Crear dos arreglos unidimensionales con nombre A y B y de tamaño 10, con elementos aleatorios de números enteros del 0 al 300, luego:
#Mostrar por pantalla la suma de los elementos de cada arreglo.
#Mostrar por pantalla la suma de los elementos de ambos arreglos.
#Mostrar por pantalla la tabla de multiplicar de los elementos impares del arreglo B.

import numpy as np
import random as ran

A = np.zeros(10, dtype=int)
B = np.zeros(10, dtype=int)

for i in range(len(A)):
    A[i] = ran.randint(0,300)
    B[i] = ran.randint(0,300)
print("Arreglo A:\t", A, "\nArreglo B:\t", B)
print("Suma de elementos de cada arreglo:\nSuma de A:\t", A.sum(), "\nSuma de B:\t",B.sum())
print("Suma de los elementos de ambos arreglos:\t",A.sum() + B.sum())

for i in range(len(B)):
    if i % 2 != 0:
        print("\nTabla del indice ",i, ", número ",B[i],":")
        for n in range(1,11):
            print(B[i]," X ",n," = ",n * B[i])


