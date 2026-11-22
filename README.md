# Clasificador de movimientos de banco

Hice este programa para no clasificar movimientos a mano. Le paso una lista en CSV y él solo los separa por categoría y me dice cuánto entró, cuánto salió y cuánto quedó.

Los datos que trae son inventados, solo son de ejemplo.

## Qué hay aquí

- `clasificador.py`, el programa
- `movimientos_ejemplo.csv`, la lista de ejemplo con fecha, descripción y monto
- `resumen.txt` y `resumen.csv`, el reporte que genera

## Cómo lo corro

Abro la terminal en esta carpeta y pongo:

```bash
python3 clasificador.py
```

No hay que instalar nada, solo usa lo que ya trae Python.

## Qué hace

Lee cada movimiento y busca palabras como venta, gasolina, luz, nómina, etc. y lo pone en su categoría. Si no reconoce nada lo deja como "Por revisar" para verlo después. Al final suma todo por categoría.

Un ejemplo de lo que trae:

```csv
fecha,descripcion,monto
2026-11-01,Venta a cliente - Tienda La Esquina,4500.00
2026-11-03,Gasolina - Estacion Veracruz,-600.00
2026-11-08,Nomina - Sueldo empleado Luis,-5000.00
```

Y el reporte que sale es algo así:

```text
Total de movimientos: 18
Total de ingresos: $14050.00
Total de gastos: $-16100.00
Saldo (ingresos + gastos): $-2050.00
```

Lo hice para practicar Python y el manejo de archivos CSV y reportes.
