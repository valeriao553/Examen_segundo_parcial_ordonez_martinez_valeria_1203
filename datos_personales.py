print(" ")
print("Ordonez Martinez Valeria 3W 1203")
print(" ")
dic = dict() #Crear diccionario
print(dic) #Imprimir el diccionario
nombre = input("Introducir su nombre: ") #Solicitar que se introdusca el nombre
dic.setdefault("Nombre", nombre) #Asignar valor a la variable del nombre
print(" ")
edad = int(input("Ingrese su edad: ")) #Solicitar que se introdusca la edad
dic.setdefault("Edad", edad) #Asignar  valor a la variable de edad
print(" ")
direccion = input("Introducir su dirección: ") #Solicitar que se introdusca la direccion
dic.setdefault("Dirección", direccion) #Asignar valor a la direccion
print (" ")
telefono = input("Ingrese su número de teléfono: ") #Solicitar que se ingrese el numero de telefono
dic.setdefault("Teléfono", telefono) #Asignar valor a el telefono
print(" ")
#Imprimir el mensaje y usar f-string para mostrar la información del diccionario
print(f"{dic['Nombre']} tiene {dic['Edad']} años, vive en {dic['Dirección']} y su número de teléfono es {dic['Teléfono']}.")
print (" ")