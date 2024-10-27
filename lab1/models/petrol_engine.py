from domain.engine import Engine

class PetrolEngine(Engine):
    def start(self):
        print("Starting petrol engine.")

    def stop(self):
        print("Stopping petrol engine.")

    def __str__(self):
        return "Petrol Engine"
