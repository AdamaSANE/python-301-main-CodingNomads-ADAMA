# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """
    Modélise une planète avec ses caractéristiques physiques.
    """
    def __init__(self, nom, type_planete, diametre_km, a_des_anneaux=False):
        # Variables d'instance
        self.nom = nom
        self.type = type_planete  # ex: Rocheuse, Gazeuse
        self.diametre = diametre_km
        self.anneaux = a_des_anneaux

    def __str__(self):
        """
        Méthode Dunder pour un affichage informatif lors de l'utilisation de print()
        """
        info_anneaux = "avec" if self.anneaux else "sans"
        return f"Planète {self.nom} ({self.type}), diamètre : {self.diametre} km, {info_anneaux} anneaux."

    def calculer_circonference(self):
        """
        Calcule la circonférence de la planète à l'équateur (C = π * d)
        """
        from math import pi
        return pi * self.diametre

# --- Instanciation d'objets ---

terre = Planet("Terre", "Rocheuse", 12742)
saturne = Planet("Saturne", "Gazeuse", 116460, a_des_anneaux=True)

# --- Test de l'affichage ---
print("===== Affichage des planètes =====")
print(terre)
print(saturne)

# Utilisation d'une méthode personnalisée
print(f"La circonférence de la {terre.nom} est d'environ {terre.calculer_circonference():.2f} km.")