# main.py

from configuracion_global import ConfiguracionGlobal
from inventario import Inventario
from gestion_ventas import GestionVentas
from reportes import ReporteBuilder, ReporteDirector

def configurar_global():
    config = ConfiguracionGlobal.get_instance()
    idioma = input("Ingrese el idioma de la aplicación: ")
    tema = input("Ingrese el tema (oscuro/claro): ")
    impresion = input("Ingrese el formato de impresión de reportes (PDF/Excel): ")
    config.set_parametro('idioma', idioma)
    config.set_parametro('tema', tema)
    config.set_parametro('impresion', impresion)
    print("Configuración Global Guardada:", config.mostrar_configuracion())

# main.py

def gestionar_inventario(inventario):
    while True:
        print("\nOpciones de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad en stock: "))
            precio = float(input("Ingrese precio unitario: "))
            if inventario.agregar_producto(id_producto, nombre, cantidad, precio):
                print(f"Producto '{nombre}' agregado al inventario.")

        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print(f"Producto con ID '{id_producto}' eliminado del inventario.")

        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nombre = input("Ingrese nuevo nombre del producto (deje vacío si no desea cambiar): ")
            cantidad = input("Ingrese nueva cantidad en stock (deje vacío si no desea cambiar): ")
            precio = input("Ingrese nuevo precio unitario (deje vacío si no desea cambiar): ")
            actualizar_info = {}
            if nombre:
                actualizar_info['nombre'] = nombre
            if cantidad:
                actualizar_info['cantidad'] = int(cantidad)
            if precio:
                actualizar_info['precio'] = float(precio)
            inventario.actualizar_producto(id_producto, **actualizar_info)
            print(f"Producto con ID '{id_producto}' actualizado.")

        elif opcion == '4':
            criterio = input("Ingrese criterio de búsqueda (nombre o id): ")
            valor = input("Ingrese valor del criterio: ")
            productos = inventario.buscar_producto(**{criterio: valor})
            print("Resultados de búsqueda:")
            for producto in productos:
                print(producto)

        elif opcion == '5':
            criterio = input("Ordenar por (nombre, cantidad o precio): ")
            orden = input("Orden ascendente (si/no): ").lower() == 'si'
            productos_ordenados = inventario.listar_inventario(criterio, orden)
            print("Inventario:")
            for producto in productos_ordenados:
                print(producto)

        elif opcion == '6':
            break
        else:
            print("Opción no válida.")

def gestionar_ventas(ventas, inventario):
    while True:
        print("\nOpciones de Ventas:")
        print("1. Registrar venta")
        print("2. Listar ventas")
        print("3. Producto más vendido")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_venta = input("Ingrese ID de la venta: ")
            fecha = input("Ingrese fecha de la venta (DD/MM/AAAA): ")
            productos_vendidos = []

            while True:
                id_producto = input("Ingrese ID del producto (o 'fin' para terminar): ")
                if id_producto.lower() == 'fin':
                    break
                cantidad = int(input("Ingrese cantidad vendida: "))

                # Verificar si el producto existe en el inventario y si hay suficiente stock
                producto = inventario.buscar_producto(id=id_producto)
                if not producto:
                    print("Producto no encontrado en inventario.")
                    continue

                # Intentar reducir el stock
                if inventario.reducir_stock(id_producto, cantidad):
                    producto_info = producto[0].copy()  # Copiar la información del producto
                    producto_info['cantidad'] = cantidad
                    productos_vendidos.append(producto_info)

            if productos_vendidos and ventas.registrar_venta(id_venta, productos_vendidos, fecha):
                print(f"Venta con ID '{id_venta}' registrada exitosamente.")

        elif opcion == '2':
            print("Historial de Ventas:")
            todas_ventas = ventas.listar_ventas()
            for venta in todas_ventas:
                print(venta)

        elif opcion == '3':
            producto_mas_vendido = ventas.producto_mas_vendido()
            print(f"Producto más vendido: {producto_mas_vendido}")

        elif opcion == '4':
            break
        else:
            print("Opción no válida.")


def generar_reportes(inventario, ventas):
    builder = ReporteBuilder()
    director = ReporteDirector(builder)
    while True:
        print("\nOpciones de Reportes:")
        print("1. Reporte de inventario bajo stock")
        print("2. Reporte de ventas mensual")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n" + director.reporte_inventario_bajo_stock(inventario))
        elif opcion == '2':
            print("\n" + director.reporte_ventas_mensual(ventas))
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")

def main():
    config = ConfiguracionGlobal.get_instance()
    inventario = Inventario()
    ventas = GestionVentas()

    while True:
        print("\nOpciones del Sistema:")
        print("1. Configuración Global")
        print("2. Gestión de Inventario")
        print("3. Gestión de Ventas")
        print("4. Generación de Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            configurar_global()
        elif opcion == '2':
            gestionar_inventario(inventario)
        elif opcion == '3':
            gestionar_ventas(ventas, inventario)
        elif opcion == '4':
            generar_reportes(inventario, ventas)
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
