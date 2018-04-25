otra = "SI"
while otra == "SI":

    numero_a_convertir = input("Introduce el numero: ")
    resultado_en_centigrados = (float(numero_a_convertir) - 32) / 1.8
    print("El resultado es {} ºC".format(resultado_en_centigrados))
    otra = input("¿Quieres realizar otra operacion? ( SI / NO ): ").upper()

    if otra != "SI":
        print("Pues hasta luego!! :)")
        break
