"""
main.py
Punto de entrada del sistema EcoMove.
Ejecutar con:  python main.py   (desde la carpeta ecomove/)
"""

# Imports absolutos usando los __init__.py de cada paquete:
from modelos import BicicletaElectrica, ScooterElectrico, Cliente
from gestion import Menu


def main():
    print("=" * 60)
    print("   SISTEMA ECOMOVE - DEMOSTRACIÓN")
    print("=" * 60)

    menu = Menu()

    # 1. Clientes
    cliente1 = Cliente("Ana Rodríguez", "1-1111-1111", "8888-1234")
    cliente2 = Cliente("Luis Fernández", "2-2222-2222")
    menu.registrar_cliente(cliente1)
    menu.registrar_cliente(cliente2)

    # 2. Vehículos de distintas subclases concretas
    bici1 = BicicletaElectrica("B-01", tarifa_base=500, nivel_bateria=15)
    bici2 = BicicletaElectrica("B-02")
    scooter1 = ScooterElectrico("S-01", tarifa_base=700, velocidad_max=35)

    menu.registrar_vehiculo(bici1)
    menu.registrar_vehiculo(bici2)
    menu.registrar_vehiculo(scooter1)

    menu.listar_vehiculos()
    menu.listar_clientes()

    # 3. DEMOSTRACIÓN DE POLIMORFISMO
    print("\n--- Demostración de polimorfismo: calcular_costo(10 km) ---")
    flota = [bici1, bici2, scooter1]
    for vehiculo in flota:
        print(f"  {type(vehiculo).__name__:20s} -> "
              f"calcular_costo(10) = ₡{vehiculo.calcular_costo(10):.2f}")

    # 4. Ejecución de servicios reales
    menu.ejecutar_servicio(cliente1, bici1, 10)
    menu.ejecutar_servicio(cliente2, scooter1, 10)
    menu.ejecutar_servicio(cliente1, bici2, 5)

    menu.listar_servicios()

    print(f"\nTotal recaudado por EcoMove: ₡{menu.total_recaudado:.2f}")
    print(f"Servicios realizados por Ana: {cliente1.cantidad_servicios}")

    # 5. Validaciones de @property
    try:
        bici1.tarifa_base = -100
    except ValueError as e:
        print(f"\n[Validación OK] No se permitió tarifa negativa: {e}")

    try:
        bici1.disponible = "sí"
    except TypeError as e:
        print(f"[Validación OK] No se permitió tipo inválido: {e}")


if __name__ == "__main__":
    main()