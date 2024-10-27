from abc import ABC, abstractmethod
from domain.engine import Engine
from models.diesel_engine import DieselEngine
from models.petrol_engine import PetrolEngine

class EngineFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

class DieselEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return DieselEngine()

class PetrolEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return PetrolEngine()
