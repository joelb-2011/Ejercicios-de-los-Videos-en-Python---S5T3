pares = 0
n = int(input("Número (-1 para terminar el programa): "))
while n != -1:
    if n%2 == 0:
        pares += 1
    suma = 0
    while n != 0:
        digito = n%10
        suma += digito
        n = n//10
    print("Suma de sus dígitos: ", suma)
    n = int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares.")