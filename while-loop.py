"""
Ciclo While 
Es una sentencia que repetira un conjunto de instrucciones 
mientras que una condicion sea verdadera

Loop infinito

"""

contador = 1
#Cuando la condicion deja de ser verdadera se rompe el ciclo

while contador < 10:
    print (contador)
    contador +=1
    
    
"""
Pide al usuario que ingrese todos los estudiantes de un curso 
Y al final debes imprimir un saludos para cada uno 

"""
"""estudiantes = []
opcion = input("quiere continuar? Si o No: ")

while opcion != "No":
    #De forma provisional guardamos el estudiante en una variable
    nombre = input("Ingresa un estudiante: ")
    #Llamos la lista para agregarlo
    estudiantes.append(nombre)
    #Vuelvo a preguntar
    opcion = input("quiere continuar? Si o No: ")
print (estudintes)
"""

estudiantes = []
while True:
    #de forma provisional guardamos el estudiante en una variable
    nombre = input("Ingresa un estudiante: ")
    estudiantes.append(nombre)
    
    #Voy a preguntarle al usuario si quiere acabar
    opcion = input("quiere continuar? Si o No: ")
    if opcion == "No":
        break #detendra cualquier ciclo
    print(estudiantes)
for estudiante in estudiantes:
    print ("Hola ", estudiante)