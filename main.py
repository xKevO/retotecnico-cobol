import csv
import argparse

def procesar_transacciones(nombre_archivo):
    # Variables para almacenar resultados
    balance = 0.0
    mayor_monto = 0.0
    id_mayor = None
    conteo = {"Crédito": 0, "Débito": 0}

    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                tipo = fila["tipo"]
                monto = float(fila["monto"])
                trans_id = fila["id"]

                # Actualizamos el balance y conteo según el tipo
                if tipo == "Crédito":
                    balance += monto
                    conteo["Crédito"] += 1
                elif tipo == "Débito":
                    balance -= monto
                    conteo["Débito"] += 1

                # Comprobamos si es el mayor monto
                if monto > mayor_monto:
                    mayor_monto = monto
                    id_mayor = trans_id

        # Imprimir el reporte final
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")


if __name__ == "__main__":
    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description="Procesar transacciones bancarias desde un archivo CSV.")
    parser.add_argument("archivo", help="Ruta del archivo CSV a procesar")
    args = parser.parse_args()

    # Llamar a la función principal con el archivo dado
    procesar_transacciones(args.archivo)
