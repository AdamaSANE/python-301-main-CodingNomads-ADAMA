# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.


import math

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        # Formule : L * l
        return self.longueur * self.largeur

    def calculer_perimetre(self):
        # Formule : 2 * (L + l)
        return 2 * (self.longueur + self.largeur)

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_aire(self):
        # Formule : π * r²
        return math.pi * (self.rayon ** 2)

    def calculer_circonference(self):
        # Formule : 2 * π * r
        return 2 * math.pi * self.rayon

# --- Test des classes ---

# Création d'un rectangle de 10x5
mon_rectangle = Rectangle(10, 5)
print("\n===== Rectangle =====\n")
print(f"Rectangle - Aire: {mon_rectangle.calculer_aire()}")
print(f"Rectangle - Périmètre: {mon_rectangle.calculer_perimetre()}")
print("\n===== Cercle =====")

# Création d'un cercle de rayon 7
mon_cercle = Cercle(7)
print(f"\nCercle - Aire: {mon_cercle.calculer_aire():.2f}")
print(f"Cercle - Circonférence: {mon_cercle.calculer_circonference():.2f}")
print("\n===== Fin des tests =====")