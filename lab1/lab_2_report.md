# *Structural Design Patterns*

**Author**: Popov Nichita

**Group**: FAF-222

----

## Objectives:
&ensp; &ensp; __1. Study and understand the Structural Design Patterns.__

&ensp; &ensp; __2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.__

&ensp; &ensp; __3. Implement some additional functionalities using structural design patterns.__

## Used Design Patterns:

* Adapter Pattern
* Decorator Pattern
* Facade Pattern

## Implementation

Current itteration of the project expands the Vehicle Manufacturing System, focusing on structural design patterns(for this lab). The main goal is to widen flexibility in building vehicles and adding features without modifying the core structure. The three patterns—Adapter, Decorator, and Facade will be implmented along with new features such as support to electric vehicles, dynamic vehicle feature customization, and simplified user interaction.

### Adapter Pattern

The Adapter Pattern is used in my code to integrate electric engines inside the system initially built for petrol and diesel engines. This pattern allowed to “adapt” the interface of electric engines using elready existing `Engine` interface.

To accomplish this I created `ElectricEngineAdapter`, which acts as an intermediary, allowing electric engines to use the same `start()` and `stop()` methods as other engine types.

Code Snippet:

Here is the example of how I “adapted” the `power_off()` method from the `ElectricEngine` class to match the `start()` and `stop()` methods:

```python
class ElectricEngineAdapter(Engine):
    def __init__(self, electric_engine: ElectricEngine):
        self.electric_engine = electric_engine

    def start(self):
        self.electric_engine.power_on()  # Adapts to 'start'
```

### Decorator Pattern

The Decorator Pattern makes possible modification of a vehicle dynamically at runtime. Instead of applying changes to the vehicle classes in order to add specific features, I created a bunch of decorators that wrap vehicle objects and add new features, such as a sunroof and/or GPS.

Code Snippet:

As you can see in this code snippet, `SunroofDecorator` and `GPSDecorator` extend the base vehicle `specifications()`

```python
class SunroofDecorator(VehicleDecorator):
    def specifications(self):
        super().specifications()
        print("Additional Feature: Sunroof")

class GPSDecorator(VehicleDecorator):
    def specifications(self):
        super().specifications()
        print("Additional Feature: GPS Navigation")
```


### Facade Pattern

The Facade Pattern in this mini-project provides an interface that makes interaction with system’s complex functionality easier. Instead of interacting with factories, builders, and other peviously and currently implmented functionality, users can now use the `VehicleCreationFacade`, which collects these interactions in one class.

Code Snippet:
As you can see from this snippet, in order to configure the specification user should just call the method with desired parameter and value
```python
    facade = VehicleCreationFacade()
    facade.configure_vehicle('max_speed', '250km/h')
```

## Conclusions / Results

As a result we have modified Vehcile Manufacturing System with additionaly implemented structural design patterns such as:
* Adapter Pattern - to add support of electrical engines
* Decorator Pattern - to add features to the cars without modifying the source code
* Facade Pattern - to simplify interaction between user and project
<!-- Dunno how to write it like it was not written by ChatGPT cause all the nearly academic stuff looks the same like it was created by an AI -->