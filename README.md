# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python que procesa un archivo CSV con transacciones bancarias y genera un reporte con información clave.

## 📌 Objetivo

Leer un archivo CSV con transacciones bancarias y generar un reporte que incluya:
- **Balance Final:** Créditos menos Débitos.
- **Transacción de Mayor Monto:** ID y monto de la transacción más alta.
- **Conteo de Transacciones:** Número total de Créditos y Débitos.

## 🛠️ Instrucciones de Ejecución

1. Clona este repositorio:
   ```
   git clone https://github.com/xKevO/retotecnico-cobol.git
   cd retotecnico-cobol
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   .\venv\Scripts\activate    # Windows
   ```

3. Ejecuta el programa pasando como argumento el archivo CSV:
   ```
   python main.py transacciones.csv
   ```

## 📂 Estructura del Proyecto

```
retotecnico-cobol/
├── main.py                 # Código principal de la aplicación
├── transacciones.csv       # Archivo CSV de ejemplo con transacciones
└── README.md               # Documentación del proyecto
```

## ⚙️ Enfoque y Solución

- Se utiliza el módulo `csv` de Python para leer el archivo.
- Se hace uso de `argparse` para permitir pasar el nombre del archivo como argumento.
- El programa calcula el balance final, identifica la transacción con mayor monto y cuenta las transacciones por tipo.
- Se agregaron validaciones para manejar errores comunes como archivo no encontrado.

## ✅ Ejemplo de salida

```
Reporte de Transacciones
---------------------------------------------
Balance Final: 2134.25
Transacción de Mayor Monto: ID 3 - 992.84
Conteo de Transacciones: Crédito: 12 Débito: 8
```

## 📌 Autor

Desarrollado por Kevin Malca — [@xKevO](https://github.com/xKevO)