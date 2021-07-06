# creador de listas str a float
def listop(lista):
    numeros = [float(i) for i in lista.split()]
    return numeros
#recolector de datos de entrada
filas = int(input()) #pide la cantidad de semanas
listpromo = []
listprop2 = []
#creador de matrices
for f in range(filas):
    listmo = listop(input()) #pide la entrada de Materia organica
    listpromo.append([])
    for c in listmo:
        listpromo[f].append(c)
for f in range(filas):
    listp2o5 = listop(input()) #pide la entrada de P2O5
    listprop2.append([])
    for c in listp2o5:
        listprop2[f].append(c)
#contadores Fijos
fil=0
col=0
na = 0
maa = 0
moa = 0
sa = 0
#contadores de Cache
na1 = 0
maa1 = 0
moa1 = 0
sa1 = 0
normal = []
#listas de maximos y minimos
maximo =[]
minimo =[]
#proseso de navegacion paralelos entre las matrices
for f in range(filas):
    if f == fil:
        for c in range(len(listmo)):
            if c == col:
                #condicionales para el conteo de repeticiones de TOTALES la matriz
                mat_org = listpromo[f][c]
                p2o5 = listprop2[f][c]
                if (mat_org < 3) or (p2o5 < 46):
                    na+=1
                    na1+=1
                elif (mat_org >= 3 and mat_org <= 4) or (p2o5 >= 46 and p2o5 <= 57):
                    maa+=1
                    maa1+=1
                elif (mat_org > 4 and mat_org <= 5) or (p2o5 > 57 and p2o5 <= 69):
                    moa+=1
                    moa1+=1
                elif (mat_org > 5) or (p2o5 > 69):
                    sa+=1
                    sa1+=1
            col+=1
        #creacion de la lista cache
        normal.append(na1)
        normal.append(maa1)
        normal.append(moa1)
        normal.append(sa1)
        mini = max(normal)
        #identificacion de la categoria que MAS se presento por semana
        if sa1 >= moa1 and sa1 >= maa1 and sa1 >= na1:
            maximo.append("sumamente apto")
        elif moa1 >= maa1 and moa1 >= na1:
            maximo.append("moderadamente apto")
        elif maa1 >= na1:
            maximo.append("marginalmente apto")
        else:
            maximo.append("no apto")
        #identificacion de la categoria que MENOS se presento por semana
        for x in range(len(normal)):
            if normal[x] != 0:
                if normal[x] <= mini:
                    mini = normal[x]
                    id = x
        if id == 0:
            minimo.append("no apto")
        elif id == 1:
            minimo.append("marginalmente apto")
        elif id == 2:
            minimo.append("moderadamente apto")
        else:
            minimo.append("sumamente apto")
        #eliminar los contadores cache
        na1 -= na1
        maa1 -= maa1
        moa1 -= moa1
        sa1 -= sa1
        mini -= mini
        normal.clear()
    col-=col
    fil+=1
#impresion de los resultados esperados
print(na,maa,moa,sa)
print(",".join(maximo))
print(",".join(minimo))