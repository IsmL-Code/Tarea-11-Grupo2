# ecommerce_basic.py
# Solución básica: prototipo sencillo en memoria

products = [
    {"id": 1, "name": "Camiseta", "category": "Ropa", "price": 20.0, "stock": 10},
    {"id": 2, "name": "Taza", "category": "Hogar", "price": 8.5, "stock": 5},
]

users = [
    {"id": 1, "username": "juan", "password": "1234", "profile": {"email": "juan@mail.com"}}
]

orders = []
carts = {}  # user_id -> list of {"product_id", "qty"}

def listar_productos():
    for p in products:
        print(p)

def buscar_productos(term):
    term_l = term.lower()
    return [p for p in products if term_l in p["name"].lower() or term_l in p["category"].lower()]

def agregar_al_carrito(user_id, product_id, qty):
    cart = carts.setdefault(user_id, [])
    cart.append({"product_id": product_id, "qty": qty})
    print("Agregado al carrito.")

def ver_carrito(user_id):
    cart = carts.get(user_id, [])
    for item in cart:
        p = next((x for x in products if x["id"] == item["product_id"]), None)
        print(p["name"], item["qty"], "->", p["price"] * item["qty"])

def procesar_pago_simulado(user_id):
    # Simula siempre pago exitoso (¡no real!)
    return {"status": "approved", "transaction_id": "TX123"}

def checkout(user_id):
    cart = carts.get(user_id, [])
    if not cart:
        print("Carrito vacío.")
        return
    total = 0
    for item in cart:
        p = next((x for x in products if x["id"] == item["product_id"]), None)
        if p is None or p["stock"] < item["qty"]:
            print("Producto no disponible o stock insuficiente.")
            return
        total += p["price"] * item["qty"]

    pago = procesar_pago_simulado(user_id)
    if pago["status"] == "approved":
        # decrementar stock
        for item in cart:
            p = next(x for x in products if x["id"] == item["product_id"])
            p["stock"] -= item["qty"]
        order = {"id": len(orders) + 1, "user_id": user_id, "items": cart, "total": total, "status": "processing"}
        orders.append(order)
        carts[user_id] = []
        print("Compra completada. Pedido ID:", order["id"])
    else:
        print("Pago rechazado.")

# Menú muy simple para demo
def menu():
    print("=== ECOMMERCE BÁSICO ===")
    while True:
        print("\n1 Listar productos\n2 Buscar\n3 Agregar al carrito\n4 Ver carrito\n5 Checkout\n6 Salir")
        op = input("Opción: ")
        if op == "1":
            listar_productos()
        elif op == "2":
            term = input("Buscar: ")
            print(buscar_productos(term))
        elif op == "3":
            uid = int(input("User id: "))
            pid = int(input("Product id: "))
            q = int(input("Cantidad: "))
            agregar_al_carrito(uid, pid, q)
        elif op == "4":
            uid = int(input("User id: "))
            ver_carrito(uid)
        elif op == "5":
            uid = int(input("User id: "))
            checkout(uid)
        elif op == "6":
            break
        else:
            print("Inválido.")

if __name__ == "__main__":
    menu()
