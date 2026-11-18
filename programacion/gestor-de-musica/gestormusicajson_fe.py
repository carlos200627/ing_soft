import gestormusicajson_be

while True:
    print("\n====  GESTOR DE MUSICA ====")
    print("   1. Agregar canción")
    print("   2. Ver canciones")
    print("   3. Eliminar canción")
    print("   4. Buscar canción")
    print("   5. Recomendación")
    print("   6. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        cancion = input("Nombre de la canción a agregar: ")
        autor = input("Nombre del autor: ")
        gestormusicajson_be.agregar_cancion(cancion, autor)
    elif opcion == "2":
        gestormusicajson_be.ver_canciones()
    elif opcion == "3":
        cancion = input("Nombre de la canción a eliminar: ")
        gestormusicajson_be.eliminar_cancion(cancion)
    elif opcion == "4":
        cancion = input("Nombre de la canción a buscar: ")
        gestormusicajson_be.buscar_cancion(cancion)
    elif opcion == "5":
        gestormusicajson_be.recomendar_cancion()
    elif opcion == "6":
        print("Saliendo del gestor...")
       
        break
    else:
        print("Inválida. Intenta de nuevo.")
