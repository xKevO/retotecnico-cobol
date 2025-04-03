import csv

def procesar_transacciones(nombre_archivo):
    # Variables para almacenar los resultados
    balance = 0.0
    mayor_monto = 0.0
    id_mayor = None
    conteo = {"Crédito": 0, "Débito": 0}

    # Abrimos el archivo CSV en modo lectura
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)  # Lee cada fila como un diccionario
        for fila in lector:
            tipo = fila["tipo"]
            monto = float(fila["monto"])
            trans_id = fila["id"]

            # Actualizamos el balance según el tipo de transacción
            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1

            # Verificamos si esta transacción tiene el mayor monto hasta ahora
            if monto > mayor_monto:
                mayor_monto = monto
                id_mayor = trans_id

    # Mostramos el reporte final en consola
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")


# Punto de entrada del programa
if __name__ == "__main__":
    procesar_transacciones("transacciones.csv")
