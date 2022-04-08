from cmath import pi
from unittest.util import strclass


print("1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla")

a = 12
print(a)

print("2) Imprimir el tipo de dato de la constante 8.5")

print(type(8.5))

print("3) Imprimir el tipo de dato de la variable creada en el punto 1")

print(type(a))

print("4) Crear una variable que contenga tu nombre")

mi_nombre = "Gustavo Paz"

print("5) Crear una variable que contenga un número complejo")

n_complejo = 5+5j

print("6) Mostrar el tipo de dato de la variable crada en el punto 5")

print(type(n_complejo))

print("7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales")

pi = 3.1415
print(pi)

print("8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?")

true1 = 'True'
true2 = True

print("9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9")

print(type(true1))
print(type(true2))

print("10) Asignar a una variable, la suma de un número entero y otro decimal")

x = a + 8.5
print(x)

print("11) Realizar una operación de suma de números complejos")

print(n_complejo+(5+5j))

#12) Realizar una operación de suma de un número real y otro complejo

print(a+n_complejo)

#13) Realizar una operación de multiplicación

print(a*2)

#14) Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

division1 = 27/4
print(division1)

#16) De la división anterior solamente mostrar la parte entera

print(int(division1)) #es lo mismo que usar 27//4

#17) De la división de 27 entre 4 mostrar solamente el resto

print(27%4)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print(4*(27//4)+27%4) #'27//4' es lo mismo que usar 'int(division1)'

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

print(mi_nombre+" El Cabezon")

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print("2"==2)

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(int("2")==2)

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

b = float('3.8')
strclass(b)
print(type(b))

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

var_3 = 3
print(-=var_3)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#26) Realizar una operación válida entre valores de tipo entero y string
