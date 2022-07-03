## Clases y Programación Orientada a Objetos
#%%
#1) Crear la clase vehículo que contenga los atributos:<br>
#Color<br>
#Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor

from subprocess import call


class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

a1 = vehiculo('verde', 'moto', '110cc')
a2 = vehiculo('rojo', 'auto','1400cc')
a3 = vehiculo('azul','camion','5600cc')

print(a1.color, a1.tipo, a1.cilindrada)

#%%
#2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
#Acelerar<br>
#Frenar<br>
#Doblar<br>

class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def acelerar(self, vel):
        self.velocidad += vel
    def frenar(self, vel):
        self.velocidad -= vel
    def doblar(self, grados):
        self.direccion += grados


#%%
#3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def acelerar(self, vel):
        self.velocidad += vel
    def frenar(self, vel):
        self.velocidad -= vel
    def doblar(self, grados):
        self.direccion += grados

a1 = vehiculo('verde', 'moto', '110cc')
a2 = vehiculo('rojo', 'auto','1400cc')
a3 = vehiculo('azul','camion','5600cc')

class moto(vehiculo):
    def acelerar(vel):
        print('acelerar a',vel, 'Km/h')
    def frenar(vel):
        print('frenar a',vel,'Km/h')
    def doblar(grados):
        print('girar',grados,'grados')

class auto(vehiculo):
    def acelerar(vel):
        print('acelerar a',vel, 'Km/h')
    def frenar(vel):
        print('frenar a',vel,'Km/h')
    def doblar(grados):
        print('girar',grados,'grados')     

class camion(vehiculo):
    def acelerar(vel):
        print('acelerar a',vel, 'Km/h')
    def frenar(vel):
        print('frenar a',vel,'Km/h')
    def doblar(grados):
        print('girar',grados,'grados')

print('moto >')
moto.acelerar(50)
moto.frenar(40)
moto.doblar(90)

print('auto >')
auto.acelerar(90)
auto.frenar(60)
auto.doblar(45)

print('camion >')
camion.acelerar(80)
camion.frenar(40)
camion.doblar(30)
#%%
#4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def acelerar(self, vel):
        self.velocidad += vel
    def frenar(self, vel):
        self.velocidad -= vel
    def doblar(self, grados):
        self.direccion += grados
    def estado(self):
        print('velocidad', self.velocidad, 'km/h', 'direccion',self.direccion, 'grados')
    def detalle(self):
        print('color:',self.color,'tipo:', self.tipo,'cilindrada', self.cilindrada)

a1 = vehiculo('rojo','camion',5000)

a1.detalle()
a1.estado()
a1.acelerar(30)
a1.estado()
#%%
#5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>

#Verificar Primo<br>
#Valor modal<br>
#Conversión grados<br>
#Factorial<br>

class funciones_clase5:
    def __init__(self,valor):
        self.valor = valor
    def es_primo(x):
        es_primo = True
        for n in range(2, x):
            if (x % n == 0):
                es_primo = False
                break
        return print(x, 'es primo')
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

        for i in range(0,3):
            for j in range(0,3):
                print('conversion de',medidas[i], 'a ',medidas[j],'es:',funciones_clase5.convertir_temp(valor,medidas[i],medidas[j]))

    def factorial(valor):
        if type(valor) == str:
            return print('el factorial debe ser un numero entero')
        if valor <= 0:
            return print('el factorial debe ser mayor a 0')
        if valor > 1:
            valor = valor * funciones_clase5.factorial(valor - 1)
        return valor

lista = [1,1,1,3,4,6,8,8,9,9,8,8,8]
medidas = ("farenheit","kelvin","celsius")

funciones_clase5.es_primo(11)
funciones_clase5.valor_modal(lista,True)
funciones_clase5.convertir_temp(21,medidas,medidas)
funciones_clase5.factorial(4)

#%%
#6) Probar las funciones incorporadas en la clase del punto 5
#%%
#7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
#%%
#8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
import herramientas_clase5

lista = [1,1,1,3,4,6,8,8,9,9,8,8,8]
medidas = ("farenheit","kelvin","celsius")

funciones_clase5.es_primo(11)
funciones_clase5.valor_modal(lista,True)
funciones_clase5.convertir_temp(21,medidas,medidas)
funciones_clase5.factorial(4)

# %%
