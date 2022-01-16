digitosEnLaLinea = 0
cantLineas = 0
titulo = input("Título del libro: ")
while titulo != "*":
    if titulo == "/":
        cantLineas += 1
        print("Línea completa. Aparecen", digitosEnLaLinea, "dígitos.")
        digitosEnLaLinea = 0
    else:
        for caracter in titulo:
            if caracter in "0123456789":
                digitosEnLaLinea += 1
    titulo = input("Título del libro: ")
print("Fin. Se leyeron", cantLineas, "líneas.")