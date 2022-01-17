def DNinvalido(dni)
cantidad=0
while dni!=0:
    cantidad=cantidad+1
    dni=dni//10
return cantidad==7 or cantidad==8
#----------------------------------
def lenUltimaPalabra(cadena):
    longitud=len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=" ":
            catidad=cantidad+1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena[i+1]!=" ":
    return cantidad 