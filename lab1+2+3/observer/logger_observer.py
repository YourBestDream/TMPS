from observer.observer import Observer

class LoggerObserver(Observer):
    def update(self, message: str):
        print(f"[Logger]: {message}")
