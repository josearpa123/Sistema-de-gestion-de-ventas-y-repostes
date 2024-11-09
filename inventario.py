# inventario.py

class Inventario:
    def __init__(self):
        self.inventario = []

    def existe_producto(self, id_producto):
        return any(p['id'] == id_producto for p in self.inventario)

    def agregar_producto(self, id, nombre, cantidad, precio):
        if self.existe_producto(id):
            print(f"Error: El producto con ID '{id}' ya existe en el inventario.")
            return False
        producto = {'id': id, 'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
        self.inventario.append(producto)
        return True

    def eliminar_producto(self, id_producto):
        self.inventario = [p for p in self.inventario if p['id'] != id_producto]

    def actualizar_producto(self, id_producto, **kwargs):
        for producto in self.inventario:
            if producto['id'] == id_producto:
                producto.update(kwargs)

    def buscar_producto(self, **criterios):
        resultado = self.inventario
        for clave, valor in criterios.items():
            resultado = [p for p in resultado if p.get(clave) == valor]
        return resultado

    def listar_inventario(self, criterio='nombre', orden=True):
        return sorted(self.inventario, key=lambda x: x[criterio], reverse=not orden)

    def obtener_productos_bajo_stock(self, limite=10):
        return [p for p in self.inventario if p['cantidad'] < limite]

    def reducir_stock(self, id_producto, cantidad):
        for producto in self.inventario:
            if producto['id'] == id_producto:
                if producto['cantidad'] >= cantidad:
                    producto['cantidad'] -= cantidad
                    return True
                else:
                    print(f"Error: Stock insuficiente para el producto '{producto['nombre']}'. Disponible: {producto['cantidad']}.")
                    return False
        print("Error: Producto no encontrado en el inventario.")
        return False
