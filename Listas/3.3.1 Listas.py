#Elementos indexados
a = [12, "Python", 3.1416]
print(a[0]) #12
print(a[1]) #Python
print(a[2]) #3.1416

#Para acceder al ultimo elemento de una lista se usa el indice -1

a = [90, "Python", 3.87]
print(a[-1]) #Resultado 3.87

#Agregar elementos al final de la lista
#El metodo append(), permite agregar elementos al final de la lista

lista = [1, 2]
lista.append(3)
print(lista) #Resultado [1, 2, 3]

#Añadir lista a lista inicial
#El método extend(), permite añadir una lista a una lista inicial

lista = [1, 2]
lista.extend([3, 4])
print(lista) #Resultado [1, 2, 3, 4]

#Insert(index,obj)
#El método insert(), permite añadir un elemento en una posición determinada

lista = [1, 3]
lista.insert(1, 2)
print(lista) #Resultado [1, 2, 3]

#Remove(obj)
#El método remove(), permite recibir como argumento un objeto y lo borra de la lista

lista = [1,2,3]
lista.remove(3)
print(lista) #Resultado [1, 2]

#Pop()
#El método pop(), elimina el último elemnto de la lista

lista = [1, 2, 3]
lista.pop()
print(lista) #resultado [1, 2]

#El metodo pop(posicion), elimina el elemento que se encuentra en la posicion ingresada

lista = [1, 2, 3]
lista.pop(1)
print(lista) #Resultado [1, 3]

#Reverse()
#El método reverse(), permite invertir el orden de la lista

lista = [1, 2, 3]
lista.reverse()
print(lista) #[3, 2, 1]

#Sort()
#El metodo sort(), permite ordenar los elementos de menor a mayor

lista = [3, 2, 1]
lista.sort()
print(lista) #Resultado [1, 2, 3]

#El metodo sort(), tambien permite ordenar los elementos de mayor a menor

lista = [3, 2, 1]
lista.sort(reverse=True)
print(lista) #Resultado [1, 2, 3]

#Iterar listas

lista = [15, 99, 100]
for l in lista:
    print(l)
#Resultado: 15
           #99
           #100

#Tamaño de la lista
#El metodo len(), nos permite saber cuantos elementos existen en una lista

lista = [1, 2, 3, 4]
print(len(lista)) #Resultado 4

#Copiar lista
#El metodo copy(), permite copiar una lista, a diferencia del = esta nueva lista no estara vinculada a la original

lista = [1, 2, 3]
lista_nueva = lista.copy()
print(lista_nueva) #Resultado: [1, 2, 3]

#Eliminar todos los elelentos de una lista
#El metodo clear(), elimina los elementos de una lista

lista = [1, 2, 3]
lista.clear() #Los elementos fueron eliminados

