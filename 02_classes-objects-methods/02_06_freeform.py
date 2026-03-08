# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class DatabaseServer:
    """Modélise un serveur de base de données (ton quotidien !)."""
    def __init__(self, hostname, ram_gb, storage_tb):
        self.hostname = hostname
        self.ram = ram_gb
        self.storage = storage_tb

    def __str__(self):
        return f"Serveur [{self.hostname}] : {self.ram} Go RAM, {self.storage} To Stockage"

    def __add__(self, other):
        """Surcharge du + pour simuler la fusion de deux serveurs en un cluster."""
        new_hostname = f"Cluster-{self.hostname[:3]}-{other.hostname[:3]}"
        return DatabaseServer(new_hostname, self.ram + other.ram, self.storage + other.storage)

class Coffee:
    """Modélise ta dose de caféine pour coder."""
    def __init__(self, type_grain, intensite, volume_ml):
        self.grain = type_grain
        self.intensite = intensite # sur 10
        self.volume = volume_ml

    def __str__(self):
        return f"Café {self.grain} (Intensité: {self.intensite}/10) - {self.volume}ml"

class Book:
    """Modélise un livre de ta bibliothèque Python."""
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def __str__(self):
        return f"'{self.titre}' par {self.auteur} ({self.pages} pages)"

# --- 1. Création des instances (Instanciation) ---

# Serveurs
srv_prod = DatabaseServer("SRV-PROD-01", 64, 10)
srv_backup = DatabaseServer("SRV-BKUP-01", 32, 20)

# Cafés
expresso = Coffee("Arabica", 8, 40)
latte = Coffee("Robusta", 4, 250)

# Livres
python_301 = Book("Python Mastery", "Martin Breuss", 450)
sql_expert = Book("SQL for Pros", "Adama Sane", 300)

# --- 2. Modification des attributs ---

print("--- Mise à jour des systèmes et des goûts ---")
srv_prod.ram = 128            # Upgrade de la RAM en prod
expresso.volume = 60          # On a fait un "double" expresso
sql_expert.pages += 50        # Ajout d'un chapitre sur la POO !

# --- 3. Affichage des résultats ---

print(f"Base de données : {srv_prod}")
print(f"Pause café : {expresso}")
print(f"Lecture : {sql_expert}")

# --- 4. Démonstration de la surcharge du + (Dunder __add__) ---

print("\n--- Fusion de serveurs (Cluster) ---")
cluster_puissant = srv_prod + srv_backup
print(f"Résultat du cluster : {cluster_puissant}")