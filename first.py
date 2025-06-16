import random

def mostrar_menu():
    """Muestra el menú principal del juego y captura la elección del usuario"""
    while True: 
        print("\n Bienvenido al Juego: Piedra, Papel o Tijeras")
        print("1. Jugar solo (contra la computadora)")
        print("2. Modo multijugador (2 jugadores)")
        print("3. Salir")

        option = input("Seleccione una opción (1-3): ")
        if option == "1":
            jugar_contra_pc()
            break
        elif option == "2":
            jugar_multijugador()
            break
        elif option == "3":
            print("Gracias por jugar Piedra, Papel y Tijeras. ¡Hasta la próxima!")
            break 
        else:
            print("Opción inválida. Intente nuevamente.")

def jugar_contra_pc():
    print("\nModo: Jugar contra la computadora")
    option = input("\n1. Piedra"
          "\n2. Papel"
          "\n3. Tijeras"
          "\nSeleccione su jugada (1-3): ")
    if option not in ["1", "2", "3"]:
        print("Opción inválida. Debes elegir 1, 2 o 3.")
        return
    jugada_usuario = int(option)
    jugar_contra_pc = random.randint(1, 3)

    opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
    print(f"Tú elegiste: {opciones[jugada_usuario]}")
    print(f"La computadora eligió: {opciones[jugar_contra_pc]}")

    if jugada_usuario == jugar_contra_pc:
        print("¡Empate!")
    elif (jugada_usuario == 1 and jugar_contra_pc == 3) or \
         (jugada_usuario == 2 and jugar_contra_pc == 1) or \
         (jugada_usuario == 3 and jugar_contra_pc == 2):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    

mostrar_menu()