#Vuelos-Duoc requiere contratar sus servicios de informática para el desarrollo de un proyecto en Python, el cual consiste en la venta de sus pasajes.

#El sistema debe considerar que se encuentran disponibles un total de 42 asientos por avión, ver ejemplo:

                                    #|	1	2	3		4	5	6	|
                                    #|								|
                                    #|	7	8	9		10	11	12	|
                                    #|								|
                                    #|	13	14	15		16	17	18	|
                                    #|								|
                                    #|	19	20	21		22	23	24	|
                                    #|								|
                                    #|	25	26	27		28	29	30	|
                                    #|_____________   ______________|
                                    #|_____________   ______________|
                                    #|	31	32	33		34	35	36	|
                                    #|								|
                                    #|								|
                                    #|	37	38	39		40	41	42	|

#Dentro de las restricciones, se contempla que desde el asiento 31 al 42 son para pasajeros vip.

#Los precios son:
#•	Asiento normal, $78.900
#•	Asiento vip, $240.000.

#El sistema debe permitir al usuario:
#•	Seleccionar un asiento disponible (mostrando los que aún tienen disponibilidad)
#•	Indicar el valor, una vez que el usuario lo acepte.
#Además, solicitar los siguientes datos del usuario:
#•	nombrePasajero
#•	rutPasajero
#•	telefonoPasajero
#•	bancoPasajero
#Se pide implementar el siguiente menú:

#1.	Ver asientos disponibles
#2.	Comprar asiento
#3.	Anular vuelo
#4.	Modificar datos de pasajero
#5.	Salir

#Ver asientos disponibles: Mostrará por pantalla todos los asientos disponibles con su número de asiento y los no disponibles los con una “X”

#|	1	2	3		4	5	6	|
#|								|
#|	7	X	X		10	11	12	|
#|								|
#|	X	X	X		16	X	18	|
#|								|
#|	19	20	21		22	23	24	|
#|								|
#|	25	26	27		X	29	30	|
#|______________________________|
#|______________________________|
#|	X	32	33		34	35	36	|
#|								|
#|								|
#|	X	38	X		40	41	X	|

#Comprar asiento: Solicita los datos del usuario, luego el usuario escoge un asiento, si es usuario de “bancoDuoc” el sistema realiza un 15% de descuento en el total de su pasaje.

#Anular Pasaje: Deja el asiento nuevamente disponible y elimina los datos del usuario.

#Modificar datos de pasajero: Solicita el asiento y Rut (para verificar datos), luego muestra un submenú, en el cual, debe escoger que dato va a modificar, entre ellos se consideran únicamente el nombrePasajero y telefonoPasajero.

#Para realizar la evaluación se recomienda crear arreglo multidimensional y funciones para las opciones del menú


numero_asientos = 42
asiento_normal = 78900
asiento_vip = 240000
descuento_banco_duoc = 0.85

arreglo = [[(1 + i) for i in range(numero_asientos)], #[0] asiento
            ["X" for i in range(numero_asientos)], #[1] Nombre
            ["X" for i in range(numero_asientos)], #[2] RUT
            [0 for i in range(numero_asientos)], #[3] telefono
            ["X" for i in range(numero_asientos)]] #[4] Banco


def ver_asientos():
  print("\n________________________________________________________________")
  print("|",arreglo[0][0],arreglo[0][1],arreglo[0][2],"   ",arreglo[0][3],arreglo[0][4],arreglo[0][5],"|",sep="\t")
  print("|",arreglo[0][6],arreglo[0][7],arreglo[0][8],"   ",arreglo[0][9],arreglo[0][10],arreglo[0][11],"|",sep="\t")
  print("|",arreglo[0][12],arreglo[0][13],arreglo[0][14],"   ",arreglo[0][15],arreglo[0][16],arreglo[0][17],"|",sep="\t")
  print("|",arreglo[0][18],arreglo[0][19],arreglo[0][20],"   ",arreglo[0][21],arreglo[0][22],arreglo[0][23],"|",sep="\t")
  print("|",arreglo[0][24],arreglo[0][25],arreglo[0][26],"   ",arreglo[0][27],arreglo[0][28],arreglo[0][29],"|",sep="\t")
  print("|_______________________________________________________________|")
  print("|                                                               |")
  print("|_______________________________________________________________|")
  print("|",arreglo[0][30],arreglo[0][31],arreglo[0][32],"   ",arreglo[0][33],arreglo[0][34],arreglo[0][35],"|",sep="\t")
  print("|",arreglo[0][36],arreglo[0][37],arreglo[0][38],"   ",arreglo[0][39],arreglo[0][40],arreglo[0][41],"|",sep="\t")
  print("|_______________________________________________________________|")

