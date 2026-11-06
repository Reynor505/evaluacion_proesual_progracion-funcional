import csv
import os

ARCHIVO = "inventario.csv"
CAMPOS = ["codigo", "nombre", "precio", "cantidad"]
productos = []  # lista de diccionarios

def cargar_productos():
    """Lee el CSV al iniciar. Si no existe, empieza con lista vacía."""
    if not os.path.exists(ARCHIVO):
        return
    try:
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                productos.append({
                    "codigo": fila["codigo"],
                    "nombre": fila["nombre"],
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"]),
                })
        print(f"Se cargaron {len(productos)} productos desde {ARCHIVO}")
    except (OSError, KeyError, ValueError):
        print("Error al leer el archivo. Se inicia con inventario vacío.")
        productos.clear()


def guardar_productos():
    """Escribe todos los productos en el CSV."""
    try:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(productos)
    except OSError:
        print("No se pudo guardar el archivo.")



def codigo_valido(codigo):
    """Formato PROD-001: 'PROD-' seguido de 3 dígitos."""
    return len(codigo) == 8 and codigo[:5] == "PROD-" and codigo[5:].isdigit()


def buscar_producto(codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None


def pedir_precio():
    while True:
        try:
            precio = float(input("Precio unitario: "))
            if precio > 0:
                return precio
            print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Ingrese un número válido aqui.")


def pedir_cantidad(mensaje):
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad >= 0:
                return cantidad
            print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Ingrese un número entero aqui.")


def registrar_producto():
    codigo = input("Código (ej: PROD-001): ").strip().upper()
    if not codigo_valido(codigo):
        print("Formato inválido. Use PROD-001.")
        return
    if buscar_producto(codigo) is not None:
        print("Ese código ya existe.")
        return
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    precio = pedir_precio()
    cantidad = pedir_cantidad("Cantidad disponible: ")
    productos.append({"codigo": codigo, "nombre": nombre,
                      "precio": precio, "cantidad": cantidad})
    guardar_productos()
    print("Producto registrado correctamente.")


def consultar_productos():
    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    print(f"{'CÓDIGO':<10}{'NOMBRE':<25}{'PRECIO':>10}{'CANT.':>8}")
    for p in productos:
        print(f"{p['codigo']:<10}{p['nombre']:<25}{p['precio']:>10.2f}{p['cantidad']:>8}")


def actualizar_cantidad():
    codigo = input("Código del producto a actualizar: ").strip().upper()
    producto = buscar_producto(codigo)
    if producto is None:
        print("El producto no está registrado.")
        return
    print(f"{producto['nombre']} - cantidad actual: {producto['cantidad']}")
    nueva = pedir_cantidad("Nueva cantidad: ")
    producto["cantidad"] = nueva
    guardar_productos()
    print("Cantidad actualizada correctamente.")


def menu():
    cargar_productos()
    opcion = ""
    while opcion != "4":
        print("\n=== INVENTARIO DE LA DISTRIBUIDORA ===")
        print("1. Registrar un nuevo producto")
        print("2. Consultar los productos registrados")
        print("3. Actualizar la cantidad de un producto")
        print("4. Salir")
        opcion = input("Elija una opción: ").strip()
        match opcion:
            case "1":
                registrar_producto()
            case "2":
                consultar_productos()
            case "3":
                actualizar_cantidad()
            case "4":
                print("Hasta luego.")
            case _:
                print("Opción inválida.")


menu()
        