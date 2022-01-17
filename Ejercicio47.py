def ejerVIDEO13_1_2(self):
        contadores = {}
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for letra in alfabeto.upper():
            contadores[letra] = 0
        for i in range(3):
            cadena = input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() in alfabeto:
                    contadores[caracter]+=1
        
        for caracter,cantidad in contadores.items():
            print(caracter, ":", cantidad)

   