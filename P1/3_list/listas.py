import os
os.system("cls")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
lista="["
nums=[1,45,65,34,78,9,100]
for i in nums:
    print(i)

for i in range(0,len(nums)):
   lista+=f"{nums[i]}"
print(f"{lista}")

lista="["
i=0
while i<len(nums):
    lista+=f" {nums[i]}"
    i+=1
print(f"{lista}")
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")
palabras=["hola", "bonjour", "gutentaj", "hello", "ni hao", "bonjour"]
#palabra_busc=input("Dame la palabra a buscar: ")
#1er Forma
'''
if palabra_busc in palabras:
   print("Se encontro")
else:
   print("No se encontro")
os.system("cls")
'''
#2da Forma
encontro=False
veces=0
pos=[]
'''
for i in palabras:
    if i == palabra_busc:
       encontro=True
if encontro:
      print("Se encontro")
else:
        print("No se encontro")
'''
'''
for i in palabras:
    if i == palabra_busc:
       encontro=True
       veces+=1
       pos.append(palabras.index(i))
if encontro:
      print("Se encontro")
else:
        print("No se encontro")
'''
#3er Forma
'''
for i in range(0,len(palabras)):
    if palabras[i]==palabra_busc:
        encontro=True
        pos.append(i)
if encontro:
      print("Se encontro")
else:
        print("No se encontro")
'''

#Ejemplo 3 Añadir elementos a la lista
os.system("cls")
numeros=[]
opc="si"
while opc=="si":
    numeros.append(float(input("Dame un numero cualquiera? ")))
    opc=input("Desea agregar otro numero? (si/no): ").lower()
print(numeros)

#Ejemplo 4 Crear una lista ,multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[["Fernandez", "Gutierrez", "Peña"],[618122345, 6181098888, 6180009999]]
for i in range (0,2):
    for j in range (0,3):
     print(agenda[i][j])

