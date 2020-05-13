import matplotlib.pyplot as plt
import pandas as p 
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elementos vs Unidades", fontsize=20)
plt.bar(inventario["Elementos"].values(),inventario["Unidades"].values(),align="center")
plt.xlabel("Elementos")
plt.ylabel("Unidades")
plt.savefig("Inventario1.png")
plt.show()

plt.title("Elementos vs Elementos viejos", fontsize=20)
plt.bar(inventario["Elementos"].values(),inventario["Viejos"].values(),align="center")
plt.xlabel("Elementos")
plt.ylabel("Viejos")
plt.savefig("Inventario2.png")
plt.show()

plt.title("Elementos vs Elementos nuevos", fontsize=20)
plt.bar(inventario["Elementos"].values(),inventario["Nuevos"].values(),align="center")
plt.xlabel("Elementos")
plt.ylabel("Nuevos")
plt.savefig("Inventario3.png")
plt.show()

ppg = p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(ppg)
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ppg.png")
plt.show()

labels = 'Recuperandose en casa', 'Hospitalizados', 'En UCI'
sizes = [85, 10, 5]
explode = (0, 0, 0.1)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Estudio de COVID-19 en una población")
plt.savefig("Grafico_pie.png")
plt.show()