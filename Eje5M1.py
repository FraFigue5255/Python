#Enunciado: Pide una calificación (0 al 10) y muestra:
#9–10: Excelente
#6–8: Aprobado
#0–5: Desaprobado

nota = int(input("Ingresa su nota: "))
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")