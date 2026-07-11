class Cliente:
    def __init__(self, nombre, edad, telefono, cliente_frecuente):
        self.nombre = nombre                  # str
        self.edad = edad                      # int
        self.telefono = telefono              # str
        self.cliente_frecuente = cliente_frecuente  # bool

    def mostrar_informacion(self):
        tipo = "Sí" if self.cliente_frecuente else "No"

        print(f"Cliente: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Teléfono: {self.telefono}")
        print(f"Cliente frecuente: {tipo}")