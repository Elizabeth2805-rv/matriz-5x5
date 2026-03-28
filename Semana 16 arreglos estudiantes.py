estudiantes = []
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)
    print("Estudiante agregado correctamente.\n")
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.\n")
    else:
        print("Lista de estudiantes:")
        for i, estudiante in enumerate(estudiantes):
            print(f"{i + 1}. {estudiante}")
        print()
def buscar_estudiante():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in estudiantes:
        print("El estudiante sí está en la lista.\n")
    else:
        print("El estudiante no se encontró.\n")
def eliminar_estudiante():
    nombre = input("Ingrese el nombre a eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
        print("Estudiante eliminado correctamente.\n")
    else:
        print("El estudiante no se encontró.\n")
def menu():
    while True:
        print("=== MENÚ ===")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")
menu()
