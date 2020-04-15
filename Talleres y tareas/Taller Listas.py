lista_edades=[1,2,4,8,16,32,64]
print ("Esta son las edades de los pacientes presentes", lista_edades)

def pacientesdehoy():
    pacientesdehoy=[]
    registro=input("si -> para agregar, no -> para finalizar:")
    while(registro=="si"):
        pacientesdehoy.append(input("Ingrese edad del paciente:"))
        registro=input("si -> para agregar, no -> para finalizar:")
    return pacientesdehoy
print("¿Desea registrar paciente?")
edadesnuevas=pacientesdehoy()
print("Esta son las edades de los pacientes ingresados el día de hoy", edadesnuevas)
lista_nueva=lista_edades+edadesnuevas
print("Y estas son las edades del total de los pacientes", lista_nueva)

suma=0
i=0
for edad in lista_nueva:
    suma += edad
    i+=1
promedio=suma/i
print ("El promedio de las edades es", promedio)
print("La edad del paciente más longevo es {}".format(max(lista_nueva)))
print("La edad del paciente más joven es {}".format(min(lista_nueva)))
lista_nueva.sort()
print("La lista en orden creciente es {}".format(lista_nueva))
lista_nueva.sort(reverse=True)
print("La lista en orden decreciente es {}".format(lista_nueva))

lista_nueva.insert(3,87)
print(lista_nueva)
lista_nueva.pop(5)
print(lista_nueva)