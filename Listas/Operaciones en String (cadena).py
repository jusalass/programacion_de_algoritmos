#Dejar toda la cadena en mayusculas
#El metodo upper() permite dejar toda la cadena solo en mayusculas

cadena = ("Hola Mundo")
cadena.upper()
print(cadena) #Resultado HOLA MUNDO

#Dejar toda la cadena en minusculas
#El metodo lower(), permite dejar toda la cadena en minusculas

cadena = ("HOLA MUNDO")
cadena.lower()
print(cadena) #Resultado: hola mundo

#Encontrar caracteres en cadena
#El metodo find(), permite encontrar caracteres  en una cadena, indicando en que posicion comienza o esta dicho caracter

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
a = cadenaDeTexto.find('quien')
print(a) #Resultado 52
#En caso de no encontrar el caracter el metodo find() devuelve el valor -1

#Reemplazar todas las ocurrencias de un caracter en una cadena
#replace()

cadenaDeTexto = ("Hola Mundo")
a = cadenaDeTexto.replace("o","a") #primero se ingresa el caracter a reemplazar y luego el que lo reemplaza
print(a) #Resultado: Hala Munda
