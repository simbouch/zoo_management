class Animal:
    def __init__(self, name, species, diet):
        self.name = name
        self.species = species
        self.diet = diet  # Can be 'carnivore', 'herbivore', or 'omnivore'

    def __str__(self):
        return f"{self.species} nommé {self.name}"

    def feed(self, food_type, food_name):
        """Check if the food type matches the animal's diet."""
        if self.diet == food_type:
            return f"✅ {self.name} a été nourri correctement avec {food_name} ({food_type})."
        else:
            return f"❌ {self.name} ne peut pas manger {food_name}. C'est un {self.diet} et ne mange pas de nourriture {food_type}."

# Carnivores
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion", "carnivore")

class Tigre(Animal):  # Tiger
    def __init__(self, name):
        super().__init__(name, "Tigre", "carnivore")

class Mangouste(Animal):  # Mongoose
    def __init__(self, name):
        super().__init__(name, "Mangouste", "carnivore")

class Serpent(Animal):  # Snake
    def __init__(self, name):
        super().__init__(name, "Serpent", "carnivore")

# Herbivores
class Éléphant(Animal):  # Elephant
    def __init__(self, name):
        super().__init__(name, "Éléphant", "herbivore")

class Zèbre(Animal):  # Zebra
    def __init__(self, name):
        super().__init__(name, "Zèbre", "herbivore")

class Okapi(Animal):  # Okapi (uncommon)
    def __init__(self, name):
        super().__init__(name, "Okapi", "herbivore")

class Gazelle(Animal):  # Gazelle
    def __init__(self, name):
        super().__init__(name, "Gazelle", "herbivore")

# Omnivores
class Ours(Animal):  # Bear
    def __init__(self, name):
        super().__init__(name, "Ours", "omnivore")

class RatonLaveur(Animal):  # Raccoon
    def __init__(self, name):
        super().__init__(name, "Raton Laveur", "omnivore")

class Coati(Animal):  # Coati (uncommon)
    def __init__(self, name):
        super().__init__(name, "Coati", "omnivore")

class Chimpanzé(Animal):  # Chimpanzee
    def __init__(self, name):
        super().__init__(name, "Chimpanzé", "omnivore")
