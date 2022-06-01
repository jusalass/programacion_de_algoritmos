#Declarar y poblar un arreglo unidimensional de largo 10 con números enteros positivos, utilizando la función random
# luego ingrese un número e indique si éste se encuentra en el arreglo.

import random as rand
import numpy as np

arreglo = np.zeros(10, dtype=int)

for i in range(len(arreglo)):
    arreglo[i] = rand.randint(0, 500)
print("Arreglo:\n", arreglo)

sw = True
while sw == True:
    try:
        num = int(input("Ingrese un numero entero: "))
        sw = False
    except:
        print("Error")

pertenece = True
while pertenece == True:
    for i in arreglo:
        if i == num:
            print("\nEl número ", num, " se encuentra en el arreglo. ")
            break
        else:
            pertenece = False

if pertenece == False and i != num:
    print("\nEl número ", num, "no se encuentra en el arreglo.")
