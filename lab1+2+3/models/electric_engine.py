from domain.engine import Engine

class ElectricEngine(Engine):
    def power_on(self):
        print("Electric engine powering on.")

    def power_off(self):
        print("Electric engine powering off.")

    def __str__(self):
        return "Electric Engine"
