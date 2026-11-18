import random 

archivo = "canciones.json"

canciones = []
autores = []

def cargar():
    open(archivo, "a").close()
    with open(archivo, "r") as f:
        for linea in f:
            if linea.strip() != "":
                partes = linea.strip().split(",")
                canciones.append(partes[0])
                if len(partes) > 1:
                    autores.append(partes[1])
                else:
                    autores.append("Desconocido")
                
def guardar():
    with open(archivo, "w") as f:
        for i in range(len(canciones)):
            f.write(canciones[i] + "," + autores[i] + "\n")

cargar()

def agregar_cancion(nombre,autor):
    canciones.append(nombre)
    autores.append(autor)
    guardar()
    print(f"'{nombre}' de {autor} fue agregada.")

def ver_canciones():
    if not canciones:
        print("La playlist está vacía.")
    else:
        print("\n--- TU PLAYLIST ---")
        for i, cancion in enumerate(canciones, start=1):
            print(f"{i}. {cancion} - {autores[i-1]}")

def eliminar_cancion(nombre):
    encontrada = False
    for i in range (len(canciones)):
        if canciones[i].lower() == nombre.lower():
            canciones.pop(i)
            autores.pop(i)
            guardar()
            print(f"'{nombre}' fue eliminada.")
            encontrada = True
            break
    if not encontrada:
        print(f"No se encontro '{nombre}'.")

def buscar_cancion(nombre):
    posiciones = [i for i in range(len(canciones)) if nombre.lower() in canciones[i].lower()]
    if posiciones:
        print("Canciones encontradas:")
        for i in posiciones:
            print(f"- {canciones[i]} - {autores[i]}")
    else:
        print(f"No hay coincidencias para '{nombre}'.")

def recomendar_cancion():
    if not canciones:
        print("No hay rolas")
        return 
    i = random.randrange(len(canciones))
    print(f"Cancion aleatoria: {canciones[i]} - {autores[i]}")
