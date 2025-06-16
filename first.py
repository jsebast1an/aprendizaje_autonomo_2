def mostrar_menu():
    """Muestra el menú principal del juego y captura la elección del usuario"""
    while True: 
        print("\n Bienvenido al Juego: Piedra, Papel o Tijeras")
        print("1. Jugar solo (contra la computadora)")
        print("2. Modo multijugador (2 jugadores)")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            jugar_contra_pc()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            print("Gracias por jugar Piedra, Papel y Tijeras. ¡Hasta la próxima!")
            break 
        else:
            print("Opción inválida. Intente nuevamente.")
