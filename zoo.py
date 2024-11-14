
from cage import Cage

class Zoo:
    def __init__(self):
        self.cages = []

    def add_cage(self, cage):
        self.cages.append(cage)
        print("A new cage has been added to the zoo.")

    def count_cages(self):
        return len(self.cages)

    def list_cages(self):
        for i, cage in enumerate(self.cages, 1):
            print(f"Cage {i}: {cage.list_animals()}")
    