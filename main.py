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
        
        # Listbox for existing items
        self.list_frame = tk.Frame(root, bg="#f5f5dc")
        self.list_frame.pack(pady=10)
        
        tk.Label(self.list_frame, text="État Actuel du Zoo :", font=("Arial", 14), fg="green", bg="#f5f5dc").pack(pady=5)
        
        self.listbox = tk.Listbox(self.list_frame, width=60, height=15, font=("Arial", 10))
        self.listbox.pack(padx=10, pady=5)
        
        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(self.listbox, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Buttons with colors
        btn_style = {"width": 30, "bg": "#87ceeb", "fg": "black", "font": ("Arial", 12)}  # Sky blue background

        tk.Button(root, text="Ajouter une Cage", command=self.add_cage, **btn_style).pack(pady=5)
        tk.Button(root, text="Ajouter un Animal", command=self.add_animal_window, **btn_style).pack(pady=5)
        tk.Button(root, text="Nourrir un Animal", command=self.feed_animal_window, **btn_style).pack(pady=5)
        tk.Button(root, text="Quitter", command=root.quit, bg="#ff4d4d", fg="white", font=("Arial", 12), width=30).pack(pady=10)

    def update_listbox(self):
        """Update the listbox with the current state of the zoo."""
        self.listbox.delete(0, tk.END)
        if not self.zoo.count_cages():
            self.listbox.insert(tk.END, "Aucune cage n'est disponible.")
            return
        for i, cage in enumerate(self.zoo.cages, 1):
            self.listbox.insert(tk.END, f"Cage {i} :")
            if cage.animals:
                for animal in cage.animals:
                    self.listbox.insert(tk.END, f"  - {animal}")
            else:
                self.listbox.insert(tk.END, "  (La cage est vide)")

    def add_cage(self):
        self.zoo.add_cage(Cage())
        messagebox.showinfo("Succès", "✅ Une nouvelle cage a été ajoutée au zoo.")
        self.update_listbox()

    def add_animal_window(self):
        if not self.zoo.count_cages():
            messagebox.showwarning("Aucune Cage", "⚠️ Veuillez ajouter une cage avant d'ajouter des animaux.")
            return
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Ajouter un Animal")
        add_window.configure(bg="#f0f8ff")  # Alice blue background

        # Available Animal Types
        animal_types = ["Lion", "Tigre", "Mangouste", "Serpent", "Éléphant", "Zèbre", "Okapi", "Gazelle", "Ours", "Raton Laveur", "Coati", "Chimpanzé"]
        tk.Label(add_window, text=f"Types d'Animaux Disponibles : {', '.join(animal_types)}", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
        
        # Animal Type Entry
        tk.Label(add_window, text="Type d'Animal (e.g., Lion, Tigre, Gazelle)", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
        animal_type_entry = tk.Entry(add_window)
        animal_type_entry.pack(pady=5)
        
        # Animal Name
        tk.Label(add_window, text="Nom de l'Animal (e.g., Simba, Bella)", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
        animal_name_entry = tk.Entry(add_window)
        animal_name_entry.pack(pady=5)
        
        # Cage Number
        tk.Label(add_window, text=f"Numéros de Cages Disponibles : {', '.join([str(i+1) for i in range(self.zoo.count_cages())])}", bg="#f0f8ff", fg="black", font=("Arial", 10)).pack(pady=5)
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
                    messagebox.showerror("Erreur", f"❌ Type d'animal invalide. Choisissez parmi : {', '.join(animal_types)}.")
                    return
                
                self.zoo.cages[cage_index].add_animal(animal)
                messagebox.showinfo("Succès", f"✅ {animal} a été ajouté à la cage {cage_index + 1}.")
                add_window.destroy()
                self.update_listbox()
            except ValueError:
                messagebox.showerror("Erreur", "❌ Numéro de cage invalide.")

        tk.Button(add_window, text="Ajouter l'Animal", command=add_animal, bg="#87ceeb", fg="black", font=("Arial", 10)).pack(pady=10)

    def feed_animal_window(self):
        if not self.zoo.count_cages():
            messagebox.showwarning("Aucune Cage", "⚠️ Ajoutez des cages avant de nourrir les animaux.")
            return
        
        feed_window = tk.Toplevel(self.root)
        feed_window.title("Nourrir un Animal")
        feed_window.configure(bg="#ffe4e1")  # Misty rose background

        # Cage Numbers
        tk.Label(feed_window, text=f"Numéros de Cages Disponibles : {', '.join([str(i+1) for i in range(self.zoo.count_cages())])}", bg="#ffe4e1", fg="black", font=("Arial", 10)).pack(pady=5)
        cage_number_entry = tk.Entry(feed_window)
        cage_number_entry.pack(pady=5)
        
        # Food Types
        food_types = ["carnivore", "herbivore", "omnivore"]
        tk.Label(feed_window, text=f"Types de Nourriture Disponibles : {', '.join(food_types)}", bg="#ffe4e1", fg="black", font=("Arial", 10)).pack(pady=5)
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
                if food_type not in food_types:
                    messagebox.showerror("Erreur", f"❌ Type de nourriture invalide. Choisissez parmi : {', '.join(food_types)}.")
                    return
                
                food_name = food_name_entry.get()
                results = [animal.feed(food_type, food_name) for animal in animals]
                messagebox.showinfo("Résultats", "\n".join(results))
                feed_window.destroy()
                self.update_listbox()
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
