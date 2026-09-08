"""
Módulo: menu.py
Contiene la clase Menu, encargada de administrar clientes,
vehículos y servicios.
"""

# Import ABSOLUTO desde el paquete 'modelos' (evita ciclos:
# 'gestion' depende de 'modelos', pero 'modelos' NUNCA
# importa nada de 'gestion' -> no hay dependencia circular).
from modelos import Cliente, Vehiculo, Servicio


class Menu:
    """Administra clientes, vehículos y la ejecución de servicios."""

    def __init__(self):
        self.__clientes = []
        self.__vehiculos = []
        self.__servicios = []

    def registrar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Solo se pueden registrar objetos de tipo Cliente.")
        self.__clientes.append(cliente)
        print(f"[Menu] Cliente registrado -> {cliente}")

    def registrar_vehiculo(self, vehiculo: Vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("Solo se pueden registrar objetos de tipo Vehiculo.")
        self.__vehiculos.append(vehiculo)
        print(f"[Menu] Vehículo registrado -> {vehiculo}")

    def listar_clientes(self):
        print("\n--- Clientes registrados ---")
        for c in self.__clientes:
            print(f"  {c}")

    def listar_vehiculos(self):
        print("\n--- Vehículos registrados ---")
        for v in self.__vehiculos:
            print(f"  {v}")

    def listar_servicios(self):
        print("\n--- Servicios ejecutados ---")
        for s in self.__servicios:
            print(f"  {s}")

    def ejecutar_servicio(self, cliente: Cliente, vehiculo: Vehiculo,
                           distancia_km: float) -> Servicio:
        if not vehiculo.disponible:
            raise RuntimeError(f"El vehículo {vehiculo.id_vehiculo} no está disponible.")

        servicio = Servicio(cliente, vehiculo, distancia_km)
        self.__servicios.append(servicio)
        print(f"[Menu] Servicio ejecutado -> {servicio}")
        return servicio

    @property
    def total_recaudado(self) -> float:
        return round(sum(s.calcular_monto() for s in self.__servicios), 2)