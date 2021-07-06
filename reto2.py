contar = int(input("cuantas secuencias de datos ingresara: "))
i = 1
sa = 0
moa = 0
maa = 0
na = 0
smat_org = 0
sp2o5 = 0

if i <= contar:
    while (i <= contar):
        mat_org = float(input("Porcentaje (%) de Materia Organica: "))
        p2o5 = float(input("Cantidad (Kg/ha) de P2O5: "))
        smat_org = smat_org + mat_org
        sp2o5 = sp2o5 + p2o5
        if (mat_org < 3) or (p2o5 < 46):
            na += 1
        elif (mat_org >= 3 and mat_org < 4) or (p2o5 >= 46 and p2o5 <= 57):
            maa += 1
        elif (mat_org >= 4 and mat_org <= 5) or (p2o5 > 57 and p2o5 <= 69):
            moa += 1
        elif (mat_org > 5) or (p2o5 > 69):
            sa += 1
        i += 1
        pmat_org = smat_org/(i-1)
        pp2o5 = sp2o5/(i-1)
    print("{:.2f}".format(pmat_org))
    print("{:.2f}".format(pp2o5))
    print(f"sumamente apto {sa}")
    print(f"moderadamente apto {moa}")
    print(f"marginalmente apto {maa}")
    print(f"no apto {na}")
else:
    print("{:.2f}".format(0))
    print("{:.2f}".format(0))
    print(f"sumamente apto {sa}")
    print(f"moderadamente apto {moa}")
    print(f"marginalmente apto {maa}")
    print(f"no apto {na}")