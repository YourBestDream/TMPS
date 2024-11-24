from factory.vehicle_factory import CarFactory, TruckFactory
from singleton.configuration_manager import ConfigurationManager
from builder.predefined_vehicle_builder import PredefinedVehicleBuilder
from my_decorator.feature_decorator import SunroofDecorator, GPSDecorator
from facade.vehicle_creation_facade import VehicleCreationFacade
from builder.vehicle_builder import VehicleBuilder

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
    
    # Build a car with additional features using decorator pattern
    basic_car = PredefinedVehicleBuilder.construct_sports_car()
    car_with_sunroof = SunroofDecorator(basic_car)
    car_with_gps_and_sunroof = GPSDecorator(car_with_sunroof)
    car_with_gps_and_sunroof.specifications()
    
    # Creation of car and configuring it using facade pattern
    facade = VehicleCreationFacade()
    facade.create_standard_car()

    # Create a custom sports car
    sports_car = facade.create_custom_sports_car()

    # Configure max speed
    facade.configure_vehicle('max_speed', '250km/h')
    print(f"Max Speed Config: {facade.config_manager.get_setting('max_speed')}")
    
    # Observer
    builder = VehicleBuilder()
    builder.create_new_vehicle("car")
    builder.add_engine("Petrol Engine")
    builder.add_wheels(4)
    builder.add_chassis("Standard Chassis")
    vehicle = builder.get_vehicle()
    
    vehicle.drive()
    vehicle.specifications()

if __name__ == "__main__":
    main()
