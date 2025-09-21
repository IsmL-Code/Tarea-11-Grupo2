# -----------------------------
# Sistema de Gestión de Pacientes - Versión Básica
# -----------------------------

pacientes = []
citas = []
historias = []

def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    genero = input("Género: ")
    condicion = input("Condición médica: ")
    paciente = {
        "id": len(pacientes) + 1,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "condicion": condicion
    }
    pacientes.append(paciente)
    print("Paciente registrado con éxito.")

def programar_cita():
    id_paciente = int(input("ID del paciente: "))
    doctor = input("Nombre del doctor: ")
    fecha = input("Fecha (dd-mm-aaaa): ")
    hora = input("Hora (HH:MM): ")

    # Validar si ya existe una cita en ese horario
    for cita in citas:
        if cita["fecha"] == fecha and cita["hora"] == hora and cita["doctor"] == doctor:
            print("Error: ese horario ya está ocupado.")
            return

    cita = {
        "id": len(citas) + 1,
        "id_paciente": id_paciente,
        "doctor": doctor,
        "fecha": fecha,
        "hora": hora
    }
    citas.append(cita)
    print("Cita programada con éxito.")

def agregar_historia():
    id_paciente = int(input("ID del paciente: "))
    descripcion = input("Descripción del historial médico: ")
    historia = {
        "id": len(historias) + 1,
        "id_paciente": id_paciente,
        "descripcion": descripcion
    }
    historias.append(historia)
    print("Historial agregado con éxito.")

def mostrar_datos():
    print("\nPacientes:", pacientes)
    print("Citas:", citas)
    print("Historias:", historias)

# -----------------------------
# Menú Principal
# -----------------------------
def menu():
    while True:
        print("\n--- Sistema de Gestión Clínica ---")
        print("1. Registrar Paciente")
        print("2. Programar Cita")
        print("3. Agregar Historial Médico")
        print("4. Mostrar Datos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            programar_cita()
        elif opcion == "3":
            agregar_historia()
        elif opcion == "4":
            mostrar_datos()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

menu()
