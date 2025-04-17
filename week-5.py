# Base class: Superhero
class Superhero:
    # Constructor to initialize superhero details
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    # Method to introduce the superhero
    def introduce(self):
        print(f"I am {self.name} from {self.universe} 🌍!")

    # Method to use their power
    def use_power(self):
        print(f"{self.name} uses {self.power}! 💥")

# Subclass: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    # Constructor with an additional attribute for flight speed
    def __init__(self, name, power, universe, flight_speed):
        # Call parent constructor
        super().__init__(name, power, universe)
        self.flight_speed = flight_speed

    # Override use_power method to show unique flying ability
    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h! 🚀")


# Example usage
hero1 = Superhero("IronFist", "Super Strength", "Marvel")
hero1.introduce()      # Output: I am IronFist from Marvel 🌍!
hero1.use_power()      # Output: IronFist uses Super Strength! 💥

hero2 = FlyingHero("SkyHawk", "Flight", "DC", 800)
hero2.introduce()      # Output: I am SkyHawk from DC 🌍!
hero2.use_power()      # Output: SkyHawk soars through the sky at 800 km/h! 🚀


# Base class: Vehicle
class Vehicle:
    # Generic move method (can be overridden)
    def move(self):
        print("Vehicle is moving...")

# Subclass: Car
class Car(Vehicle):
    # Override move method for car
    def move(self):
        print("Driving on the road 🚗")

# Subclass: Plane
class Plane(Vehicle):
    # Override move method for plane
    def move(self):
        print("Flying in the sky ✈️")

# Subclass: Boat
class Boat(Vehicle):
    # Override move method for boat
    def move(self):
        print("Sailing on the water 🚢")


# Example usage showing polymorphism
vehicles = [Car(), Plane(), Boat()]  # A list of different vehicle types

# Loop through each vehicle and call move() method
for v in vehicles:
    v.move()  # Each move() behaves differently depending on the class
