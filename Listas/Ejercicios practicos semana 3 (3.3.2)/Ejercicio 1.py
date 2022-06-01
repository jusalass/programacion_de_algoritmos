#Ingrese un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10.
#Ejemplo: si ingresa el numero 3, la lista debe contener: 3,6,9,12,15,18,21,27,30

tabla = []
multi = []
num = int(input("Ingrese un numero entero: "))

for i in range(1, 11):
    tabla.append(num * i)


print(tabla)