fecha = input("Fecha en formato DDMMAAAA: ")
dia = fecha[:2]
mes = fecha[2:4]
año = fecha[4:]
print(dia, "/", mes, "/", año)