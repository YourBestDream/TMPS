from domain.observable_vehicle import ObservableVehicle
from observer.logger_observer import LoggerObserver

class VehicleBuilder:
    def __init__(self):
        self.vehicle = None

    def create_new_vehicle(self, vehicle_type):
        self.vehicle = ObservableVehicle()
        logger = LoggerObserver()
        self.vehicle.attach(logger)

    def add_engine(self, engine):
        self.vehicle.engine = engine
        self.vehicle.notify(f"Added engine: {engine}")

    def add_wheels(self, number):
        self.vehicle.wheels = ['Wheel'] * number
        self.vehicle.notify(f"Added {number} wheels.")

    def add_chassis(self, chassis_type):
        self.vehicle.chassis = chassis_type
        self.vehicle.notify(f"Chassis type set to: {chassis_type}")

    def get_vehicle(self):
        self.vehicle.notify("Vehicle assembly complete.")
        return self.vehicle
