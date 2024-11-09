# configuracion_global.py

class ConfiguracionGlobal:
    _instance = None
    _configuracion = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set_parametro(self, clave, valor):
        self._configuracion[clave] = valor

    def get_parametro(self, clave):
        return self._configuracion.get(clave)

    def mostrar_configuracion(self):
        return self._configuracion
