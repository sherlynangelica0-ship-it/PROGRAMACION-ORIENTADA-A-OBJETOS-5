class Producto:
    def __init__(self, nombre, precio, categoria, disponible):
        self.nombre = nombre          # str
        self.precio = precio          # float
        self.categoria = categoria    # str
        self.disponible = disponible  # bool

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Categoría: {self.categoria}")
        print(f"Estado: {estado}")