mayor=-1
n = int(input("Número positivo: "))
while n >= 0:
    if n > mayor:
        mayor = n
    n = int(input("Número positivo: "))
print("Mayor número ingresado: ", mayor)