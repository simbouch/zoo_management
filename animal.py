# animal.py

class Animal:
    def __init__(self, name, species, diet):
        self.name = name
        self.species = species
        self.diet = diet  # Can be 'carnivore', 'herbivore', or 'omnivore'

    def __str__(self):
        return f"{self.species} named {self.name}"

    def feed(self, food_type):
        """Check if the food type matches the animal's diet."""
        if self.diet == food_type:
            return f"✅ {self.name} has been fed correctly with {food_type} food."
        else:
            return f"❌ {self.name} cannot eat {food_type}. It's a {self.diet}."

# Carnivores
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion", "carnivore")

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Tiger", "carnivore")

class Hyena(Animal):
    def __init__(self, name):
        super().__init__(name, "Hyena", "carnivore")

class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake", "carnivore")

# Herbivores
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant", "herbivore")

class Zebra(Animal):
    def __init__(self, name):
        super().__init__(name, "Zebra", "herbivore")

class Gazelle(Animal):
    def __init__(self, name):
        super().__init__(name, "Gazelle", "herbivore")

# Omnivores
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Monkey", "omnivore")

class Bear(Animal):
    def __init__(self, name):
        super().__init__(name, "Bear", "omnivore")
