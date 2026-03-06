# def selfless():
#         """
#         Méthode définie sans paramètre self (incorrect pour une méthode d'instance).
#         """
#         print("Je suis une méthode sans self !")
# # Création d'un ingrédient 'peas' (petits pois)
# i = Ingredient("peas")

# # Test de l'appel de la méthode selfless sur un objet
# try:
#     i.selfless()
# except TypeError as e:
#     print("Erreur lors de l'appel à selfless() :", e)

# Exemple 1 : Création d'une classe vide
# class Ingredient:
#   """Crée un objet ingrédient vide"""
#   pass

# i = Ingredient()  # Instanciation d'un ingrédient vide
# i.name = "Sugar"  # Ajout d'un attribut dynamiquement
# print(i.name)     # Affiche le nom de l'ingrédient

# Exemple 2 : Classe avec un attribut par défaut
# class Ingredient:
#     """Modélise un ingrédient. Actuellement seulement des carottes !"""
#
#     def __init__(self):
#         self.name = "carrot"  # Attribut par défaut
#
# i = Ingredient()
# print(i.name)  # Affiche : carrot
# c = Ingredient()
# print(c.name)  # Affiche : carrot

# Exemple 3 : Classe avec un attribut dynamique passé au constructeur
# class Ingredient:
#     """
#     Modélise un aliment utilisé comme ingrédient.
#     Attributs :
#         name (str) : nom de l'ingrédient
#         quantity (float) : quantité de l'ingrédient
#         unit (str) : unité de mesure (ex: 'g', 'ml', 'pcs')
#     """

#     def __init__(self, name, quantity, unit):
#         self.name = name            # Nom de l'ingrédient
#         self.quantity = quantity    # Quantité
#         self.unit = unit            # Unité de mesure

# # Exemples d'utilisation avec les nouveaux attributs
# i = Ingredient("peas", 200, "g")
# c = Ingredient("cauliflower", 1, "pcs")
# b = Ingredient("broccoli", 0.5, "pcs")
# d = Ingredient("dandelion", 50, "g")

# print(c.name, c.quantity, c.unit)  # Affiche : cauliflower 1 pcs
# print(b.name, b.quantity, b.unit)  # Affiche : broccoli 0.5 pcs
# print(d.name, d.quantity, d.unit)  # Affiche : dandelion 50 g

# print(i.name, i.quantity, i.unit)  # Affiche : peas 200 g 

class Ingredient:
    """
    Modélise un aliment utilisé comme ingrédient.
    """

    def __init__(self, name):
        # Attribut d'instance : nom de l'ingrédient
        self.name = name

    def expire(self):
        """
        Méthode pour signaler que l'ingrédient est périmé.
        Affiche un message et modifie le nom de l'ingrédient.
        """
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

# Création d'un ingrédient 'peas' (petits pois)
i = Ingredient("peas")
# Affiche le nom de l'ingrédient (avant expiration)
print(i.name)  # OUTPUT: peas
# Appelle la méthode expire pour signaler que l'ingrédient est périmé
i.expire()
# Affiche le nom de l'ingrédient après expiration
print(i.name)  # OUTPUT: expired peas
# Affiche à nouveau pour montrer que le nom reste modifié
print(i.name)  # OUTPUT: expired peas


class Ingredient:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    # FONCTION ? Non, MÉTHODE (car elle est dans la classe et utilise self)
    def afficher_infos(self):
        # self.nom permet d'aller chercher la donnée PROPRE à cet objet
        print(f"Ingrédient : {self.nom}, Stock : {self.quantite}g")

# --- Test ---
sel = Ingredient("Sel", 100)

# Appel de la méthode : on ne passe pas d'argument, 
# Python passe 'sel' automatiquement à la place de 'self'.
sel.afficher_infos()