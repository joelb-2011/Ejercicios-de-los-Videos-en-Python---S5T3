 def ejerVIDEO13_1_3(self):
        def funcion1(pacientes):
            e=0
            t=0
            for datos in pacientes.values():
                if datos[2]:
                    e+=datos[1]
                    t+=1
            if t>0:
                return e/t
            else:
                return 0

        def funcion2(pacientes, medicos, dni):
            for medico in medicos:
                if medico[0] == pacientes[dni][3]:
                    return medico[1]
            return ""
        pacientes = {10267489:["Marta Ramos",68,True,829], 22819922: ["Lucas Pérez", 47, False, 437], 40526661: ["Facundo Lucero", 29, True, 829]}
        print(funcion1(pacientes))
        medicos = {(829,"Gabriela Ríos"),(437, "Pedro Olivares"), (561, "Soledad Fuentes")}
        print(funcion2(pacientes,medicos,22819922))

   