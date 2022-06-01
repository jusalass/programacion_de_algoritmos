#Cree una lista para almacenar nombres. El proceso se realiza preguntando si desea seguir ingresando.
#Si la respuesta es NO, se detiene el proceso. Luego, elimine el nombre con la menor cantidad de caracteres.

lista = []
sw = True

nombre = str(input("Ingrese nombre: "))
lista.append(nombre)
while sw == True:
    try:
        opcion = int(input("¿Desea ingresar otro nombre?\n1. Si\n2. No\nOpcion: "))
        if opcion == 1:
            nombre = str(input("Ingrese nombre: "))
            lista.append(nombre)
        elif opcion == 2:
            sw = False
    except:
        print("ERROR")

lista.sort(reverse=True)
print(lista)
lista.pop()
lista.sort()
print(lista)
