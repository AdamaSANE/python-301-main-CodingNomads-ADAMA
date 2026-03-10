class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        # Chaque objet Ingredient stocke son propre nom et sa propre quantite.
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        # Cette methode modifie l'etat de l'objet en prefixant son nom.
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount, taste):
        # On reutilise l'initialisation de la classe parente pour name et amount.
        super().__init__(name, amount)
        # taste est un attribut supplementaire propre aux epices.
        self.taste = taste

    def expire(self):
        # Ici, on redefinit le comportement herite de Ingredient.expire().
        print(f"your {self.name} has expired. it's probably still good.")
        self.name = "old " + self.name

    def grind(self):
        # Methode specifique a Spice, absente de la classe Ingredient.
        print(f"You have now {self.amount} of ground {self.name}.")


# Creation d'un ingredient simple.
c = Ingredient("carrots", 2)
# Creation d'une epice: elle herite de Ingredient et ajoute taste.
p = Spice("pepper", 2, "hot")
# Appel de la version surchargee de expire() definie dans Spice.
p.expire()
# print() utilise automatiquement la methode speciale __str__().
print(c, p)
