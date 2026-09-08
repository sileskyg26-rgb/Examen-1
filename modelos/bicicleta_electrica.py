"""
Módulo: bicicleta_electrica.py
Subclase concreta de Vehiculo.
"""

# Import RELATIVO dentro del mismo paquete 'modelos'
from .vehiculo import Vehiculo


class BicicletaElectrica(Vehiculo):
    """>>> HERENCIA: extiende Vehiculo."""

    def __init__(self, id_vehiculo: str, tarifa_base: float = 500.0,
                 nivel_bateria: int = 100):
        super().__init__(id_vehiculo, tarifa_base)
        self.__nivel_bateria = nivel_bateria  # privado

    @property
    def nivel_bateria(self):
        return self.__nivel_bateria

    @nivel_bateria.setter
    def nivel_bateria(self, valor):
        if not (0 <= valor <= 100):
            raise ValueError("El nivel de batería debe estar entre 0 y 100.")
        self.__nivel_bateria = valor

    def calcular_costo(self, distancia_km: float) -> float:
        """>>> POLIMORFISMO: fórmula propia de la bicicleta."""
        costo = self._tarifa_base + distancia_km * 150
        if self.__nivel_bateria < 20:
            costo *= 1.10
        return round(costo, 2)

    def __str__(self):
        return (f"BicicletaElectrica[{self._id_vehiculo}] "
                f"batería={self.__nivel_bateria}% "
                f"tarifa_base=₡{self._tarifa_base:.2f}")