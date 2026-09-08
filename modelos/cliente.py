"""
Módulo: cliente.py
Contiene la clase Cliente.
"""


class Cliente:
    """Representa a un cliente registrado en el sistema EcoMove."""

    def __init__(self, nombre: str, cedula: str, telefono: str = "No registrado"):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__telefono = telefono
        self.__historial_servicios = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cedula(self):
        return self.__cedula

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if not isinstance(nuevo_telefono, str) or len(nuevo_telefono) < 8:
            raise ValueError("Teléfono inválido: debe tener al menos 8 caracteres.")
        self.__telefono = nuevo_telefono

    def agregar_servicio(self, servicio):
        self.__historial_servicios.append(servicio)

    @property
    def cantidad_servicios(self):
        return len(self.__historial_servicios)

    def __str__(self):
        return (f"Cliente({self.__nombre}, cédula={self.__cedula}, "
                f"tel={self.__telefono}, servicios_realizados={self.cantidad_servicios})")