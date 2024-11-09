***🛒 Sistema de Gestión de Inventario y Ventas***

Un sistema modular de gestión de inventario y ventas, diseñado para manejar productos, registrar ventas, configurar opciones globales y generar reportes de forma eficiente.
📋 Características del Proyecto

    Gestión de Inventario:
        Agrega, actualiza, elimina y busca productos.
        Control de integridad: asegura IDs únicos para los productos.
        Control de stock: evita ventas si el stock es insuficiente.

    Gestión de Ventas:
        Registra ventas calculando el total automáticamente.
        Evita duplicados al asegurar IDs únicos en cada venta.
        Identifica el producto más vendido y permite listar todas las ventas.

    Generación de Reportes:
        Reporte de productos bajo stock.
        Reporte mensual de ventas.

    Configuración Global:
        Configura idioma, tema y formato de impresión de reportes para la aplicación.

📐 Patrones de Diseño Utilizados
Patrón	Descripción
Singleton	ConfiguracionGlobal utiliza este patrón para garantizar una única instancia global de la configuración.
Builder	ReporteBuilder permite una creación paso a paso de reportes personalizados.
Director	ReporteDirector organiza y dirige la construcción de reportes mediante el builder.
📁 Estructura del Proyecto

📦 Proyecto Inventario y Ventas
├── main.py                     # Punto de entrada principal
├── configuracion_global.py      # Configuración global (Singleton)
├── inventario.py                # Gestión de inventario
├── gestion_ventas.py            # Gestión de ventas
└── reportes.py                  # Generación de reportes (Builder y Director)

Descripción de Módulos

    configuracion_global.py: Administra la configuración global (idioma, tema, formato de reportes).
    inventario.py: Define la clase Inventario para agregar, actualizar, eliminar y buscar productos.
    gestion_ventas.py: Define la clase GestionVentas para registrar ventas y consultar el producto más vendido.
    reportes.py: Contiene ReporteBuilder y ReporteDirector para crear reportes personalizados.

🚀 Ejecución del Proyecto

Asegúrate de tener Python 3.x instalado. Luego, en la terminal, ejecuta:

python main.py

📌 Menú Principal

    Configuración Global: Configura idioma, tema y formato de reportes.
    Gestión de Inventario: Agrega, actualiza y consulta productos.
    Gestión de Ventas: Registra ventas y consulta productos más vendidos.
    Generación de Reportes: Crea reportes de inventario bajo y ventas mensuales.
    Salir: Cierra la aplicación.

🎬 Ejemplo de Flujo de Trabajo

    Configuración Global:
        Configura idioma, tema y formato de impresión.

    Gestión de Inventario:
        Agrega productos con IDs únicos y consulta stock.
        Actualiza productos según las necesidades del inventario.

    Gestión de Ventas:
        Registra ventas validando que haya suficiente stock.
        Consulta el historial de ventas y el producto más vendido.

    Generación de Reportes:
        Reporte de inventario bajo stock.
        Reporte mensual de ventas.

📈 Recomendaciones y Mejoras Futuras

    Persistencia de Datos: Implementar una base de datos para hacer persistente el inventario y las ventas.

    Interfaz Gráfica: Desarrollar una GUI para una experiencia de usuario más intuitiva.

    Automatización de Reportes: Generación automática de reportes (diarios, semanales, mensuales).

✨ Resumen

Este sistema es modular y está optimizado con patrones de diseño que aseguran una estructura limpia y eficiente. Perfecto para la gestión de inventario y ventas en pequeños negocios.
🛠️ Requerimientos

    Python 3.x
    Ejecución del script principal: python main.py

📜 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
