candidato = input("Candidato elegido: ")
if candidato.upper() == "A":
    print("Usted ha votado por el partido rojo.")
elif candidato.upper() == "B":
    print("Usted ha votado por el partido azul.")
elif candidato.upper() == "c":
    print("Usted ha votado por el partido verde.")
else:
    print("Opción errónea.")