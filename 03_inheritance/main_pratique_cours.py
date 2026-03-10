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

# class Ingredient:
#     """Models an Ingredient."""

#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount

#     def expire(self):
#         """Expires the ingredient item."""
#         print(f"whoops, these {self.name} went bad...")
#         self.name = "expired " + self.name

#     def __str__(self):
#         return f"You have {self.amount} {self.name}."

# class Spice(Ingredient):
#     """Models a spice, which is a type of ingredient."""
#     def grind(self):
#         """Grinds the spice."""
#         print(f"You have now {self.amount} of ground {self.name}.")
#     def soupon(self):
#         """Sprinkles the spice on the soup."""
#         print(f"You sprinkle {self.amount} of {self.name} on the soup.")

#     def expire(self):
#         if self.name == "salt":
#             print("salt never expires! ask the sea!")
#         else:
#             print(f"your {self.name} has expired. it's probably still good.")
#             self.name = "old " + self.name
# # p = Ingredient('peas', 12)
# # print(p)  # OUTPUT: You have 12 peas.
# # s = Spice('salt', 200)
# # print(s)  # OUTPUT: You have 200 salt.
# # s.expire()
# # print(s)  # OUTPUT: You have 200 expired salt.

# # c = Spice('carrots', 3)
# # p = Spice('pepper', 20)

# # p.grind()  # OUTPUT: You have now 20 of ground pepper.
# # c.soupon()  # OUTPUT: You sprinkle 3 of carrots on the soup.

# s = Spice("salt", 200)
# print(s)  # OUTPUT: You have 200 salt.
# s.expire()  # OUTPUT: salt never expires! ask the sea!
# print(s)  # OUTPUT: You have 200 salt.

# i = Ingredient("salt", 200)
# print(i)  # OUTPUT: You have 200 salt.
# i.expire()  # OUTPUT: whoops, these salt went bad...
# print(i)  # OUTPUT: You have 200 expired salt.

# class Vegetable(Ingredient):
#     """Models a vegetable, which is a type of ingredient."""
#     def __setattr__(self, name, value):
#         return super().__setattr__(name, value)
#     def cook(self):
#         """Cooks the vegetable."""
#         print(f"You cook the {self.name}.")


# class Ingredient:
#     """Models an Ingredient."""

#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount


# class Spice(Ingredient):
#     """Models a spice to flavor your food."""

#     def __init__(self, name, amount, taste):
#         super().__init__(name, amount)
#         self.taste = taste

# c = Ingredient("carrots", 2)
# p = Spice("pepper", 20, "hot")


#class Example:
#    pass

#print(dir(Example()))
# OUTPUT:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

#print(dir(object()))
# OUTPUT:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


class Stove:
	"""Represente une cuisiniere avec un certain nombre de feux."""

	def __init__(self, num_burners):
		self.num_burners = num_burners
		self.on = False

	def turn_on(self):
		self.on = True
		print("Stove is now on")

	def turn_off(self):
		self.on = False
		print("Stove is now off")


class Sink:
	"""Represente un evier pouvant faire couler de l'eau."""

	def __init__(self, num_faucets):
		self.num_faucets = num_faucets
		self.water_on = False

	def turn_water_on(self):
		self.water_on = True
		print("Water is now on")

	def turn_water_off(self):
		self.water_on = False
		print("Water is now off")


class Fridge:
	"""Represente un frigo qui stocke les aliments."""

	def __init__(self, num_shelves, capacity):
		self.num_shelves = num_shelves
		self.capacity = capacity
		self.contents = []

	def add_food(self, food):
		self.contents.append(food)
		print(f"Added {food} to the fridge")

	def remove_food(self, food):
		self.contents.remove(food)
		print(f"Removed {food} from the fridge")


class Countertop:
	"""Represente un plan de travail sur lequel poser des objets."""

	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.items = []

	def add_item(self, item):
		self.items.append(item)
		print(f"Added {item} to the countertop")

	def remove_item(self, item):
		self.items.remove(item)
		print(f"Removed {item} from the countertop")


class Kitchen:
	"""Compose plusieurs objets pour modeliser une cuisine complete."""

	def __init__(self, stove, sink, fridge, countertop):
		# La cuisine ne re-implemente pas ces objets: elle les regroupe.
		self.stove = stove
		self.sink = sink
		self.fridge = fridge
		self.countertop = countertop

	def prepare_breakfast(self):
		# On coordonne les composants pour simuler une vraie tache de cuisine.
		self.fridge.add_food("Eggs")
		self.countertop.add_item("Frying pan")
		self.sink.turn_water_on()
		self.stove.turn_on()
		print("Breakfast preparation started.")


class TinyBathroom:
	"""Exemple de reutilisation d'un composant dans une autre piece."""

	def __init__(self, sink):
		self.sink = sink


if __name__ == "__main__":
	# Chaque objet represente une partie specialisee de la cuisine.
	stove = Stove(4)
	sink = Sink(2)
	fridge = Fridge(3, 200)
	countertop = Countertop(10, 5)

	# La cuisine est construite par composition de ces objets.
	kitchen = Kitchen(stove, sink, fridge, countertop)
	kitchen.prepare_breakfast()

	# On peut aussi reemployer un composant ailleurs.
	bathroom_sink = Sink(1)
	bathroom = TinyBathroom(bathroom_sink)
	print(f"Bathroom faucets: {bathroom.sink.num_faucets}")
