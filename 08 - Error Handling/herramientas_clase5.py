class funciones_clase5:
    def __init__(self,valor):
        if type(valor) != list:
            self.valor = []
            raise ValueError("Se a creado una lista vacia, se esperaba una lista con numeros enteros")
        else:
            self.valor = valor

    def es_primo(lista_valores):
        if type(lista_valores) == str:
            raise ValueError("se esperaba un numero entero como entrada")
        if type(lista_valores) == list:
            lista_primos = []
            for i in lista_valores:
                if funciones_clase5._es_primo(i) == True:                    
                    lista_primos.append(i)
            print(lista_primos,'son numeros primos')
        else:
            if funciones_clase5._es_primo(lista_valores) == True:
                print(lista_valores, 'SI es primo')
            else:
                print(lista_valores, 'NO es primo')

    def _es_primo(valor):
        for n in range(2, valor):
            if valor % n == 0:
                return False
                break
            else:
                return True
            
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

    def convertir_temp(self, valor_origen, valor_destino):
        lista_temp = []
        medidas = ('farenheit','celsius','kelvin')
        if valor_origen not in medidas:
            print('los indicadores de origen y destino deben ser celcius, farenheit o kelvin')
        if valor_destino not in medidas:
            print('los indicadores de origen y destino deben ser celcius, farenheit o kelvin')
        for i in self.valor:
            lista_temp.append(funciones_clase5._convertir_temp(i, valor_origen, valor_destino))
        print(lista_temp)

    def _convertir_temp(valor, medida_origen, medida_destino):
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

    def indicadores_temp(self, valor):
        #''se especifica un indicador de temperatura y devuelve el equivalente en otros estandares de indicadores"'
        medidas = ("farenheit","celsius","kelvin")
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
