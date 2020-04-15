class estudiantes():
    def __init__(self, nombre, edad, genero, colegio):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.colegio=colegio
    def asistir_clase(self, clases):
        for i in range (clases):
            print("El estudiante {} asistio a {} clases el día de hoy".format(self.nombre, i+1))

estudiante1=estudiantes("Rick", 23, "M", "INEM")
estudiante2=estudiantes("Morty", 18, "M", "INEM")
estudiante3=estudiantes("Ramón", 20, "M", "INEM")
estudiante4=estudiantes("Florinda", 19, "F", "INEM")
estudiante5=estudiantes("Chilindrina", 21, "F", "INEM")

class profesores():
    def __init__(self, name, age, level):
        self.name=name
        self.age=age
        self.level=level
    def dictar_clase(self, clasess):
        for i in range (clasess):
            print("El profesor {} dicto {} clases el día de hoy".format(self.name, i+1))

profesor1=profesores("Alfonso", 50, "magister")
profesor2=profesores("Rodrigo", 45, "magister")

class director(profesores):
    def contratar_profesores(self, name, age, level):
        profesor=profesores(name, age, level)
        return profesor

director1=director("El Chavo", 40, "magister")

profesorX=director1.contratar_profesores("Charles", 60, "magister")
profesorY=director1.contratar_profesores("Logan", 45, "magister")

_decisión=int(input("""
Ingrese
1- para ver detalles de los estudiantes
2- para ver detalles de los profesores
3- para ver detalles del director
4- salir"""))
while(_decisión!=4):
    if(_decisión==1):
        print("El estudiante 1 se llama", estudiante1.nombre, ", tiene", estudiante1.edad, "y es del", estudiante1.colegio)
        print("El estudiante 2 se llama", estudiante2.nombre, ", tiene", estudiante2.edad, "y es del", estudiante2.colegio)
        print("El estudiante 3 se llama", estudiante3.nombre, ", tiene", estudiante3.edad, "y es del", estudiante3.colegio)
        print("El estudiante 4 se llama", estudiante4.nombre, ", tiene", estudiante4.edad, "y es del", estudiante4.colegio)
        print("El estudiante 5 se llama", estudiante5.nombre, ", tiene", estudiante5.edad, "y es del", estudiante5.colegio)
        estudiante1.asistir_clase(5)
    elif (_decisión==2):
        print("El profesor 1 se llama", profesor1.name, "y es", profesor1.level)
        print("El profesor 2 se llama", profesor2.name, "y es", profesor2.level)
        profesor1.dictar_clase(8)
    elif (_decisión==3):
        print("El director se llama", director1.name, "y es", director1.level)    
        print("Hola! Soy", director1.name, "y he contratado dos nuevos profesores:")
        print("El profesor X se llama", profesorX.name, "y es", profesorX.level)
        print("El profesor Y se llama", profesorY.name, "y es", profesorY.level)    
    else:
        print("Ingrese numero valido")
    _decisión=int(input("""
Ingrese
1- para ver detalles de los estudiantes
2- para ver detalles de los profesores
3- para ver detalles del director
4-Salir
"""))
print("Hasta luego")