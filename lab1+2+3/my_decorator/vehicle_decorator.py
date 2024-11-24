from domain.vehicle import Vehicle

class VehicleDecorator(Vehicle):
    def __init__(self, decorated_vehicle):
        self.decorated_vehicle = decorated_vehicle

    def drive(self):
        self.decorated_vehicle.drive()

    def specifications(self):
        self.decorated_vehicle.specifications()
