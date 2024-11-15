from cage import Cage

class Zoo:
    def __init__(self):
        self.cages = []

    def add_cage(self, cage):
        self.cages.append(cage)
        print("✅ A new cage has been added to the zoo.")

    def count_cages(self):
        return len(self.cages)

    def list_cages(self):
        if not self.cages:
            print("There are no cages in the zoo yet.")
        else:
            for i, cage in enumerate(self.cages, 1):
                print(f"Cage {i}: {', '.join(cage.list_animals())}")
