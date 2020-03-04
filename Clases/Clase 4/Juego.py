import random
PREGUNTA_NUMERO="Ingrese un numero entero del 1-10"
MENSAJE_ERROR="Fallaste!"
MENSAJE_ACIERTO="Acertaste!"
MENSAJE_MAYOR="Te pasaste!"
MENSAJE_MENOR="Te falta!"
NUMEROFAVORITO=random.randint(1,10)
_numeroIngresado= int (input (PREGUNTA_NUMERO))
while(_numeroIngresado!=NUMEROFAVORITO):
    print(MENSAJE_ERROR)
    if (_numeroIngresado>NUMEROFAVORITO):
        print(MENSAJE_MAYOR)
    else: print(MENSAJE_MENOR)
    _numeroIngresado=int(input(PREGUNTA_NUMERO))
print (MENSAJE_ACIERTO)