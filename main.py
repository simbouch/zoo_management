# main.py

from zoo import Zoo
from cage import Cage
from animal import Lion, Gazelle, Hyena, Elephant, Tiger, Monkey, Zebra, Bear, Snake

def display_instructions():
    print("\n=== Welcome to the Zoo Management Console Application! ===")
    print("In this game, you are the manager of a virtual zoo. Your tasks include:")
    print(" - Adding cages to hold animals")
    print(" - Adding different types of animals to each cage")
    print(" - Feeding animals based on their diet (carnivore, herbivore, omnivore)")
    print("\nAnimal Types Available:")
    print(" - Carnivores: Lion, Tiger, Hyena, Snake")
    print(" - Herbivores: Elephant, Zebra, Gazelle")
    print(" - Omnivores: Monkey, Bear")
    print("\nInstructions:")
    print("1. Start by adding at least one cage using option '1'.")
    print("2. Then, you can add animals to any of the cages using option '2'.")
    print("3. Use the 'List all cages and animals' option (3) to see an overview of your zoo.")
    print("4. Use 'Feed an Animal' option (4) to feed animals based on their diet.")
    print("5. When you're done, select 'Exit' by typing '5' to close the application.")
    print("============================================================")

def display_menu():
    print("\n=== Zoo Management Menu ===")
    print("1. Add a cage")
    print("2. Add an animal to a cage")
    print("3. List all cages and animals")
    print("4. Feed an animal")
    print("5. Exit")
    print("===========================")

def create_animal(animal_type, name):
    """Create an animal based on type and name."""
    animal_classes = {
        "lion": Lion,
        "tiger": Tiger,
        "hyena": Hyena,
        "snake": Snake,
        "elephant": Elephant,
        "zebra": Zebra,
        "gazelle": Gazelle,
        "monkey": Monkey,
        "bear": Bear
    }
    animal_class = animal_classes.get(animal_type.lower())
    if animal_class:
        return animal_class(name)
    else:
        return None

def main():
    zoo = Zoo()
    display_instructions()  # Show instructions before starting the main loop
    
    while True:
        display_menu()
        choice = input("Enter the number of your choice (1, 2, 3, 4, or 5): ").strip()
        
        if choice == '1':
            cage = Cage()
            zoo.add_cage(cage)
            print("\n✅ A new cage has been added to the zoo.")

        elif choice == '2':
            if zoo.count_cages() == 0:
                print("\n⚠️ No cages available. Please add a cage first by choosing '1' from the menu.")
            else:
                animal_type = input("Enter animal type (e.g., Lion, Tiger, Gazelle): ").strip().capitalize()
                name = input("Enter the animal's name (e.g., Leo): ").strip().capitalize()

                # Create the animal using the helper function
                animal = create_animal(animal_type, name)
                if not animal:
                    print("\n❌ Invalid animal type. Please choose from the available animal types.")
                    continue

                # Select cage to add animal
                try:
                    cage_index = int(input(f"Select cage number (1 to {zoo.count_cages()}): ").strip()) - 1
                    if 0 <= cage_index < zoo.count_cages():
                        zoo.cages[cage_index].add_animal(animal)
                        print(f"\n✅ {animal} has been added to Cage {cage_index + 1}.")
                    else:
                        print("\n❌ Invalid cage number. Please choose a valid cage number.")
                except ValueError:
                    print("\n❌ Please enter a valid number for the cage.")

        elif choice == '3':
            print("\n=== List of Cages and Animals ===")
            if zoo.count_cages() == 0:
                print("There are no cages in the zoo yet.")
            else:
                for i, cage in enumerate(zoo.cages, 1):
                    animals = cage.list_animals()
                    animal_text = ", ".join(animals) if animals else "The cage is empty."
                    print(f"Cage {i}: {animal_text}")

        elif choice == '4':
            if zoo.count_cages() == 0:
                print("\n⚠️ No cages available. Please add a cage and animals first.")
            else:
                try:
                    cage_index = int(input(f"Select cage number to feed animals (1 to {zoo.count_cages()}): ").strip()) - 1
                    if 0 <= cage_index < zoo.count_cages():
                        animals = zoo.cages[cage_index].animals
                        if animals:
                            food_type = input("Enter food type (carnivore, herbivore, omnivore): ").strip().lower()
                            for animal in animals:
                                print(animal.feed(food_type))
                        else:
                            print("The selected cage is empty.")
                    else:
                        print("\n❌ Invalid cage number. Please choose a valid cage number.")
                except ValueError:
                    print("\n❌ Please enter a valid number for the cage.")

        elif choice == '5':
            print("\n👋 Exiting the application. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
