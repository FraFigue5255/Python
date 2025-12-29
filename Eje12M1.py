#Enunciado: Pide una palabra y muestra cuántas vocales contiene.
palabra = input("Ingresa una palabra: ").lower()
vocales = "aieou"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador = contador +1

print("Cantidad de vocales: ", contador)
