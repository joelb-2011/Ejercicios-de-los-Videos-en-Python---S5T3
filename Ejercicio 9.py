capacidad = float(input("Capacidad del tanque: "))
kmxl = float(input("Rendimiento (km por litro): "))
recorrido = float(input("Km totales a recorrer: ")) 
kmxtanque = capacidad * kmxl
print("Serán necesarios", recorrido/kmxtanque, "tanques.")