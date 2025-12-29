#Enunciado:Invierte una palabra manualmente, sin usar [::-1] ni reversed().

texto = input("Ingrese una palabra: ")
invertido= ""
for letra in texto:
    invertido = letra + invertido
print("Invertido: ", invertido)