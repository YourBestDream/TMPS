from builder.vehicle_builder import VehicleBuilder
from models.petrol_engine import PetrolEngine
from models.diesel_engine import DieselEngine
from adapter.electric_engine_adapter import ElectricEngineAdapter
from models.electric_engine import ElectricEngine

# Some Car and Truck predefined properties for builder

class PredefinedVehicleBuilder:
    @staticmethod
    def construct_sports_car():
        builder = VehicleBuilder()
        builder.create_new_vehicle('car')
        builder.add_engine(PetrolEngine())
        builder.add_wheels(4)
        builder.add_chassis('Sports Chassis')
        return builder.get_vehicle()

    @staticmethod
    def construct_heavy_truck():
        builder = VehicleBuilder()
        builder.create_new_vehicle('truck')
        builder.add_engine(DieselEngine())
        builder.add_wheels(8)
        builder.add_chassis('Heavy Duty Chassis')
        return builder.get_vehicle()

    @staticmethod
    def construct_electric_car():
        builder = VehicleBuilder()
        builder.create_new_vehicle('car')
        builder.add_engine(ElectricEngineAdapter(ElectricEngine()))
        builder.add_wheels(4)
        builder.add_chassis('Electric Chassis')
        return builder.get_vehicle()
