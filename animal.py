
class Animal:
    def __init__(self, name, species, diet):
        self.name = name
        self.species = species
        self.diet = diet  # Can be 'carnivore', 'herbivore', or 'omnivore'

    def __str__(self):
        return f"{self.species} named {self.name}"

    def feed(self, food_type):
        if self.diet == food_type:
            return f"{self.name} has been fed correctly with {food_type} food."
        else:
            return f"{self.name} cannot eat {food_type}. It's a {self.diet}."

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion", "carnivore")

class Gazelle(Animal):
    def __init__(self, name):
        super().__init__(name, "Gazelle", "herbivore")

class Hyena(Animal):
    def __init__(self, name):
        super().__init__(name, "Hyena", "carnivore")
    