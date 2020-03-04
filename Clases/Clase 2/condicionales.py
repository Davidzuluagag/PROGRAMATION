#-----------MENSAJES---------------#
PREGUNTA_NOMBRE = "Igrese su nombre \n"
PREGUTA_EDAD = "Ingrese su edad viejito"
MENSAJE_BIENVENIDO = "Bienvenido"
MENSAJE_DESPEDIDA = "CHAO"
MENSAJE_TOCAYO = "Que locura loco, somos tocayos"
MENSAJE_JOVEN = "Tienes una vida por delante"
MENSAJE_ADULTO = "Disfruta mientras puedas"
MENSAJE_VIEJO = "Te queda poco"
#------------VARIABLES----------------#
NOMBRE_PERSONAL="David"
#-----------ENTRADAS------------#
_nombrePersona = " "
_edadPersona = 0
#-----------CODIGO-------------#
print(MENSAJE_BIENVENIDO)
_nombrePersona = input (PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombrePersona) :
    print(MENSAJE_TOCAYO)
print (MENSAJE_DESPEDIDA)
_edadPersona = int (input(PREGUTA_EDAD))
if ((_edadPersona >= 0) and (_edadPersona <= 25)):
    print (MENSAJE_JOVEN)
elif((_edadPersona >= 26) and (_edadPersona <= 65)):
    print (MENSAJE_ADULTO)
else:
    print (MENSAJE_VIEJO)
print (MENSAJE_DESPEDIDA)