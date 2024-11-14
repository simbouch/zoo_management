
from zoo import Zoo
from cage import Cage
from animal import Lion, Gazelle, Hyena

def main():
    zoo = Zoo()
    
    while True:
        print("\nZoo Management")
        print("1. Add a cage")
        print("2. Add an animal to a cage")
        print("3. List all cages and animals")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            cage = Cage()
            zoo.add_cage(cage)
        
        elif choice == '2':
            if zoo.count_cages() == 0:
                print("No cages available. Please add a cage first.")
            else:
                animal_type = input("Enter animal type (Lion, Gazelle, Hyena): ")
                name = input("Enter the animal's name: ")
                
                if animal_type.lower() == "lion":
                    animal = Lion(name)
                elif animal_type.lower() == "gazelle":
                    animal = Gazelle(name)
                elif animal_type.lower() == "hyena":
                    animal = Hyena(name)
                else:
                    print("Invalid animal type.")
                    continue
                
                cage_index = int(input(f"Select cage number (1 to {zoo.count_cages()}): ")) - 1
                zoo.cages[cage_index].add_animal(animal)
        
        elif choice == '3':
            zoo.list_cages()
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    