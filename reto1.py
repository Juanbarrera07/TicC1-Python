#Reto 1
mat_org = float(input("Porcentaje (%) de Materia Organica: "))
p2o5 = float(input("Cantidad (Kg/ha) de P2O5: "))
if (mat_org < 3) or (p2o5 < 46):
    print("NO APTO")
elif (mat_org >= 3 and mat_org <= 4) or (p2o5 >= 46 and p2o5 <= 57):
    print("MARGINALMENTE APTO")
elif (mat_org >= 4.1 and mat_org <= 5) or (p2o5 >= 58 and p2o5 <= 69):
    print("MODERADAMENTE APTO")
elif (mat_org > 5) or (p2o5 >= 69):
    print("SUMAMENTE APTO")