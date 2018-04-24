
otra_operacion = "True"

while otra_operacion == "True":
    operacion_a_realizar = input("¿Que operacion quieres hacer? ( *, /, +, - ): ")
    primer_numero = input("Primer numero: ")
    segundo_numero = input("Segundo numero: ")
    resultado = 0

    if operacion_a_realizar == "*":
        resultado = int(primer_numero) * int(segundo_numero)
    if operacion_a_realizar == "/":
        resultado = int(primer_numero) / int(segundo_numero)
    if operacion_a_realizar == "+":
        resultado = int(primer_numero) + int(segundo_numero)
    if operacion_a_realizar == "-":
        resultado = int(primer_numero) - int(segundo_numero)
    print(resultado)
    otra_operacion = input("¿Quieres hacer otra operación? ( True, False): ")
    if otra_operacion != "True":
        print("Hasta luego!! :)")
        break


