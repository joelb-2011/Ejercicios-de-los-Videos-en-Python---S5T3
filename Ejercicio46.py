#1
numeros=[]
nro=int(input("Numero; "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Numero: ")

#2
eliminar=int(input("Numero a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese numero no esta entre los ingresados")

#3
print("Sumatoria de los numeros: ", sumatoria(numeros))

#4
limite=int(imput("Filtrar numeros menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)

#5
Print("Frecuencias: ")
for tupla in frecuencias(numeros):
    print(tupla[0], "parece", tupla[1], "veces")