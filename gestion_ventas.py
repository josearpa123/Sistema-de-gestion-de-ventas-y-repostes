# gestion_ventas.py

class GestionVentas:
    def __init__(self):
        self.ventas = []

    def existe_venta(self, id_venta):
        return any(v['id_venta'] == id_venta for v in self.ventas)

    def registrar_venta(self, id_venta, productos, fecha):
        if self.existe_venta(id_venta):
            print(f"Error: La venta con ID '{id_venta}' ya existe.")
            return False
        total = sum(p['cantidad'] * p['precio'] for p in productos)
        venta = {'id_venta': id_venta, 'productos': productos, 'fecha': fecha, 'total': total}
        self.ventas.append(venta)
        return True

    def listar_ventas(self):
        return self.ventas

    def producto_mas_vendido(self):
        producto_contador = {}
        for venta in self.ventas:
            for producto in venta['productos']:
                nombre = producto['nombre']
                producto_contador[nombre] = producto_contador.get(nombre, 0) + producto['cantidad']
        return max(producto_contador, key=producto_contador.get) if producto_contador else None
