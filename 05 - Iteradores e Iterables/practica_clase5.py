#%%
#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

nro_neg = []
n = -15
while(n < 0):
    nro_neg.append(n)
    n +=1
print(nro_neg)

#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
n = 0
while(n < len(nro_neg)):
    if(nro_neg[n] % 2 == 0):
        print(nro_neg[n],'es par')
    n +=1

#3) Resolver el punto anterior sin utilizar un ciclo while

for n in nro_neg[:]:
    if(nro_neg[n] % 2 == 0):
        print(nro_neg[n], 'es par')
    

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
print(nro_neg[0:3])

#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
for i, s in enumerate(nro_neg):
    print(i, s)

#%%
#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: 

lista = [1,2,5,7,8,10,13,14,15,17,20]
ultimo = lista.pop()
lista.append(ultimo)
for i, s in enumerate(lista):
    if ((i) != s and s <= ultimo):
        lista.insert(i, i)
        print(i, 'no esta en la lista, se lo agregó')
print(lista)

#%%
#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: 

n0 = 0
n1 = 1
#ni = (ni - 1) + (ni - 2)

#Crear una lista con los primeros treinta números de la sucesión.

lista = [0,1]
for i,s in enumerate(lista):
    if i <=30:
        ultimo = lista.pop()
        penultimo = lista.pop()
        lista.append(penultimo)
        lista.append(ultimo)  
        lista.append(ultimo + penultimo)
print(lista)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

sum(lista)

#%%
#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
#Donde i es la cantidad total de elementos<br>
#n<sub>i-1</sub> / n<sub>i</sub><br>
#n<sub>i-2</sub> / n<sub>i-1</sub><br>
#n<sub>i-3</sub> / n<sub>i-2</sub><br>
#n<sub>i-4</sub> / n<sub>i-3</sub><br>
#n<sub>i-5</sub> / n<sub>i-4</sub><br>

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309] 
n = 25
while (n <= 30):
    print(lista[(n+1)] / lista[n])
    n += 1

#%%
#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i,s in enumerate(cadena):
    if (s == 'n'):
        print('el caracter', i, 'contiene la letra n')

#%%
#11) Crear un diccionario e imprimir sus claves utilizando un iterador
dic_esp_ing = {'golpear':'punch', 'saltar':'jump','escribir':'write', 'ver':'show', 'escritorio':'Desktop'}

for i in dic_esp_ing:
    print(i)

#%%
#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
iterador = iter(list(cadena))
for i in list(cadena):
    print(next(iterador))

#%%
#13) Crear dos listas y unirlas en una tupla utilizando la función zip

numeros = [1,2,3,4,5]
letras = ['a','b','c','d','e']
num_letras = zip(numeros, letras)
print(list(num_letras))

#%%
#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis7 = []

for i,s in enumerate(lis):
    if (s % 7 == 0):
        lis7.append(s)
print(lis7)

#%%
#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cantidad = 0
for i,s in enumerate(lis):
    if type(s) == list:
        cantidad += len(s)
    else:
        cantidad +=1
print('la cantidad total de elementos es', cantidad)


#%%
#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

for i,s in enumerate(lis):
    if (type(s) != list):
        lis[i]=[s]

print(lis)
# %%
