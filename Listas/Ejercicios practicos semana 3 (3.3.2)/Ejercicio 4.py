#Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista
#Luego el sistema debe mostrar por pantalla el nombre que tenga mayor cantidad de caracteres.

lista = []

while (len(lista)) < 3:
    nombre = str(input("Ingrese nombre: "))
    lista.append(nombre)
lista.sort(reverse=True)
print(lista)
print("El nombre mas largo es: ", lista[0])

