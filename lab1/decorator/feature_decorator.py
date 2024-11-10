from decorator.vehicle_decorator import VehicleDecorator

class SunroofDecorator(VehicleDecorator):
    def specifications(self):
        super().specifications()
        print("Additional Feature: Sunroof")

class GPSDecorator(VehicleDecorator):
    def specifications(self):
        super().specifications()
        print("Additional Feature: GPS Navigation")
