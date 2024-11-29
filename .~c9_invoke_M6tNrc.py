# Ejercicio 1: Suma de números del 1 al 10


#Ejercicio 2
"""
palabra = (input("ingresa una palabra:  ")).lower()
contador = 0
for i in palabra: # Itera sobre cada letra de la palabra
     if i in ["a", "e", "i", "o", "u"]:# Comprueba si la letra está en la lista de vocales
         contador +=1# Incrementa el contador si es una vocal
print(contador)
    
"""
"""
#Ejercicio 4
lista = [33, 50, 20, 30, 10, 5, 0, 100, 500, 8]
num_mayor = lista [0]
for n in lista:
    if n > num_mayor:
        num_mayor = n
print (num_mayor)
"""
#Ejercicio 5:  Contar hasta que el usuario lo detenga
#Usa un ciclo while para imprimir números empezando desde 1, hasta que el usuario escriba stop.

contador=1 #inicializamos el contador en 1
while True:#ciclo infinito que lo controlaremos desde una condicion interna
    print(f"El numero actual del contador es: {contador}")
    desea_continuar = input("Ingrese YES para continuar o STOP para detener el programa: ").upper()
    if desea_continuar == "STOP":
        print("ciclo terminado")
        break
    elif desea_continuar == "YES":#SI EL USUARIO ESCRIBE yes se incrementa el contador
        contador +=1 #incrementa el contador
    else:
        print("opcion no valida")
    
    
 
 
"""
#Ejercicio 6
import random # importa la libreria de random para generar un nuerero aleatorio
aleatorio = random.randint(1,10) #utilizamos radom.randint para que el programa genere un numero aleatorio
correcto = False #inicializamos el programa con un valor False el cual cambiara al adivinar el numero correcto cambiara a True y rompera el ciclo
                 #False indica que al inicio del programa, el umero no ha sido adivinado
                 # se inicia en False ya que queremos que el programa entre en el bucle while y se continue ejecutando hasta que elija el numero correcto

#utilizamos el bucle While para que el codigo se repita hasta que se cumpla una determinada condicion
while correcto != True: #El bucle continuará ejecutándose mientras la condición correcto != True (o not correcto) sea verdadera.
    numero = int (input("ingrese un numero del 1 al 10: "))
    if numero == aleatorio:
        print (f" el numero correcto es {numero}")
        correcto = True
    else: 
        print("sigue intentando")

#Inicializamos con False para asegurarnos de que el bucle comience y 
#se mantenga activo hasta que el número correcto sea adivinado
"""
"""
#Ejercicio 7
#Pide al usuario un número y determina si es par o impar.
numero = int (input("Ingresa un numero: "))#Solicito al usuario ingresar un numero 
                                            #convierto ese numero a un int (un nuemero entero para poder usarlo con el operador %)
if numero % 2 == 0:
     print("El nuemero es par")
else:
    print("el numero es impar")
    """
"""
#Ejercicio 8: Números hasta N
#Pide al usuario un número N y usa un ciclo for para imprimir todos los números desde 1 hasta N.
n = int(input("Ingrese un numero: ")) #le pedimos al usuario ingresar un numero 
                                    #convertimos ese numero en un int para usarlo mas adelante
for i in range ( 1, n+1):#Ciclo for que se ejecutara en el rango de 1 hasta el numero que ingreso el usuario
    print(i)                #coloco n+1 ya que range no es inclusivo
    
    """
