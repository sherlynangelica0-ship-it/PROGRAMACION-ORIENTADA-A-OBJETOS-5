class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []   # Lista de productos
        self.clientes = []    # Lista de clientes

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n--- PRODUCTOS DEL RESTAURANTE ---")
        for producto in self.productos:
            producto.mostrar_informacion()
            print()

    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            cliente.mostrar_informacion()
            print()