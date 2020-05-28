import sys
import matplotlib.pyplot as plt
import pandas as p
def graficar_archivo(archivo):
  assert(archivo)
  return False 
archivo_correcto=True 

while(archivo_correcto):
  archivo=input("Ingrese el nombre del archivo:")
  try:
    archivo_correcto=open(archivo)
    archivo_correcto=False
  except FileNotFoundError :
    print("Este archivo no existe")

graficar = p.read_csv(archivo,encoding='UTF-8',header=0, delimiter=";").to_dict()
x=list(graficar["muestra"].values())
y=list(graficar["valor"].values())
plt.title(input("Ingrese un titulo para el grafico:"))
plt.xlabel(input("Ingrese el nombre para el eje x:"))
plt.ylabel(str(input("Ingrese el nombre para el eje y:")))
plt.plot(x,y)
plt.savefig("grafico.png")
plt.close()
plt.show  

nombre=(input('Ingrese su nombre:'))
edad=int(input('Ingrese su edad:'))
estatura=float(input('Ingrese su estatura:'))
peso=float(input('Ingrese su peso:'))
def validar_imc(nombre, edad, estatura, peso):
  try:
    nombre=str(nombre)
  except ValueError:
    print ("ingresaste mal tu nombre")
    nombre = (input('Ingrese su nombre :'))
    validar_imc(nombre, edad, estatura, peso)
  try:
    edad=float(edad)
  except ValueError:
    print("Error edad")
    nombre=(input('Ingrese su edad:'))
    validar_imc(nombre, edad, estatura, peso)
  try:
    estatura=float(estatura)
  except ValueError:
    print("Error estatura")
    estatura=(input('Ingrese su estatura:'))
    validar_imc(nombre, edad, estatura, peso)
  try:
    peso=float(peso)
  except ValueError:
    print("Error peso")
    peso=(input('Ingrese su peso:'))
    validar_imc(nombre, edad, estatura, peso)
  imc=(peso)/(estatura**2)
  return imc
  imc_resultado=validar_imc(nombre, edad, estatura, peso)
print("tu imc es de", imc_resultado)

arroz=float(input("Ingrese kilos de arroz:")) 
lentejas=float(input("Ingrese kilos de lenteja:"))  
frijoles=float(input("Ingrese kilos de frijoles:")) 
papa=float(input("Ingrese kilos de papa:")) 

mercado= {"Mercado": ["Arroz", "Lentejas", "Frijoles", "Papa"]}
total= (arroz, frijoles, lentejas, papa)

print(mercado["Mercado"])
print(total)

plt.bar(mercado["Mercado"],total)
plt.title("Productos vs Kilos", fontsize=20)
plt.xlabel("Mercado")
plt.ylabel("Kilos")
plt.savefig("Mercado.png")
plt.show()

def reconocer_parraf(Parrafo):
    assert(Parrafo.endswith("."))
    return False
reconocer= True

while(reconocer):
    Parrafo= input("Como se ha sentido durante el servicio prestado:")
    try:
        reconocer=reconocer_parraf(Parrafo)
    except AssertionError:
        print("La oración debe terminar con punto")

labels= "Leche", "Huevo", "Vino", "Arroz", "Queso", "Salchichas"
sizes=[12,8,4,26,30,20]
explode= (0,0,0,0,0.1,0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("porcentaje de compras")
plt.savefig("compras.png")
plt.show()