#Ingresa 10 numeros a una lista, luego muestre la suma y promedio de los elementos

lista = []
suma = 0
promedio = 0
control = 1
print("Ingrese 10 números")

while control < 11:
    try:
        print("Ingrese numero ",control,":")
        num = float(input("Numero: "))
        lista.append(num)
        control += 1
    except:
        print("ERROR\nIngrese un numero válido\n")


for i in(lista):
    suma += i
promedio = suma / 10

print("\nSuma:\t\t",suma)
print("Promedio:\t",promedio)