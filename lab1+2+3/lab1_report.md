# *Creational Design Patterns*

**Author**: Popov Nichita

**Group**: FAF-222

----

## Objectives:
__1. Study and understand the Creational Design Patterns.__

__2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.__

__3. Use some creational design patterns for object instantiation in a sample project.__

## Used Design Patterns:

* Factory Method Pattern
* Singleton Pattern
* Builder Pattern

## Implementation

In this project, I implemented three creational design patterns within a Vehicle Manufacturing System domain: Factory Method, Singleton, and Builder. The system involves creating different types of vehicles and engines, managing configuration settings, and constructing complex vehicle objects.

### Factory Method Pattern

The Factory Method Pattern defines an interface for creating an object but lets subclasses decide which class to instantiate. It promotes loose coupling by eliminating the need to bind application-specific classes into the code.

An abstract `VehicleFactory` class defines the method `create_vehicle()`. Concrete factory classes like `CarFactory` and `TruckFactory` inherit from `VehicleFactory` and implement the `create_vehicle()` method to instantiate specific vehicle types.

`vehicle_factory.py`:
```python
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

```

In the main.py, we use the factories to create vehicle instances without specifying the exact class of the object that will be created.

`main.py`:
```python
from factory.vehicle_factory import CarFactory, TruckFactory

# Using Factory Method Pattern
car_factory = CarFactory()
car = car_factory.create_vehicle()
car.drive()

truck_factory = TruckFactory()
truck = truck_factory.create_vehicle()
truck.drive()
```

### Singleton Pattern

The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. This is useful for managing shared resources like configuration settings or logging mechanisms.

A `ConfigurationManager` class is implemented as a Singleton. It stores configuration settings that can be accessed and modified globally across the application.

`configuration_manager.py`:

```python
class ConfigurationManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ConfigurationManager, cls).__new__(cls)
            cls.__instance.settings = {}
        return cls.__instance

    def get_setting(self, key):
        return self.__instance.settings.get(key, None)

    def set_setting(self, key, value):
        self.__instance.settings[key] = value
```

We access the `ConfigurationManager` in `main.py` to set and get configuration settings.

`main.py`:

```python
from singleton.configuration_manager import ConfigurationManager

# Using Singleton Pattern
config_manager = ConfigurationManager()
config_manager.set_setting('max_speed', '200km/h')
print("Configuration Manager Settings:")
print(f"Max Speed: {config_manager.get_setting('max_speed')}")
```

### Builder Pattern

The Builder Pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

A `VehicleBuilder` class provides methods to build different parts of a vehicle. The `PredefinedVehicleBuilder` class orchestrates the building process to construct specific types of vehicles like sports cars or heavy trucks.

`vehicle_builder.py`:

```python
from models.car import Car
from models.truck import Truck
from domain.engine import Engine

class VehicleBuilder:
    def __init__(self):
        self.vehicle = None

    def create_new_vehicle(self, vehicle_type):
        if vehicle_type == 'car':
            self.vehicle = Car()
        elif vehicle_type == 'truck':
            self.vehicle = Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

    def add_engine(self, engine: Engine):
        self.vehicle.engine = engine

    def add_wheels(self, number):
        self.vehicle.wheels = ['Wheel'] * number

    def add_chassis(self, chassis_type):
        self.vehicle.chassis = chassis_type

    def get_vehicle(self):
        return self.vehicle
```

`predefined_vehicle_builder.py`:

```python
from builder.vehicle_builder import VehicleBuilder
from models.petrol_engine import PetrolEngine
from models.diesel_engine import DieselEngine

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
```

In `main.py`, we use the `PredefinedVehicleBuilder` to construct complex vehicle objects.

`main.py`:

```python
from builder.vehicle_director import VehicleDirector

# Using Builder Pattern
sports_car = VehicleDirector.construct_sports_car()
sports_car.specifications()

heavy_truck = VehicleDirector.construct_heavy_truck()
heavy_truck.specifications()
```

## Conclusions / Results

Through this project, I demonstrated the practical application of three creational design patterns:
* **Factory Method Pattern**: Enabled the creation of vehicle objects without specifying their concrete classes, promoting loose coupling and scalability.
* **Singleton Pattern**: Managed global configuration settings efficiently by ensuring only one instance of the `ConfigurationManager` exists.
* **Builder Pattern**: Simplified the construction of complex vehicle objects by separating their creation process from their representation.

By applying these patterns, the codebase becomes more maintainable, extensible, and easier to understand. The separation of concerns allows for individual components to be modified or extended without affecting others, adhering to best practices in software design.