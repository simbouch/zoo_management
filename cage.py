class Cage:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"✅ {animal} has been added to the cage.")

    def list_animals(self):
        if not self.animals:
            return ["The cage is empty."]
        return [str(animal) for animal in self.animals]
