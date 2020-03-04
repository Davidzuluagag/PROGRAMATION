#-----------MENSAJES---------------#
MENSAJE_BIENVENIDO = "Bienvenido"
PREGUNTA_PESO = "Ingrese peso en kg"
PREGUNTA_TALLA = "Ingrese talla en m"
MENSAJE_1 = "Bajo peso"
MENSAJE_2 = "Normal"
MENSAJE_3 = "Sobrepeso"
MENSAJE_4 = "Obeso"
#-----------ENTRADAS------------#
_peso = 0.0
_talla = 0.0

#-----------CODIGO-------------#
print(MENSAJE_BIENVENIDO)
_peso = int(input (PREGUNTA_PESO))
_talla = float(input (PREGUNTA_TALLA))
IMC = _peso/(_talla**2)
if (IMC < 18.50):
    print (MENSAJE_1)
elif ((IMC > 18.50) and (IMC <= 24.99)):
        print (MENSAJE_2)
elif ((IMC > 24.99) and (IMC <= 29.99)):
        print(MENSAJE_3)
else:
        print (MENSAJE_4)