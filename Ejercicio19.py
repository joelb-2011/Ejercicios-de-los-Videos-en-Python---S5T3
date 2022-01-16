año = int(input("Año: "))
if año%4 != 0:
    print("No es bisiesto.")
else:
    if año%100 != 0 or año%400 == 0:
        print("Es bisiesto.")
    else:
        print("No es bisiesto.")