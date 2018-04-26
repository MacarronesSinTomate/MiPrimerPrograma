lista_original = [1, "Uno", 2, "Nueve", 6]
lista_string = []
lista_int = []

for variables in lista_original:
    if type(variables) == str:
        lista_string.append(variables)
    if type(variables) == int:
        lista_int.append(variables)

print(lista_string, lista_int)

