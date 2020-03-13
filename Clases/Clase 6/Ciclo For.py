# _cantidadSaltos=int(input("Ingrese cantidad de saltos"))
# for i in range(4):
#     print(i)

# for i in range (_cantidadSaltos):
#     print ("El canguro da su salto numero",i+1)

# DÍAS=("Lunes","Martes","Miercoles","Jueves","Viernes")
# for dia in DÍAS:
#     print(dia)

NOMBRES=["X","Y","Z","M","N","U"]
EDADES=[18, 16, 15, 19, 20, 17]
print(len(NOMBRES), len(EDADES))
for i in range(len(NOMBRES)):
    if EDADES[i]>=18:
        print(i, "La persona", NOMBRES[i], "Es mayor")

sumaEdades=0
for edad in EDADES:
    sumaEdades+=edad
print(sumaEdades)