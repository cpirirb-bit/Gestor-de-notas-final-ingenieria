from collections import deque

# =========================================
# FUNCIONES PRINCIPALES
# =========================================

def mostrar_menu():
    print("\n===============================")
    print("   GESTOR DE NOTAS ACADÉMICAS  ")
    print("===============================")
    print("1. Registrar nuevo curso y nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio general")
    print("4. Buscar curso por nombre")
    print("5. Actualizar nota de un curso")
    print("6. Eliminar curso")
    print("7. Ver historial (Pila)")
    print("8. Revisiones pendientes (Cola)")
    print("9. Ordenar notas (Burbuja e Inserción)")
    print("0. Salir")
    print("===============================")


# =========================================
# FUNCIONALIDADES BÁSICAS
# =========================================

def registrar_curso(notas, historial, revisiones):
    curso = input("Ingrese el nombre del curso: ")
    if curso in notas:
        print(" Ese curso ya está registrado.")
        return
    try:
        nota = float(input("Ingrese la nota (0 - 100): "))
    except ValueError:
        print(" Nota inválida. Debe ser un número.")
        return
    notas[curso] = nota
    historial.append(f"Registrado curso '{curso}' con nota {nota}")
    revisiones.append(f"Revisión pendiente: {curso}")
    print(f" Curso '{curso}' registrado correctamente.")


def mostrar_notas(notas):
    if not notas:
        print(" No hay cursos registrados.")
    else:
        print("\n=== LISTA DE NOTAS ===")
        for curso, nota in notas.items():
            print(f"{curso}: {nota}")


def calcular_promedio(notas):
    if not notas:
        print(" No hay notas para calcular promedio.")
        return
    promedio = sum(notas.values()) / len(notas)
    print(f" Promedio general: {promedio:.2f}")


def buscar_curso(notas):
    nombre = input("Ingrese el nombre del curso a buscar: ")
    if nombre in notas:
        print(f" {nombre}: {notas[nombre]}")
    else:
        print(" Curso no encontrado.")


def actualizar_nota(notas, historial):
    nombre = input("Ingrese el curso a actualizar: ")
    if nombre in notas:
        try:
            nueva_nota = float(input("Ingrese la nueva nota: "))
        except ValueError:
            print(" Valor inválido.")
            return
        notas[nombre] = nueva_nota
        historial.append(f"Actualizada nota de '{nombre}' a {nueva_nota}")
        print(" Nota actualizada correctamente.")
    else:
        print(" Curso no encontrado.")


def eliminar_curso(notas, historial):
    nombre = input("Ingrese el curso a eliminar: ")
    if nombre in notas:
        del notas[nombre]
        historial.append(f"Eliminado curso '{nombre}'")
        print(" Curso eliminado correctamente.")
    else:
        print(" Curso no encontrado.")


# =========================================
# FUNCIONES DE ESTRUCTURAS DE DATOS
# =========================================

def ver_historial(historial):
    if not historial:
        print(" No hay acciones registradas en el historial.")
    else:
        print("\n=== HISTORIAL DE ACCIONES ===")
        for accion in reversed(historial):  # LIFO
            print("-", accion)


def ver_revisiones(revisiones):
    if not revisiones:
        print(" No hay revisiones pendientes.")
    else:
        print("\n=== REVISIÓN DE COLA ===")
        while revisiones:
            print("", revisiones.popleft())


# =========================================
# FUNCIONES DE ORDENAMIENTO
# =========================================

def ordenar_notas(notas):
    if not notas:
        print(" No hay notas para ordenar.")
        return

    lista_notas = list(notas.items())

    print("\nOrdenamiento por Burbuja:")
    burbuja = lista_notas[:]
    for i in range(len(burbuja) - 1):
        for j in range(len(burbuja) - i - 1):
            if burbuja[j][1] > burbuja[j + 1][1]:
                burbuja[j], burbuja[j + 1] = burbuja[j + 1], burbuja[j]
    for curso, nota in burbuja:
        print(f"{curso}: {nota}")

    print("\nOrdenamiento por Inserción:")
    insercion = lista_notas[:]
    for i in range(1, len(insercion)):
        actual = insercion[i]
        j = i - 1
        while j >= 0 and insercion[j][1] > actual[1]:
            insercion[j + 1] = insercion[j]
            j -= 1
        insercion[j + 1] = actual
    for curso, nota in insercion:
        print(f"{curso}: {nota}")


# =========================================
# FUNCIÓN PRINCIPAL (MAIN)
# =========================================

def main():
    notas = {}
    historial = []
    revisiones = deque()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print(" Ingrese un número válido.")
            continue

        if opcion == 1:
            registrar_curso(notas, historial, revisiones)
        elif opcion == 2:
            mostrar_notas(notas)
        elif opcion == 3:
            calcular_promedio(notas)
        elif opcion == 4:
            buscar_curso(notas)
        elif opcion == 5:
            actualizar_nota(notas, historial)
        elif opcion == 6:
            eliminar_curso(notas, historial)
        elif opcion == 7:
            ver_historial(historial)
        elif opcion == 8:
            ver_revisiones(revisiones)
        elif opcion == 9:
            ordenar_notas(notas)
        elif opcion == 0:
            print(" Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# =========================================
# EJECUCIÓN
# =========================================
if __name__ == "__main__":
    main()
