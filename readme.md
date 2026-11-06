# Inventario de Productos – Distribuidora

## Descripción
Prototipo en Python (consola) para modernizar el sistema legado de inventario de una pequeña distribuidora comercial.

## Problema que resuelve
El inventario se llevaba en archivos de texto y hojas de cálculo, sin validaciones: había productos duplicados, cantidades incorrectas y registros inconsistentes.

## Funcionalidades
- Registrar un nuevo producto (código, nombre, precio, cantidad).
- Consultar los productos registrados.
- Actualizar la cantidad disponible de un producto.
- Validaciones: código con formato PROD-001 y sin duplicados, nombre no vacío, precio > 0, cantidad entera ≥ 0.
- Manejo de errores con `try-except`.
- Persistencia en `productos.csv`.

## Ejecución
1. Instalar Python 3.
2. Ejecutar: `python inventario.py`

## Integrantes
- Ronald Cruz Chino
- Denislson Davis Machaca Flores
- Daniel Wilfredo Pomarez Huaranca

Materia: Programación Fundamental
