from domain.vehicle import Vehicle
from observer.subject import Subject

class ObservableVehicle(Vehicle, Subject):
    def __init__(self):
        super().__init__()
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

    def drive(self):
        self.notify("Vehicle is now driving.")
        print("Driving a vehicle.")

    def specifications(self):
        self.notify("Fetching vehicle specifications.")
        print("Fetching specifications...")
