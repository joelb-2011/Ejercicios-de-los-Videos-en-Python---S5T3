frase = input("Frase: ")
cantidad = 0
for x in frase:
    if x in "aeiou":
        cantidad += 1
print("Cantidad de vocales: ", cantidad)