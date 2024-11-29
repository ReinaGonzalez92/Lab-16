#Index      0          1          2
MyFruit = ["Manzana", "Banana", "Melon", "Banana"]
print(MyFruit)

print(MyFruit[0])
print(MyFruit[1])
print(MyFruit[2])


#Agregar un elemento a la lista (por defecto se agrega al final de la lista)
MyFruit.append("Fresa")
print(MyFruit)
#Modificar un elemento de la lista
MyFruit[2] = "orange"
print (MyFruit)
#Agregar un elemento en la lista en un indice deseado
MyFruit.insert(1,"Patilla")
print (MyFruit)

#.remeve(elemento): Elimina el primer elemento que coincide con el valor
MyFruit.remove("Banana")
print(MyFruit)

#list .pop([i]) elimina el elemento indicado de una lista
MyFruit.pop(0)
print (MyFruit)
""""
Tuplas-> Son inmutables (NO SE PUEDEN MODIFICAR) y van encerradas en ()
"""
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Para acceder a la cadena apple, escriba el siguiente código:
print(myFinalAnswerTuple[0])
#Para acceder a la cadena banana, escriba el siguiente código:
print(myFinalAnswerTuple[1])
#Para acceder a la cadena pineapple, escriba el siguiente código:
print(myFinalAnswerTuple[2])


"""
Diccionario

Es una coleccion ordenada de elementos clave valor 
clave: entero o stirng
valor: cualquier tipo de dato"""

fondosRstart = {
    "Mario" : "Amarillo",
    "Luna" : "Naranja",
    "Jorge" : "Negro",
    "MAtias" : "Blanco"
}
print(fondosRstart)
print(type(fondosRstart))
#traer el fondo de Jorge
print(fondosRstart["Jorge"])
#Agregar un elemento solo creando la clave
fondosRstart["Gustavo"] = "Gris"

print(fondosRstart)






