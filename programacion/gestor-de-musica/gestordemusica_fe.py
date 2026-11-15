import gestordemusica_be

while True:
    print("\n====  GESTOR DE MUSICA ====")
    print("   1. Agregar canción")
    print("   2. Ver canciones")
    print("   3. Eliminar canción")
    print("   4. Buscar canción")
    print("   5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        cancion = input("Nombre de la canción a agregar: ")
        autor = input("Nombre del autor: ")
        gestordemusica_be.agregar_cancion(cancion, autor)
    elif opcion == "2":
        gestordemusica_be.ver_canciones()
    elif opcion == "3":
        cancion = input("Nombre de la canción a eliminar: ")
        gestordemusica_be.eliminar_cancion(cancion)
    elif opcion == "4":
        cancion = input("Nombre de la canción a buscar: ")
        gestordemusica_be.buscar_cancion(cancion)
    elif opcion == "5":
        print("Saliendo del gestor...")
        break
    else:
        print("Inválida. Intenta de nuevo.")
      

