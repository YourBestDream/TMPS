from models.car import Car
from models.truck import Truck
from domain.engine import Engine

class VehicleBuilder:
    def __init__(self):
        self.vehicle = None

    def create_new_vehicle(self, vehicle_type):
        if vehicle_type == 'car':
            self.vehicle = Car()
        elif vehicle_type == 'truck':
            self.vehicle = Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

    def add_engine(self, engine: Engine):
        self.vehicle.engine = engine

    def add_wheels(self, number):
        self.vehicle.wheels = ['Wheel'] * number

    def add_chassis(self, chassis_type):
        self.vehicle.chassis = chassis_type

    def get_vehicle(self):
        return self.vehicle
