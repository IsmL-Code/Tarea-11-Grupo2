import asyncio

# -------------------------------
# MODELOS
# -------------------------------
class Producto:
    def __init__(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - ${self.precio} | Stock: {self.stock}"


class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = []


class Pedido:
    def __init__(self, usuario, productos, total):
        self.usuario = usuario
        self.productos = productos
        self.total = total
        self.estado = "Pendiente"

    def __str__(self):
        return f"Pedido de {self.usuario.nombre} - Total: ${self.total} - Estado: {self.estado}"


# -------------------------------
# SERVICIOS / GESTORES
# -------------------------------
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_nombre(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None

    def listar_productos(self):
        return self.productos


class Inventario:
    def actualizar_stock(self, producto, cantidad):
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            return True
        return False

    def mostrar_inventario(self, catalogo):
        if not catalogo.productos:
            print("⚠️ No hay productos en el inventario.")
            return
        print("\n=== Inventario ===")
        for p in catalogo.productos:
            print(p)


class Pago:
    async def procesar_pago(self, usuario, total):
        print(f"\n=== Confirmación de pago para {usuario.nombre} ===")
        metodo = input("Seleccione método de pago (efectivo / transferencia / tarjeta): ").lower()

        if metodo not in ["efectivo", "transferencia", "tarjeta"]:
            print("Método de pago no válido. Operación cancelada.")
            return False

        print(f"Procesando pago de ${total} mediante {metodo} para {usuario.nombre}...")
        await asyncio.sleep(1)  # simulación
        print("✅ Pago exitoso")
        return True


class SistemaPedidos:
    def __init__(self, inventario, pago):
        self.inventario = inventario
        self.pago = pago
        self.pedidos = []

    async def crear_pedido(self, usuario):
        if not usuario.carrito:
            print("⚠️ El carrito está vacío, no se puede crear un pedido.")
            return None

        total = sum([p.precio for p in usuario.carrito])
        # Verificar stock
        for p in usuario.carrito:
            if p.stock <= 0:
                print(f"⚠️ Producto {p.nombre} sin stock.")
                return None

        # Descontar inventario
        for p in usuario.carrito:
            self.inventario.actualizar_stock(p, 1)

        # Procesar pago
        exito = await self.pago.procesar_pago(usuario, total)
        if not exito:
            print("❌ Error en el pago.")
            return None

        # Crear pedido
        pedido = Pedido(usuario, usuario.carrito[:], total)
        self.pedidos.append(pedido)
        usuario.carrito.clear()
        print("✅ Pedido creado:", pedido)
        return pedido

    def mostrar_pedidos(self):
        if not self.pedidos:
            print("⚠️ No hay pedidos realizados todavía.")
            return
        print("\n=== Ventas realizadas ===")
        for ped in self.pedidos:
            print(ped)


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
async def programa_principal():
    # Inicialización
    catalogo = Catalogo()
    inventario = Inventario()
    pago = Pago()
    sistema = SistemaPedidos(inventario, pago)
    usuario = None

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar producto")
        print("2. Registrar usuario")
        print("3. Ver catálogo disponible")
        print("4. Añadir productos al carrito")
        print("5. Crear pedido")
        print("6. Consultar inventario")
        print("7. Consultar ventas realizadas")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            marca = input("Marca: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))
            catalogo.agregar_producto(Producto(nombre, marca, precio, stock))
            print(f"✅ Producto '{nombre}' agregado al catálogo.")

        elif opcion == "2":
            nombre_u = input("Nombre del usuario: ")
            correo_u = input("Correo del usuario: ")
            usuario = Usuario(nombre_u, correo_u)
            print(f"✅ Usuario '{usuario.nombre}' registrado.")

        elif opcion == "3":
            print("\n--- Catálogo disponible ---")
            for p in catalogo.listar_productos():
                print(p)

        elif opcion == "4":
            if usuario is None:
                print("⚠️ Primero debe registrar un usuario.")
                continue
            nombre_producto = input("Ingrese el nombre del producto a añadir al carrito: ")
            producto = catalogo.buscar_por_nombre(nombre_producto)
            if producto:
                if producto.stock > 0:
                    usuario.carrito.append(producto)
                    print(f"✅ {producto.nombre} añadido al carrito.")
                else:
                    print(f"⚠️ {producto.nombre} está agotado.")
            else:
                print("⚠️ Producto no encontrado en el catálogo.")

        elif opcion == "5":
            if usuario is None:
                print("⚠️ Primero debe registrar un usuario.")
                continue
            print("\nCarrito de", usuario.nombre, ":", [p.nombre for p in usuario.carrito])
            await sistema.crear_pedido(usuario)

        elif opcion == "6":
            inventario.mostrar_inventario(catalogo)

        elif opcion == "7":
            sistema.mostrar_pedidos()

        elif opcion == "8":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida, intente de nuevo.")


# -------------------------------
# EJECUCIÓN SEGURA
# -------------------------------
def main():
    try:
        asyncio.run(programa_principal())
    except RuntimeError:
        # Para entornos como Jupyter
        loop = asyncio.get_event_loop()
        loop.run_until_complete(programa_principal())


if __name__ == "__main__":
    main()
