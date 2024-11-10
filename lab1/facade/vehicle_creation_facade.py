from builder.predefined_vehicle_builder import PredefinedVehicleBuilder
from factory.vehicle_factory import CarFactory, TruckFactory
from singleton.configuration_manager import ConfigurationManager

class VehicleCreationFacade:
    def __init__(self):
        self.car_factory = CarFactory()
        self.truck_factory = TruckFactory()
        self.config_manager = ConfigurationManager()

    def create_standard_car(self):
        car = self.car_factory.create_vehicle()
        car.drive()
        return car

    def create_custom_sports_car(self):
        sports_car = PredefinedVehicleBuilder.construct_sports_car()
        sports_car.specifications()
        return sports_car

    def configure_vehicle(self, key, value):
        self.config_manager.set_setting(key, value)
        print(f"Set configuration: {key} = {value}")
