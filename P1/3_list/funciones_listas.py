'''
List(ARRAY)
son colecciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valores se hace
con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite  miembros duplicados
'''

paises=["Mexico", "España", "Brasil", "Canada"]
numeros=[23,45,8,24]
varios=["hola", 3.1416, 33, True]

print(paises)
print(numeros)
print(varios)
#Recorrer listas
#1er Metodo
for i in paises:
    print(i)
#2do Metodo
for i in range (0,len(paises)):
    print(paises[i])

#ordenar elementos de una lista, listas de difernetes tipos no pueden ser ordenadas
paises.sort()
print(paises)
numeros.sort()
print(numeros)

#Invertir los elementos ordenados de una lista
paises.reverse()
print(paises)
varios.reverse()
print(varios)

#añdir un elemento a una lista
#1er forma
paises.append("Honduras")
print(paises)

#2da forma 
paises.insert(1,"Honduras")
print(paises)

paises.sort
print(paises)

#Eliminar un elemento de una lista
#1er metodo
paises.pop(5)
print(paises)

#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
print(paises)
print("Brasil" in paises)
resp="Brasil" in paises
print(resp)

#Contar numero de veces que aparece un elemento en una lista
print(numeros)
cant=numeros.count(23)
print(cant)

numeros.append(23)
cant=numeros.count(23)
print(cant)

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
print(paises)
pos=paises.index("Canada")
print(pos)

paises.append("Canada")
print(paises)
pos=paises.index("Canada")
print(pos)

#Unir el contenido de una lista dentro de otra
print(numeros)
numeros2=[100,200]
print(numeros2)

#Crear a partir de la listas de numeros 1 y 2 una resultante y mostrar el contenido ordenado descendentemente 
numeros.extend(numeros2)
print(numeros)
numeros.sort()
numeros.reverse()
print(numeros)

