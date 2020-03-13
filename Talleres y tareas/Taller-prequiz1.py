#-----------MENSAJES---------------#
MENSAJE_BIENVENIDO = "Bienvenido"
PREGUNTA_PACIENTES = "Ingrese numero de pacientes"
MENSAJE_BAJO = "Riesgo bajo"
MENSAJE_MEDIO = "Riesgo medio"
MENSAJE_ALTO = "Riesgo alto"
PREGUNTA_UCI = "Ingrese numero de pacientes en UCI"

#-----------ENTRADAS------------#
_numeroPacientes = " "
_numeroUCI = " "
#-----------CODIGO-------------#
print(MENSAJE_BIENVENIDO)
_numeroPacientes = int(input (PREGUNTA_PACIENTES))
if ((_numeroPacientes > 0) and (_numeroPacientes <= 1000)):
    print (MENSAJE_BAJO)
elif ((_numeroPacientes >= 1000) and (_numeroPacientes < 5000)):
    _numeroUCI = int(input(PREGUNTA_UCI))
    if (_numeroUCI >=1000):
        print (MENSAJE_ALTO)
    else:
        print(MENSAJE_MEDIO)
else:
    print (MENSAJE_ALTO)