apetece_helado_input = input("¿Te apetece un helado? ( Si / No ): ").upper()

if apetece_helado_input == "SI":
    apetece_helado_input = True
elif apetece_helado_input == "NO":
    apetece_helado_input = False
else:
    print("Te he dicho que me digas si o no. No se que has dicho pero cuento como que no.")

tienes_dinero_input = input("¿Tienes dinero para un helado? ( Si / No ): ").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los helados? ( Si / No ): ").upper()
esta_tu_tia_input = input("¿Estas con tu tia?  ( Si / No ): ").upper()



apetece_helado = apetece_helado_input == True
puedes_permitirtelo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puedes_permitirtelo and esta_el_senor_helados:
    print("Comete un helado")
else:
    print("Pues nada")
