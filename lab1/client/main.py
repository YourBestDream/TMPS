from factory.vehicle_factory import CarFactory, TruckFactory
from singleton.configuration_manager import ConfigurationManager
from builder.predefined_vehicle_builder import PredefinedVehicleBuilder

# Should run from .\lab1 using python -m client.main

def main():
    # Using Factory Method Pattern
    car_factory = CarFactory()
    car = car_factory.create_vehicle()
    car.drive()

    truck_factory = TruckFactory()
    truck = truck_factory.create_vehicle()
    truck.drive()

    # Using Singleton Pattern
    config_manager = ConfigurationManager()
    config_manager.set_setting('max_speed', '200km/h')
    print("Configuration Manager Settings:")
    print(f"Max Speed: {config_manager.get_setting('max_speed')}")

    # Using Builder Pattern
    sports_car = PredefinedVehicleBuilder.construct_sports_car()
    sports_car.specifications()

    heavy_truck = PredefinedVehicleBuilder.construct_heavy_truck()
    heavy_truck.specifications()

if __name__ == "__main__":
    main()
