# -----------------------------
# Sistema de Gestión Clínica - Versión Mejorada
# -----------------------------

class Paciente:
    def __init__(self, pid, nombre, edad, genero, condicion):
        self.id = pid
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.condicion = condicion

class Cita:
    def __init__(self, cid, id_paciente, doctor, fecha, hora):
        self.id = cid
        self.id_paciente = id_paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

class Historia:
    def __init__(self, hid, id_paciente, descripcion):
        self.id = hid
        self.id_paciente = id_paciente
        self.descripcion = descripcion

# -----------------------------
# Managers
# -----------------------------

class PacienteManager:
    def __init__(self):
        self.pacientes = []

    def registrar(self, nombre, edad, genero, condicion):
        pid = len(self.pacientes) + 1
        paciente = Paciente(pid, nombre, edad, genero, condicion)
        self.pacientes.append(paciente)
        return paciente

class CitaManager:
    def __init__(self):
        self.citas = []

    def programar(self, id_paciente, doctor, fecha, hora):
        for cita in self.citas:
            if cita.fecha == fecha and cita.hora == hora and cita.doctor == doctor:
                raise ValueError("Horario ocupado con este doctor.")
        cid = len(self.citas) + 1
        cita = Cita(cid, id_paciente, doctor, fecha, hora)
        self.citas.append(cita)
        return cita

class HistoriaManager:
    def __init__(self):
        self.historias = []

    def agregar(self, id_paciente, descripcion):
        hid = len(self.historias) + 1
        historia = Historia(hid, id_paciente, descripcion)
        self.historias.append(historia)
        return historia

class FacturacionManager:
    def __init__(self):
        self.facturas = []

    def generar_factura(self, id_paciente, monto):
        factura = {"id_paciente": id_paciente, "monto": monto}
        self.facturas.append(factura)
        return factura

# -----------------------------
# Menú Principal
# -----------------------------
def menu():
    pacientes = PacienteManager()
    citas = CitaManager()
    historias = HistoriaManager()
    facturacion = FacturacionManager()

    while True:
        print("\n--- Sistema de Gestión Clínica (Versión Mejorada) ---")
        print("1. Registrar Paciente")
        print("2. Programar Cita")
        print("3. Agregar Historial Médico")
        print("4. Generar Factura")
        print("5. Mostrar Pacientes")
        print("6. Mostrar Citas")
        print("7. Mostrar Historias")
        print("8. Mostrar Facturas")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                genero = input("Género: ")
                condicion = input("Condición médica: ")
                paciente = pacientes.registrar(nombre, edad, genero, condicion)
                print(f"Paciente {paciente.nombre} registrado.")
            elif opcion == "2":
                id_paciente = int(input("ID Paciente: "))
                doctor = input("Doctor: ")
                fecha = input("Fecha (dd-mm-aaaa): ")
                hora = input("Hora (HH:MM): ")
                cita = citas.programar(id_paciente, doctor, fecha, hora)
                print(f"Cita programada con el Dr. {cita.doctor} en {cita.fecha} a las {cita.hora}")
            elif opcion == "3":
                id_paciente = int(input("ID Paciente: "))
                descripcion = input("Descripción: ")
                historia = historias.agregar(id_paciente, descripcion)
                print("Historial agregado con éxito.")
            elif opcion == "4":
                id_paciente = int(input("ID Paciente: "))
                monto = float(input("Monto de la factura: "))
                factura = facturacion.generar_factura(id_paciente, monto)
                print("Factura generada:", factura)
            elif opcion == "5":
                for p in pacientes.pacientes:
                    print(vars(p))
            elif opcion == "6":
                for c in citas.citas:
                    print(vars(c))
            elif opcion == "7":
                for h in historias.historias:
                    print(vars(h))
            elif opcion == "8":
                print(facturacion.facturas)
            elif opcion == "9":
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error:", e)

menu()
