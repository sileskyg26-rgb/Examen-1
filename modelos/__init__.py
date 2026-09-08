"""
Paquete 'modelos': entidades del dominio EcoMove.

Este __init__.py centraliza las importaciones para que el resto
del proyecto (main.py, gestion/menu.py) pueda hacer:

    from modelos import Vehiculo, BicicletaElectrica, ...

en lugar de:

    from modelos.vehiculo import Vehiculo
    from modelos.bicicleta_electrica import BicicletaElectrica
    ...
"""

from .vehiculo import Vehiculo
from .bicicleta_electrica import BicicletaElectrica
from .scooter_electrico import ScooterElectrico
from .cliente import Cliente
from .servicio import Servicio

__all__ = [
    "Vehiculo",
    "BicicletaElectrica",
    "ScooterElectrico",
    "Cliente",
    "Servicio",
]