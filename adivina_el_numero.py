otro_intento = "True"
numero_elegido = ""
numero_a_adivinar = input("¿Que numero quieres que adivine tu amigo?: ")

while otro_intento == "True":

    if numero_elegido != numero_a_adivinar:
        numero_elegido = input("¿Que numero crees que ha puesto el tonto de tu amigo?: ")

    if numero_elegido == numero_a_adivinar:
        print("Que listo!! O que poco inteligente es tu colega xDD De todas formas... ¡¡FELICIDADES!!")
        otro_intento = "False"



