from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante Sabor Casero")

# Crear productos
producto1 = Producto("Hamburguesa", 8.50, "Comida", True)
producto2 = Producto("Pizza", 12.00, "Comida", True)
producto3 = Producto("Jugo Natural", 3.25, "Bebida", False)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Crear clientes
cliente1 = Cliente("Ana López", 25, "0991111111", True)
cliente2 = Cliente("Carlos Pérez", 30, "0982222222", False)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print(f"=== {restaurante.nombre} ===")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()