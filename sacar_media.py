numeros_usuario = []
numero_del_usuario = ""
numeros_a_introducir = int(input("Cuantos numeros quieres introducir: "))

while len(numeros_usuario) < numeros_a_introducir:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero añadido.")

total = 0
for numero in numeros_usuario:
        total += numero

resultado = total / numeros_a_introducir
print("Numeros: {}".format(resultado))
