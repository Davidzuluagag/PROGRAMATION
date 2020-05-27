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
estatura=float(input('Ingrese su estatura:'))
peso=float(input('Ingrese su peso:'))
def validar_imc(nombre, estatura, peso):
  try:
    nombre_verificado=str(nombre)
  except ValueError:
    print("Error nombre")
    nombre=(input('Ingrese su nombre:'))
    validar_imc(nombre,estatura,peso)
  try:
    estatura_verificada=float(estatura)
  except ValueError:
    print("Error estatura")
    estatura=(input('Ingrese su estatura:'))
    validar_imc(nombre,estatura,peso)
  try:
    peso_verificado=float(peso)
  except ValueError:
    print("Error peso")
    peso=(input('Ingrese su peso:'))
    validar_imc(nombre,estatura,peso)
  imc=(peso_verificado)/(estatura_verificada**2)
  return imc

pico_ecg= 9
pico_eeg= 10
pico_ppg= 9

picos= {"Picos": ["ECG", "EEG", "PPG"]}
total= (pico_ecg, pico_eeg, pico_ppg)

print(picos["Picos"])
print(total)

plt.bar(picos["Picos"],total)
plt.title("Picos vs Analisis", fontsize=20)
plt.xlabel("Picos")
plt.ylabel("Analisis")
plt.savefig("Picos.png")
plt.show()

labels= "Alcoba", "Sala", "Cocina", "Biblioteca", "Comedor",
sizes=[35,20,15,25,5]
explode= (0.1,0,0,0,0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Espacios de pasa tiempo en casa")
plt.savefig("casa.png")
plt.show()