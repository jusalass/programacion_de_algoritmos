
#Crear un arreglo unidimensional con nombre arreglo_1 y de tamaño 10, con elementos aleatorios de números enteros del 0 al 1000, luego:
#Mostrar por pantalla todos los elementos del arreglo.
#Contar los elementos pares.
#Sumar los elementos impares.
#Emitir mensaje de cada elemento que sea primo.

import numpy as np
import random as ran

arreglo_1 = np.zeros(10, dtype=int)

for i in range(len(arreglo_1)): #Ingresar elementos aleatorios al arreglo
    arreglo_1[i] = ran.randint(0,1000)

cont_pares = 0
suma_impares = 0
primo = 0

print("Elementos del arreglo:\n",arreglo_1,"\n")
for i in range(len(arreglo_1)):

    if arreglo_1[i] % 2 == 0: #Contar elementos pares
        cont_pares += 1
    elif arreglo_1[i] % 2 == 1: #Sumar elementos impares
        suma_impares += arreglo_1[i]
    for i in range(arreglo_1[i]+1): #Comprobar si es primo
        if i % 2 == 0:
             primo += 1
        if primo == 2:
            print("El numero ", arreglo_1[i], "es primo")




print("\nNumero de elementos pares:\t",cont_pares)
print("Suma de elementos impares:\t",suma_impares)
