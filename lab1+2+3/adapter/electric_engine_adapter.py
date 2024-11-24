from domain.engine import Engine
from models.electric_engine import ElectricEngine

class ElectricEngineAdapter(Engine):
    def __init__(self, electric_engine: ElectricEngine):
        self.electric_engine = electric_engine

    def start(self):
        self.electric_engine.power_on()

    def stop(self):
        self.electric_engine.power_off()

    def __str__(self):
        return "Electric Engine Adapter"
