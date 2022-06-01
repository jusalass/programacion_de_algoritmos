#Ingrese numeros enteros a una lista. Al ingresar el cero se detiene
#Debe mostrar los elementos de {esta en forma ordenada ascendente

lista = []
flag = True
while flag == True:
    try:
        num = int(input("Ingrese un numero entero: "))
        if num == 0:
            flag = False
        else:
            lista.append(num)
    except:
        print("ERROR\n")

lista.sort()
print(lista)