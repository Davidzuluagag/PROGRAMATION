import pandas as p
diccionario =p.read_csv("barrios.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Barrio"])

mayor_nombre = max (diccionario["Barrio"].values(), key=len)
menor_nombre = min (diccionario["Barrio"].values(), key=len)

print("El barrio con el nombre mas largo es {} y el barrio con el nombre mas corto es {}".format(mayor_nombre,menor_nombre))

consumo_agua_maximo = max (diccionario["Agua"].values())
consumo_agua_minimo = min (diccionario["Agua"].values())
print ("El consumo maximo de agua es {} y el consumo minimo de agua es {}".format(consumo_agua_maximo,consumo_agua_minimo))

consumo_energia_maximo = max (diccionario["Energía"].values())
consumo_energia_minimo = min (diccionario["Energía"].values())
print ("El consumo maximo de energía es {} y el consumo minimo de energía es {}".format(consumo_energia_maximo,consumo_energia_minimo))

consumo_gas_maximo = max (diccionario["Gas"].values())
consumo_gas_minimo = min (diccionario["Gas"].values())
print ("El consumo maximo de gas es {} y el consumo minimo de gas es {}".format(consumo_gas_maximo,consumo_gas_minimo))

consumo_internet_maximo = max (diccionario["Internet"].values())
consumo_internet_minimo = min (diccionario["Internet"].values())
print ("El consumo maximo de internet es {} y el consumo minimo de internet es {}".format(consumo_internet_maximo,consumo_internet_minimo))

cantidad_habitantes_maxima = max (diccionario["Habitantes"].values())
cantidad_habitantes_minima = min (diccionario["Habitantes"].values())
print ("La cantidad maxima de habitantes es {} y la cantidad minima de habitantes es {}".format(cantidad_habitantes_maxima,cantidad_habitantes_minima))