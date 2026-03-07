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
# class Ingredient:
# 	"""Modélise un aliment utilisé comme ingrédient."""
# 	def __init__(self, name, amount):
# 		self.name = name
# 		self.amount = amount

# 	def __str__(self):
# 		return f"{self.name} ({self.amount})"

# 	def __repr__(self):
# 		return f"Ingredient(name={self.name}, amount={self.amount})"

# # Création d'objets et tests
# carotte = Ingredient("carotte", 5)
# oeuf = Ingredient("oeuf", 12)

# print(carotte)           # Affiche avec __str__
# print(repr(carotte))     # Affiche avec __repr__
# print(oeuf)
# print(repr(oeuf))

# # --- Commente __str__ ---
# #    def __str__(self):
# #        return f"{self.name} ({self.amount})"

# # print(carotte)           # Affiche avec __str__ (désactivé)
# print(repr(carotte))     # Affiche avec __repr__

# # --- Commente __repr__ ---
# #    def __repr__(self):
# #        return f"Ingredient(name={self.name}, amount={self.amount})"

# print(carotte)           # Affiche avec __str__
# # print(repr(carotte))     # Affiche avec __repr__ (désactivé)
# c = Ingredient("cauliflower", 1, "pcs")
# b = Ingredient("broccoli", 0.5, "pcs")
# d = Ingredient("dandelion", 50, "g")

# print(c.name, c.quantity, c.unit)  # Affiche : cauliflower 1 pcs
# print(b.name, b.quantity, b.unit)  # Affiche : broccoli 0.5 pcs
# print(d.name, d.quantity, d.unit)  # Affiche : dandelion 50 g

# print(i.name, i.quantity, i.unit)  # Affiche : peas 200 g 

# class Ingredient:
#     """
#     Modélise un aliment utilisé comme ingrédient.
#     """

#     def __init__(self, name):
#         # Attribut d'instance : nom de l'ingrédient
#         self.name = name

#     def expire(self):
#         """
#         Méthode pour signaler que l'ingrédient est périmé.
#         Affiche un message et modifie le nom de l'ingrédient.
#         """
#         print(f"whoops, these {self.name} went bad...")
#         self.name = "expired " + self.name

# # Création d'un ingrédient 'peas' (petits pois)
# i = Ingredient("peas")
# # Affiche le nom de l'ingrédient (avant expiration)
# print(i.name)  # OUTPUT: peas
# # Appelle la méthode expire pour signaler que l'ingrédient est périmé
# i.expire()
# # Affiche le nom de l'ingrédient après expiration
# print(i.name)  # OUTPUT: expired peas
# # Affiche à nouveau pour montrer que le nom reste modifié
# print(i.name)  # OUTPUT: expired peas


# class Ingredient:
#     def __init__(self, nom, quantite):
#         self.nom = nom
#         self.quantite = quantite

#     # FONCTION ? Non, MÉTHODE (car elle est dans la classe et utilise self)
#     def afficher_infos(self):
#         # self.nom permet d'aller chercher la donnée PROPRE à cet objet
#         print(f"Ingrédient : {self.nom}, Stock : {self.quantite}g")

# # --- Test ---
# sel = Ingredient("Sel", 100)

# # Appel de la méthode : on ne passe pas d'argument, 
# # Python passe 'sel' automatiquement à la place de 'self'.
# sel.afficher_infos()

# class Ingredient:

#     """Models a food item used as an ingredient."""
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount

#     def expire(self):
#         """Expires the ingredient."""
#         print(f"whoops, these {self.name} went bad...")
#         self.name = "expired " + self.name

#     def __str__(self):
#         return f"{self.name} ({self.amount})"

#     def __repr__(self):
#         return f"Ingredient(name={self.name}, amount={self.amount})"
    

# c = Ingredient("carrot", 5)
# print(c)  # OUTPUT: carrot (5)
# print(repr(c))  # OUTPUT: Ingredient(name=carrot, amount=5)

# print(2 + 2)  # OUTPUT: 4
# print("hello" + "world")  # OUTPUT: helloworld


# class Ingredient:

#     """Models a food item used as an ingredient."""
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount

#     # 
#     def __str__(self):
#         return f"{self.name} ({self.amount})"

#     def __add__(self, other):
#         """Combines two ingredients."""
#         new_name = self.name + other.name
#         return Ingredient(name=new_name, amount=1)

# c = Ingredient("carrot", 5)
# p = Ingredient("pea", 4)
# s = c.__add__(p)
# print(s)  # OUTPUT: carrotpea (1)

# s = c + p
# print(s)  # OUTPUT: carrotpea (1)

