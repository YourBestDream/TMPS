from domain.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self):
        self.engine = None
        self.wheels = []
        self.chassis = None

    def drive(self):
        print("Driving a car.")

    def specifications(self):
        print("\nCar Specifications:")
        print(f"Engine: {self.engine}")
        print(f"Wheels: {len(self.wheels)}")
        print(f"Chassis: {self.chassis}")

    def __str__(self):
        return "Car"
