import csv

# Función para mostrar el menú y obtener la selección del usuario
def mostrar_menu():
    regiones = ['Tarapacá', 'Antofagasta', 'Atacama', 'Maule', 'Valparaíso', 'Los Ríos', 'Ñuble']
    zonas = ['Norte', 'Norte', 'Norte', 'Centro', 'Centro', 'Sur', 'Sur']

    print("Seleccione la región donde desea ingresar el dato del temblor:")
    for i, (region, zona) in enumerate(zip(regiones, zonas), start=1):
        print(f"{i}. {region} ({zona})")

    while True:
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            if 1 <= opcion <= len(regiones):
                return regiones[opcion - 1], zonas[opcion - 1]
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

# Función para obtener el valor del temblor en grados Richter
def obtener_valor_temblor():
    while True:
        try:
            valor = float(input("Ingrese el valor del temblor en grados Richter: "))
            return valor
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

# Función para actualizar el archivo CSV
def actualizar_csv(region, valor, zona):
    # Abrir el archivo CSV en modo lectura y escritura
    archivo_csv = r"C:\Users\fcode\Downloads\3.6_Act_Registro_SismológicoZonas.csv"  # Reemplaza con la ruta a tu archivo CSV
    temp_csv = 'temp.csv'  # Archivo temporal para escribir los datos actualizados

    with open(archivo_csv, mode='r', newline='') as csv_file, \
         open(temp_csv, mode='w', newline='') as temp_file:

        reader = csv.reader(csv_file)
        writer = csv.writer(temp_file)

        # Escribir la cabecera
        header = next(reader)
        writer.writerow(header)

        # Actualizar el valor del temblor en la región correspondiente
        for row in reader:
            if row[0] == region and row[1] == zona:
                row.append(valor)
            writer.writerow(row)

    # Reemplazar el archivo original con el archivo temporal
    import os
    os.remove(archivo_csv)
    os.rename(temp_csv, archivo_csv)

    print(f"El valor del temblor en la región {region}, zona {zona} ha sido actualizado a {valor} grados Richter.")

def main():
    region, zona = mostrar_menu()
    valor_temblor = obtener_valor_temblor()
    actualizar_csv(region, valor_temblor, zona)


main()
