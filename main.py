import tkinter as tk
from tkinter import ttk, messagebox
from zoo import Zoo
from cage import Cage
from animal import Lion, Gazelle, Serpent, Éléphant, Tigre, Ours, Zèbre, Okapi, Mangouste, RatonLaveur, Coati, Chimpanzé

class ZooApp:
    def __init__(self, root):
        self.zoo = Zoo()
        self.root = root
        self.root.title("Gestion d'un Zoo")
        self.root.configure(bg="#f5f5dc")  # Light beige background
        
        # Title with custom colors
        title_label = tk.Label(root, text="Bienvenue dans le Zoo Virtuel !", font=("Arial", 18, "bold"), fg="blue", bg="#f5f5dc")
        title_label.pack(pady=10)
        
        # Buttons with colors
        btn_style = {"width": 30, "bg": "#87ceeb", "fg": "black", "font": ("Arial", 12)}  # Sky blue background

        tk.Button(root, text="Ajouter une Cage", command=self.add_cage, **btn_style).pack(pady=5)
        tk.Button(root, text="Ajouter un Animal", command=self.add_animal_window, **btn_style).pack(pady=5)
        tk.Button(root, text="Lister les Cages et Animaux", command=self.list_cages, **btn_style).pack(pady=5)
        tk.Button(root, text="Nourrir un Animal", command=self.feed_animal_window, **btn_style).pack(pady=5)
        tk.Button(root, text="Quitter", command=root.quit, bg="#ff4d4d", fg="white", font=("Arial", 12), width=30).pack(pady=10)

    def add_cage(self):
        self.zoo.add_cage(Cage())
        messagebox.showinfo("Succès", "✅ Une nouvelle cage a été ajoutée au zoo.")

    def add_animal_window(self):
        if not self.zoo.count_cages():
            messagebox.showwarning("Aucune Cage", "⚠️ Veuillez ajouter une cage avant d'ajouter des animaux.")
            return
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Ajouter un Animal")
        add_window.configure(bg="#f0f8ff")  # Alice blue background

        # Animal Type
        tk.Label(add_window, text="Type d'Animal (e.g., Lion, Tigre, Gazelle)", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
        animal_type_entry = tk.Entry(add_window)
        animal_type_entry.pack(pady=5)
        
        # Animal Name
        tk.Label(add_window, text="Nom de l'Animal (e.g., Simba, Bella)", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
        animal_name_entry = tk.Entry(add_window)
        animal_name_entry.pack(pady=5)
        
        # Cage Number
        tk.Label(add_window, text=f"Numéro de Cage (1 à {self.zoo.count_cages()})", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
        cage_number_entry = tk.Entry(add_window)
        cage_number_entry.pack(pady=5)
        
        def add_animal():
            animal_type = animal_type_entry.get().capitalize()
            animal_name = animal_name_entry.get().capitalize()
            try:
                cage_index = int(cage_number_entry.get()) - 1
                if cage_index < 0 or cage_index >= self.zoo.count_cages():
                    raise ValueError
                
                animal = create_animal(animal_type, animal_name)
                if not animal:
                    messagebox.showerror("Erreur", "❌ Type d'animal invalide.")
                    return
                
                self.zoo.cages[cage_index].add_animal(animal)
                messagebox.showinfo("Succès", f"✅ {animal} a été ajouté à la cage {cage_index + 1}.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Erreur", "❌ Numéro de cage invalide.")

        tk.Button(add_window, text="Ajouter l'Animal", command=add_animal, bg="#87ceeb", fg="black", font=("Arial", 10)).pack(pady=10)

    def list_cages(self):
        if not self.zoo.count_cages():
            messagebox.showinfo("Cages", "Il n'y a aucune cage dans le zoo.")
            return
        
        list_window = tk.Toplevel(self.root)
        list_window.title("Liste des Cages et Animaux")
        list_window.configure(bg="#f0fff0")  # Honeydew background

        for i, cage in enumerate(self.zoo.cages, 1):
            animals = cage.list_animals()
            animal_list = "\n".join(animals) if animals else "La cage est vide."
            tk.Label(list_window, text=f"Cage {i} :\n{animal_list}", anchor="w", justify="left", bg="#f0fff0", fg="black").pack(pady=5)

    def feed_animal_window(self):
        if not self.zoo.count_cages():
            messagebox.showwarning("Aucune Cage", "⚠️ Ajoutez des cages avant de nourrir les animaux.")
            return
        
        feed_window = tk.Toplevel(self.root)
        feed_window.title("Nourrir un Animal")
        feed_window.configure(bg="#ffe4e1")  # Misty rose background

        # Cage Number
        tk.Label(feed_window, text=f"Numéro de Cage (1 à {self.zoo.count_cages()})", bg="#ffe4e1", fg="black", font=("Arial", 10)).pack(pady=5)
        cage_number_entry = tk.Entry(feed_window)
        cage_number_entry.pack(pady=5)
        
        # Food Type
        tk.Label(feed_window, text="Type de Nourriture (e.g., carnivore, herbivore)", bg="#ffe4e1", fg="black", font=("Arial", 10)).pack(pady=5)
        food_type_entry = tk.Entry(feed_window)
        food_type_entry.pack(pady=5)
        
        # Food Name
        tk.Label(feed_window, text="Nom de la Nourriture (e.g., viande, herbe)", bg="#ffe4e1", fg="black", font=("Arial", 10)).pack(pady=5)
        food_name_entry = tk.Entry(feed_window)
        food_name_entry.pack(pady=5)
        
        def feed_animal():
            try:
                cage_index = int(cage_number_entry.get()) - 1
                if cage_index < 0 or cage_index >= self.zoo.count_cages():
                    raise ValueError
                
                animals = self.zoo.cages[cage_index].animals
                if not animals:
                    messagebox.showinfo("Vide", "Cette cage est vide.")
                    return
                
                food_type = food_type_entry.get().lower()
                food_name = food_name_entry.get()
                results = [animal.feed(food_type, food_name) for animal in animals]
                messagebox.showinfo("Résultats", "\n".join(results))
                feed_window.destroy()
            except ValueError:
                messagebox.showerror("Erreur", "❌ Numéro de cage invalide.")
        
        tk.Button(feed_window, text="Nourrir", command=feed_animal, bg="#87ceeb", fg="black", font=("Arial", 10)).pack(pady=10)

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
    return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ZooApp(root)
    root.mainloop()
