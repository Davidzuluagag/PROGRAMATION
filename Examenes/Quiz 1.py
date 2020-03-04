#-----------MENSAJES---------------#
PREGUNTA_TEMPERATURA = "Igrese temperatura corporal (en °C) del usuario"
PREGUTA_PROCEDENCIA = "Ingrese procedencia del usuario"
MENSAJE_HIPOTERMIA = "Hipotermia"
MENSAJE_SALUDABLE = "Saludable"
MENSAJE_ALERTA = "Alerta"
MENSAJE_PELIGRO = "Peligro"
MENSAJE_OBSERVACIÓN = "En observación"
MENSAJE_DESPEDIDA = "Siguiente"
#-----------ENTRADAS------------#
_temperturaUsuario = 0.0
_procedenciaUsuario = " "
CHINA = "china" 
ITALIA ="italia" 
IRAN = "iran"

#-----------CODIGO-------------#
_temperturaUsuario = float(input (PREGUNTA_TEMPERATURA))
if (_temperturaUsuario < 36):
    print (MENSAJE_HIPOTERMIA)
elif ((_temperturaUsuario >= 36) and (_temperturaUsuario < 38.5)):
    print(MENSAJE_SALUDABLE)
elif ((_temperturaUsuario >= 38.5) and (_temperturaUsuario < 40)):
    print(MENSAJE_ALERTA)
else:
    print(MENSAJE_PELIGRO)
_procedenciaUsuario = (input(PREGUTA_PROCEDENCIA))
if ((_procedenciaUsuario == CHINA) or (_procedenciaUsuario == ITALIA) or (_procedenciaUsuario == IRAN)):
    print (MENSAJE_OBSERVACIÓN)
    print (MENSAJE_DESPEDIDA)
else:
    print (MENSAJE_DESPEDIDA)