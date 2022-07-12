## Manejo de errores
#%%
#1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?
import sys
from unittest.case import _AssertRaisesContext
sys.path.append(r'/home/gusta/Documentos/Henry-prep/Python-Prep/07 - Classes & OOP')
import herramientas_clase5 as h


lista1= 'hola'
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
h.funciones_clase5.es_primo('hola')

#%%
#2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.
import sys
sys.path.append(r'/home/gusta/Documentos/Henry-prep/Python-Prep/07 - Classes & OOP')
import herramientas_clase5 as h


h1 = h.funciones_clase5([1,2,3,4])

h1.convertir_temp('celsius','farenheit')

#%%
#3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
#Creacion del objeto incorrecta<br>
#Creacion correcta del objeto<br>
#Metodo valor_modal()<br>
import sys
sys.path.append(r'/home/gusta/Documentos/Henry-prep/Python-Prep/07 - Classes & OOP')
import herramientas_clase5 as h
import unittest

h1 = h.funciones_clase5([1,2,3,4])

class probando_miclase(unittest.testcase):
    
    def _AssertRaisesContext(valor):
       if type(valor) == str:

#Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

#%%
#4) Probar una creación incorrecta y visualizar la salida del "raise"

#%%
#6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

#7) Agregar casos de pruebas para el método conversion_grados()

#8) Agregar casos de pruebas para el método factorial()

#9) Completar el código en las funciones del archivo "checkpoint.py" y probarlo a partir de la ejecución del script "tests.py"