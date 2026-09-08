"""
Módulo: servicio.py
Contiene la clase Servicio, que aplica COMPOSICIÓN con
Cliente y Vehiculo.
"""

from datetime import datetime

# Imports relativos: Servicio necesita conocer los TIPOS
# Cliente y Vehiculo para las anotaciones y validaciones.
from .cliente import Cliente
from .vehiculo import Vehiculo


class Servicio:
    """
    >>> COMPOSICIÓN: un Servicio no existe sin un Cliente y un
    Vehiculo asociados.
    """

    _contador_servicios = 0

    def __init__(self, cliente: Cliente, vehiculo: Vehiculo, distancia_km: float):
        if distancia_km <= 0:
            raise ValueError("La distancia debe ser mayor a 0 km.")

        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__distancia_km = distancia_km
        self.__fecha = datetime.now()

        Servicio._contador_servicios += 1
        self.__id_servicio = Servicio._contador_servicios

        self.__cliente.agregar_servicio(self)

    @property
    def distancia_km(self):
        return self.__distancia_km

    @distancia_km.setter
    def distancia_km(self, valor):
        if valor <= 0:
            raise ValueError("La distancia debe ser mayor a 0 km.")
        self.__distancia_km = valor

    @property
    def cliente(self):
        return self.__cliente

    @property
    def vehiculo(self):
        return self.__vehiculo

    def calcular_monto(self) -> float:
        """>>> POLIMORFISMO: delega en Vehiculo.calcular_costo()."""
        return self.__vehiculo.calcular_costo(self.__distancia_km)

    def __str__(self):
        return (f"Servicio #{self.__id_servicio} | {self.__fecha:%d/%m/%Y %H:%M} | "
                f"Cliente: {self.__cliente.nombre} | "
                f"Vehículo: {self.__vehiculo} | "
                f"Distancia: {self.__distancia_km} km | "
                f"Monto: ₡{self.calcular_monto():.2f}")