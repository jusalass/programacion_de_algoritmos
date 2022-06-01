#Crear un arreglo de dos dimensiones de tamaño 10 y 4,  el cual, simula a un bus.
#Se pide asignar los números de asiento en forma automática, considerando el siguiente formato:

#1	2		3	4
#5	6		7	8
#9	10		11	12
#13	14		15	16
#17	18		19	20
#21	22		23	24
#25	26		27	28
#29	30		31	32
#33	34		35	36
#37	38		39	40

import numpy as np
arreglo = np.zeros((10, 4), dtype=int)

num = 1
while num < (np.shape(arreglo)[0] * np.shape(arreglo)[1]):
    for a in range(np.shape(arreglo)[0]):
        for b in range(np.shape(arreglo)[1]):
            arreglo[a, b] = num
            num += 1

for i in range(np.shape(arreglo)[0]):
    print(arreglo[i][:2],"   ",arreglo[i][2:])