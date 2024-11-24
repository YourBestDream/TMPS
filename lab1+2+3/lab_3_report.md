# *Behavioral Design Patterns*

**Author**: Popov Nichita

**Group**: FAF-222

----

## Objectives:
&ensp; &ensp; __1. Study and understand the Behavioral Design Patterns.__

&ensp; &ensp; __2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.__

&ensp; &ensp; __3. Implement some additional functionalities using behavioral design patterns.__

## Used Design Pattern:

* Observer Pattern

## Implementation

During this lab Vehicle Manufacturing System acquired behavioral pattern called Observer, which implemented the logging system for better understanding of processes performed by the system.

### Observer Pattern

The Observer Pattern in this little project was implemented as logging system to track events occuring like assembly of vehicles, starting and etc. It was configured to subscribe to and receive notifications another object (the subject). In our case, vehicles became observable subjects.

Code snippet:

Here is the example of `LoggerObserver` and how does the logs are being created:
```python
class LoggerObserver(Observer):
    def update(self, message: str):
        print(f"[Logger]: {message}")
```

In builder vehicle become observable objects and a lot of steps a re being logged. Here are some examples:
```python 
    def add_engine(self, engine: str):
        self.vehicle.engine = engine
        self.vehicle.notify(f"Engine added: {engine}")

    def add_wheels(self, number: int):
        self.vehicle.wheels = ['Wheel'] * number
        self.vehicle.notify(f"{number} wheels added.")
```

Example output:

```
[Logger]: Engine added: Petrol Engine
[Logger]: 4 wheels added.
[Logger]: Chassis type set to: Standard Chassis
[Logger]: Vehicle assembly complete.
[Logger]: Vehicle is now driving.
Driving the vehicle.
[Logger]: Fetching vehicle specifications.
Fetching specifications...
```

## Conclusions / Results

The logging system implemented in this lab added to the Vehicle Manufacturing System observer pattern that improve debugging speed and quality.