# class Ingredient:
#   """Create an empty ingredient object"""
#   pass

# i = Ingredient()


# i.name = "Sugar"

# print(i.name)  

class Ingredient:
    """Models an Ingredient. Currently only carrots!"""

    def __init__(self):
        self.name = "carrot"

i = Ingredient()
print(i.name)  # OUTPUT: carrot
c = Ingredient()
print(c.name)  # OUTPUT: carrot
