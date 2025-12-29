#Enunciado:
#Crea una calculadora con un menú:
#Sumar
#Restar
#Multiplicar
#Dividir
#Salir

while True:
    print("\n--Calculadora--")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "5":
        print("Saliendo..")
        break
    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))
    if opcion == "1":
        print("Resultado: ", a + b)
    elif opcion == "2":
        print("Resultado: ", a - b)
    elif opcion == "3":
        print("Resultado: ", a * b)
    elif opcion == "4":
        if b != 0:
            print("Resultado: ", a / b)
        else:
            print("No se puede dividir por 0")
    else:
        print("Opcion Invalida")
