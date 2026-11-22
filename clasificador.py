"""
Clasificador de movimientos de banco
=====================================
Lee un archivo CSV con movimientos, los clasifica por palabras clave
y crea un reporte con los totales por categoria.

Solo usa la libreria estandar de Python: no hay que instalar nada.

Archivos de entrada y salida:
- Entrada: movimientos_ejemplo.csv
- Salida: resumen.txt (para leer) y resumen.csv (para abrir en Excel)
"""

import csv
from collections import defaultdict

# Nombre de los archivos que usa el programa
ARCHIVO_ENTRADA = "movimientos_ejemplo.csv"
ARCHIVO_REPORTE_TEXTO = "resumen.txt"
ARCHIVO_REPORTE_CSV = "resumen.csv"

# Palabras clave para clasificar cada movimiento.
# Si la descripcion contiene una de estas palabras, va a esa categoria.
# El orden importa: se revisa de arriba a abajo y se queda la primera que coincida.
CATEGORIAS = {
    "Ventas e ingresos": ["venta", "ventas", "ingreso", "cliente", "factura"],
    "Proveedores": ["proveedor", "compra a proveedor", "insumos"],
    "Gasolina": ["gasolina", "combustible", "gasolinera"],
    "Servicios": ["luz", "internet", "telefono", "agua", "cfe"],
    "Comida": ["comida", "restaurante", "supermercado", "abarrotes"],
    "Nomina": ["nomina", "sueldo", "salario"],
}


def clasificar(descripcion):
    """Devuelve la categoria de un movimiento segun su descripcion.

    Si ninguna palabra clave coincide, devuelve "Por revisar".
    """
    texto = descripcion.lower()
    for categoria, palabras in CATEGORIAS.items():
        for palabra in palabras:
            if palabra in texto:
                return categoria
    return "Por revisar"


def main():
    # Totales por categoria: cantidad de movimientos y suma de montos
    totales = defaultdict(lambda: {"cantidad": 0, "total": 0.0})
    total_ingresos = 0.0
    total_gastos = 0.0
    cantidad_movimientos = 0

    # 1. Leer el archivo CSV
    # Se saltan las lineas que empiezan con # : son avisos, no datos.
    with open(ARCHIVO_ENTRADA, encoding="utf-8") as archivo:
        lineas_datos = [linea for linea in archivo if not linea.startswith("#")]
        lector = csv.DictReader(lineas_datos)
        for fila in lector:
            descripcion = fila["descripcion"]
            monto = float(fila["monto"])
            categoria = clasificar(descripcion)

            # 2. Sumar a su categoria
            totales[categoria]["cantidad"] += 1
            totales[categoria]["total"] += monto

            # 3. Sumar a ingresos o a gastos
            if monto > 0:
                total_ingresos += monto
            else:
                total_gastos += monto

            cantidad_movimientos += 1

    saldo = total_ingresos + total_gastos

    # 4. Escribir el reporte en texto (resumen.txt)
    lineas = []
    lineas.append("RESUMEN DE MOVIMIENTOS DE BANCO")
    lineas.append("==============================")
    lineas.append("Datos de ejemplo: son inventados, no son reales.")
    lineas.append("")
    lineas.append(f"Total de movimientos: {cantidad_movimientos}")
    lineas.append(f"Total de ingresos: ${total_ingresos:.2f}")
    lineas.append(f"Total de gastos: ${total_gastos:.2f}")
    lineas.append(f"Saldo (ingresos + gastos): ${saldo:.2f}")
    lineas.append("")
    lineas.append("Totales por categoria:")
    for categoria in sorted(totales):
        datos = totales[categoria]
        palabra = "movimiento" if datos["cantidad"] == 1 else "movimientos"
        lineas.append(
            f"- {categoria}: {datos['cantidad']} {palabra}, "
            f"${datos['total']:.2f}"
        )

    with open(ARCHIVO_REPORTE_TEXTO, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas) + "\n")

    # 5. Escribir el mismo resumen en CSV (resumen.csv)
    with open(ARCHIVO_REPORTE_CSV, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["categoria", "cantidad_movimientos", "total_monto"])
        for categoria in sorted(totales):
            datos = totales[categoria]
            escritor.writerow(
                [categoria, datos["cantidad"], f"{datos['total']:.2f}"]
            )

    # 6. Mostrar el resultado en pantalla
    print("\n".join(lineas))
    print("")
    print(f"Reporte guardado en {ARCHIVO_REPORTE_TEXTO}")
    print(f"Reporte guardado en {ARCHIVO_REPORTE_CSV}")


if __name__ == "__main__":
    main()
