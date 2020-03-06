#------MENÚ------#
listaNombres=["Santiago","Elena","Lesly","Camila1","Camila2","Mafe","Ysa","Zarate","Hernandez","David","Marco","Juanes"]
listaNombres[4]="Mesa"
listaNombres[5]="Betancur"
listaNombres.pop(10)
listaNombres.append ("El Marco")

listaEdades=["20","18","21","19","20","22","23","19","19","21","19","20"]
listaNotas=["4.5","4.0","5.0","3.8","2.6","3.4","4.8","4.2","3.9","4.5","3.8","4.3"]

_decision=int(input("""
Ingrese
1-para ver nombres
2-para ver edades
3-para ver notas
4-Salir
"""))
while(_decision!=4):
    if(_decision==1):
        print(listaNombres)
    elif (_decision==2):
        print(listaEdades)
    elif (_decision==3):
        print(listaNotas)
    else:
        print("Ingrese numero valido")
    _decision=int(input("""
Ingrese
1-para ver nombres
2-para ver edades
3-para ver notas
4-Salir
"""))
print("Hasta luego")