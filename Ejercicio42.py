frase=input("Frase:  ")
frase=frase.strip()
cantidad=0
len_p_mas_larga=0
while len(frase)  !=0:
    cantidad=cantidad+1
    i=frase,find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=frase[i:]
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra mas larga:", p_mas_larga)
print("cantidad de palabras:", cantidad)




