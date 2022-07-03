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