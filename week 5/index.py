class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Smartphone(Device):
    def __init__(self, brand, model, color, storage):
        super().__init__(brand, model)
        self.color = color
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def browse_internet(self, website):
        print(f"Browsing {website}")

# Example usage:
iphone14 = Smartphone("Apple", "iPhone 14", "Purple", 128)
iphone14.make_call("+1234567890")
iphone14.send_message("+9876543210", "Hello!")
iphone14.browse_internet("google.com")

# Assignment 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Creating instances of each vehicle
vehicles = [Car(), Plane(), Bicycle()]

# Demonstrating polymorphism
for vehicle in vehicles:
    vehicle.move()
