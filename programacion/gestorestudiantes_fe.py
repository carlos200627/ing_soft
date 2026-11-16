import gestorestudiantes_be

continuar = True
while continuar:
    print("\n==== GESTOR DE ESTUDIANTES ====")
    print("   1. Registrar un estudiante")
    print("   2. Mostrar todos los estudiantes")
    print("   3. Consultar el promedio de un estudiante")
    print("   4. Mostrar estadísticas del grupo")
    print("   5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        gestorestudiantes_be.registrar_estudiante()
    elif opcion == "2":
        gestorestudiantes_be.mostrar_estudiantes()
    elif opcion == "3":
        id_estudiante = input("Id del estudiante a consultar: ").strip()
        gestorestudiantes_be.consultar_promedio(id_estudiante)
    elif opcion == "4":
        gestorestudiantes_be.mostrar_estadisticas()
    elif opcion == "5":
        print("Saliendo del programa...")
        continuar = False
    else:
        print("Inexistente.")
