#Ejercicio 1 — Verificar si un número es primo
#Enunciado: Escribe un programa que pida un número entero y diga si es primo.
#¿Cómo pensarlo?
#Un número primo solo es divisible por 1 y por sí mismo.
#Probamos dividirlo entre todos los números desde 2 hasta n−1.
n = int(input("Ingrese un numero: "))
es_primo = True

if n <= 1:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
if es_primo:
    print("Es un número primo")
else:
    print("No es primo")
