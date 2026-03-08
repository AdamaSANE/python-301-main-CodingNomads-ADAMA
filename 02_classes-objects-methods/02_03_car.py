# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    """
    Modèle simple d'une voiture pour illustrer la POO.
    """
    def __init__(self, model, year, max_speed):
        # 1. Initialisation des attributs
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def boost(self):
        # 2. Méthode qui augmente la vitesse maximale de 5
        self.max_speed += 5
        print(f"> Boost appliqué à la {self.model} ! Nouvelle vitesse max : {self.max_speed}")

    def display_details(self):
        # 3. Méthode qui affiche les détails de la voiture
        print("-" * 30)
        print(f"Modèle : {self.model}")
        print(f"Année   : {self.year}")
        print(f"Vitesse Max : {self.max_speed} km/h")
        print("-" * 30)

# --- Création des objets (Instanciation) ---

voiture_adama = Car("Tesla Model 3", 2024, 225)
voiture_sport = Car("Porsche 911", 2022, 310)

# --- Démonstration des changements ---

# Affichage initial
print("État initial :")
voiture_adama.display_details()
voiture_sport.display_details()

# Application du boost sur la voiture d'Adama
voiture_adama.boost()
voiture_adama.boost() # On l'appelle deux fois pour voir l'évolution

# Affichage final après modifications
print("\nÉtat après modifications :")
voiture_adama.display_details()
voiture_sport.display_details() # Elle n'a pas bougé (indépendance des objets)