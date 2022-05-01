#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
#%%
ciudades = ['santiago del estero','cordoba', 'Tucuman', 'Salta', 'buenos aires']

#2) Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])

#3) Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])

#4) Visualizar el tipo de dato de la lista
type(ciudades)

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(ciudades[2:])

#6) Visualizar los primeros 4 elementos de la lista
print(ciudades[:3])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append('Jujuy')
ciudades.append('cordoba')

#8) Agregar otra ciudad, pero en la cuarta posición
ciudades.insert(4,'Mendoza')

#9) Concatenar otra lista a la ya creada
provincias = ['San Juan','San Luis','Catamarca']
ciudades.extend(provincias)

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada ¿Se nota alguna particularidad?
ciudades.index('cordoba')
#'devuelve el indice del primer elemento que encuentra'.

#11) ¿Qué pasa si se busca un elemento que no existe?
#'devuelve error

#12) Eliminar un elemento de la lista
ciudades.remove('cordoba')

#13) ¿Qué pasa si el elemento a eliminar no existe?
#devuelve error porque no esta en la lista

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ultimo = ciudades.pop()
print(ultimo)

#15) Mostrar la lista multiplicada por 4
print(ciudades * 4)

#16) Crear una tupla que contenga los números enteros del 1 al 20
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(tupla)

#17) Imprimir desde el índice 10 al 15 de la tupla

#18) Evaluar si los números 20 y 30 están dentro de la tupla

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

#21) Convertir la tupla en una lista

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

#24) Imprimir las claves del diccionario

#25) Imprimir las ciudades a través de su clave

# %%
