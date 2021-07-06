def promedio(suma):
    pro = sum(suma)/len(suma)
    return pro
def aumento (valor):
    valor += 1
    return valor
def listop(lista):
    numeros = [float(i) for i in lista.split()]
    return numeros
listpromo = []
listprop2 = []
i = 1
contar = int(input())
while (i <= contar):
    listmo = listop(input())
    listp2o5 = listop(input())
    plistmo = promedio(listmo)
    plistp2o5 = promedio(listp2o5)
    listpromo.append("{:.2f}".format(plistmo))
    listprop2.append("{:.2f}".format(plistp2o5))
    i = aumento(i)
i = 1
sa = 0
moa = 0
maa = 0
na = 0
if i <= contar:
    while (i <= contar):
        mat_org = float(listpromo[i-1])
        p2o5 = float(listprop2[i-1])
        if (mat_org < 3) or (p2o5 < 46):
            na = aumento(na)
        elif (mat_org >= 3 and mat_org < 4) or (p2o5 >= 46 and p2o5 <= 57):
            maa = aumento(maa)
        elif (mat_org >= 4 and mat_org <= 5) or (p2o5 > 57 and p2o5 <= 69):
            moa = aumento(moa)
        elif (mat_org > 5) or (p2o5 > 69):
            sa = aumento(sa)
        i = aumento(i)
    print(" ".join(listpromo))
    print(" ".join(listprop2))
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

