#Ingresar dos numeros enteros positivos entre 3 y 6, ambos inclusive
#luego esos numeros serán las dimensiones de un arreglo bidimensional
#posteriormente, poblar la matriz con numeros reales
#finalmente, muestre:
# - El arreglo poblado
# - La suma por filas
# - El promedio por columnas


import numpy as np 
import random as rand

sw1 = True
while sw1 == True:
  try:    
    filas = int(input("Ingrese numero entero positivo para filas entre 3 y 6:\t"))
    if filas < 3 or filas > 6:
      filas = int(input("Ingrese numero entero positivo para filas entre 3 y 6:\t"))
    columnas = int(input("Ingrese numero entero positivo para columnas entre 3 y 6:\t")) 
    if columnas < 3 or columnas > 6:
      columnas = int(input("Ingrese numero entero positivo para columnas entre 3 y 6:\t"))
    sw1 = False
  except:
      print("Error")

arreglo = np.zeros((filas, columnas), dtype=float)

for a in range(filas): #ingresar reales
  for b in range(columnas):
    arreglo[a][b] = round(rand.random(), 3)

suma_filas = [] #Sumar filas
result1 = 0
for i in range(filas):
  result1 = sum(arreglo[i][:4]) 
  suma_filas.append(result1)


lista_suma_columnas = [] #sumar columnas
suma_columnas = 0
for i in range(columnas):
    
    suma_columnas = sum(arreglo[:, i])
    lista_suma_columnas.append(suma_columnas)
  
print("Arreglo:\n", arreglo, "\n") #Mostrar arreglo
for i in range(len(suma_filas)): #mostrar suma filas
  print("Suma fila ", i , ":",round(suma_filas[i], 3))

for i in range(len(lista_suma_columnas)):
    print("Suma columna: ",i ,":", round(lista_suma_columnas[i], 3))