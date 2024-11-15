from zoo import Zoo
from cage import Cage
from animal import Lion, Gazelle, Serpent, Éléphant, Tigre, Ours, Zèbre, Okapi, Mangouste, RatonLaveur, Coati, Chimpanzé

def display_instructions():
    print("\n=== Bienvenue dans l'application de gestion d'un zoo ! ===")
    print("Dans ce jeu, vous êtes le responsable d'un zoo virtuel. Vos tâches incluent :")
    print(" - Ajouter des cages pour accueillir les animaux")
    print(" - Ajouter différents types d'animaux dans chaque cage")
    print(" - Nourrir les animaux en fonction de leur régime alimentaire (carnivore, herbivore, omnivore)")
    print("\nTypes d'animaux disponibles :")
    print(" - Carnivores : Lion, Tigre, Mangouste, Serpent")
    print(" - Herbivores : Éléphant, Zèbre, Okapi, Gazelle")
    print(" - Omnivores : Ours, Raton Laveur, Coati, Chimpanzé")
    print("\nExemples de saisies :")
    print(" - Pour ajouter un Lion, entrez 'Lion' comme type d'animal.")
    print(" - Pour nommer le Lion, entrez un nom comme 'doli'.")
    print(" - Pour nourrir les animaux, entrez des régimes comme 'carnivore', 'herbivore', ou 'omnivore'.")
    print("============================================================")

def display_menu():
    print("\n=== Menu Gestion du Zoo ===")
    print("1. Ajouter une cage")
    print("2. Ajouter un animal dans une cage")
    print("3. Lister toutes les cages et les animaux")
    print("4. Nourrir un animal")
    print("5. Quitter")
    print("===========================")

def create_animal(animal_type, name):
    """Créer un animal selon son type et son nom."""
    animal_classes = {
        "lion": Lion,
        "tigre": Tigre,
        "mangouste": Mangouste,
        "serpent": Serpent,
        "éléphant": Éléphant,
        "zèbre": Zèbre,
        "okapi": Okapi,
        "gazelle": Gazelle,
        "ours": Ours,
        "raton laveur": RatonLaveur,
        "coati": Coati,
        "chimpanzé": Chimpanzé
    }
    animal_class = animal_classes.get(animal_type.lower())
    if animal_class:
        return animal_class(name)
    else:
        return None

def main():
    zoo = Zoo()
    display_instructions()
    
    while True:
        display_menu()
        choice = input("Entrez votre choix (1, 2, 3, 4 ou 5) : ").strip()
        
        if choice == '1':
            cage = Cage()
            zoo.add_cage(cage)
            print("\n✅ Une nouvelle cage a été ajoutée au zoo.")

        elif choice == '2':
            if zoo.count_cages() == 0:
                print("\n⚠️ Aucune cage disponible. Veuillez d'abord en ajouter avec l'option '1'.")
            else:
                animal_type = input("Entrez le type d'animal (e.g., Lion, Tigre, Okapi) : ").strip().capitalize()
                name = input("Entrez le nom de l'animal (e.g., komo, doli) : ").strip().capitalize()

                animal = create_animal(animal_type, name)
                if not animal:
                    print("\n❌ Type d'animal invalide. Veuillez choisir parmi les types disponibles.")
                    continue

                try:
                    cage_index = int(input(f"Choisissez un numéro de cage (1 à {zoo.count_cages()}) : ").strip()) - 1
                    if 0 <= cage_index < zoo.count_cages():
                        zoo.cages[cage_index].add_animal(animal)
                        print(f"\n✅ {animal} a été ajouté à la cage {cage_index + 1}.")
                    else:
                        print("\n❌ Numéro de cage invalide. Veuillez choisir un numéro valide.")
                except ValueError:
                    print("\n❌ Veuillez entrer un numéro valide pour la cage.")

        elif choice == '3':
            print("\n=== Liste des cages et des animaux ===")
            zoo.list_cages()

        elif choice == '4':
            if zoo.count_cages() == 0:
                print("\n⚠️ Aucune cage disponible. Ajoutez des cages et des animaux d'abord.")
            else:
                try:
                    cage_index = int(input(f"Choisissez un numéro de cage (1 à {zoo.count_cages()}) : ").strip()) - 1
                    if 0 <= cage_index < zoo.count_cages():
                        animals = zoo.cages[cage_index].animals
                        if animals:
                            food_type = input("Entrez le type de nourriture (carnivore, herbivore, omnivore) : ").strip().lower()
                            food_name = input("Entrez le nom de la nourriture (e.g., viande, herbe, fruits) : ").strip()
                            for animal in animals:
                                print(animal.feed(food_type, food_name))
                        else:
                            print("Cette cage est vide.")
                    else:
                        print("\n❌ Numéro de cage invalide. Veuillez choisir un numéro valide.")
                except ValueError:
                    print("\n❌ Veuillez entrer un numéro valide pour la cage.")

        elif choice == '5':
            print("\n👋 Au revoir ! Merci d'avoir joué.")
            break

        else:
            print("\n❌ Choix invalide. Veuillez entrer un chiffre entre 1 et 5.")

if __name__ == "__main__":
    main()
