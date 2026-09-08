"""
Módulo: scooter_electrico.py
Subclase concreta de Vehiculo.
"""

from .vehiculo import Vehiculo


class ScooterElectrico(Vehiculo):
    """>>> HERENCIA: segunda subclase concreta."""

    def __init__(self, id_vehiculo: str, tarifa_base: float = 700.0,
                 nivel_bateria: int = 100, velocidad_max: int = 25):
        super().__init__(id_vehiculo, tarifa_base)
        self.__nivel_bateria = nivel_bateria
        self.__velocidad_max = velocidad_max

    @property
    def nivel_bateria(self):
        return self.__nivel_bateria

    @nivel_bateria.setter
    def nivel_bateria(self, valor):
        if not (0 <= valor <= 100):
            raise ValueError("El nivel de batería debe estar entre 0 y 100.")
        self.__nivel_bateria = valor

    def calcular_costo(self, distancia_km: float) -> float:
        """>>> POLIMORFISMO: fórmula distinta a BicicletaElectrica."""
        costo = self._tarifa_base + distancia_km * 250
        if self.__velocidad_max >= 30:
            costo += 300
        return round(costo, 2)

    def __str__(self):
        return (f"ScooterElectrico[{self._id_vehiculo}] "
                f"batería={self.__nivel_bateria}% "
                f"vel_max={self.__velocidad_max}km/h "
                f"tarifa_base=₡{self._tarifa_base:.2f}")