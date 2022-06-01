#Cree 2 listas, en las cuales se guardarán 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos).
# El sistema deberá mostrar de forma ordenada los nombres y apellidos.

lista_nombre = []
lista_apellido = []
count = 1
index = 0

while len(lista_nombre) < 3:
    print("Ingrese nombre numero ",count)
    nombre = str(input("Nombre: "))
    lista_nombre.append(nombre)
    print("Ingrese apellido numero",count)
    apellido = str(input("Apellido: "))
    lista_apellido.append(apellido)
    count += 1

for i in range(len(lista_nombre)):
    print((index + 1),": ",lista_nombre[index]," ",lista_apellido[index])
    index +=1
