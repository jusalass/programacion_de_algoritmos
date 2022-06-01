def calcular_iva(valor):
    iva = valor * 0.19
    return(round(iva, 2))

def descuento(precio, porcentaje):
    descuento = porcentaje / 100
    total = precio - (precio * descuento)
    return(total)

def calcular_imc(peso, estatura):
    imc = round((peso / (estatura / 100) ** 2), 2)
    print("El IMC es: ", imc)
    if imc < 18.5:
        print("Bajo Peso\n")
    elif imc >= 18.5 and imc <= 24.9:
        print("Adecuado\n")
    elif imc >= 25.0 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Obesidad grado 1")
    elif imc >= 35.0 and imc <= 39.9:
        print("Obesidad grado 2")
    elif imc > 40:
        print("Obesidad grado 2")


sw1 = True

while sw1 == True:
    try:
        opcion = int(input("Ingrese opción:\n1. Calcular IVA\n2. Calcular descuento\n3. Calcular IMC\n4. Salir\nOpcion: "))
        if opcion < 1 or opcion > 4:
            try:
                print("\nIngrese opcion correcta\n")
                opcion = int(input("Ingrese opción:\n1. Calcular IVA\n2. Calcular descuento\n3. Calcular IMC\n4. Salir\nOpcion: "))
            except:
                print("Error\nIngrese opcion correcta")

        if opcion == 1:
            try:
                valor = int(input("Ingrese valor del producto: "))
                print("El iva es:\t", calcular_iva(valor))
            except:
                print("Error\nIngrese valor correcto")
        elif opcion == 2:
                try:
                    precio = int(input("Ingrese precio: "))
                    porcentaje = int(input("Ingrese porcentaje de descuento: "))
                    print("El precio final es:\t", descuento(precio, porcentaje))
                except:
                    print("Error\nIngrese datos correctos")
        elif opcion == 3:
            try:
                peso = float(input("Ingrese peso en kg: "))
                estatura = float(input("Ingrese estatura en cms: "))
                calcular_imc(peso,estatura)
            except:
                print("Error\nIngrese datos correctos")

        elif opcion == 4:
            print("\nAdiós")
            sw1 = False
        else:
            print("Error\nIngrese opcion correcta")
    except:
        print("Error\nIngrese opcion correcta\n")



