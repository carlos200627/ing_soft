estudiantes = []

promedio_aprobatorio = 70


def pedir_texto(mensaje):
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto != "":
            valido = True
        else:
            print("Error:no puede quedar vacío.")
    return texto


def buscar_estudiante(id_estudiante):
    for estudiante in estudiantes:
        if estudiante["id"] == id_estudiante:
            return estudiante
    return None


def pedir_id():
    valido = False
    while not valido:
        id_estudiante = pedir_texto("Número de id: ")
        if buscar_estudiante(id_estudiante) is not None:
            print("Error: ya existe ese id.")
        else:
            valido = True
    return id_estudiante


def pedir_calificacion(numero):
    valido = False
    while not valido:
        texto = input(f"Calificación {numero} (0-100): ").strip()
        if texto.replace(".", "", 1).isdigit():
            calificacion = float(texto)
            if calificacion >= 0 and calificacion <= 100:
                valido = True
            else:
                print("Error: la calificación debe estar entre 0 y 100.")
        else:
            print("Error: escribe un número válido entre 0 y 100.")
    return calificacion


def calcular_promedio(calificaciones):
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion
    return suma / len(calificaciones)


def obtener_situacion(promedio):
    if promedio >= promedio_aprobatorio:
        return "Aprobado"
    return "Reprobado"


def registrar_estudiante():
    id_estudiante = pedir_id()
    nombre = pedir_texto("Nombre: ")
    calificaciones = (pedir_calificacion(1), pedir_calificacion(2), pedir_calificacion(3))
    promedio = calcular_promedio(calificaciones)
    situacion = obtener_situacion(promedio)

    estudiantes.append({
        "id": id_estudiante,
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "situacion": situacion,
    })
    print(f"'{nombre}' fue registrado. Promedio: {promedio:.2f} - {situacion}")


def mostrar_estudiantes():
    if not estudiantes:
        print("Todavía no hay estudiantes registrados.")
        return

    print("\n--- ESTUDIANTES ---")
    for estudiante in estudiantes:
        c1, c2, c3 = estudiante["calificaciones"]
        print(f"{estudiante['id']} | {estudiante['nombre']} | "
              f"{c1:.1f}, {c2:.1f}, {c3:.1f} | "
              f"Promedio: {estudiante['promedio']:.2f} | {estudiante['situacion']}")


def consultar_promedio(id_estudiante):
    if not estudiantes:
        print("Todavía no hay estudiantes registrados.")
        return

    estudiante = buscar_estudiante(id_estudiante)
    if estudiante is None:
        print(f"No se encontró el id '{id_estudiante}'.")
    else:
        print(f"{estudiante['nombre']}: promedio {estudiante['promedio']:.2f} "
              f"- {estudiante['situacion']}")


def mostrar_estadisticas():
    if not estudiantes:
        print("Todavía no hay estudiantes registrados.")
        return

    suma_promedios = 0
    aprobados = 0
    reprobados = 0
    promedio_mas_alto = estudiantes[0]["promedio"]

    for estudiante in estudiantes:
        suma_promedios += estudiante["promedio"]
        if estudiante["situacion"] == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1
        if estudiante["promedio"] > promedio_mas_alto:
            promedio_mas_alto = estudiante["promedio"]

    print("\n--- ESTADÍSTICAS DEL GRUPO ---")
    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Promedio general: {suma_promedios / len(estudiantes):.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio más alto: {promedio_mas_alto:.2f}")
    
