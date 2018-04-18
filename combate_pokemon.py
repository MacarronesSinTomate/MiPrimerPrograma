
pokemon_elegido = input("¿Contra que pokemon quieres combatir?  (Squirtle / Charmander / Bulbasaur): ")
vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_enemigo = "Squirtle"
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    nombre_enemigo = "Charmander"
elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    nombre_enemigo = "Bulbasaur"

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vamos a usar? (Chispazo / Bola voltio): ")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12
    elif ataque_elegido == "Secreto":
        vida_enemigo -= 50

    print("La vida del enemigo ahora es de {}".format(vida_enemigo))

    if pokemon_elegido == "Squirtle":
        print("{} te hace un ataque de {} de daño".format(nombre_enemigo, vida_enemigo))
        vida_pikachu -= 8
    elif pokemon_elegido == "Charmander":
        print("{} te hace un ataque de {} de daño")
        vida_pikachu -= 7
    elif pokemon_elegido == "Bulbasaur":
        print("{] te hace un ataque de {} de daño")
        vida_pikachu -= 10

    print("La vida de pikachu es de {}".format(vida_pikachu))

print("El combate ha sido terminado")
if vida_pikachu <= 0:
    print("Has perdido")
elif vida_enemigo <= 0:
    print("Has ganado tu")