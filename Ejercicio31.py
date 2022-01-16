sumaNegativos = 0
sumaPositivos = 0
cantidadPositivos = 0
for i in range(6):
    nro = int(input("Número: "))
    if nro >= 0:
        cantidadPositivos += 1
        sumaPositivos += nro
    else:
        sumaNegativos += nro
print("Sumatoria de negativos: ", sumaNegativos)
if cantidadPositivos != 0:
    print("Promedio de positivos: ", sumaPositivos / cantidadPositivos)
else:
    print("No se ingresaron números positivos.")