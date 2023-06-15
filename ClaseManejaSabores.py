from ClaseSabor import Sabor
import csv
class ManejaSabores:
    def __init__(self):
        self.sabores = []

    def cargar_sabores(self, archivo):
        with open(archivo, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                id_sabor = int(row[0])
                nombre = row[1]
                ingredientes = row[2]
                sabor = Sabor(id_sabor, nombre, ingredientes)
                self.sabores.append(sabor)

    def cargar_datos_sabores(maneja_sabores):
     maneja_sabores.cargar_sabores('sabores.csv')
     print("Datos de sabores cargados exitosamente.")