def comprar_asiento():
  print("Asientos disponibles:")
  ver_asientos()
  try:
    asiento = int(input("\nIngrese numero de asiento:\t"))
    print("Usuarios de BancoDuoc tienen 15% de descuento")
    if asiento > 0 and asiento <= 30 and arreglo[0][asiento - 1] != "X":
        print("EL valor del asiento: ",asiento," es:\t",asiento_normal)
        tipo_asiento = "normal"
    elif asiento > 30 and asiento <= 42 and arreglo[0][asiento - 1] != "X":
        print("EL valor del asiento: ",asiento," es:\t",asiento_vip)
        tipo_asiento = "vip"
    elif asiento < 0 and asiento > 42:   
      print("Ingrese numero correcto.")
    if asiento > 0 and asiento < 43 and arreglo[0][asiento - 1] != "X": 
      comprar = (int(input("¿Desea comprar el pasaje?:\n1. Si\n2. No\nOpción: ")))
      if comprar == 1:
        sw_comprar = True
      elif comprar == 2:
        sw_comprar = False
      else:
        print("Ingrese opción correcta")
      while sw_comprar == True:
        for i in arreglo[0]:
          if i == (asiento) and i != "X":
            arreglo[0][asiento - 1] = "X"

            nombre = str(input("Ingrese nombre completo:\t"))
            nombre = nombre.upper()
            arreglo[1][asiento - 1] = nombre

            rut = str(input("Ingrese RUT:\t\t"))
            arreglo[2][asiento - 1] = rut

            telefono = int(input("Ingrese teléfono:\t"))
            arreglo[3][asiento - 1] = telefono

            banco = str(input("Ingrese banco:\t"))
            arreglo[4][asiento -1] = banco
            banco = banco.upper()
            if banco == "BANCODUOC":
              if tipo_asiento == "normal":
                print("Descuento Banco Duoc 15%")
                print("Total a pagar:\t$", asiento_normal * descuento_banco_duoc)
              elif tipo_asiento == "vip":
                print("Total a pagar:\t$", asiento_vip * descuento_banco_duoc)
            else:
              if tipo_asiento == "normal":
                print("Total a pagar:\t$", asiento_normal)
              elif tipo_asiento == "vip":
                print("Total a pagar:\t$", asiento_vip)

            print("\nAsiento ",asiento," fue reservado con éxito.")
            sw_comprar = False
            break             
          elif i == asiento and i == "X":
            print("El asiento ",asiento," está ocupado.")
            ver_asientos()
            sw_comprar = False
            break  
    elif arreglo[0][asiento - 1] == "X":
      print("El asiento está ocupado, asientos disponibles:")
      ver_asientos()
  except:
    print("ERROR")

def anular_vuelo():
  try:
    asiento_eliminado = int(input("Ingrese asiento reservado:\t"))
    opcion = int(input("¿Desea eliminar la reserva?\n1. Si\n2. No\nOpción: "))
    if opcion == 1:
      if arreglo[0][asiento_eliminado - 1] == "X":
        arreglo[0][asiento_eliminado - 1] = asiento_eliminado 
        arreglo[1][asiento_eliminado - 1] = "X"
        arreglo[2][asiento_eliminado - 1] = "X"
        arreglo[3][asiento_eliminado - 1] = 0
        arreglo[4][asiento_eliminado - 1] = "X"
      else:
        print("El asiento ", asiento_eliminado, "no está reservado\n")
  except:
    print("ERROR")
  
    
def modificar_datos():
  print("Verificación de reserva:")
  try:
    asiento = int(input("Ingrese asiento:\t"))
    rut = str(input("Ingrese RUT:\t\t"))
    for i in arreglo[0]:
      if i == "X":
        control_nombre = True
        break
      else:
        control_nombre = False
    for i in arreglo[2]:
      if i == rut:
        control_rut = True
        break
      else:
        control_rut = False

    if control_nombre == True and control_rut == True:
      print("\nReserva encontrada")      
      opcion = int(input("Elija dato a modificar:\n1. Nombre\n2. Teléfono\nOpción: "))
      if opcion == 1:
        nuevo_nombre = int(input("Ingrese nuevo nombre:\t"))
      
        arreglo[1][asiento - 1] = nuevo_nombre
      elif opcion == 2:
        arreglo[3][asiento - 1] = int(input("Ingrese nuevo teléfono:\t"))
        print("\nUsuario modificado con éxito.")
    elif control_nombre == False:
      print("Nombre no encontrado")
    elif control_rut == False:
      print("RUT no encontrado")
  except:
    print("ERROR")


#menu
sw1 = True
while sw1 == True:
  try:
    opcion = int(input("\nVUELOS DUOC\nIngrese opcion:\n1. Ver asientos disponibles\n2. Comprar asiento\n3. Anular vuelo\n4. Modificar datos de pasajero\n5. Salir\nOpcion: "))
    while opcion < 1 or opcion > 5:
      opcion = int(input("Opcion incorrecta\n\nVUELOS DUOC\nIngrese opcion:\n1. Ver asientos disponibles\n2. Comprar asiento\n3. Anular vuelo\n4. Modificar datos de pasajero\n5. Salir\nOpcion: "))

    if opcion == 1:
      ver_asientos()
    elif opcion == 2:
      comprar_asiento()
    elif opcion == 3:
      anular_vuelo()
    elif opcion == 4:
      modificar_datos()
    elif opcion == 5:
      print("Adios.")
      sw1 = False
  except:
    print("Error")