from abc import ABC, abstractmethod
from domain.vehicle import Vehicle
from models.car import Car
from models.truck import Truck

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()

class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()
