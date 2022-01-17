 def ejerVIDEO13_2(self):
        def cargarSocios(socios):
            numero = int(input("Número de socio:"))
            while numero != 0:
                nombre = input("Nombre y apellido: ")
                fecha = input("Fecha de ingreso: ")
                cuota = input("Cuota al día s/n: ")
                pago = cuota.lower() == "s"
                socios[numero] = [nombre,fecha,pago]
                numero = int(input("Número de socio: "))
            return socios 
    
        def modificarFecha(socios, fecha_anterior, fecha_nueva):
            for datos in socios.values():
                if datos[1]==fecha_anterior:
                    datos[1]= fecha_nueva
            return socios

        def numeroSocio(socios,nombre):
            for numero, datos in socios.items():
                if datos[0].lower() == nombre.lower():
                    return numero
            return 0

        def formatoFecha(fecha):
            return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirListado(socios):
            for numero, datos in socios.items():
                print("-Número: ",numero)
                print("-Nombre: ",datos[0])
                print("-Fecha de ingreso: ",formatoFecha(datos[1]))
                if datos[2]:
                    print("-Cuota al día")
                else:
                    print("-En deuda")
                print("~~~~")
            return None
        socios_activos={1:["Amanda Núñez", "17032009", True], 2:["Bárbara Molina","17032009"], 3:["Lautaro Campos","17032009"]}
        print("***Cargar Socios")
        socios_acitvos=cargarSocios(socios_activos)

        print("El club tiene", len(socios_activos), "socios")

        print("***Registrar pago de cuotas")
        numero = int(input("Número de socio: "))
        socios_activos[numero][2] = True

        print("***Modificando fecha de ingreso...")
        socios_activos = modificarFecha(socios_activos, "13032018", "14032018")
        
        print("***Eliminar socio: ")
        nombre = input("Nombre y Apellido: ")
        numero = numeroSocio(socios_activos, nombre)
        del socios_activos[numero]

        imprimirListado(socios_activos)