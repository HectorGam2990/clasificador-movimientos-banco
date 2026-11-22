# Clasificador de movimientos de banco

Este proyecto lee una lista de movimientos de banco y la ordena sola por categorías, como ventas, gasolina o nómina. Después hace un reporte con cuánto entró, cuánto salió y cuánto quedó.

Es un primer proyecto de automatización: hace en segundos un trabajo que a mano tomaría mucho tiempo y se puede equivocar.

**Aviso: todos los datos de ejemplo son inventados. No son movimientos reales de ninguna persona ni empresa.**

## Archivos

- `clasificador.py`: el programa en Python. Es el que hace todo el trabajo.
- `movimientos_ejemplo.csv`: la lista de movimientos de ejemplo. Es un archivo de tabla con 3 columnas: fecha, descripción y monto. El monto positivo es dinero que entra, el negativo es dinero que sale.
- `resumen.txt`: el reporte que crea el programa, para leerlo.
- `resumen.csv`: el mismo reporte en forma de tabla, para abrirlo en Excel o en Google Sheets.

## Cómo se corre

1. Abre la terminal en la carpeta de este proyecto.
2. Escribe este comando y pulsa Enter:

```bash
python3 clasificador.py
```

No hay que instalar nada extra: solo usa lo que ya trae Python.

## Qué sale en el reporte

El programa muestra en pantalla y guarda en `resumen.txt` y `resumen.csv`:

- Cuántos movimientos leyó.
- El total de ingresos (lo que entró).
- El total de gastos (lo que salió).
- El saldo, que es ingresos más gastos.
- El total por cada categoría, con cuántos movimientos tiene.

Si un movimiento no tiene ninguna palabra que el programa reconozca, lo marca como "Por revisar", para que una persona lo revise después.

## Ejemplo pequeño

Entrada, en `movimientos_ejemplo.csv`:

```csv
fecha,descripcion,monto
2026-11-01,Venta a cliente - Tienda La Esquina,4500.00
2026-11-03,Gasolina - Estacion Veracruz,-600.00
2026-11-08,Nomina - Sueldo empleado Luis,-5000.00
```

Salida, en `resumen.txt`:

```text
Total de movimientos: 18
Total de ingresos: $14050.00
Total de gastos: $-16100.00
Saldo (ingresos + gastos): $-2050.00

Totales por categoria:
- Comida: 2 movimientos, $-1030.00
- Gasolina: 2 movimientos, $-1150.00
- Nomina: 2 movimientos, $-10000.00
- Por revisar: 1 movimiento, $-120.00
- Proveedores: 2 movimientos, $-2700.00
- Servicios: 3 movimientos, $-1100.00
- Ventas e ingresos: 6 movimientos, $14050.00
```

## Qué demuestra este proyecto para DIPROLAC

- **Python:** el programa está hecho en Python, uno de los lenguajes que pide la vacante.
- **CSV:** lee archivos de tabla (CSV), que es uno de los formatos que pide la vacante.
- **Clasificación automática:** ordena cada movimiento en su categoría sin hacerlo a mano, como pide la vacante para conciliar bancos y clasificar gastos.
- **Reportes:** crea un resumen claro con totales por categoría, ingresos, gastos y saldo, listo para revisar o compartir.
