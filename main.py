import csv
import argparse

def procesar_transacciones(nombre_archivo):
    """
    Procesa un archivo CSV de transacciones y genera un reporte en consola.

    Este método lee un archivo CSV que contiene transacciones con los campos 
    "tipo", "monto" e "id". Calcula el balance final, identifica la transacción 
    con el mayor monto y cuenta la cantidad de transacciones de tipo "Crédito" 
    y "Débito". Finalmente, imprime un reporte con los resultados.

    Args:
        nombre_archivo (str): Ruta del archivo CSV que contiene las transacciones.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe.
        ValueError: Si se encuentra un monto no numérico en el archivo.
        csv.Error: Si hay un error al leer el archivo CSV.
        Exception: Para cualquier otro error inesperado.

    Reporte generado:
        - Balance final de las transacciones.
        - ID y monto de la transacción con el mayor monto.
        - Conteo de transacciones por tipo ("Crédito" y "Débito").
    """

    # Inicialización de variables para el reporte
    balance = 0.0
    mayor_monto = 0.0
    id_mayor = None
    conteo = {"Crédito": 0, "Débito": 0}

    try:
        # Abrimos el archivo CSV y leemos sus filas como diccionarios
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Extraemos tipo, monto e ID de la transacción
                tipo = fila["tipo"]
                monto = float(fila["monto"])
                trans_id = fila["id"]

                # Procesamos la transacción según su tipo
                if tipo == "Crédito":
                    balance += monto
                    conteo["Crédito"] += 1
                elif tipo == "Débito":
                    balance -= monto
                    conteo["Débito"] += 1

                # Comprobamos si es el nuevo mayor monto
                if monto > mayor_monto:
                    mayor_monto = monto
                    id_mayor = trans_id

        # Mostramos el reporte final en consola
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except ValueError:
        print("Error: Se encontró un monto inválido. Asegúrate de que todos los montos sean numéricos.")
    except csv.Error:
        print("Error al leer el archivo CSV. Verifica su formato.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Punto de entrada del programa: captura el nombre del archivo desde la terminal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesar transacciones bancarias desde un archivo CSV.")
    parser.add_argument("archivo", help="Ruta del archivo CSV a procesar")
    args = parser.parse_args()
    procesar_transacciones(args.archivo)
