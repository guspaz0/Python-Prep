## Clases y Programación Orientada a Objetos
#%%
#1) Crear la clase vehículo que contenga los atributos:<br>
#Color<br>
#Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor

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
    
#%%
4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
Verificar Primo<br>
Valor modal<br>
Conversión grados<br>
Factorial<br>

6) Probar las funciones incorporadas en la clase del punto 5

7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
