from domain.engine import Engine

class DieselEngine(Engine):
    def start(self):
        print("Starting diesel engine.")

    def stop(self):
        print("Stopping diesel engine.")

    def __str__(self):
        return "Diesel Engine"
