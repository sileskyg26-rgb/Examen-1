"""
Módulo: vehiculo.py
Contiene la clase abstracta base Vehiculo.
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """
    Clase abstracta que define la interfaz común de todo vehículo
    eléctrico del sistema.

    >>> ABSTRACCIÓN: Vehiculo hereda de ABC y declara
    calcular_costo() como @abstractmethod. Esto impide instanciar
    Vehiculo directamente y obliga a cada subclase concreta a
    implementar su propia lógica de costo.
    """

    _contador_vehiculos = 0  # atributo de clase, protegido

    def __init__(self, id_vehiculo: str, tarifa_base: float = 500.0):
        """
        >>> CONSTRUCTOR pythónico: 'tarifa_base' tiene valor por
        defecto, simulando constructor "por defecto" y "con parámetros".
        """
        self._id_vehiculo = id_vehiculo          # protegido
        self._tarifa_base = tarifa_base           # protegido
        self.__disponible = True                  # privado (ocultamiento)

        Vehiculo._contador_vehiculos += 1

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, nuevo_valor):
        """>>> PROPIEDAD 1 con validación."""
        if not isinstance(nuevo_valor, (int, float)):
            raise TypeError("La tarifa base debe ser un valor numérico.")
        if nuevo_valor < 0:
            raise ValueError("La tarifa base no puede ser negativa.")
        self._tarifa_base = nuevo_valor

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, valor: bool):
        """>>> PROPIEDAD 2 con validación."""
        if not isinstance(valor, bool):
            raise TypeError("disponible debe ser booleano (True/False).")
        self.__disponible = valor

    @property
    def id_vehiculo(self):
        return self._id_vehiculo

    @abstractmethod
    def calcular_costo(self, distancia_km: float) -> float:
        """>>> Método abstracto: contrato polimórfico."""
        raise NotImplementedError

    def __str__(self):
        estado = "disponible" if self.__disponible else "no disponible"
        return (f"Vehiculo[{self._id_vehiculo}] "
                f"tarifa_base=₡{self._tarifa_base:.2f} ({estado})")