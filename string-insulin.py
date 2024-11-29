preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


#Almacenanos cada secuencia de elementos:

lsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin = 	"rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Imprimir "la secuencia de insulina humana" en la consola usando comandos print() sucesivos:
print ("la secuencia de la preinsulina humana:  ")
print(preproInsulin)

#Imprimir en la consola usando cadenas concatenadas dentro de la función de impresión (de una sola línea):
print("La secuencia de la insulina, cadena es: " + aInsulin)

## Calcularemos los pesos de cada molécula
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

#Cuantas veces aparece una minoacido en la secuencia de insulina:
aminoacidos =  ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']
conteo = {}
for x in aminoacidos:
   #conteo[x] = indulin
   conteo[x] = insulin.count(x.lower())
   
print("Diccionario", conteo)

#EL PESO DE CADA UNO
suma = 0
for x in aminoacidos:
    peso = conteo[x] * aaWeights[x]
    print(f"el peso de la {x} es {peso}")
    suma += peso
print("El valor de la suma es", suma)

