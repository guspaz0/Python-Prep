## Funciones
#%%
#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

def es_primo(x):
    es_primo = True
    for n in range(2, x):
        if (x % n == 0):
            es_primo = False
            break
    return es_primo

es_primo(7)
#%%
#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

def es_primo(x):
    es_primo = True
    for n in range(2, x):
        if (x % n == 0):
            es_primo = False
            break
    return es_primo

y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_primos = []

def crea_lista_primos(lista_valores):
    for elemento in lista_valores:
        if es_primo(elemento):
            lista_primos.append(elemento)

crea_lista_primos(y)         
print(lista_primos)

#%%
#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
lista = [1,1,1,3,4,6,8,8,9,9,8,8,8]

def valor_modal(n):
    if len(n) == 0:
        return None
    lista_unicos = []
    lista_repetidos = []
    for i in n:
        if i in lista_unicos:
            lista_repetidos.append(i)
        else:
            lista_unicos.append(i)
    cantidad_repetidos = []
    for i in lista_unicos:
        cantidad_repetidos.append(lista_repetidos.count(i))
    for i,e in enumerate(lista_unicos):
        if i == cantidad_repetidos.index(max(cantidad_repetidos)):
            print(e, "es la moda y se repite", max(cantidad_repetidos),"veces")

valor_modal(lista)


#%%
#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
lista = [1,1,1,3,4,6,8,8,9,9,8,8,8]

def valor_modal(n, menor):
    if len(n) == 0:
        return None
    lista_unicos = []
    lista_repetidos = []
    for i in n:
        if i in lista_unicos:
            lista_repetidos.append(i)
        else:
            lista_unicos.append(i)
    cantidad_repetidos = []
    for i in lista_unicos:
        cantidad_repetidos.append(lista_repetidos.count(i))
    if not (menor):
        for i,e in enumerate(lista_unicos):
                if i == cantidad_repetidos.index(max(cantidad_repetidos)):
                    print(e, "es la moda y se repite", max(cantidad_repetidos),"veces")
    else:
        for i,e in enumerate(lista_unicos):
                if i == cantidad_repetidos.index(min(cantidad_repetidos)):
                    print(e, "es la menor moda y se repite", min(cantidad_repetidos),"veces")

valor_modal(lista, True)

#%%
#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def convertir_temp(valor, medida_origen, medida_destino):
    if medida_origen == "celsius":
        if medida_destino == "celsius":
            return valor
        elif medida_destino == "farenheit":
            return (valor*9/5)+32
        elif medida_destino == "kelvin":
            return valor+273.15
    if medida_origen == "farenheit":
        if medida_destino == "celsius":
            return (valor/(9/5))-32
        elif medida_destino == "farenheit":
            return valor
        elif medida_destino == "kelvin":
            return (valor/9/5) - 32 + 273.15
    if medida_origen == "kelvin":
        if medida_destino == "celsius":
            return valor - 273.15
        elif medida_destino == "farenheit":
            return ((valor - 273.15)*9/5)+32
        elif medida_destino == "kelvin":
            return valor

    
convertir_temp(21,"farenheit","celsius")


#%%
#6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
def convertir_temp(valor, medida_origen, medida_destino):
    if medida_origen == "celsius":
        if medida_destino == "celsius":
            return valor
        elif medida_destino == "farenheit":
            return (valor*9/5)+32
        elif medida_destino == "kelvin":
            return valor+273.15
    if medida_origen == "farenheit":
        if medida_destino == "celsius":
            return (valor/(9/5))-32
        elif medida_destino == "farenheit":
            return valor
        elif medida_destino == "kelvin":
            return (valor/9/5) - 32 + 273.15
    if medida_origen == "kelvin":
        if medida_destino == "celsius":
            return valor - 273.15
        elif medida_destino == "farenheit":
            return ((valor - 273.15)*9/5)+32
        elif medida_destino == "kelvin":
            return valor

medidas = ("farenheit","kelvin","celsius")
valor = 21
for i in range(0,3):
    for j in range(0,3):
        print('conversion de',medidas[i], 'a ',medidas[j],'es:',convertir_temp(valor,medidas[i],medidas[j]))

#%%
#7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo+

def factorial(valor):
    if type(valor) == str:
        return print('el factorial debe ser un numero entero')
    if valor <= 0:
        return print('el factorial debe ser mayor a 0')
    if valor > 1:
        valor = valor * factorial(valor - 1)
    return valor

factorial(4)
                       
# %%
