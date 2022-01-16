c = int(input("Cantidad de números: "))
total = 0
for variable in range(c):
    numero = int(input("Número a sumar: "))
    total = total + numero
print("Total de la suma: ", total)