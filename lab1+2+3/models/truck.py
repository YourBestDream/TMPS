from domain.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self):
        self.engine = None
        self.wheels = []
        self.chassis = None

    def drive(self):
        print("Driving a truck.")

    def specifications(self):
        print("\nTruck Specifications:")
        print(f"Engine: {self.engine}")
        print(f"Wheels: {len(self.wheels)}")
        print(f"Chassis: {self.chassis}")

    def __str__(self):
        return "Truck"
