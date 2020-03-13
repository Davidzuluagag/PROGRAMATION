def marco():
    print("#"*30)
def saludar (nombre):
    print("Bienvenido", nombre, "a este codigo")
marco()
saludar("David")
saludar(input("Ingrese nombre:"))

def sumar (x,y):
    suma=x+y
    return suma
resultado=sumar(2,4)
print(resultado)