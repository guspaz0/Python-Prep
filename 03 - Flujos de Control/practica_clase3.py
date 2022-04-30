# In[1]:
#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

x = -1
if(x < 0):
    print('x es menor a 0')
elif(x > 0):
    print('x es mayor a 0')
else:
    print('x es igual a 0')

# In[2]:
#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

a = 1
b = '2'
if(type(a) == type(b)):
    print('a y b son del mismo tipo')
else:
    print('a y b son de distinto tipo')

# In[3]:
#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

i = 1
while (i <= 20):
    if (i % 2 == 0):
        print(f'[{i} es par')
    else:
        print(f'{i} es impar')
    i = i + 1

# In[4]:
#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i2 in range(0 , 5):
    print(i2 ** 3)

# In[5]:
#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

n = 6
for n in range(0,n):
    pass
    print(f'este es el ciclo n°{n} de 5')

# In[6]:
#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

nro = 6
factorial = 1
if (type(nro) == int):
    if (nro > 0):
        while(nro > 1):
            factorial = factorial * (nro -1)
            nro = nro - 1
        print(f'el factorial es {factorial}')
    else:
        print('la variable a factorizar debe ser un entero mayor a 0')
else:
    print('la variable a factorizar debe ser un entero mayor a 0')

# In[7]:
#7) Crear un ciclo for dentro de un ciclo while
n2 = 10
while(n2 == 10):
    for n2 in range(1 , n2):
        print(n2)
    print('se llegó a la condicion while')

# In[8]:
#8) Crear un ciclo while dentro de un ciclo for

n = 10
for n in range(1 , n):
    while(n == 5):
        print(n,'es la cond. while')
        break

#%%
#9) Imprimir los números primos existentes entre 0 y 30

import time
inicio = time.time()

tope_rango = 30
n = 0
primo = True
while (n < 30):
    for div in range(2 , n):
        if(n % div == 0):
            primo = False
    if primo:
        print(n, 'es primo')
    else:
        primo= True
        print(n, 'no es primo')
    n += 1

fin = time.time()
print(fin-inicio)          
    
#%%
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

tope_rango = 30
n = 0
primo = True
while (n < 30):
    for div in range(2 , n):
        if(n % div == 0):
            primo = False
            break
    if primo:
        print(n, 'es primo')
    else:
        primo= True
        print(n,'no es primo')
    n += 1

#%%
#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

import time
inicio = time.time()

tope_rango = 120
n = 0
primo = True
while (n < 120):
    for div in range(2 , n):
        if(n % div == 0):
            primo = False
            break
    if primo:
        print(n, 'es primo')
    else:
        primo= True
        print(n,'no es primo')
    n += 1

fin = time.time()
print(fin-inicio)

#%%
#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

no, porque aumenta la cantidad de entrada de datos

#%%
#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

tope = 201
i = 100
div = 12
while(tope > i):
    if(i % div == 0):
        print(i, 'es divisible por', div)
        continue
    i += 1
    print('fin de ciclo', i)

#%%
#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

#%%
#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# %%