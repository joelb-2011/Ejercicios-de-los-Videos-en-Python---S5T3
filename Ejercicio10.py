CapacidadM2 = 4
PorcentajeGradas = 0.2
PorcentajeEspeciales = 0.3
PorcentajeComunes = 0.7

dimensiones = float(input("Dimensiones del estadio (en m2): "))
personasengradas = int(input("Cantidad de personas que caben en las gradas: "))
porcentajesescenario = int(input("Porcentaje que ocupa el escenario: "))
m2gradas = dimensiones * PorcentajeGradas
m2escenario = dimensiones * (porcentajesescenario/100)
m2disponibles = dimensiones - m2gradas - m2escenario
personastotales = (m2disponibles * 4) + personasengradas

print("Caben", personastotales, "personas.")
precioentradaespecial = float(input("Precio entrada especial: $"))
precioentradacomun = float(input("Precio entrada común: $"))
print("Ingreso total de ventas: $", (personastotales * PorcentajeEspeciales) * precioentradaespecial + (personastotales * PorcentajeComunes) * precioentradacomun)