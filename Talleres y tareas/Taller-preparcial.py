class Canguro():
    def __init__(self, color, peso, numero, sexo):
        self.color=color
        self.peso=peso
        self.numero=numero
        self.sexo=sexo
    def saltar (self, saltos):
        for i in range (saltos):
            print("uno de los canguros saltó {} veces".format(i+2))

canguro1=Canguro ("rojo", 60, 10, "masculino")
canguro2=Canguro ("rojo", 80, 20, "masculino")
canguro3=Canguro ("gris", 62, 30, "femenino")
canguro4=Canguro ("rojo", 85, 40, "masculino")
canguro5=Canguro ("gris", 65, 50, "femenino")
canguro6=Canguro ("gris", 70, 60, "femenino")
canguro7=Canguro ("rojo", 64, 70, "femenino")
canguro8=Canguro ("rojo", 40, 80, "masculino")
canguro9=Canguro ("gris", 56, 90, "femenino")
canguro10=Canguro ("rojo", 60, 100, "femenino")

print("el color del canguro 1 es", canguro1.color, "y su sexo es", canguro1.sexo)
print("el color del canguro 2 es", canguro2.color, "y su sexo es", canguro2.sexo)
print("el color del canguro 3 es", canguro3.color, "y su sexo es", canguro3.sexo)
print("el color del canguro 4 es", canguro4.color, "y su sexo es", canguro4.sexo)
print("el color del canguro 5 es", canguro5.color, "y su sexo es", canguro5.sexo)
print("el color del canguro 6 es", canguro6.color, "y su sexo es", canguro6.sexo)
print("el color del canguro 7 es", canguro7.color, "y su sexo es", canguro7.sexo)
print("el color del canguro 8 es", canguro8.color, "y su sexo es", canguro8.sexo)
print("el color del canguro 9 es", canguro9.color, "y su sexo es", canguro9.sexo)
print("el color del canguro 10 es", canguro10.color, "y su sexo es", canguro10.sexo)
canguro1.saltar(9)

class Cuidador():
    def __init__(self, identificación, nombre):
        self.identificación=identificación
        self.nombre=nombre

cuidador1=Cuidador (123, "Firulais")
cuidador2=Cuidador (124, "Modesto")
cuidador3=Cuidador (125, "Tobías")
cuidador4=Cuidador (126, "Milo")
cuidador5=Cuidador (127, "Choco")

print ("el nombre del cuidador 1 es", cuidador1.nombre)
print ("el nombre del cuidador 2 es", cuidador2.nombre)
print ("el nombre del cuidador 3 es", cuidador3.nombre)
print ("el nombre del cuidador 4 es", cuidador4.nombre)
print ("el nombre del cuidador 5 es", cuidador5.nombre)

cuidador1=Cuidador (123, "Firulais")
alimentó=8
print("uno de los cuidadores,", cuidador1.nombre, ", alimentó a", alimentó, "de los canguros")

class Jefe(Cuidador):
    def contratar_cuidador (self, id, name):
        nuevo=Cuidador(identificación, nombre)
        return nuevo
    def dar_mensaje(self, mensaje):
        print("¡Les cuento que esta sera la mejor temporada de todas y para todos!")
        print(mensaje)

jefe1=Jefe(000, "Ruben")
jefe1.dar_mensaje("¡Hola, soy el nuevo jefe y he contratado a", cuidador6.nombre, "; un nuevo cuidador!")
cuidador6=jefe1.contratar_cuidador(128, "Nemecio")