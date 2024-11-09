# reportes.py

class ReporteBuilder:
    def __init__(self):
        self.secciones = []

    def agregarResumenInventario(self, inventario):
        self.secciones.append("Resumen de Inventario:\n" + "\n".join(str(p) for p in inventario))

    def agregarResumenVentas(self, ventas):
        self.secciones.append("Resumen de Ventas:\n" + "\n".join(str(v) for v in ventas))

    def agregarProductoMasVendido(self, producto):
        self.secciones.append(f"Producto más vendido: {producto}")

    def obtener_reporte(self):
        return "\n\n".join(self.secciones)

class ReporteDirector:
    def __init__(self, builder):
        self.builder = builder

    def reporte_inventario_bajo_stock(self, inventario):
        self.builder.agregarResumenInventario(inventario.obtener_productos_bajo_stock())
        return self.builder.obtener_reporte()

    def reporte_ventas_mensual(self, ventas):
        self.builder.agregarResumenVentas(ventas.listar_ventas())
        self.builder.agregarProductoMasVendido(ventas.producto_mas_vendido())
        return self.builder.obtener_reporte()
